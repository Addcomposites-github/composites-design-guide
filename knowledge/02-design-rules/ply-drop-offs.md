---
title: "Ply Drop-offs"
category: "design-rules"
tags: ["ply-drop", "taper", "ramp-ratio", "thickness-transition", "drop-off"]
difficulty: "intermediate"
related: ["stacking-sequences.md", "zone-design.md", "splices-and-joints.md", "../01-fundamentals/failure-modes.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Ply Drop-offs

Real composite structures are not uniform thickness everywhere. A wing skin is thicker near the root (where loads are highest) and thinner towards the tip. A car body panel might be reinforced locally around a mounting point. To change thickness, you terminate — or "drop off" — individual plies. How you do this matters enormously for structural integrity.

## What Is a Ply Drop-off?

A ply drop-off is where a ply ends within the laminate rather than continuing to the edge of the part. The laminate transitions from a thicker region (more plies) to a thinner region (fewer plies). This creates a small step in the internal geometry — a resin-rich pocket at the termination point.

```
Side view of a ply drop-off (internal drop):

    ────────────────────────────────────   ← outer ply (continuous)
    ────────────────────────────────────   ← continuous ply
    ────────────────┐
                    │ ← dropped ply ends here
    ────────────────┘
    ════════════════════════════════════   ← tool surface

    |←  thick zone →|← thin zone       →|
```

## Why Ply Drop-offs Are Critical

The termination point is a stress concentration. At the end of a dropped ply:

- **Interlaminar stresses spike** — the sudden change in stiffness forces the surrounding plies to carry the load that the terminated ply was carrying. This transfer happens through shear between layers.
- **A resin pocket forms** — the triangular gap left by the ply end fills with pure resin, which is weaker than the surrounding fibre-reinforced material.
- **Delamination can initiate** — the combination of stress concentration and the resin pocket makes this the most likely location for delamination (layers separating).

## The Ramp Ratio

The **ramp ratio** (also called taper ratio) controls how gradually the thickness transition occurs. It is the ratio of the horizontal distance over which plies are dropped to the change in thickness.

```
Ramp ratio = horizontal distance / thickness change

    ←───── L ─────→
    ┌───────────────────────────────┐
    │               /               │
    │            /                  │   Δt = thickness change
    │         /                    │
    │      /                       │
    └───────────────────────────────┘

    Ramp ratio = L / Δt
```

**Typical ramp ratios:**
| Application | Ramp ratio | Notes |
|---|---|---|
| General aerospace | 1:20 | Conservative, most common |
| Lightly loaded structure | 1:10 | Acceptable for secondary structure |
| Highly loaded / fatigue critical | 1:30 or shallower | Spar caps, wing skins under fatigue |
| Minimum (do not go steeper) | 1:8 | Absolute minimum for most material specs |

A ramp ratio of 1:20 means that for every 1 mm of thickness change, the plies are dropped over 20 mm of length.

## Internal vs. External Drops

Plies can be dropped on the **inside** (tool side) or **outside** (bag side / outer mould line) of the laminate.

**Internal drops** (preferred in most cases):
- The outer surface remains smooth and aerodynamically clean
- The step is hidden inside the laminate
- The continuous outer plies bridge over the drop, containing the resin pocket

**External drops:**
- The step appears on the outer surface
- Simpler to manufacture in some cases (the tool surface stays flat)
- Used when the inner mould line must be smooth (e.g., inner surface of a fuel tank)

**General rule:** Drop plies internally unless there is a specific reason to drop externally.

## Stagger Distance

When multiple plies need to be dropped, do not drop them all at the same location. Stagger the drop points — space them apart along the length of the part.

```
Good — staggered drops:

    ─────────────────────────────────   continuous ply
    ────────────────────────┐
    ──────────────────┐     │           ← drops spaced apart
    ────────────┐     │     │
    ════════════════════════════════════

Bad — coincident drops:

    ─────────────────────────────────   continuous ply
    ────────────┐
    ────────────┐  ← all drops at same location = severe stress concentration
    ────────────┐
    ════════════════════════════════════
```

**Minimum stagger distance:** Typically 4–6 mm between successive ply drops, though this varies by material system and ply thickness. Some aerospace specs require stagger distances based on a multiple of ply thickness (e.g., 10× to 20× the cured ply thickness).

## Which Plies to Drop

Not all plies are equal when it comes to dropping:

1. **Drop interior plies first, keep outer plies continuous** — the outer plies provide the most bending stiffness and protect the surface.

2. **Avoid dropping 0° plies if the primary load is axial** — 0° plies carry the majority of the axial load. Dropping them introduces the largest stress redistribution.

3. **Prefer dropping ±45° or 90° plies in tension-dominated structures** — but maintain the 10% rule (at least 10% of plies in each direction at every cross-section).

4. **Maintain symmetry and balance at every cross-section** — as you drop plies, the remaining laminate at the thin end must still be symmetric and balanced. This constrains which plies you can drop. Often, plies are dropped in symmetric pairs (one above and one below the midplane).

5. **Do not drop plies at or very near a highly loaded feature** — keep drops away from bolt holes, cutouts, ply splices, and bond lines.

## Common Mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| Dropping too many plies at once | Severe stress concentration, delamination | Stagger drops with minimum spacing |
| Ramp ratio too steep (e.g., 1:5) | Peel stresses exceed interlaminar strength | Use 1:20 or shallower |
| Dropping all 0° plies in one region | Loss of axial load path, local failure | Distribute drops across orientations |
| Breaking symmetry after drops | Warping, coupling, analysis errors | Drop in symmetric pairs |
| Placing drops at a bolt hole | Fastener pulls laminate apart at the weak point | Keep drops at least 2–3 diameters away |

## Key Takeaways

- A ply drop-off is where a ply terminates inside the laminate to create a thickness change
- Ramp ratios of 1:20 are standard; never go steeper than 1:8
- Stagger successive ply drops by at least 4–6 mm — never drop multiple plies at the same location
- Drop plies internally (tool side) to keep the outer surface smooth
- Maintain symmetry and balance at every cross-section after dropping plies
- Keep ply drops away from bolt holes, cutouts, and other stress concentrations

## Further Reading / Tools

- [Stacking Sequences](stacking-sequences.md) — the rules your thinned-down laminate must still follow
- [Zone Design](zone-design.md) — organising your part into thickness zones that define where drops occur
- [Splices and Joints](splices-and-joints.md) — related topic: what happens when plies overlap rather than terminate
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — verify that your reduced layup still passes failure criteria
