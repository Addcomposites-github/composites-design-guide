---
title: "Analysis Tools in Composites CAD"
category: "catia"
tags: ["analysis", "core-sampling", "numerical-analysis", "ply-section", "inspection"]
difficulty: "intermediate"
related: ["ply-creation-workflow.md", "stacking-and-sequences.md", "flat-pattern-and-flattening.md", "../04-structural-analysis/sizing-a-panel.md"]
tools: []
last_updated: "2026-02"
---

# Analysis Tools in Composites CAD

Composites CAD tools include built-in analysis features that let you inspect, verify, and interrogate the laminate without leaving the design environment. These are not full structural FEA tools — they are design-time checks that catch problems before the model goes to the stress engineer or the shop floor.

## On-the-Fly Information

The most frequently used analysis is **on-the-fly information** — pointing at any element in the model and seeing its properties immediately. Information is available for:

- **Plies** — material, direction, contour area, position in the stacking
- **Ply groups** — total number of plies, total thickness, material breakdown
- **Sequences** — number of plies, sequence order
- **Limit contours** — stagger values, stagger direction
- **Cut pieces** — splice zones, overlap values
- **Material excess** — excess dimensions at each edge
- **Producibility** — fibre deviation at the cursor location

This instant feedback accelerates design decisions — you do not have to run a separate report to see basic ply information.

## Core Sampling

**Core sampling** is the composites equivalent of taking a cross-section through the laminate at a specific point. You select a location on the part surface, and the tool reports:

- Every ply that passes through that point
- Each ply's material, orientation, and thickness
- The total laminate thickness at that point
- The stacking order from tool surface to bag surface

```
Core sample at point P:

    Point P on the part surface
            ↓
    ┌──────────────┐  Ply 8: ±45° carbon, 0.13 mm
    ├──────────────┤  Ply 7: 0°   carbon, 0.13 mm
    ├──────────────┤  Ply 6: 90°  carbon, 0.13 mm
    ├──────────────┤  Ply 5: 0°   carbon, 0.13 mm
    ├──────────────┤  Ply 4: ±45° carbon, 0.13 mm
    ├──────────────┤  Ply 3: 0°   carbon, 0.13 mm
    ├──────────────┤  Ply 2: 90°  carbon, 0.13 mm
    ├──────────────┤  Ply 1: ±45° carbon, 0.13 mm
    └══════════════┘  Tool surface
    Total: 8 plies, 1.04 mm
```

Core sampling is used to:
- Verify the laminate at critical locations (bolt holes, load introduction points)
- Generate stack-up files for specific locations for FEA input
- Compare the actual stacking against the design intent from zone definitions

Results can be exported for documentation or FEA preprocessing.

## Numerical Analysis

Composites CAD tools can perform basic **numerical analysis** on the laminate:

- **Thickness distribution** — a colour map showing total laminate thickness across the entire part surface. Useful for identifying unexpectedly thick or thin regions.
- **Ply count distribution** — number of plies at each point, colour-coded
- **Orientation distribution** — percentage of plies in each direction at each point
- **Stacking compliance** — visual check of symmetry, balance, and other rules across the part

These are not structural analyses (no stress, no failure checking) — they are geometric and laminate-level checks. For structural analysis, export the laminate data to a dedicated FEA tool.

## Ply Sections

A **ply section** cuts through the laminate along a plane, showing the cross-section of every ply. This reveals:

- Ply drop-off locations and ramp geometry
- Core samples along an entire line (not just a single point)
- The relationship between zone thickness and ply coverage
- Any gaps, overlaps, or misalignments between adjacent plies

Section types include:
- **Linear** — a straight cut across the part
- **Block** — a thick section showing a slab of the laminate
- **Surfacic** — a section following a curved surface
- **Ramp** — following the slope of a ply drop-off

Sections can be generated as drawings (CATDrawing format) for documentation and design review.

## Producibility Inspection

Beyond the producibility analysis done during flattening (fibre deviation, shear angle), a dedicated **producibility inspection** tool performs the analysis across the entire part or a selection of ply groups, and exports the results:

- Fibre deviation maps per ply
- Shear angle maps (for woven fabrics)
- Limit angle violations flagged automatically
- Full producibility reports exportable for review

This is the tool that determines whether a ply can be manufactured as designed, or whether the design needs darts, material changes, or geometry modifications.

## Zones Bridge Analysis

After creating zones and transition zones, a **zones bridge analysis** checks the geometric connections between zones:

- Are all zones properly connected through transition zones?
- Are there geometric gaps or overlaps between zones?
- Is the solid model consistent with the zone definitions?

This is the geometric validation step that catches errors in the preliminary design before plies are generated.

## Key Takeaways

- On-the-fly information provides instant ply properties at the cursor — the fastest way to check the design
- Core sampling reports the full laminate stack-up at any point on the part surface
- Numerical analysis provides colour-mapped thickness and orientation distributions across the part
- Ply sections cut through the laminate to reveal drop-off geometry and ply stacking visually
- Producibility inspection flags fibre deviation and shear angle violations before manufacturing
- These are design-time checks — not structural FEA. Export laminate data for stress analysis.

## Further Reading / Tools

- [Flat Pattern and Flattening](flat-pattern-and-flattening.md) — producibility analysis during flattening
- [Ply Creation Workflow](ply-creation-workflow.md) — the plies being analysed
- [Sizing a Panel](../04-structural-analysis/sizing-a-panel.md) — structural analysis after CAD design
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — the rules that numerical analysis checks

> Workflow concepts informed by CATIA V5 Composites Design documentation.
