"""Bolted joint analysis service for composite laminates.

Provides bearing, net-tension, shear-out, and bearing-bypass interaction
checks for mechanically fastened joints in composite structures.  Also
includes a recommendation function that sizes the joint geometry (bolt
diameter, edge distance, width, pitch) given load and material data.

Engineering formulae follow:
    * CMH-17 (Composite Materials Handbook), Vol. 3, Ch. 14 — Mechanically
      Fastened Joints.
    * MIL-HDBK-17-3F, Ch. 6 — Structural Joints.
    * Hart-Smith, L.J., "Bolted Joint Analyses for Composite Structures,"
      *Joining and Repair of Composite Structures*, ASTM STP 1455.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Bolt / fastener database
# ---------------------------------------------------------------------------
# Typical aerospace-grade fastener data.  Max shear and tension loads are
# approximate values for A286 / Ti-6Al-4V protruding-head fasteners at
# room temperature.  Always verify against the specific fastener spec
# (e.g. NAS, MS, or Hi-Lok data sheets) for real design work.

BOLT_DATABASE: Dict[str, Dict[str, Any]] = {
    "M4": {
        "name": "M4 (4.0 mm nominal)",
        "nominal_diameter_mm": 4.0,
        "max_shear_load_N": 5_200,
        "max_tension_load_N": 6_100,
        "weight_g": 2.5,
        "common_use": "Light structures, avionics brackets, fairings",
    },
    "M5": {
        "name": "M5 (5.0 mm nominal)",
        "nominal_diameter_mm": 5.0,
        "max_shear_load_N": 8_100,
        "max_tension_load_N": 9_500,
        "weight_g": 4.0,
        "common_use": "Light to medium structures, control surfaces",
    },
    "M6": {
        "name": "M6 (6.0 mm nominal)",
        "nominal_diameter_mm": 6.0,
        "max_shear_load_N": 11_700,
        "max_tension_load_N": 13_700,
        "weight_g": 6.0,
        "common_use": "Primary structure, spar joints, rib attachments",
    },
    "M8": {
        "name": "M8 (8.0 mm nominal)",
        "nominal_diameter_mm": 8.0,
        "max_shear_load_N": 20_800,
        "max_tension_load_N": 24_400,
        "weight_g": 14.0,
        "common_use": "Primary structure, wing root fittings, lugs",
    },
    "M10": {
        "name": "M10 (10.0 mm nominal)",
        "nominal_diameter_mm": 10.0,
        "max_shear_load_N": 32_500,
        "max_tension_load_N": 38_100,
        "weight_g": 28.0,
        "common_use": "Heavy primary structure, engine mounts",
    },
}


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------


def list_bolts() -> List[Dict[str, Any]]:
    """Return the bolt database as a list, each entry including its ``id``."""
    result: List[Dict[str, Any]] = []
    for bolt_id, props in BOLT_DATABASE.items():
        result.append({"id": bolt_id, **props})
    return result


def get_bolt(bolt_id: str) -> Optional[Dict[str, Any]]:
    """Return a single bolt entry by identifier, or *None*."""
    props = BOLT_DATABASE.get(bolt_id)
    if props is None:
        return None
    return {"id": bolt_id, **props}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _bearing_stress(load_N: float, diameter_mm: float, thickness_mm: float) -> float:
    """Bearing stress: sigma_br = P / (d * t).

    Reference: CMH-17, Vol. 3, Sec. 14.3.1
    The bearing stress is the compressive stress on the bolt hole wall,
    computed as the applied load divided by the bearing area (bolt diameter
    times laminate thickness).

    Parameters
    ----------
    load_N : float
        Bearing load through the fastener (N).
    diameter_mm : float
        Bolt (or hole) diameter used for the bearing area (mm).
    thickness_mm : float
        Laminate thickness at the joint (mm).

    Returns
    -------
    float
        Bearing stress in MPa.
    """
    return load_N / (diameter_mm * thickness_mm)


def _net_tension_stress(
    load_N: float,
    width_mm: float,
    diameter_mm: float,
    thickness_mm: float,
) -> float:
    """Net-tension stress: sigma_nt = P / ((w - d) * t).

    Reference: CMH-17, Vol. 3, Sec. 14.3.2
    Net-section tensile failure occurs when the laminate ruptures across the
    net section at the bolt hole row.  The net area is the total width minus
    the hole diameter, times the thickness.

    Parameters
    ----------
    load_N : float
        Applied tensile load through the joint (N).
    width_mm : float
        Total coupon / strip width (mm).
    diameter_mm : float
        Hole diameter (mm).
    thickness_mm : float
        Laminate thickness (mm).

    Returns
    -------
    float
        Net-tension stress in MPa.
    """
    net_width = width_mm - diameter_mm
    if net_width <= 0:
        return float("inf")
    return load_N / (net_width * thickness_mm)


def _shear_out_stress(
    load_N: float,
    edge_distance_mm: float,
    thickness_mm: float,
) -> float:
    """Shear-out (tear-out) stress: tau_so = P / (2 * e * t).

    Reference: CMH-17, Vol. 3, Sec. 14.3.3
    Shear-out is a plug pull-out failure where two shear planes form
    between the hole and the free edge.  The resisting area is
    2 * edge_distance * thickness.

    Parameters
    ----------
    load_N : float
        Applied load through the fastener (N).
    edge_distance_mm : float
        Distance from the hole centre to the free edge (mm).
    thickness_mm : float
        Laminate thickness (mm).

    Returns
    -------
    float
        Shear-out stress in MPa.
    """
    return load_N / (2.0 * edge_distance_mm * thickness_mm)


def _cleavage_check(
    edge_distance_mm: float,
    diameter_mm: float,
    width_mm: float,
) -> Dict[str, Any]:
    """Check cleavage (splitting) susceptibility for composite joints.

    Cleavage failure is a matrix-dominated splitting mode that occurs when
    the edge distance or width-to-diameter ratio is too small, particularly
    in laminates with insufficient +/-45 plies.

    Reference: MIL-HDBK-17-3F, Sec. 6.3.2.3

    Design rules to avoid cleavage:
        * e/d >= 3  (edge distance to bolt diameter)
        * w/d >= 4  (width to bolt diameter)

    Returns
    -------
    dict
        ``pass`` (bool), ``e_over_d``, ``w_over_d``, ``detail`` (str).
    """
    e_d = edge_distance_mm / diameter_mm if diameter_mm > 0 else 0.0
    w_d = width_mm / diameter_mm if diameter_mm > 0 else 0.0

    e_d_ok = e_d >= 3.0
    w_d_ok = w_d >= 4.0
    passed = e_d_ok and w_d_ok

    details: List[str] = []
    if not e_d_ok:
        details.append(
            f"e/d = {e_d:.2f} < 3.0 minimum — increase edge distance to "
            f"reduce cleavage risk."
        )
    if not w_d_ok:
        details.append(
            f"w/d = {w_d:.2f} < 4.0 minimum — increase strip width to "
            f"reduce cleavage risk."
        )
    if passed:
        details.append(
            f"e/d = {e_d:.2f} >= 3.0 and w/d = {w_d:.2f} >= 4.0 — "
            f"cleavage geometry is acceptable."
        )

    return {
        "pass": passed,
        "e_over_d": round(e_d, 2),
        "w_over_d": round(w_d, 2),
        "detail": " ".join(details),
    }


def _bearing_bypass_interaction(
    bearing_stress_MPa: float,
    bearing_strength_MPa: float,
    bypass_ratio: float,
    tension_strength_MPa: float,
    net_tension_stress_MPa: float,
) -> Dict[str, Any]:
    """Simplified bearing-bypass interaction check.

    Reference: CMH-17, Vol. 3, Sec. 14.4 and Hart-Smith bearing-bypass
    interaction diagrams.

    The bearing-bypass interaction envelope is approximated as a linear
    interaction between the bearing axis and the bypass (net-tension) axis:

        (sigma_br / sigma_br_ult) + (sigma_bypass / sigma_nt_ult) <= 1.0

    where:
        * sigma_br is the applied bearing stress (from the bearing load
          fraction: (1 - bypass_ratio) * total load).
        * sigma_bypass is the bypass stress (from the bypass load fraction:
          bypass_ratio * total load), evaluated at the net section.
        * sigma_br_ult is the bearing strength.
        * sigma_nt_ult is the open-hole or filled-hole tension strength.

    This linear interaction is conservative.  Actual envelopes from test
    data (CMH-17 Fig. 14.4.1) curve outward, giving more margin.

    Parameters
    ----------
    bearing_stress_MPa : float
        Applied bearing stress from the bearing load fraction.
    bearing_strength_MPa : float
        Material bearing strength (MPa).
    bypass_ratio : float
        Fraction of total load that bypasses the fastener (0.0 to 1.0).
    tension_strength_MPa : float
        Open-hole or filled-hole tension strength (MPa).
    net_tension_stress_MPa : float
        Net-section stress from the bypass load fraction.

    Returns
    -------
    dict
        ``interaction_index`` (< 1.0 is passing), ``pass`` (bool),
        ``bearing_ratio``, ``bypass_ratio_applied``, ``detail`` (str).
    """
    bearing_ratio = (
        bearing_stress_MPa / bearing_strength_MPa
        if bearing_strength_MPa > 0
        else float("inf")
    )
    bypass_stress = net_tension_stress_MPa * bypass_ratio
    bypass_ratio_applied = (
        bypass_stress / tension_strength_MPa
        if tension_strength_MPa > 0
        else float("inf")
    )

    interaction_index = bearing_ratio + bypass_ratio_applied
    passed = interaction_index <= 1.0

    return {
        "interaction_index": round(interaction_index, 4),
        "pass": passed,
        "bearing_ratio": round(bearing_ratio, 4),
        "bypass_ratio_applied": round(bypass_ratio_applied, 4),
        "detail": (
            f"Bearing-bypass interaction index = {interaction_index:.4f} "
            f"(bearing ratio = {bearing_ratio:.4f}, bypass ratio = "
            f"{bypass_ratio_applied:.4f}).  "
            f"{'PASS' if passed else 'FAIL'} — linear envelope limit is 1.0."
        ),
    }


def _load_per_fastener_spring_analogy(
    total_load_N: float,
    num_fasteners: int,
) -> float:
    """Distribute load across fasteners using the spring-analogy method.

    For a single-shear multi-fastener joint with equal fastener stiffnesses
    and equal member stiffnesses, the most heavily loaded fastener carries
    more than 1/N of the total load due to load-path eccentricity.

    Reference: CMH-17, Vol. 3, Sec. 14.2; MIL-HDBK-17-3F, Sec. 6.2.

    Simplified peak-fastener load fractions (ratio of peak fastener load
    to (P/n)):
        n=1  ->  1.00
        n=2  ->  1.15  (15 % overload on end bolt)
        n=3  ->  1.25
        n=4  ->  1.30
        n=5  ->  1.33
        n>=6 ->  1.35  (practical upper bound for balanced joints)

    These factors are approximate and assume metallic-to-composite or
    composite-to-composite single-shear joints.  Double-shear joints and
    joints with tapered fastener patterns will differ.

    Parameters
    ----------
    total_load_N : float
        Total applied load through the joint (N).
    num_fasteners : int
        Number of fasteners in a row.

    Returns
    -------
    float
        Peak load on the most heavily loaded fastener (N).
    """
    if num_fasteners <= 0:
        return total_load_N

    # Peak-fastener load fraction lookup
    overload_factors = {
        1: 1.00,
        2: 1.15,
        3: 1.25,
        4: 1.30,
        5: 1.33,
    }
    factor = overload_factors.get(num_fasteners, 1.35)

    average_load = total_load_N / num_fasteners
    return average_load * factor


# ---------------------------------------------------------------------------
# Main analysis function
# ---------------------------------------------------------------------------


def analyze_bolted_joint(
    bolt_diameter_mm: float,
    hole_diameter_mm: float,
    laminate_thickness_mm: float,
    laminate_width_mm: float,
    edge_distance_mm: float,
    applied_load_N: float,
    bearing_strength_MPa: float,
    tension_strength_MPa: float,
    shear_out_strength_MPa: float,
    bypass_ratio: float = 0.0,
    num_fasteners: int = 1,
) -> Dict[str, Any]:
    """Analyse a bolted joint in a composite laminate.

    Performs bearing, net-tension, shear-out, cleavage, and bearing-bypass
    interaction checks.  For multi-fastener joints the load distribution
    is estimated using the spring-analogy method.

    Parameters
    ----------
    bolt_diameter_mm : float
        Nominal bolt shank diameter (mm).
    hole_diameter_mm : float
        Drilled hole diameter (mm).  Typically bolt_diameter + 0.1 to 0.2 mm
        for interference-fit or clearance-fit aerospace holes.
    laminate_thickness_mm : float
        Laminate thickness at the joint (mm).
    laminate_width_mm : float
        Strip width for a single-bolt row, or pitch between bolts for
        multi-row analysis (mm).
    edge_distance_mm : float
        Distance from hole centre to the nearest free edge in the load
        direction (mm).
    applied_load_N : float
        Total applied tensile or compressive load through the joint (N).
    bearing_strength_MPa : float
        Laminate bearing strength — typically from test (ASTM D5961) or from
        material data sheets.  Common CFRP values: 400-800 MPa.
    tension_strength_MPa : float
        Open-hole tension (OHT) or filled-hole tension (FHT) strength of
        the laminate (MPa).  Used for the net-tension and bypass checks.
    shear_out_strength_MPa : float
        Shear-out (tear-out) strength of the laminate (MPa).
    bypass_ratio : float
        Fraction of total load that bypasses the fastener (0.0 to 1.0).
        0.0 means all load transfers through the bolt (single-bolt joint).
        In a multi-bolt joint, intermediate fasteners see a mix of bearing
        and bypass load.  Default is 0.0.
    num_fasteners : int
        Number of fasteners in a row.  The spring-analogy method distributes
        load and identifies the peak fastener load.  Default is 1.

    Returns
    -------
    dict
        Keys: ``bearing_check``, ``net_tension_check``, ``shear_out_check``,
        ``cleavage_check``, ``bearing_bypass_interaction``,
        ``fastener_load_distribution``, ``geometry_ratios``,
        ``overall_pass`` (bool), ``minimum_margin`` (float),
        ``design_recommendations`` (list of str), ``design_summary`` (str).
    """
    # ---- Input validation ----
    if bolt_diameter_mm <= 0:
        raise ValueError("bolt_diameter_mm must be positive.")
    if hole_diameter_mm <= 0:
        raise ValueError("hole_diameter_mm must be positive.")
    if laminate_thickness_mm <= 0:
        raise ValueError("laminate_thickness_mm must be positive.")
    if laminate_width_mm <= 0:
        raise ValueError("laminate_width_mm must be positive.")
    if edge_distance_mm <= 0:
        raise ValueError("edge_distance_mm must be positive.")
    if applied_load_N <= 0:
        raise ValueError("applied_load_N must be positive.")
    if not (0.0 <= bypass_ratio <= 1.0):
        raise ValueError("bypass_ratio must be between 0.0 and 1.0.")
    if num_fasteners < 1:
        raise ValueError("num_fasteners must be >= 1.")

    # ---- Load distribution (spring analogy) ----
    peak_fastener_load_N = _load_per_fastener_spring_analogy(
        applied_load_N, num_fasteners
    )
    average_fastener_load_N = applied_load_N / num_fasteners

    # The bearing load fraction for the critical fastener
    bearing_load_N = peak_fastener_load_N * (1.0 - bypass_ratio)
    bypass_load_N = peak_fastener_load_N * bypass_ratio

    # ---- Geometry ratios (design rule checks) ----
    d_over_t = bolt_diameter_mm / laminate_thickness_mm
    e_over_d = edge_distance_mm / bolt_diameter_mm
    w_over_d = laminate_width_mm / bolt_diameter_mm

    # ---- 1. Bearing stress check ----
    # Use hole diameter for bearing area (conservative — the hole is the
    # contact surface, and it is >= bolt diameter).
    sigma_br = _bearing_stress(bearing_load_N, hole_diameter_mm, laminate_thickness_mm)
    bearing_margin = (
        bearing_strength_MPa / sigma_br - 1.0 if sigma_br > 0 else float("inf")
    )
    bearing_pass = bearing_margin >= 0.0

    bearing_check = {
        "mode": "Bearing",
        "status": "PASS" if bearing_pass else "FAIL",
        "applied_stress_MPa": round(sigma_br, 2),
        "allowable_MPa": round(bearing_strength_MPa, 2),
        "margin_of_safety": round(bearing_margin, 3),
        "detail": (
            f"Bearing stress sigma_br = P_brg / (d_hole * t) = "
            f"{bearing_load_N:.1f} / ({hole_diameter_mm:.2f} * "
            f"{laminate_thickness_mm:.2f}) = {sigma_br:.2f} MPa.  "
            f"Allowable = {bearing_strength_MPa:.1f} MPa.  "
            f"MS = {bearing_margin:.3f}."
        ),
    }

    # ---- 2. Net-tension stress check ----
    # The net-tension load is the full peak fastener load (bearing + bypass
    # both act on the net section).
    sigma_nt = _net_tension_stress(
        peak_fastener_load_N, laminate_width_mm, hole_diameter_mm, laminate_thickness_mm
    )
    net_tension_margin = (
        tension_strength_MPa / sigma_nt - 1.0 if sigma_nt > 0 else float("inf")
    )
    net_tension_pass = net_tension_margin >= 0.0

    net_tension_check = {
        "mode": "Net tension",
        "status": "PASS" if net_tension_pass else "FAIL",
        "applied_stress_MPa": round(sigma_nt, 2),
        "allowable_MPa": round(tension_strength_MPa, 2),
        "margin_of_safety": round(net_tension_margin, 3),
        "detail": (
            f"Net-tension stress sigma_nt = P / ((w - d_hole) * t) = "
            f"{peak_fastener_load_N:.1f} / (({laminate_width_mm:.2f} - "
            f"{hole_diameter_mm:.2f}) * {laminate_thickness_mm:.2f}) = "
            f"{sigma_nt:.2f} MPa.  "
            f"Allowable = {tension_strength_MPa:.1f} MPa.  "
            f"MS = {net_tension_margin:.3f}."
        ),
    }

    # ---- 3. Shear-out stress check ----
    tau_so = _shear_out_stress(
        bearing_load_N, edge_distance_mm, laminate_thickness_mm
    )
    shear_out_margin = (
        shear_out_strength_MPa / tau_so - 1.0 if tau_so > 0 else float("inf")
    )
    shear_out_pass = shear_out_margin >= 0.0

    shear_out_check = {
        "mode": "Shear-out",
        "status": "PASS" if shear_out_pass else "FAIL",
        "applied_stress_MPa": round(tau_so, 2),
        "allowable_MPa": round(shear_out_strength_MPa, 2),
        "margin_of_safety": round(shear_out_margin, 3),
        "detail": (
            f"Shear-out stress tau_so = P_brg / (2 * e * t) = "
            f"{bearing_load_N:.1f} / (2 * {edge_distance_mm:.2f} * "
            f"{laminate_thickness_mm:.2f}) = {tau_so:.2f} MPa.  "
            f"Allowable = {shear_out_strength_MPa:.1f} MPa.  "
            f"MS = {shear_out_margin:.3f}."
        ),
    }

    # ---- 4. Cleavage check ----
    cleavage = _cleavage_check(
        edge_distance_mm, hole_diameter_mm, laminate_width_mm
    )

    cleavage_check = {
        "mode": "Cleavage",
        "status": "PASS" if cleavage["pass"] else "FAIL",
        "e_over_d": cleavage["e_over_d"],
        "w_over_d": cleavage["w_over_d"],
        "detail": cleavage["detail"],
    }

    # ---- 5. Bearing-bypass interaction ----
    bb_interaction = _bearing_bypass_interaction(
        bearing_stress_MPa=sigma_br,
        bearing_strength_MPa=bearing_strength_MPa,
        bypass_ratio=bypass_ratio,
        tension_strength_MPa=tension_strength_MPa,
        net_tension_stress_MPa=sigma_nt,
    )

    bearing_bypass_check = {
        "mode": "Bearing-bypass interaction",
        "status": "PASS" if bb_interaction["pass"] else "FAIL",
        "interaction_index": bb_interaction["interaction_index"],
        "bearing_ratio": bb_interaction["bearing_ratio"],
        "bypass_ratio_applied": bb_interaction["bypass_ratio_applied"],
        "detail": bb_interaction["detail"],
    }

    # ---- Overall assessment ----
    all_checks = [bearing_check, net_tension_check, shear_out_check,
                  cleavage_check, bearing_bypass_check]
    overall_pass = all(
        c["status"] == "PASS" for c in all_checks
    )

    # Collect numeric margins (cleavage and bearing-bypass use different
    # metrics, so we handle them separately).
    numeric_margins = [bearing_margin, net_tension_margin, shear_out_margin]
    # For bearing-bypass, convert interaction index to a margin-like metric:
    # MS_bb = (1 / interaction_index) - 1
    if bb_interaction["interaction_index"] > 0:
        bb_margin = 1.0 / bb_interaction["interaction_index"] - 1.0
        numeric_margins.append(bb_margin)

    minimum_margin = min(numeric_margins) if numeric_margins else float("inf")

    # ---- Design recommendations ----
    recommendations: List[str] = []

    # d/t ratio guidance (CMH-17 recommends d/t between 1.0 and 2.0 for
    # optimal bearing performance in composites)
    if d_over_t < 0.8:
        recommendations.append(
            f"d/t = {d_over_t:.2f} is low — the bolt is under-sized "
            f"relative to the laminate.  Consider a larger fastener or "
            f"thinner laminate to bring d/t into the 1.0-2.0 range."
        )
    elif d_over_t > 2.5:
        recommendations.append(
            f"d/t = {d_over_t:.2f} is high — the laminate is thin relative "
            f"to the bolt.  Bearing strength may be reduced.  Consider a "
            f"smaller fastener or thicker laminate."
        )
    else:
        recommendations.append(
            f"d/t = {d_over_t:.2f} is within the recommended 1.0-2.0 range "
            f"(acceptable up to ~2.5)."
        )

    # Edge distance guidance
    if e_over_d < 3.0:
        recommendations.append(
            f"e/d = {e_over_d:.2f} is below the 3.0 minimum — increase "
            f"edge distance to at least {3.0 * bolt_diameter_mm:.1f} mm."
        )

    # Width guidance
    if w_over_d < 6.0:
        recommendations.append(
            f"w/d = {w_over_d:.2f} is below the 6.0 recommendation for "
            f"single-fastener joints.  Consider widening to at least "
            f"{6.0 * bolt_diameter_mm:.1f} mm."
        )

    # Hole clearance check
    clearance = hole_diameter_mm - bolt_diameter_mm
    if clearance < 0:
        recommendations.append(
            "WARNING: Hole diameter is smaller than bolt diameter — "
            "this is physically impossible.  Check inputs."
        )
    elif clearance > 0.5:
        recommendations.append(
            f"Hole clearance = {clearance:.2f} mm is large.  Typical "
            f"aerospace clearance is 0.1-0.2 mm.  Excess clearance reduces "
            f"bearing strength due to non-uniform contact."
        )

    # Minimum margin warning
    if 0.0 <= minimum_margin < 0.15:
        recommendations.append(
            f"Minimum margin of safety is only {minimum_margin:.3f} — "
            f"consider increasing joint dimensions for a more robust design."
        )

    # ---- Fastener load distribution summary ----
    fastener_distribution = {
        "num_fasteners": num_fasteners,
        "total_applied_load_N": round(applied_load_N, 1),
        "average_fastener_load_N": round(average_fastener_load_N, 1),
        "peak_fastener_load_N": round(peak_fastener_load_N, 1),
        "peak_overload_factor": round(
            peak_fastener_load_N / average_fastener_load_N
            if average_fastener_load_N > 0 else 1.0,
            2,
        ),
        "bearing_load_N": round(bearing_load_N, 1),
        "bypass_load_N": round(bypass_load_N, 1),
    }

    # ---- Geometry ratios ----
    geometry_ratios = {
        "d_over_t": round(d_over_t, 2),
        "e_over_d": round(e_over_d, 2),
        "w_over_d": round(w_over_d, 2),
        "d_over_t_recommended": "1.0 - 2.0",
        "e_over_d_minimum": 3.0,
        "w_over_d_minimum": 6.0,
    }

    # ---- Summary string ----
    summary_parts = [
        f"Bolted joint: {bolt_diameter_mm:.1f} mm bolt in "
        f"{hole_diameter_mm:.1f} mm hole, "
        f"t = {laminate_thickness_mm:.1f} mm, "
        f"w = {laminate_width_mm:.1f} mm, "
        f"e = {edge_distance_mm:.1f} mm.",
        f"{num_fasteners} fastener(s), "
        f"bypass ratio = {bypass_ratio:.1%}.",
    ]
    if overall_pass:
        summary_parts.append(
            f"All checks PASSED.  Minimum margin of safety = "
            f"{minimum_margin:.3f}."
        )
    else:
        failed = [c["mode"] for c in all_checks if c["status"] == "FAIL"]
        summary_parts.append(
            f"FAILED modes: {', '.join(failed)}.  "
            f"Minimum margin of safety = {minimum_margin:.3f}."
        )

    return {
        "bearing_check": bearing_check,
        "net_tension_check": net_tension_check,
        "shear_out_check": shear_out_check,
        "cleavage_check": cleavage_check,
        "bearing_bypass_interaction": bearing_bypass_check,
        "fastener_load_distribution": fastener_distribution,
        "geometry_ratios": geometry_ratios,
        "overall_pass": overall_pass,
        "minimum_margin": round(minimum_margin, 3),
        "design_recommendations": recommendations,
        "design_summary": "  ".join(summary_parts),
    }


# ---------------------------------------------------------------------------
# Joint sizing recommendation
# ---------------------------------------------------------------------------


def recommend_joint_config(
    applied_load_N: float,
    laminate_thickness_mm: float,
    material_bearing_strength_MPa: float,
    safety_factor: float = 1.5,
) -> Dict[str, Any]:
    """Recommend bolt diameter, edge distance, width, and pitch.

    Uses standard composite bolted joint design rules from CMH-17 and
    MIL-HDBK-17 to size the joint geometry for the given load and laminate.

    Design rules applied:
        * Target d/t ratio between 1.0 and 2.0 (optimal for composites).
        * Bearing stress <= bearing_strength / safety_factor.
        * Edge distance >= 3 * d.
        * Strip width >= 6 * d (single fastener) or pitch >= 4 * d
          (multi-fastener).
        * Prefer standard metric bolt sizes (M4, M5, M6, M8, M10).

    Parameters
    ----------
    applied_load_N : float
        Total applied load through the joint (N).
    laminate_thickness_mm : float
        Laminate thickness at the joint (mm).
    material_bearing_strength_MPa : float
        Bearing strength of the laminate (MPa).
    safety_factor : float
        Design safety factor applied to the bearing strength.
        Default is 1.5.

    Returns
    -------
    dict
        ``recommended_bolts`` (list of viable options, ranked),
        ``design_rules_applied`` (list of str),
        ``summary`` (str).
    """
    if applied_load_N <= 0:
        raise ValueError("applied_load_N must be positive.")
    if laminate_thickness_mm <= 0:
        raise ValueError("laminate_thickness_mm must be positive.")
    if material_bearing_strength_MPa <= 0:
        raise ValueError("material_bearing_strength_MPa must be positive.")
    if safety_factor <= 0:
        raise ValueError("safety_factor must be positive.")

    allowable_bearing = material_bearing_strength_MPa / safety_factor

    # Compute minimum bolt diameter from bearing strength:
    # sigma_br = P / (d * t) <= allowable
    # => d >= P / (allowable * t)
    d_min_bearing = applied_load_N / (allowable_bearing * laminate_thickness_mm)

    # Compute ideal d range from d/t ratio
    d_ideal_low = 1.0 * laminate_thickness_mm   # d/t = 1.0
    d_ideal_high = 2.0 * laminate_thickness_mm   # d/t = 2.0

    # Standard bolt sizes to consider
    standard_sizes = ["M4", "M5", "M6", "M8", "M10"]

    candidates: List[Dict[str, Any]] = []

    for bolt_id in standard_sizes:
        bolt = BOLT_DATABASE[bolt_id]
        d = bolt["nominal_diameter_mm"]

        # Check if bolt meets minimum diameter for bearing
        if d < d_min_bearing * 0.95:  # 5 % tolerance
            continue

        # Compute geometry
        d_over_t = d / laminate_thickness_mm
        e_min = 3.0 * d                # minimum edge distance
        w_min = 6.0 * d                # minimum width (single fastener)
        pitch_min = 4.0 * d            # minimum pitch (multi-fastener)

        # Bearing stress with this bolt
        sigma_br = applied_load_N / (d * laminate_thickness_mm)
        bearing_ms = allowable_bearing / sigma_br - 1.0 if sigma_br > 0 else float("inf")

        # Check if bolt shear capacity is sufficient
        bolt_shear_ok = bolt["max_shear_load_N"] >= applied_load_N

        # d/t quality score: best if 1.0 <= d/t <= 2.0
        if 1.0 <= d_over_t <= 2.0:
            dt_quality = "optimal"
            dt_score = 0
        elif 0.8 <= d_over_t <= 2.5:
            dt_quality = "acceptable"
            dt_score = 1
        else:
            dt_quality = "outside recommended range"
            dt_score = 2

        # Multi-fastener option: how many bolts needed if single bolt
        # doesn't have enough shear capacity?
        num_fasteners_shear = 1
        if not bolt_shear_ok:
            num_fasteners_shear = math.ceil(
                applied_load_N / bolt["max_shear_load_N"]
            )

        notes: List[str] = []
        if not bolt_shear_ok:
            notes.append(
                f"Single {bolt_id} bolt shear capacity "
                f"({bolt['max_shear_load_N']:.0f} N) is insufficient for "
                f"{applied_load_N:.0f} N.  Use at least "
                f"{num_fasteners_shear} fasteners."
            )

        candidates.append({
            "bolt_id": bolt_id,
            "bolt_name": bolt["name"],
            "nominal_diameter_mm": d,
            "d_over_t": round(d_over_t, 2),
            "d_over_t_quality": dt_quality,
            "min_edge_distance_mm": round(e_min, 1),
            "min_width_mm": round(w_min, 1),
            "min_pitch_mm": round(pitch_min, 1),
            "bearing_stress_MPa": round(sigma_br, 1),
            "bearing_margin_of_safety": round(bearing_ms, 3),
            "bolt_shear_capacity_N": bolt["max_shear_load_N"],
            "bolt_shear_sufficient": bolt_shear_ok,
            "min_fasteners_for_shear": num_fasteners_shear,
            "weight_per_bolt_g": bolt["weight_g"],
            "notes": notes,
            "_sort_score": dt_score,
        })

    # Sort by d/t quality, then by bearing margin (higher is better)
    candidates.sort(
        key=lambda c: (c["_sort_score"], -c["bearing_margin_of_safety"])
    )

    # Remove internal sort score from output
    for c in candidates:
        del c["_sort_score"]

    # Design rules that were applied
    design_rules = [
        "d/t ratio target: 1.0 to 2.0 (optimal for composite bearing strength).",
        f"Bearing stress limit: {allowable_bearing:.1f} MPa "
        f"(= {material_bearing_strength_MPa:.1f} / {safety_factor:.1f} SF).",
        "Minimum edge distance: 3 * d (to prevent shear-out and cleavage).",
        "Minimum width: 6 * d (single fastener, to prevent net-tension failure).",
        "Minimum pitch: 4 * d (multi-fastener row, to avoid hole interaction).",
        "Hole diameter: typically d + 0.1 to 0.2 mm for clearance fit.",
    ]

    # Summary
    if candidates:
        best = candidates[0]
        summary = (
            f"Recommended: {best['bolt_name']} bolt (d/t = "
            f"{best['d_over_t']:.2f}, {best['d_over_t_quality']}).  "
            f"Minimum edge distance = {best['min_edge_distance_mm']:.1f} mm, "
            f"minimum width = {best['min_width_mm']:.1f} mm.  "
            f"Bearing MS = {best['bearing_margin_of_safety']:.3f} with "
            f"SF = {safety_factor:.1f}."
        )
    else:
        summary = (
            f"No standard bolt size (M4-M10) meets the bearing requirement "
            f"for {applied_load_N:.0f} N load on a "
            f"{laminate_thickness_mm:.1f} mm laminate with "
            f"{material_bearing_strength_MPa:.0f} MPa bearing strength.  "
            f"Consider a thicker laminate, higher bearing strength layup, "
            f"or a multi-fastener joint."
        )

    return {
        "recommended_bolts": candidates,
        "design_rules_applied": design_rules,
        "input_summary": {
            "applied_load_N": round(applied_load_N, 1),
            "laminate_thickness_mm": round(laminate_thickness_mm, 2),
            "material_bearing_strength_MPa": round(material_bearing_strength_MPa, 1),
            "safety_factor": round(safety_factor, 2),
            "min_bolt_diameter_from_bearing_mm": round(d_min_bearing, 2),
            "ideal_bolt_diameter_range_mm": [
                round(d_ideal_low, 1),
                round(d_ideal_high, 1),
            ],
        },
        "summary": summary,
    }
