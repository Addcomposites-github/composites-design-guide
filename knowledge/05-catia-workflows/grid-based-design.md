---
title: "Grid-Based Design and Virtual Stacking"
category: "catia"
tags: ["grid", "virtual-stacking", "panel", "cell", "rule-checking"]
difficulty: "advanced"
related: ["zone-and-group-management.md", "stacking-and-sequences.md", "../02-design-rules/stacking-sequences.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Grid-Based Design and Virtual Stacking

Zone-based design works well for parts with distinct thickness regions separated by clear boundaries. But some structures — large wing skins, fuselage panels, or complex fairings — have gradual thickness variations that are better described by a grid of cells, each with its own laminate definition. Grid-based design provides this alternative approach.

## Zone-Based vs Grid-Based — When to Use Which

| Factor | Zone-Based | Grid-Based |
|--------|-----------|------------|
| **Part type** | Distinct thickness regions | Gradual thickness variation |
| **Typical use** | Smaller parts, panels, ribs | Large skins, fuselage barrels |
| **Design freedom** | High — arbitrary zone shapes | Cell-by-cell — rectangular grid |
| **FEA alignment** | Manual mapping to FE mesh | Natural grid-to-mesh correspondence |
| **Stacking management** | Sequence-based tree | Spreadsheet-like virtual stacking |
| **Rule checking** | Manual or post-check | Built-in automated rule checking |
| **Complexity** | Simpler for <20 zones | Better for >20 zones / complex laminates |

## Defining the Panel

The grid is defined on a panel — a bounded surface region with:

- **Support surface** — the geometric surface on which plies will lie
- **Draping direction** — the direction in which material is applied
- **Grid reference elements** — a group of curves or points that define the grid layout
- **Structural group** — the structural entity that the panel belongs to
- **Limits of the panel** — the outer boundary (can be curves, edges, or surface boundaries)
- **Group prefix** — naming convention for plies generated from this grid

The panel definition establishes the coordinate frame for the grid cells and determines how fibre orientations are referenced.

## Grid Operations

Once the panel is defined, the grid is created and managed through cell operations:

### Adding Cells

Cells are added to subdivide the panel into discrete regions. Each cell represents a local laminate that can differ from its neighbours. Cells are typically rectangular but can follow the panel curvature.

### Splitting Cells

A large cell can be split into smaller cells for finer laminate control. Split along a line (horizontal or vertical within the grid) to create two cells from one.

### Merging Cells

Adjacent cells with identical laminates can be merged to simplify the model. Merging reduces the total number of cells and the complexity of the virtual stacking table.

### Editing Cells

Cell properties (laminate definition, orientation, material) can be edited individually or in bulk. Select a cell to modify its laminate, or select multiple cells for batch editing.

## The Virtual Stacking Table

The virtual stacking is a spreadsheet-like interface for managing the laminate across all grid cells simultaneously. Think of it as a matrix where:
- **Rows** represent plies (in stacking order)
- **Columns** represent grid cells (spatial locations)
- **Each intersection** defines whether that ply exists in that cell

```
Virtual Stacking Table (simplified):

              Cell A1  Cell A2  Cell B1  Cell B2
Ply 1 (0°)      ✓        ✓        ✓        ✓     ← continuous ply
Ply 2 (+45°)    ✓        ✓        ✓              ← drops in B2
Ply 3 (-45°)    ✓        ✓        ✓              ← drops in B2
Ply 4 (90°)     ✓        ✓                       ← drops in B1, B2
Ply 5 (0°)      ✓                                ← only in A1
```

### Row Operations

The virtual stacking supports extensive row manipulation:

- **Insert** a blank row (new ply) at any position
- **Copy / paste** rows to duplicate ply definitions
- **Cut / move** rows to rearrange the stacking order
- **Duplicate** a row with all its cell assignments
- **Swap** two rows to exchange their positions
- **Edit properties** of a single row or multiple rows simultaneously
- **Delete** rows that are no longer needed

### Cell Orientation Display

Cells can display colour-coded orientation values, making it easy to visually verify fibre distribution across the panel. Each orientation (0°, ±45°, 90°) gets a distinct colour, and the virtual stacking table shows the laminate composition at a glance.

### Entity-Level Control

The virtual stacking operates at multiple entity levels:
- **Ply level** — individual ply rows
- **Sequence level** — groups of plies that form a manufacturing sequence
- **Stacking area level** — the complete stacking for a defined region

## Automated Rule Checking

One of the strongest advantages of grid-based design is built-in rule checking. The system can automatically verify:

- **10% rule** — each orientation (0°, ±45°, 90°) represents at least 10% of the total plies in every cell
- **Symmetry** — the laminate is symmetric about its mid-plane in every cell
- **Balance** — for every +θ ply there is a corresponding -θ ply in every cell
- **Consecutive ply limit** — no more than 3–4 consecutive plies of the same orientation
- **Outer ply protection** — outermost plies are ±45° for damage tolerance

Rule violations are flagged in the virtual stacking table with colour highlights, allowing rapid identification and correction.

## Merging Domains

When multiple grid regions (domains) are defined on the same panel, they can be merged into a unified virtual stacking. This is useful when:
- Different engineers work on different sections of the same panel
- A preliminary grid needs to be combined with a detail grid
- Multiple loading zones need to be reconciled into a single laminate

## Managing Modified Stress Data

After FEA analysis, stress results can be fed back into the grid:
- Each cell receives updated load data
- The virtual stacking uses this data to check whether the laminate is adequate
- Under-strength cells are flagged for laminate adjustment
- This creates a closed-loop design-analysis cycle

## Generating Plies from the Grid

Once the virtual stacking is complete and rule-checked, actual ply geometry is generated:

1. The system reads the virtual stacking table
2. For each row, it identifies which cells contain that ply
3. Adjacent cells with the same ply are merged into a single ply contour
4. Ply drop-offs are created at cell boundaries where a ply terminates
5. The result is a set of plies with contours, staggering, and stacking — identical in structure to zone-based plies

From this point forward, the workflow merges with the standard ply-based workflow: flat patterns, ply books, export.

## Exporting and Importing Grid Data

Grid definitions and virtual stacking tables can be exported to and imported from external files:
- **Export** — save the grid layout and laminate assignments for review, archiving, or transfer
- **Import** — load a grid definition from an external source (spreadsheet, FEA tool, optimiser output)

This enables integration with external optimisation tools that output laminate definitions in a grid format.

## Key Takeaways

- Grid-based design excels for large panels with gradual thickness variation and many local laminate changes
- The virtual stacking table provides a spreadsheet-like view of the entire laminate across all cells
- Built-in rule checking (10%, symmetry, balance, consecutive limit) catches violations during design, not after
- Grid cells map naturally to FEA mesh elements, enabling tight design-analysis integration
- Plies generated from the grid are structurally identical to zone-based plies — downstream workflows are unchanged
- Use zone-based for simple parts (<20 thickness regions) and grid-based for complex skins and panels

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) for verifying laminate rules
- [Zone and Group Management](zone-and-group-management.md) — the zone-based alternative
- [Stacking and Sequences](stacking-and-sequences.md) — how stacking works in the ply tree
- [Stacking Sequences (Design Rules)](../02-design-rules/stacking-sequences.md) — the rules that grid checking enforces

> Workflow concepts informed by CATIA V5 Composites Design documentation.
