"""Materials routes -- search and lookup composite material properties.

GET  /api/materials?query=...   Search materials by name, type, or grade.
GET  /api/materials/{id}        Get a specific material by its identifier.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.schemas import MaterialResponse
from app.services import material_service

router = APIRouter(tags=["materials"])


@router.get(
    "/materials",
    response_model=MaterialResponse,
    summary="Search composite materials",
    description=(
        "Search the materials database by name, fibre type, grade, "
        "resin family, or application keyword.  Returns matching "
        "material records with full mechanical properties."
    ),
)
async def search_materials(
    query: Optional[str] = Query(
        default=None,
        description="Search term (e.g. 'carbon epoxy', 'T700', 'glass').",
    ),
) -> MaterialResponse:
    """Search or list all materials."""
    if query:
        results = material_service.search(query)
    else:
        results = material_service.get_all()

    return MaterialResponse(materials=results, count=len(results))


@router.get(
    "/materials/{material_id}",
    response_model=Dict[str, Any],
    summary="Get a material by ID",
    description=(
        "Look up a single material record by its identifier, "
        "e.g. 't700-epoxy-ud'."
    ),
)
async def get_material(material_id: str) -> Dict[str, Any]:
    """Return a single material record."""
    result = material_service.get_by_id(material_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Material '{material_id}' not found.",
        )
    return result
