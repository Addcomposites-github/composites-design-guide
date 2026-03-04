"""Stacking rule verification service.

Checks a composite laminate stacking sequence against standard design
rules: symmetry, balance, 10 % rule, and consecutive ply limit.
Direct Python port of the stacking-check functions from
mcp-server/src/index.ts.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Individual rule checks
# ---------------------------------------------------------------------------

def check_symmetry(angles: List[float]) -> Dict[str, Any]:
    """Check whether the laminate is symmetric about its midplane.

    For each ply *i* from the top, the corresponding ply from the
    bottom (ply *n-1-i*) must have the same angle.

    Returns
    -------
    dict
        ``rule``, ``passed`` (bool), ``detail`` (str).
    """
    n = len(angles)
    symmetric = True
    mismatches: List[str] = []

    for i in range(n // 2):
        if angles[i] != angles[n - 1 - i]:
            symmetric = False
            mismatches.append(
                f"Ply {i + 1} ({angles[i]}deg) != "
                f"Ply {n - i} ({angles[n - 1 - i]}deg)"
            )

    if symmetric:
        detail = f"Laminate is symmetric about the midplane ({n} plies)."
    else:
        detail = (
            f"Laminate is NOT symmetric. Mismatches: "
            f"{'; '.join(mismatches)}. "
            f"Non-symmetric laminates have bending-stretching coupling "
            f"(B matrix != 0), causing warping during cure and under load."
        )

    return {"rule": "Symmetry", "passed": symmetric, "detail": detail}


def check_balance(angles: List[float]) -> Dict[str, Any]:
    """Check whether every +theta ply has a matching -theta ply.

    0 and 90 degree plies do not need balancing.

    Returns
    -------
    dict
        ``rule``, ``passed`` (bool), ``detail`` (str).
    """
    counts: Dict[float, int] = {}
    for a in angles:
        normalised = ((a % 360) + 360) % 360
        counts[normalised] = counts.get(normalised, 0) + 1

    imbalances: List[str] = []
    checked: set[float] = set()

    for a in angles:
        normalised = ((a % 360) + 360) % 360
        if normalised in checked:
            continue
        checked.add(normalised)

        # 0 and 90 (and their equivalents 180, 270) do not need balancing
        if normalised in (0, 90, 180, 270):
            continue

        complement = (360 - normalised) % 360
        positive_count = counts.get(normalised, 0)
        negative_count = counts.get(complement, 0)
        checked.add(complement)

        if positive_count != negative_count:
            angle_label = normalised if normalised <= 180 else normalised - 360
            comp_label = complement if complement <= 180 else complement - 360
            imbalances.append(
                f"{angle_label}deg has {positive_count} plies but "
                f"{comp_label}deg has {negative_count} plies"
            )

    balanced = len(imbalances) == 0
    if balanced:
        detail = (
            "Laminate is balanced: every +theta ply has a matching -theta ply."
        )
    else:
        detail = (
            f"Laminate is NOT balanced. {'; '.join(imbalances)}. "
            f"Unbalanced laminates develop shear-extension coupling "
            f"under in-plane loads, causing unexpected twisting."
        )

    return {"rule": "Balance", "passed": balanced, "detail": detail}


def check_ten_percent_rule(angles: List[float]) -> Dict[str, Any]:
    """Check that each major orientation (0, +/-45, 90) has >= 10 % of plies.

    Returns
    -------
    dict
        ``rule``, ``passed`` (bool), ``detail`` (str).
    """
    n = len(angles)
    if n == 0:
        return {"rule": "10% Rule", "passed": False, "detail": "No plies provided."}

    count_0 = 0
    count_45 = 0
    count_90 = 0
    count_other = 0

    for a in angles:
        normalised = ((a % 180) + 180) % 180  # Map to 0-179
        if normalised == 0:
            count_0 += 1
        elif normalised in (45, 135):
            count_45 += 1
        elif normalised == 90:
            count_90 += 1
        else:
            count_other += 1

    pct_0 = (count_0 / n) * 100
    pct_45 = (count_45 / n) * 100
    pct_90 = (count_90 / n) * 100

    violations: List[str] = []
    if pct_0 < 10:
        violations.append(f"0deg: {count_0} plies ({pct_0:.1f}%) < 10%")
    if pct_45 < 10:
        violations.append(f"+/-45deg: {count_45} plies ({pct_45:.1f}%) < 10%")
    if pct_90 < 10:
        violations.append(f"90deg: {count_90} plies ({pct_90:.1f}%) < 10%")

    passed = len(violations) == 0
    summary_parts = [
        f"0deg: {count_0} plies ({pct_0:.1f}%)",
        f"+/-45deg: {count_45} plies ({pct_45:.1f}%)",
        f"90deg: {count_90} plies ({pct_90:.1f}%)",
    ]
    if count_other > 0:
        pct_other = (count_other / n) * 100
        summary_parts.append(
            f"Other angles: {count_other} plies ({pct_other:.1f}%)"
        )
    summary = ", ".join(summary_parts)

    if passed:
        detail = (
            f"All major orientations have at least 10% representation. "
            f"{summary}."
        )
    else:
        detail = (
            f"10% rule VIOLATED. {'; '.join(violations)}. "
            f"Distribution: {summary}. "
            f"The 10% rule ensures minimum stiffness and strength in all "
            f"directions to prevent unexpected matrix-dominated failures."
        )

    return {"rule": "10% Rule", "passed": passed, "detail": detail}


def check_consecutive_plies(
    angles: List[float],
    max_consecutive: int = 4,
) -> Dict[str, Any]:
    """Check that no more than *max_consecutive* plies of the same angle
    appear in a row.

    Returns
    -------
    dict
        ``rule``, ``passed`` (bool), ``detail`` (str).
    """
    if len(angles) == 0:
        return {
            "rule": f"Consecutive Ply Limit (max {max_consecutive})",
            "passed": True,
            "detail": "No plies provided.",
        }

    violations: List[str] = []
    run_angle = angles[0]
    run_start = 0
    run_length = 1

    for i in range(1, len(angles)):
        if angles[i] == run_angle:
            run_length += 1
            if run_length == max_consecutive + 1:
                violations.append(
                    f"{run_length}+ consecutive {run_angle}deg plies "
                    f"starting at ply {run_start + 1}"
                )
        else:
            # Update the last violation count if run grew
            if run_length > max_consecutive and violations:
                violations[-1] = (
                    f"{run_length} consecutive {run_angle}deg plies "
                    f"starting at ply {run_start + 1}"
                )
            run_angle = angles[i]
            run_start = i
            run_length = 1

    # Final run check
    if run_length > max_consecutive and violations:
        violations[-1] = (
            f"{run_length} consecutive {run_angle}deg plies "
            f"starting at ply {run_start + 1}"
        )

    passed = len(violations) == 0
    if passed:
        detail = (
            f"No more than {max_consecutive} consecutive plies of the "
            f"same angle anywhere in the laminate."
        )
    else:
        detail = (
            f"Consecutive ply limit VIOLATED. {'; '.join(violations)}. "
            f"Thick blocks of same-angle plies create high interlaminar "
            f"stresses and promote matrix cracking and delamination."
        )

    return {
        "rule": f"Consecutive Ply Limit (max {max_consecutive})",
        "passed": passed,
        "detail": detail,
    }


# ---------------------------------------------------------------------------
# Convenience: check all rules at once
# ---------------------------------------------------------------------------

def check_all(
    angles: List[float],
    max_consecutive: int = 4,
) -> List[Dict[str, Any]]:
    """Run all four stacking rule checks and return the results.

    Parameters
    ----------
    angles : list of float
        Ply angles in degrees, top to bottom.
    max_consecutive : int
        Max allowed consecutive same-angle plies (default 4).

    Returns
    -------
    list of dict
        One dict per rule with ``rule``, ``passed``, ``detail``.
    """
    return [
        check_symmetry(angles),
        check_balance(angles),
        check_ten_percent_rule(angles),
        check_consecutive_plies(angles, max_consecutive),
    ]
