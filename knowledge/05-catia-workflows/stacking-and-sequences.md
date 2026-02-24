---
title: "Stacking and Sequences in Composites CAD"
category: "catia"
tags: ["stacking", "sequence", "virtual-stacking", "ply-order", "reorder"]
difficulty: "intermediate"
related: ["ply-creation-workflow.md", "zone-and-group-management.md", "../02-design-rules/stacking-sequences.md"]
tools: []
last_updated: "2026-02"
---

# Stacking and Sequences in Composites CAD

The stacking is the master data structure of a composite part in CAD. It contains every ply, organised into sequences (manufacturing groups), in the order they are laid onto the tool. Managing the stacking — reordering plies, checking design rules, and synchronising with manufacturing — is where composites CAD tools spend most of their time.

## Stacking Structure

The stacking is organised as a tree:

```
Stacking
├── Sequence 1
│   ├── Ply 1 (attributes + geometry)
│   ├── Ply 2
│   └── Ply 3
├── Sequence 2
│   ├── Ply 4
│   ├── Ply 5
│   └── Ply 6
└── Sequence 3
    ├── Ply 7
    └── Ply 8
```

**Sequences** are manufacturing groups — sets of plies that a machine or technician places in one pass or phase. They define the order in which material is applied to the mould.

Each **ply** contains:
- **Attributes** — material, orientation angle, ply name/ID, thickness
- **Geometry** — the contour (boundary) on the reference surface

## Virtual Stacking Management

For large laminates (60+ plies across multiple zones), managing the stacking manually is impractical. A **virtual stacking** provides a spreadsheet-like interface for managing the entire laminate:

- **Rows** represent plies
- **Columns** represent zones or cells
- **Cells** show which material and direction occupy each ply-zone intersection

### Operations in the Virtual Stacking

**Editing rows:** Change the material, direction, or zone assignment of any ply. Edit single rows or bulk-edit multiple rows at once.

**Inserting and duplicating:** Add blank rows (new plies) at any position, or duplicate existing rows. Insert new sequences to reorganise the manufacturing order.

**Moving and reordering:** Move plies between sequences, reorder sequences within the stacking. This is how you adjust the manufacturing order without recreating plies.

**Cutting, copying, pasting:** Standard spreadsheet operations for rapid stacking modification.

**Merging sequences/plies:** Combine sequences that should be manufactured together, or merge plies that have been split unnecessarily.

### Detailed Row Operations

The virtual stacking supports comprehensive row manipulation:

| Operation | What It Does |
|-----------|-------------|
| **Insert blank** | Add a new empty ply at any position |
| **Duplicate** | Copy an existing row with all its cell assignments |
| **Copy / Cut / Paste** | Standard clipboard operations for rapid reorganisation |
| **Move** | Drag a row to a new position in the stack |
| **Swap** | Exchange two rows' positions in one step |
| **Edit properties** | Change material, direction, or zone assignment for one or multiple rows simultaneously |
| **Delete** | Remove a row from the stacking |

**Sequence-level operations:** Insert blank sequences, merge sequences that should be manufactured together, or split a sequence into two. Sources and recipients track where plies came from and where they go during reorganisation.

**Display modes:** The virtual stacking can show 3D information overlaid on the model, entity-level detail (ply, sequence, or stacking area), and import/export capability for external spreadsheet editing.

### Cell Orientation Valuating

Each cell in the virtual stacking can display its fibre orientation. A visual colour code shows the direction at a glance:

| Colour | Typical meaning |
|---|---|
| Blue/Red | 0° plies |
| Green | 90° plies |
| Yellow/Orange | ±45° plies |

The exact colour mapping depends on the tool configuration.

## Checking Stacking Rules

Composites CAD tools can automatically check the stacking against design rules:

- **Symmetry** — is the laminate symmetric about its midplane?
- **Balance** — does every +θ ply have a matching -θ ply?
- **10% rule** — is there at least 10% of plies in each principal direction (0°, +45°, -45°, 90°)?
- **Consecutive plies** — are there more than 3–4 consecutive plies at the same angle?
- **Outer ply orientation** — are the outermost plies at the preferred angle (typically ±45°)?

These automated checks save hours compared to manual verification and catch errors that are easy to miss in a 60-ply laminate.

### What Gets Checked in Detail

| Rule | What the Check Verifies |
|------|------------------------|
| **Symmetry** | For each zone/cell, is the top half of the stack a mirror of the bottom half? |
| **Balance** | Does every +θ ply have a corresponding -θ ply at the same zone/cell? |
| **10% minimum** | Is each of 0°, +45°, -45°, 90° at least 10% of the total plies? |
| **Consecutive limit** | Are there more than N plies (typically 3–4) of the same angle in sequence? |
| **Outer ply** | Are the outermost plies at ±45° for damage tolerance? |

Violations are highlighted in the virtual stacking table with colour coding, allowing rapid identification. The check can run on the complete stacking or on a selection of zones/cells.

## Stack-up Files

A **stack-up file** is a text or spreadsheet export of the stacking. It lists every ply with its:
- Position in the stack (geometric level)
- Material
- Orientation
- Zone coverage

Stack-up files serve as the bridge between CAD and other tools — FEA software, manufacturing systems, and documentation. They can be exported, modified externally (e.g., by a stress engineer who adjusts the stacking for structural reasons), and re-imported into the CAD model.

## Managing Stacking Areas

For complex parts with multiple panels or sub-components, the stacking can be divided into **stacking areas** — separate stacking regions that are managed independently but exist within the same CAD model. This is useful for parts where different sections have fundamentally different stacking architectures (e.g., a wing skin with separate upper and lower stackings).

## Key Takeaways

- The stacking is the master data structure: sequences contain plies, plies contain attributes and geometry
- Virtual stacking provides a spreadsheet interface for efficiently managing large laminates
- Automated rule checking validates symmetry, balance, 10% rule, and consecutive ply limits
- Stack-up files bridge between CAD, FEA, and manufacturing systems
- Plies can be reordered, moved between sequences, merged, and bulk-edited
- Stacking areas manage multiple independent stacking regions within one model

## Further Reading / Tools

- [Ply Creation Workflow](ply-creation-workflow.md) — how plies are created before stacking management
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — the design rules the stacking must satisfy
- [Ply Book Generation](ply-book-generation.md) — documenting the final stacking for manufacturing

> Workflow concepts informed by CATIA V5 Composites Design documentation.
