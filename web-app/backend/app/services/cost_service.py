"""Parametric cost estimation service.

Provides rough order-of-magnitude cost estimates for composite parts
based on material type, manufacturing process, part weight, ply count,
and annual volume.  Direct Python port of the ``estimateCost`` function
from mcp-server/src/index.ts.
"""

from __future__ import annotations

from typing import Any, Dict, List

from app.services import material_service, process_service


def estimate(
    fibre_type: str,
    process_id: str,
    part_weight_kg: float,
    number_of_plies: int,
    annual_volume: int,
) -> Dict[str, Any]:
    """Estimate per-part manufacturing cost.

    Parameters
    ----------
    fibre_type : str
        Fibre / material search string, e.g. ``"carbon"``, ``"T700"``.
    process_id : str
        Manufacturing process ID or name, e.g. ``"wet-layup"``.
    part_weight_kg : float
        Estimated finished part weight in kg.
    number_of_plies : int
        Number of plies in the laminate.
    annual_volume : int
        Annual production volume for tooling amortisation.

    Returns
    -------
    dict
        Keys: ``material_cost``, ``labour_cost``, ``tooling_cost``,
        ``consumables_cost``, ``total_cost``, ``breakdown_notes`` (list),
        ``disclaimer`` (str).
    """
    notes: List[str] = []

    # ---- Find material ----
    all_materials = material_service.get_all()
    material = None
    fibre_lower = fibre_type.lower()
    for m in all_materials:
        if (
            fibre_lower in m.get("fibre_type", "").lower()
            or fibre_lower in m.get("fibre_grade", "").lower()
            or fibre_lower in m.get("category", "").lower()
            or fibre_lower in m.get("id", "").lower()
        ):
            material = m
            break

    if material:
        cost_range = material.get("cost_usd_per_kg", {"low": 30, "high": 70})
        material_cost_per_kg = (cost_range["low"] + cost_range["high"]) / 2.0
        notes.append(
            f"Material: {material['name']} at ~${material_cost_per_kg:.0f}/kg "
            f"(avg of ${cost_range['low']}-${cost_range['high']} range)."
        )
    else:
        material_cost_per_kg = 30.0
        notes.append(
            f'Material "{fibre_type}" not found in database. '
            f"Using default estimate of ${material_cost_per_kg:.0f}/kg."
        )

    # ---- Find process ----
    all_processes = process_service.get_all()
    process = None
    process_lower = process_id.lower()
    for p in all_processes:
        if (
            p.get("id", "").lower() == process_lower
            or process_lower in p.get("name", "").lower()
        ):
            process = p
            break

    if process:
        cost_data = process.get("cost", {})
        labour_hours_per_kg: float = cost_data.get("labour_hours_per_kg", {}).get(
            "typical", 4.0
        )
        difficulty = process.get("difficulty", "intermediate")
        if difficulty == "advanced":
            labour_rate = 55.0
        elif difficulty == "intermediate":
            labour_rate = 40.0
        else:
            labour_rate = 28.0
        waste_percent: float = cost_data.get("material_waste_pct", {}).get(
            "typical", 15.0
        )
        tooling_cost: float = cost_data.get("tooling_per_part_usd", {}).get(
            "moderate", 5000.0
        )
        notes.append(
            f"Process: {process['name']}. "
            f"Labour: {labour_hours_per_kg} hrs/kg at ${labour_rate:.0f}/hr. "
            f"Material waste: {waste_percent}%."
        )
    else:
        labour_hours_per_kg = 4.0
        labour_rate = 35.0
        waste_percent = 15.0
        tooling_cost = 5000.0
        notes.append(
            f'Process "{process_id}" not found in database. '
            f"Using default estimates."
        )

    # ---- Material cost ----
    effective_weight = part_weight_kg * (1.0 + waste_percent / 100.0)
    material_cost = effective_weight * material_cost_per_kg
    notes.append(
        f"Material cost: {part_weight_kg:.2f} kg part + {waste_percent}% waste = "
        f"{effective_weight:.2f} kg x ${material_cost_per_kg:.0f}/kg = "
        f"${material_cost:.2f}."
    )

    # ---- Labour cost ----
    ply_factor = 1.0 + max(0, number_of_plies - 16) * 0.02 if number_of_plies > 16 else 1.0
    labour_hours = labour_hours_per_kg * part_weight_kg * ply_factor
    labour_cost = labour_hours * labour_rate
    notes.append(
        f"Labour: {labour_hours:.1f} hrs x ${labour_rate:.0f}/hr = "
        f"${labour_cost:.2f} (ply factor: {ply_factor:.2f} for "
        f"{number_of_plies} plies)."
    )

    # ---- Tooling cost amortised ----
    tooling_amortised = tooling_cost / max(annual_volume, 1)
    notes.append(
        f"Tooling: ${tooling_cost:.0f} amortized over {annual_volume} parts/yr = "
        f"${tooling_amortised:.2f}/part."
    )

    # ---- Consumables ----
    consumables_cost = part_weight_kg * 5.0  # ~$5/kg
    notes.append(f"Consumables estimate: ${consumables_cost:.2f} (~$5/kg).")

    total_cost = material_cost + labour_cost + tooling_amortised + consumables_cost

    return {
        "material_cost": round(material_cost, 2),
        "labour_cost": round(labour_cost, 2),
        "tooling_cost": round(tooling_amortised, 2),
        "consumables_cost": round(consumables_cost, 2),
        "total_cost": round(total_cost, 2),
        "breakdown_notes": notes,
        "disclaimer": (
            "These are rough parametric estimates for preliminary planning "
            "only. Actual costs depend on specific materials, suppliers, "
            "tooling complexity, location, and manufacturing capability. "
            "Get quotes from suppliers for accurate pricing."
        ),
    }
