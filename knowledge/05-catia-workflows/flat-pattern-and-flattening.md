---
title: "Flat Pattern and Flattening"
category: "catia"
tags: ["flat-pattern", "flattening", "producibility", "draping", "fibre-direction"]
difficulty: "intermediate"
related: ["ply-creation-workflow.md", "analysis-tools.md", "../02-design-rules/design-for-manufacture.md", "../03-manufacturing-processes/common-defects.md"]
tools: []
last_updated: "2026-02"
---

# Flat Pattern and Flattening

Every composite ply starts as a flat piece of material — a 2D shape cut from a roll of prepreg or fabric. The **flat pattern** is the 2D shape that, when draped onto the 3D tool surface, produces the correct 3D ply contour. Generating accurate flat patterns is essential for manufacturing: it determines how material is cut and how much distortion occurs when draping.

## Why Flattening Matters

A 3D ply contour on a curved surface cannot simply be "projected" onto a flat plane. The 3D surface has curvature, which means distances and angles on the surface differ from their flat equivalents. Flattening accounts for this distortion to produce a 2D pattern that, when physically placed on the mould, matches the intended 3D contour.

On a singly curved surface (cylinder), flattening is straightforward — the surface unrolls perfectly. On a doubly curved surface (sphere, saddle shape), some distortion is inevitable. The flattening algorithm must determine the best compromise.

## The Flattening Process

```mermaid
graph LR
    A[3D ply contour on tool surface] --> B[Flattening algorithm]
    B --> C[2D flat pattern]
    C --> D[CNC ply cutter / manual cutting]
    D --> E[Flat material piece]
    E --> F[Draped onto 3D tool]
```

The flattening algorithm simulates the reverse of draping: starting from the 3D shape, it "unwraps" the ply onto a flat plane while tracking how the fibre directions distort.

Key inputs to flattening:
- **3D ply contour** — the boundary of the ply on the tool surface
- **Fibre direction** — the reference direction for the fibres, defined by the rosette
- **Seed point** — a starting point on the surface from which the flattening propagates outward
- **Location point** — a reference point that maps a specific 3D location to a specific 2D location, anchoring the flat pattern

## Producibility Analysis

Before cutting material, composites CAD tools analyse **producibility** — how well the ply can be manufactured. The key producibility measures are:

### Fibre Deviation (Delta Angle)

The **deviation angle** is the difference between the intended fibre direction (from the rosette) and the actual fibre direction after draping. On a flat surface, the deviation is zero everywhere. On a curved surface, fibres distort as they conform to the geometry.

- **Small deviation (< 3–5°)** — acceptable for most applications
- **Moderate deviation (5–15°)** — may be acceptable depending on structural requirements; check with the stress engineer
- **Large deviation (> 15°)** — likely unacceptable; the ply needs darts, reorientation, or a material with better drapability (e.g., fabric instead of UD tape)

### Shear Deformation

For woven fabrics, the producibility analysis measures the **shear angle** — how much the warp and weft fibres rotate relative to each other during draping. Each fabric has a **locking angle** beyond which it wrinkles:
- Typical locking angle for woven carbon: 25–40° depending on weave style
- If the shear angle exceeds the locking angle, wrinkles will form

### Warp and Weft Analysis

The analysis can display the distortion of both the warp (0°) and weft (90°) fibre families independently, showing where each family is under tension, compression, or shear.

## Displaying Fibre Direction

A separate tool displays the **theoretical fibre directions** on the 3D ply surface. This shows:
- The intended fibre direction at any point (from the rosette transfer)
- The actual fibre direction after draping simulation
- The deviation between the two

This visualisation helps the designer identify problem areas before manufacturing.

## Transferring Geometry Between 2D and 3D

The flat pattern workflow involves bidirectional transfers:

**3D to 2D:** The standard flattening — takes the 3D ply contour and produces the 2D flat pattern. Additional features (dart lines, splice lines, identification marks) are also transferred.

**2D to 3D:** The reverse operation. If the flat pattern is modified in 2D (e.g., a manufacturing engineer adjusts a dart location), the change can be transferred back to the 3D model.

## Optimising the Flattening

Several parameters control flattening quality:

- **Seed point location** — where the algorithm starts propagating. Different seed points produce slightly different flat patterns. Central seed points generally minimise overall distortion.
- **Propagation type** — circular (radial from the seed) or along fibre directions. Circular is the default; fibre-aligned propagation can reduce distortion along the primary load path.
- **Minimum distortion mode** — an optimisation that adjusts the flat pattern to minimise total fibre deviation across the ply

For large or highly curved plies, optimising these parameters can significantly reduce material waste and improve as-manufactured fibre alignment.

## Material Roll Width Check

After flattening, the 2D flat pattern must fit within the available material roll width. An automated check compares the flat pattern dimensions against the roll width and flags plies that are too wide — these will need splices.

## Key Takeaways

- Flat patterns are 2D shapes that, when draped onto the 3D tool, produce the correct ply geometry
- Flattening accounts for surface curvature — singly curved surfaces unroll exactly; doubly curved surfaces involve distortion
- Producibility analysis measures fibre deviation angle and fabric shear to predict manufacturing problems
- Fibre deviations above 15° typically require darts, material changes, or ply redesign
- Seed point location and propagation type affect flattening accuracy
- Material roll width checks identify plies that need splicing before reaching the cutting table

## Further Reading / Tools

- [Design for Manufacture](../02-design-rules/design-for-manufacture.md) — draping constraints and DFM principles
- [Common Defects](../03-manufacturing-processes/common-defects.md) — wrinkles and bridging caused by poor drapability
- [Analysis Tools](analysis-tools.md) — other analysis capabilities in composites CAD
- [Ply Creation Workflow](ply-creation-workflow.md) — creating the plies that are then flattened

> Workflow concepts informed by CATIA V5 Composites Design documentation.
