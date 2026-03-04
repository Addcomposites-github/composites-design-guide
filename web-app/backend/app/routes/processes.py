"""Processes routes -- manufacturing process recommendation.

POST  /api/processes/recommend   Rank processes by suitability for given
                                  part requirements.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.models.schemas import (
    ProcessRecommendationRequest,
    ProcessRecommendationResponse,
)
from app.services import process_service

router = APIRouter(tags=["processes"])


@router.post(
    "/processes/recommend",
    response_model=ProcessRecommendationResponse,
    summary="Recommend manufacturing processes",
    description=(
        "Given part size, annual volume, performance class, and geometry "
        "type, returns a ranked list of manufacturing processes with "
        "suitability scores and reasoning."
    ),
)
async def recommend_processes(
    request: ProcessRecommendationRequest,
) -> ProcessRecommendationResponse:
    """Return ranked process recommendations."""
    recs = process_service.recommend(
        part_size_m2=request.part_size_m2,
        annual_volume=request.annual_volume,
        performance_class=request.performance_class,
        geometry_type=request.geometry_type,
    )

    # Strip the full process_data from the response to keep it lighter;
    # include the most useful fields instead.
    slim_recs = []
    for r in recs:
        proc_data = r.get("process_data", {})
        slim_recs.append(
            {
                "process_id": r["process_id"],
                "process_name": r["process_name"],
                "suitability_score": r["suitability_score"],
                "reasoning": r["reasoning"],
                "warnings": r["warnings"],
                "difficulty": proc_data.get("difficulty", ""),
                "description": proc_data.get("description", ""),
                "advantages": proc_data.get("advantages", []),
                "limitations": proc_data.get("limitations", []),
                "knowledge_base_page": proc_data.get(
                    "knowledge_base_page", None
                ),
            }
        )

    return ProcessRecommendationResponse(recommendations=slim_recs)
