"""Cost estimation route.

POST  /api/estimate-cost   Estimate per-part manufacturing cost.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.models.schemas import CostEstimateRequest, CostEstimateResponse
from app.services import cost_service

router = APIRouter(tags=["cost"])


@router.post(
    "/estimate-cost",
    response_model=CostEstimateResponse,
    summary="Estimate manufacturing cost per part",
    description=(
        "Provides a rough parametric cost estimate including material, "
        "labour, tooling (amortised), and consumables.  These are "
        "order-of-magnitude estimates for preliminary planning."
    ),
)
async def estimate_cost(request: CostEstimateRequest) -> CostEstimateResponse:
    """Return a per-part cost breakdown."""
    result = cost_service.estimate(
        fibre_type=request.fibre_type,
        process_id=request.process,
        part_weight_kg=request.part_weight_kg,
        number_of_plies=request.number_of_plies,
        annual_volume=request.annual_volume,
    )

    return CostEstimateResponse(
        material_cost=result["material_cost"],
        labour_cost=result["labour_cost"],
        tooling_cost=result["tooling_cost"],
        consumables_cost=result["consumables_cost"],
        total_cost=result["total_cost"],
        breakdown_notes=result["breakdown_notes"],
        disclaimer=result["disclaimer"],
    )
