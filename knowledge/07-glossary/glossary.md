---
title: "Composites Design Glossary"
category: "glossary"
tags: ["glossary", "definitions", "terminology", "composites", "reference"]
difficulty: "beginner"
related: ["../01-fundamentals/what-are-composites.md"]
tools: []
last_updated: "2026-02"
---

# Composites Design Glossary

Plain-English definitions of terms used throughout this knowledge base. Terms are grouped by topic for easier browsing, with cross-references to the pages where they are discussed in detail.

## Materials

**Fibre** — the reinforcing element in a composite. Carries the primary structural load. Common types: carbon, glass, aramid (Kevlar), basalt. See [Fibre Types](../01-fundamentals/fibre-types.md).

**Matrix / Resin** — the polymer that binds the fibres together, transfers load between them, and protects them from the environment. See [Resin Systems](../01-fundamentals/resin-systems.md).

**Thermoset** — a resin that undergoes an irreversible chemical reaction (curing) to harden. Once cured, it cannot be re-melted. Examples: epoxy, polyester, vinyl ester.

**Thermoplastic** — a resin that melts when heated and solidifies when cooled. Can be re-formed. Examples: PEEK, PPS, nylon.

**Prepreg** — fibre reinforcement that is pre-impregnated with resin at the factory. Requires frozen storage. Delivers the most consistent and highest-quality laminates. See [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md).

**Dry fabric** — reinforcement without resin, wetted during the layup process (wet layup) or after layup (infusion). See [Wet Layup](../03-manufacturing-processes/wet-layup.md).

**Unidirectional (UD)** — a ply where all fibres run in a single direction. Strongest in the fibre direction, weakest at 90° to it.

**Woven fabric** — fibres interlaced in two directions (warp and weft). More balanced properties and better drapability than UD, but lower in-plane stiffness because of fibre crimp (waviness at crossover points).

**Fibre volume fraction (Vf)** — the proportion of the laminate volume occupied by fibres. Higher Vf = stronger and stiffer. Typical ranges: 35–50% (hand layup), 50–60% (infusion), 55–65% (autoclave prepreg).

## Laminate Structure

**Ply / Lamina** — a single layer of fibre-reinforced material. The fundamental building block of a composite structure. See [What Are Composites?](../01-fundamentals/what-are-composites.md).

**Laminate** — a stack of plies bonded together. The stacking sequence defines its structural behaviour.

**Stacking sequence** — the order, angles, and number of plies from bottom to top. Written in shorthand: [0/±45/90]s. See [Stacking Sequences](../02-design-rules/stacking-sequences.md).

**Midplane** — the geometric centre of the laminate thickness. The axis of symmetry in a symmetric laminate.

**Symmetric laminate** — a laminate where the stacking sequence is mirrored about the midplane. Eliminates bending-stretching coupling. See [Stacking Sequences](../02-design-rules/stacking-sequences.md).

**Balanced laminate** — a laminate where every +θ ply has a corresponding -θ ply. Eliminates extension-shear coupling.

**Quasi-isotropic** — a laminate with equal proportions of 0°, +45°, -45°, and 90° plies. Behaves approximately the same in all in-plane directions.

**Ply drop-off** — where a ply terminates inside the laminate to create a thickness change. See [Ply Drop-offs](../02-design-rules/ply-drop-offs.md).

**Splice** — a joint within a single ply layer where two pieces of material meet. See [Splices and Joints](../02-design-rules/splices-and-joints.md).

**Zone** — a region of a composite part with a constant laminate definition (same number and angles of plies). See [Zone Design](../02-design-rules/zone-design.md).

## Analysis Terms

**Classical Laminate Theory (CLT)** — the mathematical framework for predicting laminate stiffness, ply stresses, and strains from ply properties and stacking sequence. See [Laminate Theory](../01-fundamentals/laminate-theory.md).

**ABD matrix** — the 6×6 stiffness matrix of a laminate. A = in-plane stiffness, B = bending-stretching coupling, D = bending stiffness.

**Running load** — force per unit width, in N/mm. The standard way to express loads on thin structures. Nx (in-plane x), Ny (in-plane y), Nxy (in-plane shear).

**Margin of safety (MoS)** — (Allowable / Applied) - 1. Positive = the ply passes. Negative = redesign needed. See [Sizing a Panel](../04-structural-analysis/sizing-a-panel.md).

**Failure index (FI)** — a normalised measure from a failure criterion. FI ≥ 1 = the ply has failed.

**First Ply Failure (FPF)** — the load at which the first ply in the laminate reaches its failure criterion. Conservative design limit.

**Last Ply Failure (LPF)** — the load at which the entire laminate collapses. Requires progressive damage analysis.

**Knockdown factor** — a multiplier (less than 1) applied to material properties to account for environmental effects (hot/wet), damage (BVID), or statistical scatter.

## Failure Modes

**Fibre failure** — breakage of fibres in tension or micro-buckling/kinking in compression. See [Failure Modes](../01-fundamentals/failure-modes.md).

**Matrix cracking** — cracks in the resin parallel to the fibre direction. The first damage mode to appear in most laminates.

**Delamination** — separation between adjacent ply layers. The most common and dangerous composite failure mode.

**BVID (Barely Visible Impact Damage)** — internal damage (delamination, matrix cracking) caused by low-energy impact that leaves little visible surface mark. Drives damage tolerance design in aerospace.

**Buckling** — structural instability where a thin panel bows out of plane under compression before the material fails. See [Buckling Basics](../04-structural-analysis/buckling-basics.md).

**Wrinkling** — local buckling of a thin face sheet on a compressible core (in sandwich structures).

## Manufacturing Terms

**Layup** — the process of placing plies onto a mould to build up the laminate.

**Mould / Tool** — the surface on which the composite part is laid up and cured. Defines one surface of the finished part.

**OML (Outer Mould Line)** — the external (aerodynamic or visible) surface of the part.

**IML (Inner Mould Line)** — the internal surface of the part.

**Debulk** — applying vacuum to a partially-completed layup to compact the plies and remove trapped air. Done every 3–5 plies for thick laminates.

**Cure** — the chemical reaction (for thermosets) or cooling solidification (for thermoplastics) that converts the soft layup into a hard structural part.

**Post-cure** — a secondary heat treatment after initial cure to improve the degree of cure and final mechanical properties.

**Autoclave** — a pressurised oven used to cure prepreg laminates under combined heat and pressure (typically 0.3–0.7 MPa). See [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md).

**Vacuum bagging** — sealing a laminate under a flexible bag and pulling vacuum to apply atmospheric pressure for compaction. See [Vacuum Bagging](../03-manufacturing-processes/vacuum-bagging.md).

**VARTM (Vacuum Assisted Resin Transfer Moulding)** — vacuum-driven resin infusion through a dry fabric stack. See [Resin Infusion / VARTM](../03-manufacturing-processes/resin-infusion-vartm.md).

**AFP (Automated Fibre Placement)** — robotic placement of narrow prepreg tows onto a tool surface. See [AFP / ATL](../03-manufacturing-processes/afp-atl.md).

**ATL (Automated Tape Laying)** — robotic placement of wide prepreg tape onto a tool surface.

**Tow** — a narrow strip of unidirectional fibres. In AFP, typically 3.175 mm, 6.35 mm, or 12.7 mm wide.

**Course** — one pass of an AFP or ATL machine head across the part surface.

**Peel ply** — a fabric layer applied to the laminate surface during cure that peels off after cure, leaving a clean, textured surface ready for bonding.

**Flow media** — a coarse mesh used in resin infusion to distribute resin quickly across the part surface.

**Void** — a gas-filled cavity trapped inside the cured laminate. See [Common Defects](../03-manufacturing-processes/common-defects.md).

**Bridging** — where a ply spans across a concavity rather than conforming to the tool surface, leaving a gap underneath.

**Ramp ratio** — the ratio of horizontal distance to thickness change at a ply drop-off. Typical: 1:20.

## Sandwich Structure Terms

**Sandwich panel** — a structural element with two thin face sheets separated by a lightweight core. See [Sandwich Structures](../04-structural-analysis/sandwich-structures.md).

**Face sheet** — the thin composite laminate on each side of a sandwich panel. Carries bending and in-plane loads.

**Core** — the lightweight material between face sheets. Carries shear loads and maintains face sheet separation. Types: honeycomb, foam.

**Honeycomb** — a core material with hexagonal cells. Made from aluminium, Nomex, or thermoplastic.

**Potted insert** — a threaded insert bonded into a sandwich panel using structural adhesive to carry concentrated fastener loads.

## Abbreviations

| Abbreviation | Full term |
|---|---|
| CFRP | Carbon Fibre Reinforced Polymer |
| GFRP | Glass Fibre Reinforced Polymer |
| CLT | Classical Laminate Theory |
| FEA / FEM | Finite Element Analysis / Method |
| NDI / NDT | Non-Destructive Inspection / Testing |
| OML | Outer Mould Line |
| IML | Inner Mould Line |
| AFP | Automated Fibre Placement |
| ATL | Automated Tape Laying |
| VARTM | Vacuum Assisted Resin Transfer Moulding |
| OOA | Out-of-Autoclave |
| BVID | Barely Visible Impact Damage |
| MoS | Margin of Safety |
| FI | Failure Index |
| FPF | First Ply Failure |
| LPF | Last Ply Failure |
| UD | Unidirectional |
| Vf | Fibre Volume Fraction |

## Key Takeaways

- This glossary provides plain-English definitions for composites terminology
- Terms are grouped by topic: materials, structure, analysis, failure, manufacturing, sandwich
- Each definition links to the knowledge base page where the concept is explained in depth
- Use the abbreviations table as a quick reference when reading technical documents

## Further Reading / Tools

- [What Are Composites?](../01-fundamentals/what-are-composites.md) — start here if you are new to composites
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — start designing laminates
