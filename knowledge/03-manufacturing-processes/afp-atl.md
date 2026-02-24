---
title: "Automated Fibre Placement and Automated Tape Laying"
category: "manufacturing"
tags: ["AFP", "ATL", "automated-layup", "tow", "fibre-placement", "tape-laying"]
difficulty: "intermediate"
related: ["prepreg-and-autoclave.md", "common-defects.md", "../02-design-rules/design-for-manufacture.md", "../02-design-rules/splices-and-joints.md"]
tools: []
last_updated: "2026-02"
---

# Automated Fibre Placement and Automated Tape Laying

When a composite part is large, complex, or needs to be produced at volume, laying up prepreg by hand becomes impractical. Automated Tape Laying (ATL) and Automated Fibre Placement (AFP) are robotic processes that do the layup for you. A machine head mounted on a gantry or robot arm places prepreg tape onto the tool surface, applying heat and pressure to tack it down. These machines can lay up hundreds of kilograms of material per shift with positional accuracy better than ±1 mm.

## ATL vs. AFP: What's the Difference?

Both do the same fundamental job — place prepreg onto a tool — but they use different material formats and suit different geometries.

### Automated Tape Laying (ATL)

- Lays **wide tape**: 75 mm (3″), 150 mm (6″), or 300 mm (12″) widths
- Best for **large, flat or gently curved** surfaces — wing skins, fuselage panels, flat spars
- High deposition rate — can lay 20–50 kg/hr depending on tape width
- Limited ability to steer around tight curves or contours — the wide tape wants to go straight

### Automated Fibre Placement (AFP)

- Lays **narrow tows**: 3.175 mm (1/8″), 6.35 mm (1/4″), or 12.7 mm (1/2″) each
- Multiple tows (8, 16, 24, or 32) are placed simultaneously as a **band**
- Best for **complex curved** surfaces — fuselage barrels, nacelles, ducts, contoured skins
- Each tow can be independently started, stopped, or cut — allowing the machine to conform to complex boundaries
- Lower deposition rate than ATL for flat parts, but far more versatile on contoured geometry

```
ATL head lays one wide tape:          AFP head lays multiple narrow tows:

    ┌────────────────────────────┐     ┌──┬──┬──┬──┬──┬──┬──┬──┐
    │     150 mm wide tape       │     │t1│t2│t3│t4│t5│t6│t7│t8│
    └────────────────────────────┘     └──┴──┴──┴──┴──┴──┴──┴──┘
                                         each tow: 6.35 mm
    Good for: flat wing skin            Good for: curved nacelle
```

## How AFP Works in Detail

1. **Programming** — the part surface is divided into zones, and a software tool generates the machine path for each ply. The path defines where each tow starts, follows, and stops.
2. **Material loading** — tow spools (creels) are loaded into the machine. Each spool feeds one tow through the head.
3. **Laying a course** — the head moves over the tool surface, paying out tows and pressing them down with a compaction roller. Heat (IR lamp, laser, or hot gas) softens the resin just enough for tack.
4. **Tow cut and add** — at ply boundaries or complex shapes, individual tows are cut or restarted. This is how AFP handles contoured edges — it drops and adds tows to match the boundary.
5. **Next course** — the head indexes over by the band width and lays the adjacent course. The process repeats until the ply is complete.
6. **Repeat for each ply** — the full stacking sequence is built up ply by ply.

## Key Concepts

### Courses and Bands

A **course** is one pass of the machine head across the part. A **band** is the total width of material deposited in one course (all tows combined). Courses are laid side by side to fill a ply.

### Gaps and Overlaps

Where adjacent courses meet, there is ideally neither a gap nor an overlap. In practice:
- **Gap tolerance:** 0–2 mm between courses is typical. Larger gaps create resin-rich channels.
- **Overlap tolerance:** 0–2 mm overlap is typical. Larger overlaps create local thickness bumps.

AFP programmes are tuned to minimise both.

### Steering

AFP can **steer** tows to follow curved paths on the tool surface — for example, following a geodesic path on a fuselage barrel. There is a minimum steering radius below which the tow buckles or lifts. Typical minimum: 500–1500 mm radius depending on tow width and material.

### Tow Drops and Adds

When a ply boundary is not perpendicular to the course direction, some tows reach the boundary before others. The machine cuts individual tows as they reach the edge (**tow drops**) and restarts tows as the boundary is re-entered (**tow adds**). Each drop/add is effectively a butt splice within that tow — the same splice rules from [Splices and Joints](../02-design-rules/splices-and-joints.md) apply.

## Defects Specific to AFP/ATL

| Defect | Cause | Impact |
|---|---|---|
| Tow gaps | Courses not indexed correctly | Resin-rich channels, reduced stiffness |
| Tow overlaps | Excessive course overlap | Local thickness bumps, surface waviness |
| Tow wrinkles | Steering too tight, or tow tension issues | Fibre misalignment, strength reduction |
| Bridging | Head cannot push tow into a concavity | Unbonded region, void |
| Tow pull-off | Insufficient tack on convex surface | Loose tow, potential FOD |

## When to Use Automated Layup

| Use AFP/ATL when | Stick with hand layup when |
|---|---|
| Parts are large (> 1–2 m²) | Parts are small or one-off |
| Production volume justifies capital cost | Low volume (< 10–20 parts) |
| Complex contour requires precise tow steering | Geometry is simple and flat |
| Tight tolerances on fibre angle and position | Tolerance is relaxed |
| Reproducibility and traceability are required | Prototype / proof of concept |

**Capital cost:** An AFP cell costs $2–10 million depending on size and capability. ATL machines are similarly priced. This technology is economically viable only for programmes with hundreds to thousands of parts — or for very large structures where hand layup is physically impractical.

## Emerging Developments

- **Dry fibre AFP** — placing dry tows (no resin), then infusing with liquid resin. Combines AFP precision with infusion cost savings.
- **Thermoplastic AFP** — placing thermoplastic prepreg tows, using laser heating to weld tows in place. No autoclave needed — the part is consolidated as it is laid up (in-situ consolidation).
- **Smaller, more affordable AFP systems** — desktop and small gantry AFP machines are emerging for research, small production, and education.

## Key Takeaways

- ATL lays wide tape for large flat parts; AFP lays multiple narrow tows for complex curved parts
- AFP can start, stop, and cut individual tows to match complex ply boundaries
- Course gaps and overlaps must be controlled (0–2 mm tolerance typical)
- Tow steering has a minimum radius — too tight and the tow wrinkles or lifts
- AFP/ATL is justified for large parts, high volumes, or where precision and traceability are required
- Capital cost is high ($2–10M+), making it an aerospace and industrial-scale technology

## Further Reading / Tools

- [Prepreg and Autoclave](prepreg-and-autoclave.md) — the material and cure process used with AFP/ATL
- [Splices and Joints](../02-design-rules/splices-and-joints.md) — every tow start/stop is a splice
- [Design for Manufacture](../02-design-rules/design-for-manufacture.md) — how AFP/ATL capabilities influence design decisions
- [Common Defects](common-defects.md) — gap, overlap, and wrinkle defects in automated layup
