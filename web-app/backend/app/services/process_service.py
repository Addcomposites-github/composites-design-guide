"""Manufacturing process recommendation service.

Loads processes.json and provides a scoring-based recommendation engine.
Direct Python port of the ``recommendProcesses`` logic from
mcp-server/src/index.ts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.config import settings


# ---------------------------------------------------------------------------
# Lookup tables (mirrors TypeScript constants)
# ---------------------------------------------------------------------------

GEOMETRY_MAP: Dict[str, str] = {
    "flat": "flat_panels",
    "single_curve": "single_curvature",
    "double_curve": "double_curvature",
    "axisymmetric": "axisymmetric",
    "constant_cross_section": "constant_cross_section",
}

PERFORMANCE_TO_QUALITY: Dict[str, List[str]] = {
    "hobby": ["hobby", "industrial"],
    "structural": [
        "industrial",
        "marine",
        "wind-energy",
        "automotive",
        "aerospace-secondary",
        "motorsport",
    ],
    "aerospace": [
        "aerospace-primary",
        "aerospace-secondary",
        "defence",
        "space",
        "motorsport",
    ],
}


# ---------------------------------------------------------------------------
# Module-level state
# ---------------------------------------------------------------------------

_processes: List[Dict[str, Any]] = []
_meta: Dict[str, Any] = {}
_comparison_notes: Dict[str, Any] = {}
_loaded: bool = False


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load(processes_path: Optional[Path] = None) -> None:
    """Load (or reload) the processes database from disk."""
    global _processes, _meta, _comparison_notes, _loaded
    path = processes_path or settings.PROCESSES_PATH
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        _processes = data.get("processes", [])
        _meta = data.get("meta", {})
        _comparison_notes = data.get("comparison_notes", {})
        _loaded = True
    except Exception as exc:
        print(f"Warning: Could not load processes.json at {path}: {exc}")
        _processes = []
        _meta = {}
        _comparison_notes = {}
        _loaded = True


def _ensure_loaded() -> None:
    if not _loaded:
        load()


# ---------------------------------------------------------------------------
# Recommendation engine
# ---------------------------------------------------------------------------

def recommend(
    part_size_m2: float,
    annual_volume: int,
    performance_class: str,
    geometry_type: str,
) -> List[Dict[str, Any]]:
    """Rank manufacturing processes by suitability for the given requirements.

    Parameters
    ----------
    part_size_m2 : float
        Approximate part surface area in square metres.
    annual_volume : int
        Expected annual production volume.
    performance_class : str
        One of ``"hobby"``, ``"structural"``, ``"aerospace"``.
    geometry_type : str
        One of ``"flat"``, ``"single_curve"``, ``"double_curve"``,
        ``"axisymmetric"``, ``"constant_cross_section"``.

    Returns
    -------
    list of dict
        Processes sorted by descending ``suitability_score``.  Each dict
        contains ``process_id``, ``process_name``, ``suitability_score``,
        ``reasoning`` (list of str), ``warnings`` (list of str), and
        full ``process_data`` from the database.
    """
    _ensure_loaded()

    geometry_key = GEOMETRY_MAP.get(geometry_type)
    acceptable_quality = PERFORMANCE_TO_QUALITY.get(performance_class, [])

    recommendations: List[Dict[str, Any]] = []

    for proc in _processes:
        score = 0
        reasoning: List[str] = []
        warnings: List[str] = []

        # --- Geometry compatibility ---
        part_geom = proc.get("part_geometry", {})
        if geometry_key:
            if part_geom.get(geometry_key) is True:
                score += 30
                reasoning.append(
                    f"Geometry compatible: supports {geometry_type} parts."
                )
            elif part_geom.get(geometry_key) is False:
                score -= 50
                warnings.append(
                    f"Geometry mismatch: {proc['name']} does NOT support "
                    f"{geometry_type} geometry."
                )

        # --- Quality class match ---
        quality_classes = proc.get("quality_class", [])
        quality_match = any(qc in acceptable_quality for qc in quality_classes)
        if quality_match:
            score += 25
            reasoning.append(
                f"Quality class match: process rated for "
                f"{', '.join(quality_classes)}."
            )
        else:
            score -= 20
            warnings.append(
                f"Quality class mismatch: {performance_class} requires "
                f"{'/'.join(acceptable_quality)} but process is rated for "
                f"{', '.join(quality_classes)}."
            )

        # --- Volume suitability ---
        production = proc.get("production", {})
        suitable_vol = production.get("suitable_volume", {})
        vol_min = suitable_vol.get("min", 1)
        vol_max = suitable_vol.get("sweet_spot_max", 1000)

        if vol_min <= annual_volume <= vol_max:
            score += 20
            reasoning.append(
                f"Volume sweet spot: {annual_volume}/yr is within "
                f"{vol_min}-{vol_max}/yr range."
            )
        elif annual_volume < vol_min:
            ratio = vol_min / max(annual_volume, 1)
            score -= min(20, ratio * 5)
            warnings.append(
                f"Volume below minimum: {annual_volume}/yr is below "
                f"recommended {vol_min}/yr. Tooling cost may not amortize."
            )
        else:
            score += 10
            reasoning.append(
                f"Volume exceeds sweet spot ({vol_max}/yr) but process "
                f"can handle it."
            )

        # --- Part size ---
        capabilities = proc.get("capabilities", {})
        max_size = capabilities.get("max_part_size_m2")
        if max_size is not None and part_size_m2 > max_size:
            score -= 30
            warnings.append(
                f"Part too large: {part_size_m2} m2 exceeds max "
                f"{max_size} m2 for {proc['name']}."
            )
        else:
            score += 5

        # --- Bonus for performance / difficulty alignment ---
        difficulty = proc.get("difficulty", "")
        if performance_class == "aerospace" and difficulty == "advanced":
            score += 10
            reasoning.append(
                "Advanced process suitable for aerospace requirements."
            )
        if performance_class == "hobby" and difficulty == "beginner":
            score += 15
            reasoning.append(
                "Beginner-friendly process suitable for hobby use."
            )

        recommendations.append(
            {
                "process_id": proc.get("id", ""),
                "process_name": proc.get("name", ""),
                "suitability_score": score,
                "reasoning": reasoning,
                "warnings": warnings,
                "process_data": proc,
            }
        )

    recommendations.sort(key=lambda r: r["suitability_score"], reverse=True)
    return recommendations


# ---------------------------------------------------------------------------
# Simple accessors
# ---------------------------------------------------------------------------

def get_all() -> List[Dict[str, Any]]:
    """Return all process records."""
    _ensure_loaded()
    return list(_processes)


def get_by_id(process_id: str) -> Optional[Dict[str, Any]]:
    """Look up a process by its ``id`` field."""
    _ensure_loaded()
    for p in _processes:
        if p.get("id") == process_id:
            return p
    return None


def get_count() -> int:
    """Return the number of loaded processes."""
    _ensure_loaded()
    return len(_processes)
