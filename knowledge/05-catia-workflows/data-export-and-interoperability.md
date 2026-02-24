---
title: "Data Export, Stack-Up Files, and Interoperability"
category: "catia"
tags: ["export", "stack-up", "DXF", "XML", "mirror-part"]
difficulty: "advanced"
related: ["ply-book-generation.md", "manufacturing-preparation.md", "stacking-and-sequences.md"]
tools: []
last_updated: "2026-02"
---

# Data Export, Stack-Up Files, and Interoperability

A composites design exists not just in the CAD model but in the data that flows to FEA, CNC cutting, manufacturing execution systems (MES), and quality inspection. Understanding export formats, stack-up files, and interoperability ensures that the design intent survives the journey from engineering to the shop floor.

## Stack-Up Files

A stack-up file is a text-based representation of the laminate stacking order. It is the critical bridge between design, analysis, and manufacturing.

### Three Ways to Create a Stack-Up File

**1. From zones (preliminary design phase):**
- Generated before plies exist, using zone laminate definitions
- Contains: ply geometric level, material, orientation, set of zones
- Use case: early design reviews, FEA preprocessing, checking the default stacking order
- Allows manual reordering before plies are created

**2. From plies (detailed design phase):**
- Generated after plies are fully defined with contours and staggering
- Can export the complete stacking or a selection of plies groups
- Options: include cut-piece information, include or exclude sub-plies
- This is the most common export for manufacturing

**3. From core samples (inspection/verification):**
- Generated from specific points on the part where the laminate composition is "sampled"
- Contains: ply stack at each sample point, useful for QC documentation
- Each core sample can be exported with a unique prefix for traceability

### Stack-Up File Content

A typical stack-up file contains:

```
Ply Level | Material    | Orientation | Zone(s)     | Sequence
----------|-------------|-------------|-------------|----------
1         | T300/914    | 45          | Z1, Z2, Z3  | Seq.1
2         | T300/914    | 0           | Z1, Z2      | Seq.1
3         | T300/914    | -45         | Z1, Z2, Z3  | Seq.2
4         | T300/914    | 90          | Z1           | Seq.2
...
```

### Reading (Importing) Stack-Up Files

The round-trip workflow allows modifications outside the CAD tool:
1. Export stack-up file from the CAD model
2. Modify stacking order, add/remove plies in a text editor or spreadsheet
3. Re-import the modified stack-up file
4. The CAD model updates to match the new stacking

This is valuable when the FEA team needs to adjust the laminate and feed changes back to the design model.

## Ply Data Export Formats

| Format | Extension | Use Case | What It Contains |
|--------|-----------|----------|-----------------|
| **DXF (2D)** | .dxf | CNC ply cutters, nesting software | Flat pattern geometry, ply outlines, dart positions |
| **IGES (3D)** | .igs | 3D contour transfer to other CAD/CAM | 3D ply boundary curves, fibre directions |
| **XML** | .xml | PLM systems, MES, digital thread | Full laminate definition with metadata |
| **Stack-up file** | .txt/.csv | FEA preprocessing, spreadsheet review | Stacking order, materials, orientations |

### DXF Export (Flat Patterns)

DXF exports the flattened (2D) ply geometry — what the cutting machine actually uses. Export options:
- **One file per ply** — each ply gets its own DXF file
- **One file per material** — all plies of the same material in one file (efficient for single-material nesting)
- **All sub-plies** — includes cut-pieces from splicing and darting

The DXF includes: ply outline, dart cuts, splice lines, fibre direction indicator, and identification text.

### IGES Export (3D Contours)

IGES exports the 3D ply boundary curves — useful for transferring geometry to another CAD system or to a laser projection system that projects ply outlines onto the tool surface during hand layup.

### XML Export

XML provides the richest data export:
- Full laminate structure (zones, plies, sequences, groups)
- Material properties and orientations
- Geometric references
- NCF-specific data (sub-ply structure within NCF layers)
- Suitable for integration with PLM and digital manufacturing systems

### Export Options

Common options across formats:
- **Entity name** — custom naming for exported plies
- **Direction name** — how fibre directions are labelled
- **Rosette and strategy point** — reference coordinate system and draping start point
- **Taking thickness update into account** — includes thickness changes from producibility analysis
- **Multiple lines vs one line** — format preference for stack-up data

## Mirror Parts

Many composite structures are symmetric about a plane — left and right wing skins, left and right fuselage panels, etc. Rather than designing both independently, you design one and mirror it.

### Creating a Mirror Part

The mirror operation creates a new part that is the geometric reflection of the original:
- **Mirror plane** — the plane of symmetry
- **Associative** — changes to the master propagate to the mirror (preferred)
- **Non-associative** — a one-time copy; subsequent changes to the master do not propagate

What gets mirrored:
- Ply contours and stacking order
- Material assignments and fibre directions (directions are mirrored correctly)
- Reference surfaces and rosettes (axis systems are reflected)
- Cut-pieces and flatten geometry (optional: associative or non-associative)

### Synchronising a Mirror Part

When the master part changes, the mirror part must be synchronised:
1. Open both master and mirror parts
2. Run synchronisation — detects which plies changed in the master
3. Propagates geometry changes to the mirror
4. Preserves mirror-specific manufacturing additions where applicable

### Mirror Design Considerations

- **Fibre directions flip** — a +45° ply in the master becomes -45° in the mirror (this is correct for structural symmetry)
- **Tooling** — mirror parts often share the same tool with a left/right setup, or use a mirrored tool
- **Stacking order** — verify that the mirrored stacking still satisfies design rules (symmetry, balance)

## Drawing and Ply Book Production

Beyond the standalone ply book (covered in [ply-book-generation.md](ply-book-generation.md)), integration with drafting tools enables:

**Generative View Styles (GVS):**
- Customisable drawing templates for composites-specific views
- Automatic generation of ply-by-ply drawings
- Options: one sheet per ply, one sheet per sequence
- Customisable naming conventions for ply identification

**Core sample drawings:**
- Visualise the laminate composition at specific inspection points
- Export core sample data for quality documentation
- Overlay on cross-section views in the drawing

## Interoperability with Other Systems

Modern composites design tools integrate with:

- **Knowledge Expert / rule engines** — embedding design rules (10% rule, symmetry, balance) as automated checks that run during design
- **FEA preprocessors** — exporting zone definitions and laminate properties directly to FEA models
- **Functional Tolerancing & Annotation (FTA)** — linking composites annotations (ply counts, orientations) to 3D annotations for model-based definition (MBD)
- **PLM systems** — managing composite part data lifecycle, revision control, and release workflows

## Key Takeaways

- Stack-up files are the critical data bridge between design, FEA, and manufacturing — create them at each design phase
- DXF for CNC cutting, IGES for 3D contour transfer, XML for full digital thread — choose the format for your downstream consumer
- Mirror parts save 50% of design effort for symmetric structures — use associative mirroring to maintain synchronisation
- Round-trip stack-up file editing enables FEA-driven laminate optimisation to feed back into the CAD model
- Export early and validate — catch format issues before the design is frozen

## Further Reading / Tools

- [Ply Book Generation](ply-book-generation.md) — creating manufacturing documentation
- [Manufacturing Preparation](manufacturing-preparation.md) — the broader manufacturing workflow
- [Stacking and Sequences](stacking-and-sequences.md) — how stacking is managed in the design model
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) for quick laminate verification

> Workflow concepts informed by CATIA V5 Composites Design documentation.
