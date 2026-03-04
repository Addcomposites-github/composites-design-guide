"""Sandwich panel design and analysis service.

Provides tools for designing sandwich structures with composite face sheets
and various core materials (honeycomb, foam, balsa). Checks for common
failure modes: face wrinkling, dimpling, core shear failure, core crush,
and overall buckling.

Engineering formulae are based on standard sandwich panel theory as
described in MIL-HDBK-23A (Structural Sandwich Composites),
Zenkert — *An Introduction to Sandwich Construction*, and
HexWeb Honeycomb Sandwich Design Technology (Hexcel).
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Core material database
# ---------------------------------------------------------------------------

CORE_MATERIALS: Dict[str, Dict[str, Any]] = {
    "nomex_honeycomb_48": {
        "name": "Nomex Honeycomb (48 kg/m3)",
        "density_kg_m3": 48,
        "shear_strength_MPa": 1.5,
        "shear_modulus_MPa": 35,
        "compressive_strength_MPa": 2.2,
        "compressive_modulus_MPa": 130,
        "cell_size_mm": 3.2,
        "cost_usd_per_m2": 40,
    },
    "nomex_honeycomb_96": {
        "name": "Nomex Honeycomb (96 kg/m3)",
        "density_kg_m3": 96,
        "shear_strength_MPa": 3.5,
        "shear_modulus_MPa": 75,
        "compressive_strength_MPa": 6.5,
        "compressive_modulus_MPa": 310,
        "cell_size_mm": 3.2,
        "cost_usd_per_m2": 65,
    },
    "aluminium_honeycomb_72": {
        "name": "Aluminium Honeycomb (72 kg/m3)",
        "density_kg_m3": 72,
        "shear_strength_MPa": 2.8,
        "shear_modulus_MPa": 330,
        "compressive_strength_MPa": 4.5,
        "compressive_modulus_MPa": 1100,
        "cell_size_mm": 6.35,
        "cost_usd_per_m2": 30,
    },
    "pmi_foam_52": {
        "name": "PMI Foam - Rohacell 51 (52 kg/m3)",
        "density_kg_m3": 52,
        "shear_strength_MPa": 0.8,
        "shear_modulus_MPa": 19,
        "compressive_strength_MPa": 0.9,
        "compressive_modulus_MPa": 75,
        "cell_size_mm": 0,  # continuous (no cells)
        "cost_usd_per_m2": 50,
    },
    "pvc_foam_80": {
        "name": "PVC Foam - Divinycell H80 (80 kg/m3)",
        "density_kg_m3": 80,
        "shear_strength_MPa": 1.15,
        "shear_modulus_MPa": 31,
        "compressive_strength_MPa": 1.4,
        "compressive_modulus_MPa": 90,
        "cell_size_mm": 0,
        "cost_usd_per_m2": 25,
    },
    "pvc_foam_130": {
        "name": "PVC Foam - Divinycell H130 (130 kg/m3)",
        "density_kg_m3": 130,
        "shear_strength_MPa": 2.2,
        "shear_modulus_MPa": 50,
        "compressive_strength_MPa": 2.8,
        "compressive_modulus_MPa": 170,
        "cell_size_mm": 0,
        "cost_usd_per_m2": 35,
    },
    "balsa_150": {
        "name": "End-Grain Balsa (150 kg/m3)",
        "density_kg_m3": 150,
        "shear_strength_MPa": 2.6,
        "shear_modulus_MPa": 108,
        "compressive_strength_MPa": 9.6,
        "compressive_modulus_MPa": 3800,
        "cell_size_mm": 0,
        "cost_usd_per_m2": 15,
    },
}

# Assumed adhesive areal weight (kg/m2) — typical for structural film adhesive
# applied to both face-core interfaces.
_ADHESIVE_WEIGHT_KG_M2 = 0.3


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------


def list_core_materials() -> List[Dict[str, Any]]:
    """Return the full core-materials database as a list of dicts.

    Each entry includes the dictionary key as ``id``.
    """
    result: List[Dict[str, Any]] = []
    for core_id, props in CORE_MATERIALS.items():
        entry = {"id": core_id, **props}
        result.append(entry)
    return result


def get_core_material(core_id: str) -> Optional[Dict[str, Any]]:
    """Return a single core material by its identifier, or *None*."""
    props = CORE_MATERIALS.get(core_id)
    if props is None:
        return None
    return {"id": core_id, **props}


# ---------------------------------------------------------------------------
# Internal calculation helpers
# ---------------------------------------------------------------------------


def _compute_load_effects(
    load_type: str,
    applied_load: float,
    panel_length_mm: float,
    panel_width_mm: float,
) -> Dict[str, float]:
    """Derive maximum bending moment *M* (N-mm) and shear force *V* (N)
    for a simply-supported rectangular panel under the given load type.

    Supported *load_type* values:

    * ``"uniform_pressure"`` — *applied_load* is pressure in Pa (N/m2).
    * ``"point_load"`` — *applied_load* is a concentrated force in N at
      the centre of the panel.
    * ``"bending"`` — *applied_load* is a line load in N/m applied along
      the width, treated as a simply-supported beam of length
      *panel_length_mm*.

    Returns a dict with keys ``M_Nmm``, ``V_N``, and ``q_Nmm``
    (distributed line load in N/mm used for buckling checks).
    """
    a = panel_length_mm  # span (mm)
    b = panel_width_mm   # width (mm)

    if load_type == "uniform_pressure":
        # applied_load is pressure in Pa = N/m2
        # Convert to N/mm2 for consistency with mm units
        p_MPa = applied_load * 1e-6  # N/mm2

        # Simply-supported beam strip of width *b*:
        # line load q = p * b  (N/mm)
        q_Nmm = p_MPa * b
        M_Nmm = q_Nmm * a**2 / 8.0
        V_N = q_Nmm * a / 2.0

    elif load_type == "point_load":
        # Central point load on a simply-supported beam
        P = applied_load  # N
        q_Nmm = P / a  # equivalent uniform load for buckling estimate
        M_Nmm = P * a / 4.0
        V_N = P / 2.0

    elif load_type == "bending":
        # Line load (N/m) along the width
        # Convert to N/mm
        w_Nmm = applied_load / 1000.0
        q_Nmm = w_Nmm
        M_Nmm = w_Nmm * a**2 / 8.0
        V_N = w_Nmm * a / 2.0

    else:
        raise ValueError(
            f"Unknown load_type '{load_type}'. "
            f"Must be 'uniform_pressure', 'point_load', or 'bending'."
        )

    return {"M_Nmm": M_Nmm, "V_N": V_N, "q_Nmm": q_Nmm}


# ---------------------------------------------------------------------------
# Main analysis function
# ---------------------------------------------------------------------------


def analyze_sandwich(
    face_thickness_mm: float,
    core_thickness_mm: float,
    face_E_GPa: float,
    face_sigma_ult_MPa: float,
    core_material_id: str,
    panel_length_mm: float,
    panel_width_mm: float,
    load_type: str,
    applied_load: float,
) -> Dict[str, Any]:
    """Analyse a sandwich panel and check all critical failure modes.

    Parameters
    ----------
    face_thickness_mm : float
        Thickness of each face sheet (top and bottom are equal).
    core_thickness_mm : float
        Thickness of the core.
    face_E_GPa : float
        Young's modulus of the face sheet material in GPa.
    face_sigma_ult_MPa : float
        Ultimate tensile/compressive strength of the face sheet in MPa.
    core_material_id : str
        Key into the ``CORE_MATERIALS`` database.
    panel_length_mm : float
        Panel span (simply-supported direction) in mm.
    panel_width_mm : float
        Panel width in mm.
    load_type : str
        One of ``"uniform_pressure"``, ``"point_load"``, ``"bending"``.
    applied_load : float
        Load magnitude — units depend on *load_type* (Pa, N, or N/m).

    Returns
    -------
    dict
        ``stiffness`` (sub-dict), ``weight_per_m2_kg``, ``failure_checks``
        (list), ``overall_pass`` (bool), ``design_summary`` (str).
    """
    # ---- Validate core material ----
    core = CORE_MATERIALS.get(core_material_id)
    if core is None:
        available = ", ".join(CORE_MATERIALS.keys())
        raise ValueError(
            f"Unknown core_material_id '{core_material_id}'. "
            f"Available: {available}"
        )

    tf = face_thickness_mm          # mm
    tc = core_thickness_mm          # mm
    Ef = face_E_GPa * 1000.0        # MPa
    sigma_ult = face_sigma_ult_MPa  # MPa
    Gc = core["shear_modulus_MPa"]  # MPa
    Ec = core["compressive_modulus_MPa"]  # MPa
    tau_core_ult = core["shear_strength_MPa"]  # MPa
    sigma_core_crush = core["compressive_strength_MPa"]  # MPa
    cell_size = core["cell_size_mm"]  # mm (0 for foams)

    # ---- Total sandwich depth ----
    d = tc + tf  # distance between face-sheet centroids (thin face approx)
    h_total = tc + 2 * tf  # total panel height

    # ---- Bending stiffness (thin-face-sheet approximation) ----
    # D = Ef * tf * d^2 / 2   (N-mm per mm width)
    D = Ef * tf * d**2 / 2.0  # N-mm2/mm (bending stiffness per unit width)

    # ---- Shear stiffness ----
    # S = Gc * d^2 / tc   (N/mm per mm width)
    S = Gc * d**2 / tc  # N/mm (shear stiffness per unit width)

    # ---- Weight per unit area ----
    # Face sheet: assume CFRP density ~1550 kg/m3 or derive from E?
    # We use a typical value for CFRP (~1550 kg/m3). For glass ~1900.
    # A rough heuristic: density ~ 1550 kg/m3 for most structural composites.
    face_density = 1550.0  # kg/m3
    core_density = core["density_kg_m3"]  # kg/m3

    face_weight = 2 * tf * 1e-3 * face_density  # kg/m2
    core_weight = tc * 1e-3 * core_density       # kg/m2
    adhesive_weight = _ADHESIVE_WEIGHT_KG_M2
    total_weight = face_weight + core_weight + adhesive_weight  # kg/m2

    stiffness_to_weight = D / total_weight if total_weight > 0 else 0.0

    # ---- Load effects ----
    loads = _compute_load_effects(load_type, applied_load, panel_length_mm, panel_width_mm)
    M = loads["M_Nmm"]
    V = loads["V_N"]

    # ---- Failure mode checks ----
    failure_checks: List[Dict[str, Any]] = []

    # 1. Face yielding / failure
    # sigma_face = M / (tf * d)   (thin face sheet bending stress)
    sigma_face = M / (tf * d) if (tf * d) > 0 else float("inf")
    face_margin = sigma_ult / sigma_face if sigma_face > 0 else float("inf")
    failure_checks.append({
        "mode": "Face yielding / failure",
        "status": "PASS" if face_margin >= 1.0 else "FAIL",
        "margin": round(face_margin, 3),
        "detail": (
            f"Face bending stress = {sigma_face:.2f} MPa vs "
            f"face ultimate = {sigma_ult:.1f} MPa. "
            f"Margin of safety = {face_margin:.3f}."
        ),
    })

    # 2. Core shear failure
    # tau_core = V / (d * b_width) but V is already total shear force
    # For a beam strip of width b, tau = V / (d * b).
    # Here V is total panel shear, so per-unit-width tau = V / (d * panel_width)
    # Actually _compute_load_effects already gives V for the full panel strip,
    # but we need shear stress in the core:
    # For uniform pressure or distributed load on a strip of width b:
    #   V is the total shear at the support for the whole width strip.
    #   tau_core = V / (d * b)  ... but actually V from beam theory for
    #   a strip of unit width is q*a/2, so tau = V_per_unit_width / d.
    #
    # Let's redo this properly.  The shear force V from _compute_load_effects
    # is for a beam of width panel_width_mm.  Shear flow per unit width:
    tau_core = V / (d * panel_width_mm) if (d * panel_width_mm) > 0 else float("inf")
    core_shear_margin = tau_core_ult / tau_core if tau_core > 0 else float("inf")
    failure_checks.append({
        "mode": "Core shear failure",
        "status": "PASS" if core_shear_margin >= 1.0 else "FAIL",
        "margin": round(core_shear_margin, 3),
        "detail": (
            f"Core shear stress = {tau_core:.3f} MPa vs "
            f"core shear strength = {tau_core_ult:.2f} MPa. "
            f"Margin of safety = {core_shear_margin:.3f}."
        ),
    })

    # 3. Face wrinkling (compressive instability of face sheet into core)
    # sigma_wr = 0.5 * (Ef * Ec * Gc)^(1/3)
    # Reference: Hoff & Mautner (1945), Allen (1969)
    sigma_wr = 0.5 * (Ef * Ec * Gc) ** (1.0 / 3.0)
    wrinkling_margin = sigma_wr / sigma_face if sigma_face > 0 else float("inf")
    failure_checks.append({
        "mode": "Face wrinkling",
        "status": "PASS" if wrinkling_margin >= 1.0 else "FAIL",
        "margin": round(wrinkling_margin, 3),
        "detail": (
            f"Wrinkling stress = {sigma_wr:.1f} MPa vs "
            f"face bending stress = {sigma_face:.2f} MPa. "
            f"Margin of safety = {wrinkling_margin:.3f}. "
            f"Formula: sigma_wr = 0.5 * (Ef * Ec * Gc)^(1/3)."
        ),
    })

    # 4. Dimpling (honeycomb only — face buckling into cells)
    if cell_size > 0:
        # sigma_d = 2 * Ef * (tf / cell_size)^2
        # Reference: Hexcel HexWeb sandwich design guide
        sigma_d = 2.0 * Ef * (tf / cell_size) ** 2
        dimpling_margin = sigma_d / sigma_face if sigma_face > 0 else float("inf")
        failure_checks.append({
            "mode": "Face dimpling (honeycomb)",
            "status": "PASS" if dimpling_margin >= 1.0 else "FAIL",
            "margin": round(dimpling_margin, 3),
            "detail": (
                f"Dimpling stress = {sigma_d:.1f} MPa vs "
                f"face bending stress = {sigma_face:.2f} MPa. "
                f"Margin of safety = {dimpling_margin:.3f}. "
                f"Cell size = {cell_size} mm. "
                f"Formula: sigma_d = 2 * Ef * (tf / s)^2."
            ),
        })
    else:
        failure_checks.append({
            "mode": "Face dimpling (honeycomb)",
            "status": "N/A",
            "margin": float("inf"),
            "detail": (
                "Dimpling check is not applicable for foam or "
                "balsa cores (no cell structure)."
            ),
        })

    # 5. Core crush (flatwise compressive load)
    # For uniform pressure, the through-thickness stress equals the
    # applied pressure.  For point loads, use a reasonable contact area.
    if load_type == "uniform_pressure":
        sigma_crush = applied_load * 1e-6  # Pa -> MPa
    elif load_type == "point_load":
        # Assume load spreads over ~50 mm x 50 mm contact patch
        contact_area_mm2 = 2500.0
        sigma_crush = applied_load / contact_area_mm2  # MPa
    else:
        # For bending line load, through-thickness stress is small
        sigma_crush = 0.0

    crush_margin = (
        sigma_core_crush / sigma_crush if sigma_crush > 0 else float("inf")
    )
    failure_checks.append({
        "mode": "Core crush",
        "status": "PASS" if crush_margin >= 1.0 else "FAIL",
        "margin": round(crush_margin, 3),
        "detail": (
            f"Through-thickness stress = {sigma_crush:.3f} MPa vs "
            f"core compressive strength = {sigma_core_crush:.2f} MPa. "
            f"Margin of safety = {crush_margin:.3f}."
        ),
    })

    # 6. Overall panel buckling (simply-supported, Euler with shear correction)
    # For a simply-supported sandwich panel under uniform compression:
    #
    #   N_euler = pi^2 * D / a^2          (Euler buckling load per unit width)
    #   N_cr = N_euler / (1 + N_euler / S) (shear-corrected)
    #
    # Then compare the applied in-plane load to N_cr.
    # The bending-induced compressive force in the face is:
    #   N_face = sigma_face * tf           (per unit width)
    a = panel_length_mm
    N_euler = math.pi**2 * D / a**2  # N/mm
    N_cr = N_euler / (1.0 + N_euler / S) if S > 0 else N_euler  # N/mm

    N_face = sigma_face * tf  # compressive load in face, N/mm
    buckling_margin = N_cr / N_face if N_face > 0 else float("inf")

    failure_checks.append({
        "mode": "Overall panel buckling",
        "status": "PASS" if buckling_margin >= 1.0 else "FAIL",
        "margin": round(buckling_margin, 3),
        "detail": (
            f"Critical buckling load = {N_cr:.2f} N/mm vs "
            f"applied face load = {N_face:.3f} N/mm. "
            f"Margin of safety = {buckling_margin:.3f}. "
            f"Euler load = {N_euler:.2f} N/mm, "
            f"shear correction applied."
        ),
    })

    # ---- Overall assessment ----
    real_checks = [c for c in failure_checks if c["status"] != "N/A"]
    overall_pass = all(c["status"] == "PASS" for c in real_checks)
    min_margin = min(
        (c["margin"] for c in real_checks),
        default=float("inf"),
    )

    # Cost estimate (per m2)
    core_cost = core["cost_usd_per_m2"]
    # Rough face-sheet cost: ~$60/m2 per mm of CFRP prepreg
    face_cost = 2 * tf * 60.0  # USD/m2
    adhesive_cost = 15.0  # USD/m2
    total_cost = core_cost + face_cost + adhesive_cost

    summary_parts = [
        f"Sandwich panel: {tf:.1f} mm face / {tc:.1f} mm {core['name']} core / {tf:.1f} mm face.",
        f"Total thickness: {h_total:.1f} mm.",
        f"Weight: {total_weight:.2f} kg/m2.",
        f"Bending stiffness D = {D:.0f} N-mm2/mm.",
        f"Estimated cost: ${total_cost:.0f}/m2.",
    ]
    if overall_pass:
        summary_parts.append(
            f"All failure checks PASSED. Minimum margin = {min_margin:.2f}."
        )
    else:
        failed = [c["mode"] for c in real_checks if c["status"] == "FAIL"]
        summary_parts.append(
            f"FAILED modes: {', '.join(failed)}. Minimum margin = {min_margin:.2f}."
        )

    return {
        "stiffness": {
            "D_bending_Nmm2_per_mm": round(D, 1),
            "S_shear_N_per_mm": round(S, 1),
            "stiffness_to_weight_ratio": round(stiffness_to_weight, 1),
            "total_thickness_mm": round(h_total, 2),
        },
        "weight_per_m2_kg": round(total_weight, 3),
        "cost_per_m2_usd": round(total_cost, 2),
        "failure_checks": failure_checks,
        "overall_pass": overall_pass,
        "design_summary": " ".join(summary_parts),
    }


# ---------------------------------------------------------------------------
# Optimisation
# ---------------------------------------------------------------------------

# Search grids
_CORE_THICKNESSES_MM = [5, 10, 15, 20, 25, 30, 40, 50]
_FACE_THICKNESSES_MM = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]


def optimize_sandwich(
    face_E_GPa: float,
    face_sigma_ult_MPa: float,
    panel_length_mm: float,
    panel_width_mm: float,
    load_type: str,
    applied_load: float,
    target_stiffness: Optional[float] = None,
    max_weight_kg_m2: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """Find the lightest sandwich configurations that pass all failure modes.

    Iterates over the core-material database and discrete thickness grids.
    Filters designs that:

    * Pass every failure mode with a margin >= 1.2 (20 % reserve).
    * Meet the optional *target_stiffness* (bending stiffness D, N-mm2/mm).
    * Meet the optional *max_weight_kg_m2* constraint.

    Results are ranked by weight (lightest first), then cost, then minimum
    margin.  Returns the top 5 designs.

    Parameters
    ----------
    face_E_GPa, face_sigma_ult_MPa
        Face sheet material properties.
    panel_length_mm, panel_width_mm
        Panel geometry.
    load_type, applied_load
        Loading — see :func:`analyze_sandwich`.
    target_stiffness : float, optional
        Minimum required bending stiffness D (N-mm2/mm).
    max_weight_kg_m2 : float, optional
        Maximum allowable weight per unit area (kg/m2).

    Returns
    -------
    list of dict
        Up to 5 designs, each containing the full analysis result plus
        the input configuration.
    """
    candidates: List[Dict[str, Any]] = []

    for core_id in CORE_MATERIALS:
        for tc in _CORE_THICKNESSES_MM:
            for tf in _FACE_THICKNESSES_MM:
                try:
                    result = analyze_sandwich(
                        face_thickness_mm=tf,
                        core_thickness_mm=tc,
                        face_E_GPa=face_E_GPa,
                        face_sigma_ult_MPa=face_sigma_ult_MPa,
                        core_material_id=core_id,
                        panel_length_mm=panel_length_mm,
                        panel_width_mm=panel_width_mm,
                        load_type=load_type,
                        applied_load=applied_load,
                    )
                except (ValueError, ZeroDivisionError):
                    continue

                # Filter: all real checks must pass with margin >= 1.2
                real_checks = [
                    c for c in result["failure_checks"] if c["status"] != "N/A"
                ]
                if not all(c["margin"] >= 1.2 for c in real_checks):
                    continue

                # Filter: stiffness target
                if target_stiffness is not None:
                    if result["stiffness"]["D_bending_Nmm2_per_mm"] < target_stiffness:
                        continue

                # Filter: weight constraint
                if max_weight_kg_m2 is not None:
                    if result["weight_per_m2_kg"] > max_weight_kg_m2:
                        continue

                min_margin = min(c["margin"] for c in real_checks)

                candidates.append({
                    "configuration": {
                        "face_thickness_mm": tf,
                        "core_thickness_mm": tc,
                        "core_material_id": core_id,
                        "core_material_name": CORE_MATERIALS[core_id]["name"],
                    },
                    "weight_per_m2_kg": result["weight_per_m2_kg"],
                    "cost_per_m2_usd": result["cost_per_m2_usd"],
                    "min_margin": round(min_margin, 3),
                    "analysis": result,
                })

    # Sort: lightest first, then cheapest, then highest minimum margin
    candidates.sort(
        key=lambda c: (c["weight_per_m2_kg"], c["cost_per_m2_usd"], -c["min_margin"])
    )

    return candidates[:5]
