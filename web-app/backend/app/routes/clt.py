"""CLT (Classical Lamination Theory) API routes.

POST  /api/calculate-laminate   Calculate ABD matrices and effective moduli.
POST  /api/check-failure        Run failure analysis on a loaded laminate.
POST  /api/optimize-laminate    Find the lightest laminate that passes failure.
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    CalculateLaminateRequest,
    CalculateLaminateResponse,
    CheckFailureRequest,
    CheckFailureResponse,
    OptimizeLaminateRequest,
    OptimizeLaminateResponse,
)
from app.services import clt_service

logger = logging.getLogger(__name__)
router = APIRouter(tags=["clt"])


# ---------------------------------------------------------------------------
# POST /api/calculate-laminate
# ---------------------------------------------------------------------------

@router.post(
    "/calculate-laminate",
    response_model=CalculateLaminateResponse,
    summary="Calculate laminate properties using Classical Lamination Theory",
    description=(
        "Accepts a layup (list of plies with angles, thickness, and elastic "
        "constants) and optionally applied loads.  Returns the ABD stiffness "
        "matrices, effective engineering constants (Ex, Ey, Gxy, nuxy), and "
        "ply-by-ply stresses/strains if loads are provided."
    ),
)
async def calculate_laminate(
    request: CalculateLaminateRequest,
) -> CalculateLaminateResponse:
    """Compute ABD matrices and effective moduli for a composite laminate."""
    try:
        layup_dicts = [ply.model_dump() for ply in request.layup]
        loads_dict = request.loads.model_dump() if request.loads else None

        result = clt_service.calculate_laminate(layup_dicts, loads_dict)

        return CalculateLaminateResponse(**result)

    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        logger.error("CLT calculation error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"CLT calculation failed: {exc}",
        ) from exc


# ---------------------------------------------------------------------------
# POST /api/check-failure
# ---------------------------------------------------------------------------

@router.post(
    "/check-failure",
    response_model=CheckFailureResponse,
    summary="Check laminate failure under applied loads",
    description=(
        "Runs a failure analysis on a loaded laminate using the specified "
        "criterion (max_stress, tsai_wu, tsai_hill, or hashin).  Returns "
        "per-ply failure indices, the first ply to fail, overall pass/fail, "
        "and the minimum margin of safety."
    ),
)
async def check_failure(
    request: CheckFailureRequest,
) -> CheckFailureResponse:
    """Evaluate failure for each ply under the given loads and criterion."""
    try:
        layup_dicts = [ply.model_dump() for ply in request.layup]
        strengths_dict = request.strengths.model_dump()
        loads_dict = request.loads.model_dump()

        result = clt_service.check_failure(
            layup=layup_dicts,
            strengths=strengths_dict,
            loads=loads_dict,
            criterion=request.criterion,
        )

        return CheckFailureResponse(**result)

    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        logger.error("Failure check error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failure check failed: {exc}",
        ) from exc


# ---------------------------------------------------------------------------
# POST /api/optimize-laminate
# ---------------------------------------------------------------------------

@router.post(
    "/optimize-laminate",
    response_model=OptimizeLaminateResponse,
    summary="Find the lightest laminate that passes failure for given loads",
    description=(
        "Tries standard laminate families (quasi-isotropic, 0-dominated, "
        "90-dominated, +-45-dominated, angle-ply, cross-ply) at increasing "
        "thicknesses until each passes max-stress failure.  Returns all "
        "passing candidates ranked by total thickness (lightest first)."
    ),
)
async def optimize_laminate(
    request: OptimizeLaminateRequest,
) -> OptimizeLaminateResponse:
    """Optimise laminate thickness for the given loads and material."""
    try:
        loads_dict = request.loads.model_dump()
        material_dict = request.material.model_dump()
        strengths_dict = request.strengths.model_dump()
        constraints_dict = (
            request.constraints.model_dump() if request.constraints else None
        )

        result = clt_service.optimize_laminate(
            loads=loads_dict,
            material_props=material_dict,
            strengths=strengths_dict,
            constraints=constraints_dict,
        )

        return OptimizeLaminateResponse(**result)

    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        logger.error("Laminate optimization error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Laminate optimization failed: {exc}",
        ) from exc
