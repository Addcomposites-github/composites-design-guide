---
title: "Manufacturing Preparation and Document Synchronisation"
category: "catia"
tags: ["manufacturing", "skin-swap", "stagger", "core", "synchronisation"]
difficulty: "advanced"
related: ["ply-book-generation.md", "flat-pattern-and-flattening.md", "../02-design-rules/material-excess-and-boundaries.md"]
tools: []
last_updated: "2026-02"
---

# Manufacturing Preparation and Document Synchronisation

Composites design does not end when the engineering model is complete. A separate manufacturing preparation phase translates the engineering definition into shop-floor-ready data. Industry-leading tools like CATIA separate engineering and manufacturing into distinct but synchronised models, and this pattern applies regardless of which software you use.

## Engineering vs Manufacturing Model

The engineering model defines what the part must be structurally: ply orientations, stacking sequences, zone definitions, and material specifications. The manufacturing model adds everything the shop floor needs that the stress engineer does not: material excess, trim lines, flat patterns, ply books, and layup sequences.

```mermaid
graph LR
    A[Engineering Model] -->|Synchronise| B[Manufacturing Model]
    B --> C[Skin Swap if needed]
    C --> D[Define EOP / EEOP / MEOP]
    D --> E[Add stagger origin points]
    E --> F[Generate flat patterns]
    F --> G[Create ply book]
    G --> H[Export data to CNC / MES]
```

**Why separate them?** Because engineering changes happen. When the stress team updates the laminate, the manufacturing model must update automatically — without losing manufacturing-specific additions like trim lines and flat pattern tweaks. Synchronisation ensures this round-trip works cleanly.

## Creating a Manufacturing Document

The manufacturing document is created from the engineering model, either as a new part or within the existing document. It inherits:
- All ply definitions (geometry, material, orientation, stacking order)
- Zone and group structure
- Reference surfaces and rosettes

What it adds:
- Manufacturing-specific ply boundaries (MEOP)
- Stagger origin points
- Flat pattern data
- Ply book pages
- Core insert definitions for local reinforcement

## Synchronising Engineering and Manufacturing

When the engineering model changes (a ply is added, removed, or its geometry modified), the manufacturing model must be synchronised. The synchronisation process:

1. **Detects changes** — identifies which plies were added, removed, or modified
2. **Propagates geometry** — updates ply contours in the manufacturing model
3. **Preserves manufacturing data** — keeps existing flat patterns, trim lines, and ply book settings where they still apply
4. **Flags conflicts** — highlights cases where a manufacturing addition (e.g., a dart) conflicts with the engineering change

Best practice: synchronise after each engineering design iteration, not just at the end. Early synchronisation catches manufacturing feasibility issues before the design is frozen.

## Skin Swapping

Skin swapping reverses the draping direction — critical when the layup tool surface differs from the engineering reference surface.

**When skin swapping is needed:**
- Engineering defines the part from the OML (aerodynamic surface), but the layup tool is IML (inner surface)
- The stacking order in engineering is top-to-bottom, but manufacturing needs bottom-to-top for the chosen tool
- A female mould (OML tool) requires material laid on the concave side; a male mould (IML tool) requires the convex side

**What happens during skin swap:**
- The ply stacking order is reversed
- The draping direction flips
- Ply contours are re-projected onto the manufacturing surface
- Material excess and trim lines reference the new surface

**Skin swapping with wrap curves** handles complex geometry where simple projection is not sufficient. A wrap curve defines how the material wraps around features like flanges, joggle transitions, or undercuts. The manufacturing tool uses these curves to guide the re-projection of ply contours onto the manufacturing surface.

## Stagger Origin Points

A stagger origin point defines where the stagger pattern begins for a group of plies. Without it, ply edges can stack up at the same location — creating a "chimney" of ply terminations through the thickness.

```
Without stagger origin (chimney effect):

    ┌─────────────────────────┐  Ply 1
    ├────────────────────┐     │  Ply 2
    ├───────────────┐    │     │  Ply 3
    ├──────────┐    │    │     │  Ply 4
    │          │    │    │     │
              All edges line up = stress riser


With stagger origin point applied:

    ┌─────────────────────────┐  Ply 1
    ├──────────────────────┐  │  Ply 2
    ├─────────────────┐    │  │  Ply 3
    ├──────────────┐  │    │  │  Ply 4
    │              │  │    │  │
              Edges offset = load distributed
```

The stagger origin defines:
- **Start location** — the point from which stagger offsets are measured
- **Direction** — the direction along which the stagger progresses
- **Step** — the offset distance between successive ply terminations (typically 4–8 mm)

Place stagger origins away from high-stress regions, bolt holes, and ply drop-off concentrations.

## Core Inserts

A core insert is a solid element (typically honeycomb or foam) placed within the laminate to provide local stiffening. Cores are defined by:

- **Geometry** — the 3D solid shape of the insert
- **Material** — honeycomb type, foam density, or potting compound
- **Location** — between which plies the core sits in the stacking
- **Orientation** — cell direction for honeycomb (the ribbon direction affects shear properties)

Core inserts in the manufacturing model are linked to the engineering definition and update when the engineering model changes.

## Synchronising Data Between Models

Beyond the initial creation and engineering-manufacturing sync, data synchronisation covers:

- **Core sample drawings** — transferring inspection data (laminate composition at specific points) into manufacturing documentation
- **Ply table data** — updating ply tables when the stacking changes
- **Mirror part synchronisation** — keeping left-hand and right-hand parts aligned after changes to the master

## Key Takeaways

- Separate engineering and manufacturing models to allow independent evolution with controlled synchronisation
- Synchronise early and often — do not wait until design freeze
- Skin swapping reverses draping direction when the layup tool differs from the engineering reference surface
- Use stagger origin points to prevent the chimney effect at ply terminations
- Core inserts need material, geometry, and orientation defined for correct manufacturing
- All manufacturing additions (trim lines, flat patterns, ply books) survive synchronisation when the underlying ply geometry changes

## Further Reading / Tools

- [Material Excess and Boundaries](../02-design-rules/material-excess-and-boundaries.md) — EOP, EEOP, MEOP definitions
- [Ply Book Generation](ply-book-generation.md) — creating shop-floor documentation
- [Flat Pattern and Flattening](flat-pattern-and-flattening.md) — generating flat patterns for cutting
- [Splices and Joints](../02-design-rules/splices-and-joints.md) — splice management in manufacturing

> Workflow concepts informed by CATIA V5 Composites Design documentation.
