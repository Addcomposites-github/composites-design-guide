"""Bolted joint analysis routes.

POST /api/bolted-joint/analyze     Analyse a bolted joint for all failure modes.
POST /api/bolted-joint/recommend   Get joint sizing recommendations.
GET  /api/bolted-joint/bolts       List all available bolt sizes.
GET  /api/bolted-joint/bolts/{bolt_id}  Get a single bolt's properties.
"""

from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    BoltedJointAnalysisRequest,
    BoltedJointAnalysisResponse,
    BoltedJointRecommendRequest,
    BoltedJointRecommendResponse,
    BoltResponse,
)
from app.services import bolted_joint_service

router = APIRouter(tags=["bolted-joint"])


# ---------------------------------------------------------------------------
# POST /api/bolted-joint/analyze
# ---------------------------------------------------------------------------


@router.post(
    "/bolted-joint/analyze",
    response_model=BoltedJointAnalysisResponse,
    summary="Analyse a bolted joint in a composite laminate",
    description=(
        "Evaluate a mechanically fastened joint for bearing, net-tension, "
        "shear-out, cleavage, and bearing-bypass interaction failure modes.  "
        "Supports single- and multi-fastener joints with spring-analogy "
        "load distribution."
    ),
)
async def analyze_bolted_joint(
    request: BoltedJointAnalysisRequest,
) -> BoltedJointAnalysisResponse:
    """Run a full bolted joint analysis."""
    try:
        result = bolted_joint_service.analyze_bolted_joint(
            bolt_diameter_mm=request.bolt_diameter_mm,
            hole_diameter_mm=request.hole_diameter_mm,
            laminate_thickness_mm=request.laminate_thickness_mm,
            laminate_width_mm=request.laminate_width_mm,
            edge_distance_mm=request.edge_distance_mm,
            applied_load_N=request.applied_load_N,
            bearing_strength_MPa=request.bearing_strength_MPa,
            tension_strength_MPa=request.tension_strength_MPa,
            shear_out_strength_MPa=request.shear_out_strength_MPa,
            bypass_ratio=request.bypass_ratio,
            num_fasteners=request.num_fasteners,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return BoltedJointAnalysisResponse(**result)


# ---------------------------------------------------------------------------
# POST /api/bolted-joint/recommend
# ---------------------------------------------------------------------------


@router.post(
    "/bolted-joint/recommend",
    response_model=BoltedJointRecommendResponse,
    summary="Get joint sizing recommendations",
    description=(
        "Given a load, laminate thickness, and bearing strength, recommend "
        "bolt diameters, edge distances, widths, and pitch using standard "
        "composite bolted joint design rules from CMH-17."
    ),
)
async def recommend_joint(
    request: BoltedJointRecommendRequest,
) -> BoltedJointRecommendResponse:
    """Return joint sizing recommendations."""
    try:
        result = bolted_joint_service.recommend_joint_config(
            applied_load_N=request.applied_load_N,
            laminate_thickness_mm=request.laminate_thickness_mm,
            material_bearing_strength_MPa=request.material_bearing_strength_MPa,
            safety_factor=request.safety_factor,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return BoltedJointRecommendResponse(**result)


# ---------------------------------------------------------------------------
# GET /api/bolted-joint/bolts
# ---------------------------------------------------------------------------


@router.get(
    "/bolted-joint/bolts",
    response_model=List[BoltResponse],
    summary="List all available bolt sizes",
    description=(
        "Returns the built-in database of common aerospace-grade bolt "
        "sizes (M4 through M10) with shear and tension load capacities."
    ),
)
async def list_bolts() -> List[BoltResponse]:
    """Return all bolt entries."""
    bolts = bolted_joint_service.list_bolts()
    return [BoltResponse(**b) for b in bolts]


# ---------------------------------------------------------------------------
# GET /api/bolted-joint/bolts/{bolt_id}
# ---------------------------------------------------------------------------


@router.get(
    "/bolted-joint/bolts/{bolt_id}",
    response_model=BoltResponse,
    summary="Get a bolt by ID",
    description=(
        "Look up a single bolt by its identifier, e.g. 'M6' or 'M8'."
    ),
)
async def get_bolt(bolt_id: str) -> BoltResponse:
    """Return a single bolt's properties."""
    bolt = bolted_joint_service.get_bolt(bolt_id)
    if bolt is None:
        available = [b["id"] for b in bolted_joint_service.list_bolts()]
        raise HTTPException(
            status_code=404,
            detail=(
                f"Bolt '{bolt_id}' not found.  "
                f"Available: {', '.join(available)}"
            ),
        )
    return BoltResponse(**bolt)
