---
title: "Ply Book Generation"
category: "catia"
tags: ["ply-book", "documentation", "manufacturing-document", "drawing", "EOP"]
difficulty: "intermediate"
related: ["ply-creation-workflow.md", "stacking-and-sequences.md", "flat-pattern-and-flattening.md"]
tools: []
last_updated: "2026-02"
---

# Ply Book Generation

A **ply book** is the definitive manufacturing document for a composite part. It contains a drawing or image for every ply (or every sequence) showing exactly where that ply goes, its material, orientation, and boundary. The technician on the shop floor uses the ply book to lay up each ply in the correct position, in the correct order, with the correct material. Getting the ply book wrong means getting the part wrong.

## What Goes in a Ply Book

A complete ply book typically includes:

**For each ply (or each sequence):**
- Ply name and ID number
- Material and orientation angle
- Ply contour drawn on the part geometry
- Flat pattern (2D shape for cutting)
- Position in the stacking order
- Any splices, darts, or stagger offsets

**For the overall part:**
- Edge of Part (EOP) — the outer boundary of all plies
- Engineering Edge of Part (EEOP) — the engineering outer boundary (may differ from manufacturing EOP)
- Manufacturing Edge of Part (MEOP) — the boundary for manufacturing purposes, which may include material excess for trimming
- Total thickness map or zone diagram
- Stacking table — the complete ply-by-ply stacking sequence

## Generation Options

Ply books can be generated with different levels of detail:

**One sheet per ply:** Every individual ply gets its own drawing sheet. Gives maximum clarity but produces a very large document for thick laminates. A 60-ply part produces a 60+ page ply book.

**One sheet per sequence:** Groups of plies that are laid in one manufacturing pass share a sheet. Reduces document size but shows less detail per ply.

**Generation level:** Controls the naming convention and numbering scheme. Different companies use different conventions (sequential numbers, material-based prefixes, zone-based naming).

## Edge of Part Definitions

Three related but distinct boundary concepts appear in the ply book:

**EOP (Edge of Part):** The outer boundary of the plies — where the composite material physically ends.

**EEOP (Engineering Edge of Part):** The engineering boundary. This is where the structural designer intends the part to end. It may be inside the EOP if material excess is added for manufacturing.

**MEOP (Manufacturing Edge of Part):** The manufacturing boundary, which often extends beyond the EEOP. The extra material (material excess) is trimmed after cure.

```
Boundary relationships:

    ┌── MEOP (manufacturing boundary — includes excess) ──┐
    │  ┌── EOP (actual edge of material) ──────────────┐  │
    │  │  ┌── EEOP (engineering boundary) ───────────┐ │  │
    │  │  │                                          │ │  │
    │  │  │     Structural part                      │ │  │
    │  │  │                                          │ │  │
    │  │  └──────────────────────────────────────────┘ │  │
    │  └───────────────────────────────────────────────┘  │
    └─────────────────────────────────────────────────────┘
              ↑ material excess for trimming
```

**Material excess** is the extra material beyond the EEOP that allows for:
- Trimming inaccuracies during manufacturing
- Edge bleed of resin during cure
- Tooling grip areas
- Dimensional tolerance on the final trimmed edge

## Drawing Production with Generative View Styles

Ply books can be produced as formal engineering drawings using **Generative View Styles (GVS)** — customisable templates that control how composites-specific views are rendered:

- **GVS customisation** — define drawing templates for composites that include ply outlines, fibre direction arrows, material labels, and stacking tables
- **One sheet per ply vs one sheet per sequence** — choose the detail level appropriate for your manufacturing process
- **Naming conventions** — configure how plies, sequences, and ply books are named (sequential numbers, material-based prefixes, zone-based identifiers)

Drawings can be generated in CATDrawing format for integration with company documentation systems. The GVS can be modified and reapplied to regenerate drawings when the design changes.

## Manufacturing Document Creation

Beyond the ply book itself, a **manufacturing document** is a separate part file that contains all the manufacturing-specific information:

- Ply contours with material excess applied
- Flat patterns for each ply
- Splice locations and overlap dimensions
- Dart locations and geometries
- Stagger origin points and offset values

The manufacturing document is linked to the engineering model. When the engineering design changes, the manufacturing document can be **synchronised** to reflect those changes — updating ply contours, stagger values, and flat patterns.

## Skin Swapping

In some manufacturing processes, the reference surface (Inner Mould Line) and the manufacturing surface (Outer Mould Line) are on opposite sides of the laminate. **Skin swapping** reverses the draping direction so that the ply book references the correct surface for the shop floor.

## Data Export

Ply data can be exported in various formats for different downstream tools:

- **Stack-up files** — for FEA import or manufacturing execution systems
- **DXF/IGES** — flat pattern geometry for CNC ply cutters
- **XML export** — structured data for integration with PLM (Product Lifecycle Management) systems
- **Ply export data** — individual ply contours in 2D or 3D formats

Export options include:
- One file per ply or one file per material
- Multiple export formats simultaneously
- Rosette and stacking information embedded in the file

## Key Takeaways

- The ply book is the shop-floor document — one drawing per ply or per sequence showing contour, material, and position
- EOP, EEOP, and MEOP define the engineering, actual, and manufacturing boundaries of the part
- Material excess beyond the EEOP provides trimming tolerance for manufacturing
- Manufacturing documents are linked to the engineering model and can be synchronised when the design changes
- Flat patterns, splice details, and stagger values are all included in the manufacturing documentation
- Ply data exports in DXF/IGES format drive CNC ply cutters directly

## Further Reading / Tools

- [Stacking and Sequences](stacking-and-sequences.md) — the stacking that the ply book documents
- [Flat Pattern and Flattening](flat-pattern-and-flattening.md) — generating the 2D patterns included in the ply book
- [Ply Creation Workflow](ply-creation-workflow.md) — creating the plies that appear in the ply book

> Workflow concepts informed by CATIA V5 Composites Design documentation.
