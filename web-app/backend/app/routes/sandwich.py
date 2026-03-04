"""Sandwich panel design routes.

POST /api/sandwich/analyze   Analyse a sandwich panel for all failure modes.
POST /api/sandwich/optimize  Find optimal sandwich configurations.
GET  /api/sandwich/cores     List all available core materials.
GET  /api/sandwich/cores/{core_id}  Get a single core material's properties.
"""

from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    CoreMaterialResponse,
    SandwichAnalysisRequest,
    SandwichAnalysisResponse,
    SandwichOptimizationRequest,
)
from app.services import sandwich_service

router = APIRouter(tags=["sandwich"])


# ---------------------------------------------------------------------------
# POST /api/sandwich/analyze
# ---------------------------------------------------------------------------


@router.post(
    "/sandwich/analyze",
    response_model=SandwichAnalysisResponse,
    summary="Analyse a sandwich panel design",
    description=(
        "Evaluate a sandwich panel with composite face sheets and a "
        "selected core material.  Returns bending/shear stiffness, "
        "weight, and checks six failure modes: face failure, core shear, "
        "face wrinkling, dimpling (honeycomb), core crush, and overall "
        "panel buckling."
    ),
)
async def analyze_sandwich(request: SandwichAnalysisRequest) -> SandwichAnalysisResponse:
    """Run a full sandwich panel analysis."""
    try:
        result = sandwich_service.analyze_sandwich(
            face_thickness_mm=request.face_thickness_mm,
            core_thickness_mm=request.core_thickness_mm,
            face_E_GPa=request.face_E_GPa,
            face_sigma_ult_MPa=request.face_sigma_ult_MPa,
            core_material_id=request.core_material_id,
            panel_length_mm=request.panel_length_mm,
            panel_width_mm=request.panel_width_mm,
            load_type=request.load_type.value,
            applied_load=request.applied_load,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return SandwichAnalysisResponse(**result)


# ---------------------------------------------------------------------------
# POST /api/sandwich/optimize
# ---------------------------------------------------------------------------


@router.post(
    "/sandwich/optimize",
    response_model=List[Dict[str, Any]],
    summary="Find optimal sandwich panel configurations",
    description=(
        "Search across core materials and thickness combinations to "
        "find the lightest sandwich designs that pass all failure modes "
        "with adequate margin.  Optionally constrained by target "
        "stiffness and maximum weight."
    ),
)
async def optimize_sandwich(
    request: SandwichOptimizationRequest,
) -> List[Dict[str, Any]]:
    """Return up to 5 optimal sandwich configurations."""
    try:
        results = sandwich_service.optimize_sandwich(
            face_E_GPa=request.face_E_GPa,
            face_sigma_ult_MPa=request.face_sigma_ult_MPa,
            panel_length_mm=request.panel_length_mm,
            panel_width_mm=request.panel_width_mm,
            load_type=request.load_type.value,
            applied_load=request.applied_load,
            target_stiffness=request.target_stiffness_Nm,
            max_weight_kg_m2=request.max_weight_kg_m2,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    if not results:
        raise HTTPException(
            status_code=404,
            detail=(
                "No sandwich configurations found that meet all constraints.  "
                "Try relaxing the target stiffness, increasing the max weight, "
                "or reducing the applied load."
            ),
        )

    return results


# ---------------------------------------------------------------------------
# GET /api/sandwich/cores
# ---------------------------------------------------------------------------


@router.get(
    "/sandwich/cores",
    response_model=List[CoreMaterialResponse],
    summary="List all available core materials",
    description=(
        "Returns the built-in database of sandwich core materials "
        "including honeycomb, foam, and balsa options with mechanical "
        "properties and cost estimates."
    ),
)
async def list_cores() -> List[CoreMaterialResponse]:
    """Return all core materials."""
    cores = sandwich_service.list_core_materials()
    return [CoreMaterialResponse(**c) for c in cores]


# ---------------------------------------------------------------------------
# GET /api/sandwich/cores/{core_id}
# ---------------------------------------------------------------------------


@router.get(
    "/sandwich/cores/{core_id}",
    response_model=CoreMaterialResponse,
    summary="Get a core material by ID",
    description=(
        "Look up a single core material by its identifier, "
        "e.g. 'nomex_honeycomb_48' or 'pvc_foam_80'."
    ),
)
async def get_core(core_id: str) -> CoreMaterialResponse:
    """Return a single core material's properties."""
    core = sandwich_service.get_core_material(core_id)
    if core is None:
        available = [c["id"] for c in sandwich_service.list_core_materials()]
        raise HTTPException(
            status_code=404,
            detail=(
                f"Core material '{core_id}' not found.  "
                f"Available: {', '.join(available)}"
            ),
        )
    return CoreMaterialResponse(**core)
