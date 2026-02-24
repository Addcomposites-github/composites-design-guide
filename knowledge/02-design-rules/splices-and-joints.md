---
title: "Splices and Joints"
category: "design-rules"
tags: ["splice", "overlap", "scarf", "butt-joint", "stagger", "ply-joint"]
difficulty: "intermediate"
related: ["ply-drop-offs.md", "stacking-sequences.md", "design-for-manufacture.md", "../03-manufacturing-processes/common-defects.md"]
tools: []
last_updated: "2026-02"
---

# Splices and Joints

Composite plies come in finite widths and lengths. When a ply is too small to cover the entire part in one piece, you need a **splice** — a joint within a single ply layer. Large aircraft skins, wind turbine blades, boat hulls, and long automotive panels all require splices. How you design them determines whether the structure carries full load or fails prematurely at the joint.

## Why Splices Exist

Material rolls have a fixed width (commonly 150 mm to 1500 mm depending on the material form). Parts are often wider or longer than the available material. Even with automated fibre placement (AFP), individual courses (strips of material) must start and stop. Every start and stop is a potential splice location.

Additionally, complex part geometries — double curvature, tight radii, cutouts — make it impossible to lay a single piece of material flat without wrinkling. Splitting a ply into sections and splicing them is the practical solution.

## Types of Ply Splices

### Butt Splice

The two ply edges are placed end-to-end with a small gap between them.

```
Butt splice (top view of a single ply):

    ══════════════╡ gap ╞══════════════
      ← ply A →   (1-3mm)  ← ply B →
```

**Characteristics:**
- Simple to manufacture
- Creates a small resin-rich gap (no fibre continuity across the joint)
- Load transfer relies on the adjacent plies above and below to bridge the gap
- Typical gap: 1–3 mm (too small and the plies overlap; too large and the resin pocket becomes a defect)

**Use when:** The ply is not a primary load carrier at the splice location, and adjacent plies provide adequate load bridging.

### Overlap Splice

One ply edge overlaps the other, creating a double-thickness region at the joint.

```
Overlap splice (side view):

    ═══════════════╗
                   ║ overlap zone (10–25 mm typical)
              ╔════╩════════════════════
              ║
```

**Characteristics:**
- Full fibre continuity through the load path (the overlap transfers load via shear)
- Creates a local thickness increase — a bump that can cause print-through on the surface or a stress concentration in the adjacent structure
- The overlap length must be long enough to transfer the full ply load through shear

**Typical overlap lengths:**
| Material form | Minimum overlap |
|---|---|
| Prepreg tape (unidirectional) | 10–15 mm |
| Woven prepreg | 15–25 mm |
| Dry fabric (for infusion) | 20–30 mm |

**Use when:** The ply must carry load across the splice and a small thickness bump is acceptable.

### Scarf Splice

Both ply edges are tapered (feathered) so they overlap gradually, maintaining a nearly constant total thickness.

```
Scarf splice (side view):

    ═══════════════╲
                    ╲  taper zone
                     ╲═══════════════
```

**Characteristics:**
- Smooth thickness transition — no bump
- Excellent load transfer — the long taper distributes shear stress gradually
- Much harder to manufacture than butt or overlap splices
- Primarily used in repairs and bonded joints between cured parts, less common in ply-level splicing during layup

**Use when:** Surface smoothness is critical and the joint must carry full load (especially in repairs).

## Splice Design Rules

### 1. Stagger Splices Between Plies

Never place splices in adjacent plies at the same location. Stagger them so that no two splices in consecutive plies line up.

```
Good — staggered splices:

    Ply 4: ═══════════════╡gap╞═══════════════
    Ply 3: ═════════╡gap╞════════════════════
    Ply 2: ══════════════════════╡gap╞════════
    Ply 1: ════════╡gap╞═════════════════════

Bad — aligned splices (all at the same location):

    Ply 4: ═══════════╡gap╞══════════════════
    Ply 3: ═══════════╡gap╞══════════════════
    Ply 2: ═══════════╡gap╞══════════════════
    Ply 1: ═══════════╡gap╞══════════════════
             ↑ all load-carrying ability lost at this line
```

**Minimum stagger distance:** Typically 15–25 mm between splices in adjacent plies. Some design standards specify stagger distances as a multiple of the overlap length.

### 2. Limit the Number of Spliced Plies at Any Cross-section

At any given cross-section through the laminate, no more than **one in every four plies** (25%) should contain a splice. This ensures that enough continuous plies exist to carry load through the splice zone.

More conservative designs limit splices to one in every five or six plies at a given cross-section.

### 3. Avoid Splicing Primary Load-carrying Plies

If the structure is primarily loaded in the 0° direction, avoid splicing the 0° plies if possible. Splice the ±45° or 90° plies instead — these contribute less to the axial load path, so the penalty is smaller.

When a primary-direction ply must be spliced, use overlap splices rather than butt splices to maintain fibre continuity.

### 4. Keep Splices Away from Stress Concentrations

Do not place splices:
- Within 2–3 hole diameters of a fastener hole
- At a ply drop-off location
- At or near a radius or joggle (a step in the tool surface)
- In a bond line region

### 5. Align Butt Splice Gaps with the Fibre Direction

For butt splices in unidirectional plies, the gap should run perpendicular to the fibre direction. This minimises the interruption in the load path.

```
Correct butt splice in a 0° ply (gap runs at 90° to fibres):

    →→→→→→→→→→→→ │ │ →→→→→→→→→→→→
    →→→→→→→→→→→→ │ │ →→→→→→→→→→→→   ← fibres (0°)
    →→→→→→→→→→→→ │ │ →→→→→→→→→→→→
                  gap
```

## Splices in Automated Layup (AFP/ATL)

Automated processes create splices at every course (strip) boundary. Key considerations:

- **Course gaps and overlaps:** AFP machines can be programmed for butt-splice (gap) or overlap. A typical gap tolerance is 0–2 mm; overlap tolerance is 0–2 mm.
- **Stagger is built into the programme:** Splice locations shift from ply to ply by a defined offset.
- **Tow drops and adds:** When courses start or stop mid-ply to follow a contoured boundary, each start/stop is effectively a splice. These are called tow drops (at the end) and tow adds (at the beginning).

## 3D Multi-Splice on Curved Surfaces

When a ply covers a large curved surface that exceeds the material roll width, a single straight splice line is not sufficient. A **3D multi-splice** divides the ply into multiple overlapping sections (cut-pieces) that follow the surface curvature.

Key parameters:
- **Overlap value** — how much adjacent cut-pieces overlap (typically 10–25 mm, same as flat overlap splices)
- **Stagger direction** — the direction along which splice lines are offset between plies
- **Stagger value** — the offset distance between splice lines in adjacent plies

On cylindrical surfaces (fuselage barrels, ducts), the multi-splice typically runs along the axis of the cylinder, with overlap along the circumference. On compound-curved surfaces, splice lines follow geodesic paths to minimise fibre distortion at the overlap.

**Roll width constraint:** If the flattened ply exceeds the material roll width, the number of splices is: `ceil(flat pattern width / roll width) - 1`. Verify this during the flat pattern check, not after manufacturing.

## Butt Splice Zones and No-Splice Zones

In zone-based design, entire regions can be designated as splice or no-splice zones:

**Butt splice zones** define areas where ply sections meet with a controlled gap. Parameters include the gap size (1–3 mm typical) and a parallel gap surface that guides the gap geometry on curved parts.

**No-splice zones** define areas where splices are strictly prohibited — typically near bolt holes, high-stress regions, structural joints, or areas with tight inspection requirements. When generating splices automatically, the tool routes splice lines around no-splice zones.

These zone designations apply to all plies within the designated region, ensuring consistent splice management across the laminate.

## Bonded Structural Joints (Component-Level)

Beyond ply-level splices, composite structures often need joints between separate components — skin-to-spar, skin-to-stiffener, or panel-to-panel. These are distinct from ply splices but share the same principles:

- **Scarf joints:** Taper both parts, bond together. Strongest joint type but requires precise machining.
- **Stepped-lap joints:** Similar to scarf but with discrete steps. Common in repair and manufacturing.
- **Single-lap and double-lap bonds:** Overlap one or both sides. Simple but peel stresses at the ends limit load capacity.

> These structural joints are a deep topic. This page focuses on ply-level splices within a layup. Structural bonded joint design deserves its own treatment.

## Key Takeaways

- Splices are necessary when material rolls are smaller than the part — design them, don't ignore them
- Butt splices are simplest but carry no load across the gap; overlap splices maintain fibre continuity
- Stagger splices between adjacent plies by at least 15–25 mm — never align them
- No more than 25% of plies should be spliced at any given cross-section
- Avoid splicing primary load-carrying plies when possible
- Keep splices away from holes, ply drops, radii, and bond lines

## Further Reading / Tools

- [Ply Drop-offs](ply-drop-offs.md) — the related problem of terminating plies for thickness changes
- [Design for Manufacture](design-for-manufacture.md) — how material width and part geometry drive splice locations
- [Stacking Sequences](stacking-sequences.md) — the stacking rules that must still be met at every cross-section, including through splice zones
