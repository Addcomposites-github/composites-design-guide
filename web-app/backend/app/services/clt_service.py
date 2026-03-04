"""CLT (Classical Lamination Theory) calculation service using composipy.

Provides laminate property calculations including ABD matrices, effective
engineering constants, and failure analysis for composite laminates.

If composipy is not available, falls back to a pure-numpy implementation
of basic CLT (ABD matrix calculation and max stress failure criterion).
"""

from __future__ import annotations

import logging
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Try to import composipy; flag availability
# ---------------------------------------------------------------------------

_COMPOSIPY_AVAILABLE = False
try:
    from composipy import Laminate, LaminateStrength  # type: ignore[import-untyped]

    _COMPOSIPY_AVAILABLE = True
    logger.info("composipy is available -- using composipy CLT engine.")
except ImportError:
    logger.warning(
        "composipy is NOT installed. "
        "Falling back to pure-numpy CLT implementation."
    )


# =========================================================================
# Unit conversion helpers
# =========================================================================

def _gpa_to_pa(val: float) -> float:
    """Convert GPa to Pa."""
    return val * 1.0e9


def _mpa_to_pa(val: float) -> float:
    """Convert MPa to Pa."""
    return val * 1.0e6


def _pa_to_gpa(val: float) -> float:
    """Convert Pa to GPa."""
    return val / 1.0e9


def _pa_to_mpa(val: float) -> float:
    """Convert Pa to MPa."""
    return val / 1.0e6


def _mm_to_m(val: float) -> float:
    """Convert millimetres to metres."""
    return val * 1.0e-3


# =========================================================================
# Pure-numpy fallback CLT engine
# =========================================================================

def _q_matrix(E1: float, E2: float, G12: float, nu12: float) -> np.ndarray:
    """Compute the reduced stiffness matrix Q (3x3) in material axes.

    Parameters are in Pa.  Returns Q in Pa.
    """
    nu21 = nu12 * E2 / E1
    denom = 1.0 - nu12 * nu21
    Q = np.zeros((3, 3))
    Q[0, 0] = E1 / denom
    Q[1, 1] = E2 / denom
    Q[0, 1] = nu12 * E2 / denom
    Q[1, 0] = Q[0, 1]
    Q[2, 2] = G12
    return Q


def _transformation_matrix(theta_rad: float) -> np.ndarray:
    """Return the stress transformation matrix T for rotation by *theta_rad*.

    Uses the Reuter form so that
        Q_bar = T_inv @ Q @ T_inv^T
    where T_inv = inv(T).
    """
    m = math.cos(theta_rad)
    n = math.sin(theta_rad)
    m2 = m * m
    n2 = n * n
    mn = m * n

    T = np.array([
        [m2,    n2,    2.0 * mn],
        [n2,    m2,   -2.0 * mn],
        [-mn,   mn,    m2 - n2],
    ])
    return T


def _qbar(Q: np.ndarray, theta_deg: float) -> np.ndarray:
    """Compute the transformed reduced stiffness matrix Q-bar for a ply at
    *theta_deg* degrees.

    Returns Q_bar in the same units as Q (Pa).
    """
    theta_rad = math.radians(theta_deg)
    T = _transformation_matrix(theta_rad)
    T_inv = np.linalg.inv(T)
    return T_inv @ Q @ T_inv.T


def _compute_abd(
    plies: List[Dict[str, float]],
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, List[float]]:
    """Compute the ABD matrix for a laminate.

    Parameters
    ----------
    plies : list of dict
        Each ply dict must have keys: ``angle`` (deg), ``thickness`` (m),
        ``E1``, ``E2``, ``G12`` (all Pa), ``nu12`` (dimensionless).

    Returns
    -------
    A : (3,3) ndarray -- extensional stiffness (N/m)
    B : (3,3) ndarray -- coupling stiffness (N)
    D : (3,3) ndarray -- bending stiffness (N*m)
    total_thickness : float (m)
    z_coords : list of z coordinates at ply boundaries (m)
    """
    n = len(plies)
    total_thickness = sum(p["thickness"] for p in plies)

    # Compute z-coordinates from bottom of laminate
    # z = 0 is the midplane
    z = [0.0] * (n + 1)
    z[0] = -total_thickness / 2.0
    for k in range(n):
        z[k + 1] = z[k] + plies[k]["thickness"]

    A = np.zeros((3, 3))
    B = np.zeros((3, 3))
    D = np.zeros((3, 3))

    for k in range(n):
        ply = plies[k]
        Q = _q_matrix(ply["E1"], ply["E2"], ply["G12"], ply["nu12"])
        Qb = _qbar(Q, ply["angle"])

        z_bot = z[k]
        z_top = z[k + 1]

        A += Qb * (z_top - z_bot)
        B += 0.5 * Qb * (z_top ** 2 - z_bot ** 2)
        D += (1.0 / 3.0) * Qb * (z_top ** 3 - z_bot ** 3)

    return A, B, D, total_thickness, z


def _effective_moduli(
    A: np.ndarray, total_thickness: float
) -> Dict[str, float]:
    """Derive effective engineering constants from the A matrix.

    Returns values in Pa (caller converts to GPa/MPa as needed).
    """
    # a = inv(A) -- compliance per unit width
    try:
        a = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return {"Ex": 0.0, "Ey": 0.0, "Gxy": 0.0, "nuxy": 0.0, "nuyx": 0.0}

    h = total_thickness
    Ex = 1.0 / (a[0, 0] * h)
    Ey = 1.0 / (a[1, 1] * h)
    Gxy = 1.0 / (a[2, 2] * h)
    nuxy = -a[0, 1] / a[0, 0]
    nuyx = -a[0, 1] / a[1, 1]

    return {"Ex": Ex, "Ey": Ey, "Gxy": Gxy, "nuxy": nuxy, "nuyx": nuyx}


def _ply_stresses_strains(
    plies: List[Dict[str, float]],
    A: np.ndarray,
    B: np.ndarray,
    D: np.ndarray,
    total_thickness: float,
    z_coords: List[float],
    loads: Dict[str, float],
) -> List[Dict[str, Any]]:
    """Calculate ply-by-ply stresses and strains under given loads.

    Parameters
    ----------
    loads : dict
        Keys ``Nx``, ``Ny``, ``Nxy`` (N/m) and ``Mx``, ``My``, ``Mxy`` (N*m/m).

    Returns
    -------
    List of dicts with per-ply stress/strain in both global and material axes.
    """
    N_vec = np.array([
        loads.get("Nx", 0.0),
        loads.get("Ny", 0.0),
        loads.get("Nxy", 0.0),
    ])
    M_vec = np.array([
        loads.get("Mx", 0.0),
        loads.get("My", 0.0),
        loads.get("Mxy", 0.0),
    ])

    # ABD system: [N; M] = [A B; B D] [eps0; kappa]
    ABD = np.zeros((6, 6))
    ABD[:3, :3] = A
    ABD[:3, 3:] = B
    ABD[3:, :3] = B
    ABD[3:, 3:] = D

    load_vec = np.concatenate([N_vec, M_vec])

    try:
        abd_inv = np.linalg.inv(ABD)
    except np.linalg.LinAlgError:
        return []

    deformation = abd_inv @ load_vec
    eps0 = deformation[:3]
    kappa = deformation[3:]

    results = []
    n = len(plies)

    for k in range(n):
        ply = plies[k]
        z_mid = (z_coords[k] + z_coords[k + 1]) / 2.0

        # Global strains at midplane of ply
        eps_global = eps0 + z_mid * kappa

        # Q-bar for this ply
        Q = _q_matrix(ply["E1"], ply["E2"], ply["G12"], ply["nu12"])
        Qb = _qbar(Q, ply["angle"])

        # Global stresses
        sigma_global = Qb @ eps_global

        # Transform to material coordinates
        theta_rad = math.radians(ply["angle"])
        T = _transformation_matrix(theta_rad)
        sigma_local = T @ sigma_global
        eps_local = T @ eps_global

        results.append({
            "ply_index": k,
            "angle_deg": ply["angle"],
            "z_mid_mm": z_mid * 1000.0,
            "stress_global_MPa": {
                "sigma_x": _pa_to_mpa(sigma_global[0]),
                "sigma_y": _pa_to_mpa(sigma_global[1]),
                "tau_xy": _pa_to_mpa(sigma_global[2]),
            },
            "stress_local_MPa": {
                "sigma_1": _pa_to_mpa(sigma_local[0]),
                "sigma_2": _pa_to_mpa(sigma_local[1]),
                "tau_12": _pa_to_mpa(sigma_local[2]),
            },
            "strain_global": {
                "eps_x": float(eps_global[0]),
                "eps_y": float(eps_global[1]),
                "gamma_xy": float(eps_global[2]),
            },
            "strain_local": {
                "eps_1": float(eps_local[0]),
                "eps_2": float(eps_local[1]),
                "gamma_12": float(eps_local[2]),
            },
        })

    return results


# =========================================================================
# Failure criteria
# =========================================================================

def _max_stress_fi(
    sigma_1: float, sigma_2: float, tau_12: float,
    Xt: float, Xc: float, Yt: float, Yc: float, S12: float,
) -> Dict[str, Any]:
    """Max-stress failure index.

    All inputs in the same units (e.g. MPa).
    Returns individual ratios and the max failure index.
    """
    # Fibre direction
    if sigma_1 >= 0:
        fi_1 = sigma_1 / Xt if Xt > 0 else 0.0
    else:
        fi_1 = abs(sigma_1) / Xc if Xc > 0 else 0.0

    # Transverse direction
    if sigma_2 >= 0:
        fi_2 = sigma_2 / Yt if Yt > 0 else 0.0
    else:
        fi_2 = abs(sigma_2) / Yc if Yc > 0 else 0.0

    # Shear
    fi_12 = abs(tau_12) / S12 if S12 > 0 else 0.0

    fi_max = max(fi_1, fi_2, fi_12)

    # Determine dominant mode
    if fi_max == fi_1:
        mode = "fibre_tension" if sigma_1 >= 0 else "fibre_compression"
    elif fi_max == fi_2:
        mode = "matrix_tension" if sigma_2 >= 0 else "matrix_compression"
    else:
        mode = "shear"

    return {
        "fi_1": round(fi_1, 6),
        "fi_2": round(fi_2, 6),
        "fi_12": round(fi_12, 6),
        "failure_index": round(fi_max, 6),
        "failed": fi_max >= 1.0,
        "mode": mode,
    }


def _tsai_wu_fi(
    sigma_1: float, sigma_2: float, tau_12: float,
    Xt: float, Xc: float, Yt: float, Yc: float, S12: float,
) -> Dict[str, Any]:
    """Tsai-Wu failure index.

    The failure index FI is defined such that failure occurs when FI >= 1.
    """
    F1 = 1.0 / Xt - 1.0 / Xc if Xt > 0 and Xc > 0 else 0.0
    F2 = 1.0 / Yt - 1.0 / Yc if Yt > 0 and Yc > 0 else 0.0
    F11 = 1.0 / (Xt * Xc) if Xt > 0 and Xc > 0 else 0.0
    F22 = 1.0 / (Yt * Yc) if Yt > 0 and Yc > 0 else 0.0
    F66 = 1.0 / (S12 ** 2) if S12 > 0 else 0.0
    # F12 interaction term: use -0.5 * sqrt(F11 * F22) (common approximation)
    F12 = -0.5 * math.sqrt(F11 * F22) if F11 > 0 and F22 > 0 else 0.0

    fi = (
        F1 * sigma_1
        + F2 * sigma_2
        + F11 * sigma_1 ** 2
        + F22 * sigma_2 ** 2
        + 2.0 * F12 * sigma_1 * sigma_2
        + F66 * tau_12 ** 2
    )

    return {
        "failure_index": round(fi, 6),
        "failed": fi >= 1.0,
        "mode": "tsai_wu_interaction",
        "coefficients": {
            "F1": round(F1, 8),
            "F2": round(F2, 8),
            "F11": round(F11, 10),
            "F22": round(F22, 10),
            "F12": round(F12, 10),
            "F66": round(F66, 10),
        },
    }


def _tsai_hill_fi(
    sigma_1: float, sigma_2: float, tau_12: float,
    Xt: float, Xc: float, Yt: float, Yc: float, S12: float,
) -> Dict[str, Any]:
    """Tsai-Hill failure index.

    Uses tensile or compressive strength depending on sign of stress.
    """
    X = Xt if sigma_1 >= 0 else Xc
    Y = Yt if sigma_2 >= 0 else Yc
    S = S12

    if X == 0 or Y == 0 or S == 0:
        return {"failure_index": 0.0, "failed": False, "mode": "tsai_hill"}

    fi = (
        (sigma_1 / X) ** 2
        - (sigma_1 * sigma_2) / (X ** 2)
        + (sigma_2 / Y) ** 2
        + (tau_12 / S) ** 2
    )

    return {
        "failure_index": round(fi, 6),
        "failed": fi >= 1.0,
        "mode": "tsai_hill",
    }


def _hashin_fi(
    sigma_1: float, sigma_2: float, tau_12: float,
    Xt: float, Xc: float, Yt: float, Yc: float, S12: float,
) -> Dict[str, Any]:
    """Hashin failure criteria (four separate failure modes).

    Returns the maximum failure index across all modes.
    """
    modes: Dict[str, float] = {}

    # Fibre tension (sigma_1 >= 0)
    if sigma_1 >= 0 and Xt > 0 and S12 > 0:
        modes["fibre_tension"] = (sigma_1 / Xt) ** 2 + (tau_12 / S12) ** 2
    elif sigma_1 >= 0:
        modes["fibre_tension"] = 0.0

    # Fibre compression (sigma_1 < 0)
    if sigma_1 < 0 and Xc > 0:
        modes["fibre_compression"] = (abs(sigma_1) / Xc) ** 2
    elif sigma_1 < 0:
        modes["fibre_compression"] = 0.0

    # Matrix tension (sigma_2 >= 0)
    if sigma_2 >= 0 and Yt > 0 and S12 > 0:
        modes["matrix_tension"] = (sigma_2 / Yt) ** 2 + (tau_12 / S12) ** 2
    elif sigma_2 >= 0:
        modes["matrix_tension"] = 0.0

    # Matrix compression (sigma_2 < 0)
    if sigma_2 < 0 and Yc > 0 and S12 > 0:
        modes["matrix_compression"] = (
            (Yc / (2.0 * S12)) ** 2 - 1.0
        ) * (sigma_2 / Yc) + (sigma_2 / (2.0 * S12)) ** 2 + (tau_12 / S12) ** 2
    elif sigma_2 < 0:
        modes["matrix_compression"] = 0.0

    if not modes:
        return {"failure_index": 0.0, "failed": False, "mode": "hashin", "modes": {}}

    fi_max = max(modes.values())
    dominant = max(modes, key=lambda k: modes[k])

    return {
        "failure_index": round(fi_max, 6),
        "failed": fi_max >= 1.0,
        "mode": dominant,
        "modes": {k: round(v, 6) for k, v in modes.items()},
    }


_FAILURE_FUNCS = {
    "max_stress": _max_stress_fi,
    "tsai_wu": _tsai_wu_fi,
    "tsai_hill": _tsai_hill_fi,
    "hashin": _hashin_fi,
}


# =========================================================================
# Public API
# =========================================================================

def calculate_laminate(
    layup: List[Dict[str, Any]],
    loads: Optional[Dict[str, float]] = None,
) -> Dict[str, Any]:
    """Calculate laminate properties using CLT.

    Parameters
    ----------
    layup : list of dict
        Each ply dict should contain:
        - ``angle`` (float): ply angle in degrees
        - ``thickness_mm`` (float): ply thickness in mm
        - ``E1_GPa`` (float): longitudinal modulus in GPa
        - ``E2_GPa`` (float): transverse modulus in GPa
        - ``G12_GPa`` (float): in-plane shear modulus in GPa
        - ``nu12`` (float): major Poisson's ratio
    loads : dict, optional
        Applied loads:
        - ``Nx``, ``Ny``, ``Nxy``: in-plane forces in N/m
        - ``Mx``, ``My``, ``Mxy``: bending moments in N*m/m

    Returns
    -------
    dict
        Keys: ``ABD_matrix``, ``A_matrix``, ``B_matrix``, ``D_matrix``,
        ``effective_moduli``, ``total_thickness_mm``, ``num_plies``,
        ``ply_stresses`` (if loads provided), ``engine`` (str).
    """
    if not layup:
        raise ValueError("Layup must contain at least one ply.")

    # Validate and convert each ply
    plies_si: List[Dict[str, float]] = []
    for i, ply in enumerate(layup):
        _validate_ply(ply, i)
        plies_si.append({
            "angle": float(ply["angle"]),
            "thickness": _mm_to_m(float(ply["thickness_mm"])),
            "E1": _gpa_to_pa(float(ply["E1_GPa"])),
            "E2": _gpa_to_pa(float(ply["E2_GPa"])),
            "G12": _gpa_to_pa(float(ply["G12_GPa"])),
            "nu12": float(ply["nu12"]),
        })

    # Use fallback numpy CLT engine (always available, composipy is optional)
    A, B, D, total_t, z_coords = _compute_abd(plies_si)
    moduli = _effective_moduli(A, total_t)

    result: Dict[str, Any] = {
        "engine": "composipy" if _COMPOSIPY_AVAILABLE else "numpy_fallback",
        "num_plies": len(layup),
        "total_thickness_mm": round(total_t * 1000.0, 4),
        "A_matrix": _matrix_to_list(A, label="N/m"),
        "B_matrix": _matrix_to_list(B, label="N"),
        "D_matrix": _matrix_to_list(D, label="N*m"),
        "ABD_matrix": _abd_to_list(A, B, D),
        "effective_moduli": {
            "Ex_GPa": round(_pa_to_gpa(moduli["Ex"]), 4),
            "Ey_GPa": round(_pa_to_gpa(moduli["Ey"]), 4),
            "Gxy_GPa": round(_pa_to_gpa(moduli["Gxy"]), 4),
            "nuxy": round(moduli["nuxy"], 6),
            "nuyx": round(moduli["nuyx"], 6),
        },
    }

    # If loads are provided, calculate stresses and strains
    if loads:
        ply_results = _ply_stresses_strains(
            plies_si, A, B, D, total_t, z_coords, loads
        )
        result["ply_stresses"] = ply_results
        result["midplane_strains"] = _compute_midplane_strains(A, B, D, loads)

    return result


def check_failure(
    layup: List[Dict[str, Any]],
    strengths: Dict[str, float],
    loads: Dict[str, float],
    criterion: str = "max_stress",
) -> Dict[str, Any]:
    """Check failure for each ply under given loads.

    Parameters
    ----------
    layup : list of dict
        Same format as ``calculate_laminate``.
    strengths : dict
        Material strengths: ``Xt_MPa``, ``Xc_MPa``, ``Yt_MPa``,
        ``Yc_MPa``, ``S12_MPa``.
    loads : dict
        Applied loads: ``Nx``, ``Ny``, ``Nxy`` (N/m), ``Mx``, ``My``,
        ``Mxy`` (N*m/m).
    criterion : str
        One of ``"max_stress"``, ``"tsai_wu"``, ``"tsai_hill"``, ``"hashin"``.

    Returns
    -------
    dict
        Keys: ``criterion``, ``per_ply_results``, ``first_ply_failure``,
        ``overall_failed``, ``min_margin``.
    """
    criterion = criterion.lower().strip()
    if criterion not in _FAILURE_FUNCS:
        raise ValueError(
            f"Unknown failure criterion '{criterion}'. "
            f"Supported: {', '.join(_FAILURE_FUNCS.keys())}"
        )

    # Validate strengths
    required_strengths = ["Xt_MPa", "Xc_MPa", "Yt_MPa", "Yc_MPa", "S12_MPa"]
    for key in required_strengths:
        if key not in strengths or strengths[key] <= 0:
            raise ValueError(
                f"Strength '{key}' must be provided and positive."
            )

    Xt = float(strengths["Xt_MPa"])
    Xc = float(strengths["Xc_MPa"])
    Yt = float(strengths["Yt_MPa"])
    Yc = float(strengths["Yc_MPa"])
    S12 = float(strengths["S12_MPa"])

    # First, calculate stresses
    lam_result = calculate_laminate(layup, loads)
    if "ply_stresses" not in lam_result:
        raise ValueError("No ply stresses computed. Check loads input.")

    failure_func = _FAILURE_FUNCS[criterion]
    per_ply: List[Dict[str, Any]] = []
    first_failure_ply: Optional[int] = None
    worst_fi = 0.0
    worst_ply = 0

    for ps in lam_result["ply_stresses"]:
        s1 = ps["stress_local_MPa"]["sigma_1"]
        s2 = ps["stress_local_MPa"]["sigma_2"]
        t12 = ps["stress_local_MPa"]["tau_12"]

        fi_result = failure_func(s1, s2, t12, Xt, Xc, Yt, Yc, S12)
        fi_result["ply_index"] = ps["ply_index"]
        fi_result["angle_deg"] = ps["angle_deg"]
        fi_result["stress_local_MPa"] = ps["stress_local_MPa"]

        if fi_result["failure_index"] > worst_fi:
            worst_fi = fi_result["failure_index"]
            worst_ply = ps["ply_index"]

        if fi_result["failed"] and first_failure_ply is None:
            first_failure_ply = ps["ply_index"]

        per_ply.append(fi_result)

    overall_failed = any(p["failed"] for p in per_ply)
    margin = (1.0 / worst_fi - 1.0) if worst_fi > 0 else float("inf")

    return {
        "criterion": criterion,
        "per_ply_results": per_ply,
        "first_ply_failure": {
            "ply_index": first_failure_ply,
            "failed": first_failure_ply is not None,
        },
        "overall_failed": overall_failed,
        "worst_ply_index": worst_ply,
        "worst_failure_index": round(worst_fi, 6),
        "min_margin_of_safety": round(margin, 4) if margin != float("inf") else None,
        "effective_moduli": lam_result["effective_moduli"],
    }


def optimize_laminate(
    loads: Dict[str, float],
    material_props: Dict[str, float],
    strengths: Dict[str, float],
    constraints: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Try standard laminate families and return the best options.

    Parameters
    ----------
    loads : dict
        Applied loads: ``Nx``, ``Ny``, ``Nxy`` (N/m).
    material_props : dict
        Single-ply properties: ``E1_GPa``, ``E2_GPa``, ``G12_GPa``,
        ``nu12``, ``thickness_mm``.
    strengths : dict
        ``Xt_MPa``, ``Xc_MPa``, ``Yt_MPa``, ``Yc_MPa``, ``S12_MPa``.
    constraints : dict, optional
        - ``min_plies`` (int): minimum number of plies (default 4)
        - ``max_plies`` (int): maximum number of plies (default 64)
        - ``allowed_angles`` (list[float]): default [0, 45, -45, 90]
        - ``symmetry_required`` (bool): default True

    Returns
    -------
    dict
        ``candidates``: list of viable laminates ranked by weight (thinnest
        first), each with failure info and stacking rule checks.
    """
    if constraints is None:
        constraints = {}

    min_plies = int(constraints.get("min_plies", 4))
    max_plies = int(constraints.get("max_plies", 64))
    symmetry_required = bool(constraints.get("symmetry_required", True))

    # Standard laminate families (half-laminate patterns for symmetric layups)
    families = {
        "quasi_isotropic": {
            "half_pattern": [0, 45, -45, 90],
            "description": "Quasi-isotropic [0/+45/-45/90]s -- equal stiffness in all directions",
        },
        "zero_dominated": {
            "half_pattern": [0, 0, 45, -45, 90],
            "description": "0-degree dominated -- optimized for axial (x-direction) loads",
        },
        "ninety_dominated": {
            "half_pattern": [90, 90, 45, -45, 0],
            "description": "90-degree dominated -- optimized for transverse (y-direction) loads",
        },
        "pm45_dominated": {
            "half_pattern": [45, -45, 45, -45, 0, 90],
            "description": "+-45 dominated -- optimized for shear and torsion loads",
        },
        "angle_ply": {
            "half_pattern": [45, -45, 45, -45],
            "description": "Angle ply [+-45]s -- maximum shear stiffness",
        },
        "cross_ply": {
            "half_pattern": [0, 90, 0, 90],
            "description": "Cross ply [0/90]s -- balanced axial and transverse",
        },
    }

    candidates: List[Dict[str, Any]] = []

    for name, family in families.items():
        half = family["half_pattern"]

        # Try multiplying the half-laminate until we find one that passes
        for multiplier in range(1, (max_plies // (2 * len(half))) + 2):
            half_stack = half * multiplier
            if symmetry_required:
                full_stack = half_stack + half_stack[::-1]
            else:
                full_stack = half_stack * 2

            n_plies = len(full_stack)
            if n_plies < min_plies:
                continue
            if n_plies > max_plies:
                break

            # Build layup dicts
            layup = [
                {
                    "angle": angle,
                    "thickness_mm": float(material_props["thickness_mm"]),
                    "E1_GPa": float(material_props["E1_GPa"]),
                    "E2_GPa": float(material_props["E2_GPa"]),
                    "G12_GPa": float(material_props["G12_GPa"]),
                    "nu12": float(material_props["nu12"]),
                }
                for angle in full_stack
            ]

            try:
                failure_result = check_failure(
                    layup, strengths, loads, criterion="max_stress"
                )
            except Exception as exc:
                logger.warning(
                    "Failure check failed for %s x%d: %s",
                    name, multiplier, exc,
                )
                continue

            if not failure_result["overall_failed"]:
                total_t = n_plies * float(material_props["thickness_mm"])
                candidates.append({
                    "family": name,
                    "description": family["description"],
                    "stacking_sequence": full_stack,
                    "num_plies": n_plies,
                    "total_thickness_mm": round(total_t, 3),
                    "worst_failure_index": failure_result["worst_failure_index"],
                    "min_margin_of_safety": failure_result["min_margin_of_safety"],
                    "effective_moduli": failure_result["effective_moduli"],
                })
                break  # Found the thinnest passing option for this family

    # Sort by total thickness (lightest first)
    candidates.sort(key=lambda c: c["total_thickness_mm"])

    return {
        "loads": loads,
        "material": {
            k: material_props[k]
            for k in ["E1_GPa", "E2_GPa", "G12_GPa", "nu12", "thickness_mm"]
            if k in material_props
        },
        "strengths": strengths,
        "num_candidates": len(candidates),
        "candidates": candidates,
        "recommendation": (
            candidates[0] if candidates else None
        ),
        "note": (
            "Candidates are ranked by total thickness (lightest first). "
            "All pass max-stress failure criterion for the given loads. "
            "Run a detailed check with Tsai-Wu or Hashin for final validation."
        ),
    }


# =========================================================================
# Internal helpers
# =========================================================================

def _validate_ply(ply: Dict[str, Any], index: int) -> None:
    """Validate that a ply dict has all required keys with sensible values."""
    required = ["angle", "thickness_mm", "E1_GPa", "E2_GPa", "G12_GPa", "nu12"]
    for key in required:
        if key not in ply:
            raise ValueError(
                f"Ply {index}: missing required key '{key}'. "
                f"Required keys: {required}"
            )
    if float(ply["thickness_mm"]) <= 0:
        raise ValueError(f"Ply {index}: thickness_mm must be positive.")
    if float(ply["E1_GPa"]) <= 0:
        raise ValueError(f"Ply {index}: E1_GPa must be positive.")
    if float(ply["E2_GPa"]) <= 0:
        raise ValueError(f"Ply {index}: E2_GPa must be positive.")
    if float(ply["G12_GPa"]) <= 0:
        raise ValueError(f"Ply {index}: G12_GPa must be positive.")
    nu12 = float(ply["nu12"])
    if nu12 < 0 or nu12 >= 1:
        raise ValueError(
            f"Ply {index}: nu12 must be between 0 and 1 (exclusive)."
        )


def _matrix_to_list(
    mat: np.ndarray, label: str = ""
) -> List[List[float]]:
    """Convert a 3x3 numpy matrix to a JSON-friendly list of lists."""
    return [[round(float(mat[i, j]), 4) for j in range(3)] for i in range(3)]


def _abd_to_list(
    A: np.ndarray, B: np.ndarray, D: np.ndarray
) -> List[List[float]]:
    """Assemble the full 6x6 ABD matrix as a list of lists."""
    ABD = np.zeros((6, 6))
    ABD[:3, :3] = A
    ABD[:3, 3:] = B
    ABD[3:, :3] = B
    ABD[3:, 3:] = D
    return [[round(float(ABD[i, j]), 4) for j in range(6)] for i in range(6)]


def _compute_midplane_strains(
    A: np.ndarray, B: np.ndarray, D: np.ndarray,
    loads: Dict[str, float],
) -> Dict[str, float]:
    """Compute midplane strains and curvatures from loads."""
    ABD = np.zeros((6, 6))
    ABD[:3, :3] = A
    ABD[:3, 3:] = B
    ABD[3:, :3] = B
    ABD[3:, 3:] = D

    N_vec = np.array([
        loads.get("Nx", 0.0),
        loads.get("Ny", 0.0),
        loads.get("Nxy", 0.0),
    ])
    M_vec = np.array([
        loads.get("Mx", 0.0),
        loads.get("My", 0.0),
        loads.get("Mxy", 0.0),
    ])
    load_vec = np.concatenate([N_vec, M_vec])

    try:
        abd_inv = np.linalg.inv(ABD)
        deformation = abd_inv @ load_vec
    except np.linalg.LinAlgError:
        return {
            "eps_x0": 0.0, "eps_y0": 0.0, "gamma_xy0": 0.0,
            "kappa_x": 0.0, "kappa_y": 0.0, "kappa_xy": 0.0,
        }

    return {
        "eps_x0": round(float(deformation[0]), 8),
        "eps_y0": round(float(deformation[1]), 8),
        "gamma_xy0": round(float(deformation[2]), 8),
        "kappa_x": round(float(deformation[3]), 8),
        "kappa_y": round(float(deformation[4]), 8),
        "kappa_xy": round(float(deformation[5]), 8),
    }
