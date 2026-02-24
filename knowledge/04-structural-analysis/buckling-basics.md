---
title: "Buckling Basics"
category: "analysis"
tags: ["buckling", "compression", "stability", "panel", "stiffener", "eigenvalue"]
difficulty: "intermediate"
related: ["sizing-a-panel.md", "sandwich-structures.md", "../02-design-rules/stacking-sequences.md", "../01-fundamentals/failure-modes.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Buckling Basics

A thin composite panel loaded in compression does not fail by the material crushing — it bows outward and loses its load-carrying ability long before the fibres reach their strength limit. This is **buckling**: a structural instability, not a material failure. Understanding buckling is essential because most composite structures are thin-walled (skins, panels, shells) and compression or shear loads are everywhere.

## What Is Buckling?

Imagine pressing down on a thin ruler standing on end. It does not shatter — it snaps sideways. The ruler has plenty of material strength left, but it has lost geometric stability. The same thing happens to a flat composite panel under in-plane compression: at a critical load, the panel deflects out of plane and can no longer carry increasing load.

```
Panel under compression — before and after buckling:

    Before:                    After (buckled):
    ┌──────────────┐          ┌──────────────┐
    │              │          │    ╱    ╲     │
    │  flat panel  │   →→→    │  ╱        ╲   │  ← out-of-plane
    │              │          │╱            ╲ │     deflection
    └──────────────┘          └──────────────┘
    →→  compression  ←←       →→  compression  ←←
```

**Critical point:** Buckling load depends on the panel's **geometry** (length, width, thickness) and **bending stiffness** (D-matrix from CLT), NOT on the material's compressive strength. A panel can buckle at 20% of the material's failure load if it is thin and unsupported.

## What Controls Buckling Load?

Three factors dominate:

### 1. Bending Stiffness (D-matrix)

The laminate's bending stiffness comes from the D-matrix in Classical Laminate Theory. It depends on:
- **Ply modulus** — stiffer fibres (carbon vs. glass) increase buckling resistance
- **Ply angles** — 0° plies contribute most to bending stiffness in the 0° direction; ±45° plies contribute to shear buckling resistance
- **Distance from the midplane** — plies far from the midplane contribute much more to bending stiffness than plies at the centre (stiffness scales with the cube of distance)

This is why the outer plies matter so much for buckling, and why sandwich panels (thin face sheets with a thick core) are so effective.

### 2. Panel Dimensions

Buckling load is inversely proportional to the square of the unsupported length. Double the unsupported span → buckling load drops to one quarter.

This is why stiffeners exist: they break a large panel into smaller bays, each with a higher buckling load.

```
One large unsupported panel:         Same panel with stiffeners:

    ┌────────────────────────┐       ┌────────┬────────┬────────┐
    │                        │       │        │        │        │
    │  low buckling load     │       │ higher │ higher │ higher │
    │  (wide unsupported)    │       │ buck.  │ buck.  │ buck.  │
    │                        │       │ load   │ load   │ load   │
    └────────────────────────┘       └────────┴────────┴────────┘
                                         ↑ stiffeners ↑
```

### 3. Boundary Conditions

How the panel edges are supported affects buckling load significantly:
- **Simply supported** (edges can rotate but not translate) — baseline
- **Clamped** (edges fixed against rotation and translation) — roughly 2–4× higher buckling load than simply supported
- **Free** (edge unsupported) — dramatic reduction in buckling load

Real structures fall between these idealised conditions.

## Types of Buckling in Composite Structures

### Global (Euler) Buckling

The entire panel or column bows in a single half-wave. This is the classical textbook case. Relevant for:
- Columns and struts
- Long, narrow stiffeners
- Slender sandwich beams

### Local (Bay) Buckling

The skin between stiffeners buckles in multiple half-waves while the stiffeners remain straight. This is the most common buckling mode in stiffened composite panels (wing skins, fuselage panels).

### Shear Buckling

A panel under in-plane shear (Nxy) buckles with a diagonal wave pattern. Relevant for:
- Shear webs (spar webs)
- Fuselage skins under torsion
- Wing skins under combined loads

±45° plies are most effective at resisting shear buckling.

### Crippling

A stiffener flange or web under compression buckles locally — the cross-section distorts. This is a local instability of the stiffener itself, distinct from the skin buckling between stiffeners.

## Designing Against Buckling

Several strategies increase buckling resistance without excessive weight:

**1. Add stiffeners** — the most common approach. Stringers (lengthwise) and frames (circumferential) divide skins into smaller bays. Each bay has a higher buckling load than the original large panel.

**2. Use sandwich construction** — a lightweight core (honeycomb or foam) separates two thin face sheets, dramatically increasing bending stiffness with minimal weight gain. See [Sandwich Structures](sandwich-structures.md).

**3. Optimise the stacking sequence** — place 0° plies on the outside for axial compression resistance, ±45° plies on the outside for shear buckling resistance. The outer plies contribute disproportionately to bending stiffness.

**4. Increase thickness** — adding plies increases bending stiffness (D-matrix scales with thickness cubed), but also adds weight. This is the least efficient approach.

**5. Reduce unsupported dimensions** — closer stiffener spacing, smaller panel bays, more frequent supports.

## Post-Buckling: Life After the Buckle

In metallic structures, post-buckling design is common — the skin is allowed to buckle at limit load, with stiffeners carrying the remaining load. The buckled skin continues to carry load in a redistributed pattern.

Composite structures are more cautious about post-buckling:
- Buckled composite skins develop high interlaminar stresses at the buckle crest
- Repeated buckling under cyclic loading can initiate delamination
- Post-buckling shapes are harder to predict accurately for composites

**Current practice:** Many aerospace programmes design composite skins to be buckling-free up to limit load. Some newer programmes allow limited post-buckling in non-critical areas with supporting test evidence.

## Key Takeaways

- Buckling is a geometric instability, not a material failure — thin panels bow out under compression before the material reaches its strength
- Buckling load depends on bending stiffness (D-matrix), panel dimensions, and boundary conditions
- Stiffeners are the primary solution: they break large panels into smaller bays with higher buckling loads
- Sandwich construction dramatically increases bending stiffness with minimal weight
- Outer plies contribute disproportionately to buckling resistance — place the most effective angles there
- Composite structures are generally designed to avoid buckling up to limit load

## Further Reading / Tools

- [Sandwich Structures](sandwich-structures.md) — the most weight-efficient buckling solution
- [Sizing a Panel](sizing-a-panel.md) — buckling check as part of the sizing workflow
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — outer ply placement affects buckling
- [Failure Modes](../01-fundamentals/failure-modes.md) — buckling as a structural failure mode
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — compute D-matrix for buckling inputs
