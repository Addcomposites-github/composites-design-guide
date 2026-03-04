# Plan: Complete the Knowledge Base — Fill All Gaps

## What We Have (31 files, ~30,000 words)
All 7 sections populated. But the CATIA source (~165 pages, ~87,000 words) has
topics we either didn't cover or only touched lightly.

## Strategy: New Files + Expansions + Glossary

Everything below is grouped into **3 work phases** so we can commit after each.

---

## PHASE 1 — New Files (8 new .md files)

### 02-design-rules/ (3 new files)

**1. `dart-design.md`** — NEW
- When darts are necessary (double curvature, Gaussian curvature metric)
- Dart shapes: radial, line, curve, combined relief cuts
- Design parameters: length, angle, overlap/gap sizing
- Interaction with fibre direction and load paths
- Darts in UD tape vs woven fabric
- Multiple darts on one ply: arrangement strategy
- Quality risks: crack propagation from dart tips
- Source: CATIA "Creating Darts" (3039 chars) + universal principles

**2. `material-excess-and-boundaries.md`** — NEW
- EOP, EEOP, MEOP definitions and relationships (with ASCII diagram)
- Why manufacturing needs more material than engineering boundary
- Typical excess values by process (hand layup, AFP, RTM)
- How excess interacts with tooling (OML vs IML)
- Trimming strategy: laser, waterjet, CNC router, manual
- Material excess effect on laminate thickness surveys
- Source: CATIA "Defining the Material Excess", "Defining EOP/EEOP/MEOP", "Swapping the Skin"

**3. `non-crimp-fabrics.md`** — NEW
- What NCFs are and how they differ from woven and UD
- Construction: stitched multi-axial (biaxial, triaxial, quadraxial)
- Advantages: faster layup, higher fibre volume, no crimp
- Disadvantages: limited orientations, binder issues, cost
- Design implications: constrained ply angles, ply thickness changes
- Manufacturing window: infusion-friendly, preform-friendly
- When to specify NCF vs UD prepreg vs woven
- Source: CATIA "Using Non Crimp Fabrics" (5711 chars) + industry knowledge

### 05-catia-workflows/ (3 new files)

**4. `manufacturing-preparation.md`** — NEW
- Creating a manufacturing document (engineering → manufacturing model split)
- Synchronising engineering and manufacturing models
- Skin swapping: IML vs OML tool, draping direction reversal
- Skin swapping with wrap curves (complex geometry)
- Stagger origin points: chimney effect avoidance
- Core creation for local reinforcement/inserts
- Mermaid workflow: design → manufacturing document → sync → flat pattern → ply book
- Source: CATIA "Creating a Manufacturing Document", "Synchronizing", "Swapping the Skin", "Swapping the Skin with Wrap Curve", "Adding a Stagger Origin Point", "Creating a Core"

**5. `data-export-and-interoperability.md`** — NEW
- Stack-up files: from zones, from plies, from core samples (3 creation paths)
- Reading/importing stack-up files (round-trip workflow)
- Ply data export formats: DXF (CNC cutters), IGES (3D), XML (PLM/MES)
- What each format preserves and what it loses
- XML export structure and use cases
- Mirror part creation and synchronisation
- Interoperability: Knowledge Expert, GSD, FTA integration concepts
- Drawing/ply book generation for shop floor
- Source: CATIA "Exporting Ply Data", "Exporting To XML", "Creating Mirror Part", "Synchronizing Mirror Part", "Stack-up File from Zones/Plies/Core Samples", "Reading Stack-Up File", "Creating a Drawing", "Producing Drawings with GVS"

**6. `grid-based-design.md`** — NEW
- What grid-based design is (alternative to zone-based)
- When to use: complex geometries, large panels, design-to-FEA alignment
- Defining the panel: support surface, structural group, grid reference
- Grid operations: add/merge/split/edit cells
- Virtual stacking dialog: cell-by-cell laminate definition
- Colour coding and orientation valuating
- Automated rule checking within grid
- Merging domains, managing modified stress data
- Generating plies from the virtual stacking
- Exporting/importing grid information
- Comparison table: zone-based vs grid-based approach
- Source: CATIA "Defining the Panel" (7686 chars), "Defining the Grid" (4076 chars), "About the Virtual Stacking Dialog Box" (12424 chars), "Editing a Row", "Generating Plies from Virtual Stacking" (3337 chars), "Exporting/Importing Grid Information" (3564 chars)

### 03-manufacturing-processes/ (1 new file)

**7. `post-processing-and-trimming.md`** — NEW
- After cure: what happens next
- Trimming methods: CNC 5-axis router, waterjet, laser, manual
- Inspection: NDI (ultrasonic, thermography, X-ray), tap testing
- Assembly: drilling, fastening, bonding, co-curing vs co-bonding vs secondary bonding
- Surface finishing: painting, gel coat, lightning strike protection
- Tooling removal, demoulding
- Quality documentation and traceability
- Source: general composites knowledge + CATIA manufacturing document concepts

### 04-structural-analysis/ (1 new file)

**8. `damage-tolerance-and-repair.md`** — NEW
- BVID and damage tolerance philosophy (no-growth, slow-growth)
- CAI (Compression After Impact) as key metric
- Design for inspectability
- Repair approaches: scarf, stepped lap, bolted doubler
- Knockdown factors in practice
- Source: universal composites knowledge (extends failure-modes.md)

---

## PHASE 2 — Expand Existing Files (11 files get new sections)

### 02-design-rules/ expansions

**9. Expand `splices-and-joints.md`** — add ~400 words
- NEW section: "## 3D Multi-Splice on Curved Surfaces"
  - Roll width exceeding ply size → must splice
  - Overlap vs gap management on non-planar geometry
  - Splice staggering relative to other ply splices
- NEW section: "## No-Splice Zones"
  - Locations where splices are prohibited (bolt holes, high-stress, radii)
  - Butt splice zone concept vs no-splice zone concept

**10. Expand `ply-drop-offs.md`** — add ~400 words
- NEW section: "## Limit Contours and Staggering Workflow"
  - ETBS (Edges To Be Staggered) identification
  - Stagger direction and offset modes
  - Generating staggering data files
  - Verification: symmetry/balance maintained after stagger
- NEW section: "## Local Drop-Offs and Ramp Supports"
  - Local drop-off creation for small reinforcements
  - Ramp support editing: adjusting taper geometry
  - No-drop-off areas: where drops are prohibited

**11. Expand `zone-design.md`** — add ~500 words
- NEW section: "## Rosette Systems and Fibre Direction"
  - Cartesian rosette: flat/gently curved panels
  - Cylindrical rosette: barrels, ducts (neutral fibre reference)
  - Rosette transfer types and when to use each
  - Fibre direction distortion on curved surfaces
- NEW section: "## Advanced Zone Operations"
  - Refining transition zones (curve selection, contour adjustment)
  - Zone bridge analysis: validating connectivity
  - Iso-thickness areas from existing zones
  - Junction lines between zones
  - Angle cuts at zone boundaries

**12. Expand `design-for-manufacture.md`** — add ~300 words
- NEW section: "## Mirror and Symmetric Part Strategy"
  - When to design half and mirror
  - Associative vs non-associative mirror
  - Manufacturing benefits: shared tooling, halved programming
  - Verifying symmetry: structural and manufacturing checks

### 01-fundamentals/ expansion

**13. Expand `fibre-types.md`** — add ~200 words
- Add NCF cross-reference in existing fibre forms discussion
- Add "## Fibre Sizing and Surface Treatment" mini-section
- Link to new non-crimp-fabrics.md for detailed NCF coverage

### 05-catia-workflows/ expansions

**14. Expand `zone-and-group-management.md`** — add ~500 words
- NEW section: "## Connection Generator in Detail"
  - Four connection types (structural edges, structural CTPs, transition edges, transition CTPs)
  - Colour coding: red/green/magenta/light blue for connection types
  - Yellow/dark blue for free edges
  - Fixing connection errors
- NEW section: "## ITP and ITP Height — When and Why"
  - ITP: impose thickness at a zone vertex
  - ITP Height: impose total height at a zones group vertex
  - Practical scenarios: multi-zone junctions, local reinforcement points
- EXPAND existing: add drop-off creation from zones (ramp slope, direction, limits, offset)

**15. Expand `ply-creation-workflow.md`** — add ~600 words
- NEW section: "## Plies from Slicing (Alternative Approach)"
  - Slicing a solid model into layers
  - When to use: reverse engineering, imported FEA solids
  - Parameters: slice thickness, curve degree, geometrical level
  - Creating plies from slicing output
- NEW section: "## Manual Ply Creation — Full Workflow"
  - Surface, contour, direction, material, rosette selection
  - When manual beats automatic: repairs, local patches, inserts
- NEW section: "## Ply Merging, Relimiting, and Re-routing"
  - Merging plies and merging stackings
  - Relimiting plies after geometry changes
  - Re-routing ply contours (start/end vertex, new route, other side)
  - Removing ply shells
- EXPAND "Modifying Plies": add direction modification, material change workflows

**16. Expand `stacking-and-sequences.md`** — add ~400 words
- NEW section: "## Virtual Stacking in Detail"
  - Cell dispatch and cell management
  - Row operations: insert, copy, cut, paste, duplicate, move, swap, edit properties
  - Sequence and ply sources/recipients
  - Entity-level display and 3D information display
  - Import/export within virtual stacking
- EXPAND rule checking: specific rules checked (symmetry, balance, 10%, consecutive, outer ply)

**17. Expand `flat-pattern-and-flattening.md`** — add ~400 words
- NEW section: "## Producibility Analysis — Full Parameters"
  - Deformation mode vs deviation mode
  - Warn angle and limit angle settings
  - Warp vs weft fibre directions
  - Seed point: point indication vs point selection
  - Propagation types: minimum distortion, keep, symmetric
  - Full stacking vs ply group only analysis
  - With/without thickness update
- NEW section: "## Unfolding Entities"
  - Unfolding a surface (non-composites geometry)
  - Transferring elements between 3D and 2D workspaces

**18. Expand `analysis-tools.md`** — add ~400 words
- NEW section: "## Interpreting Producibility Results"
  - Colour maps: what red/yellow/green mean
  - Failure remediation: darts, material change, fibre reorientation, geometry change
  - Acceptance criteria by application class
- NEW section: "## Producibility Inspection — Detailed"
  - Export results to file
  - Inspection on complete stacking vs selection of groups
  - Inspection points and reporting

**19. Expand `ply-book-generation.md`** — add ~300 words
- EXPAND EOP/EEOP/MEOP: add ASCII diagram showing relationship
- NEW section: "## Drawing Production with Generative View Styles"
  - GVS customization for composites
  - One sheet per ply vs one sheet per sequence trade-offs
  - Naming conventions for ply book sheets

---

## PHASE 3 — Glossary + Audit + Index + Commit

**20. Expand `glossary.md`** — add ~25 new terms
New terms to add:
- Rosette (coordinate system for fibre directions)
- ITP / Imposed Thickness Point
- ITP Height
- ETBS / Edges To Be Staggered
- Transition Zone (zone-design context)
- Zones Bridge
- Connection Generator
- Virtual Stacking
- Stacking Area
- Grid-Based Design
- NCF / Non-Crimp Fabric
- Locking Angle
- Material Excess
- EOP / Edge Of Part
- EEOP / Engineering Edge Of Part
- MEOP / Manufacturing Edge Of Part
- Skin Swap / Skin Swapping
- Stack-up File
- Ply Exploder
- Fibre Deviation Angle
- Chimney Effect
- Core Insert
- Stagger Origin Point
- Draping Direction
- Knockdown Factor

**21. Run audit** — `python scripts/audit_knowledge_base.py`
**22. Rebuild index** — `python scripts/build_index.py`
**23. Commit and push**

---

## Summary

| Phase | Action | Count |
|-------|--------|-------|
| 1 | New files | 8 |
| 2 | Expand existing files | 11 |
| 3 | Glossary + audit + index + commit | 1 + scripts |
| **Total** | **New + expanded** | **19 files touched, ~8,000–10,000 new words** |

Estimated final state: **39 files, ~40,000 words** — covering 90%+ of the CATIA source material's universal knowledge plus all CATIA-specific workflows framed as "industry-leading tool" reference.
