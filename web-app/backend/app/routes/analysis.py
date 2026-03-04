"""Analysis route -- the Photo-to-Plan endpoint.

POST /api/analyze accepts a part description (and optional photo),
calls the vision service for AI analysis, enriches the result with
knowledge-base context, stacking rule checks, and cost estimation,
then returns a comprehensive AnalysisResponse with a markdown report.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

from fastapi import APIRouter, Header, HTTPException

from app.config import settings
from app.models.schemas import AnalysisRequest, AnalysisResponse
from app.services import (
    cost_service,
    knowledge_service,
    report_service,
    stacking_service,
    vision_service,
)

logger = logging.getLogger(__name__)
router = APIRouter(tags=["analysis"])


@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Analyze a part and generate a composites manufacturing plan",
    description=(
        "Accepts a part description (and optional base64 photo), calls "
        "Claude for AI-powered analysis, enriches the result with "
        "knowledge-base search, stacking rule checks, and cost estimation, "
        "and returns a full manufacturing plan with a markdown report."
    ),
)
async def analyze_part(
    request: AnalysisRequest,
    x_anthropic_key: Optional[str] = Header(None, alias="X-Anthropic-Key"),
) -> AnalysisResponse:
    """Main Photo-to-Plan endpoint."""

    # Resolve which API key to use: header overrides server config
    api_key = x_anthropic_key or settings.ANTHROPIC_API_KEY
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="No API key provided. Enter your Anthropic API key in Settings.",
        )

    # ---- 1. Call Claude vision service ----
    try:
        ai_result: Dict[str, Any] = await vision_service.analyze_part(
            description=request.part_description,
            intended_use=request.intended_use,
            skill_level=request.skill_level or "beginner",
            photo_base64=request.photo_base64,
            api_key=api_key,
        )
    except RuntimeError as exc:
        logger.error("Vision service error: %s", exc)
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        logger.error("Vision service parse error: %s", exc)
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    # ---- 2. Enrich: stacking rule check ----
    laminate = ai_result.get("laminate_design", {})
    stacking_seq = laminate.get("stacking_sequence", [])
    stacking_results = []
    if stacking_seq and all(isinstance(a, (int, float)) for a in stacking_seq):
        stacking_results = stacking_service.check_all(
            [float(a) for a in stacking_seq]
        )
        # Attach stacking check results to the laminate_design section
        laminate["stacking_rule_checks"] = stacking_results
        laminate["all_rules_passed"] = all(
            r["passed"] for r in stacking_results
        )

    # ---- 3. Enrich: cost estimation ----
    cost_estimate: Dict[str, Any] = {}
    try:
        mfg_plan = ai_result.get("manufacturing_plan", {})
        mat_rec = ai_result.get("material_recommendation", {})

        fibre_type = mat_rec.get("fibre_type", "carbon")
        process_id = mfg_plan.get("recommended_process", "wet-layup")
        num_plies = laminate.get("num_plies", 8)
        # Rough weight estimate from thickness and a typical density
        thickness_mm = laminate.get("estimated_thickness_mm", 2.0)
        # Assume a 0.25 m2 part at 1550 kg/m3 as a rough fallback
        estimated_weight_kg = 0.25 * (thickness_mm / 1000.0) * 1550.0

        cost_estimate = cost_service.estimate(
            fibre_type=fibre_type,
            process_id=process_id,
            part_weight_kg=max(estimated_weight_kg, 0.1),
            number_of_plies=max(num_plies, 1),
            annual_volume=1,  # Default: single part for hobbyist
        )
    except Exception as exc:
        logger.warning("Cost estimation failed: %s", exc)
        cost_estimate = {
            "material_cost": 0,
            "labour_cost": 0,
            "tooling_cost": 0,
            "consumables_cost": 0,
            "total_cost": 0,
            "breakdown_notes": [f"Cost estimation unavailable: {exc}"],
            "disclaimer": "Cost estimation could not be completed.",
        }

    # ---- 4. Build the full response dict ----
    full_analysis = {
        "part_analysis": ai_result.get("part_analysis", {}),
        "material_recommendation": ai_result.get("material_recommendation", {}),
        "laminate_design": laminate,
        "manufacturing_plan": ai_result.get("manufacturing_plan", {}),
        "cost_estimate": cost_estimate,
        "risk_assessment": ai_result.get("risk_assessment", {}),
    }

    # ---- 5. Generate markdown report ----
    report_md = report_service.generate_markdown_report(full_analysis)

    return AnalysisResponse(
        part_analysis=full_analysis["part_analysis"],
        material_recommendation=full_analysis["material_recommendation"],
        laminate_design=full_analysis["laminate_design"],
        manufacturing_plan=full_analysis["manufacturing_plan"],
        cost_estimate=full_analysis["cost_estimate"],
        risk_assessment=full_analysis["risk_assessment"],
        report_markdown=report_md,
    )
