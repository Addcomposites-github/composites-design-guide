---
title: "Failure Modes"
category: "fundamentals"
tags: ["failure", "delamination", "fibre-failure", "matrix-cracking", "buckling", "impact-damage"]
difficulty: "beginner"
related: ["what-are-composites.md", "laminate-theory.md", "../02-design-rules/stacking-sequences.md", "../04-structural-analysis/failure-criteria.md", "../03-manufacturing-processes/common-defects.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Failure Modes

Composites fail differently from metals. A steel bracket bends before it breaks — you get a visible warning. A composite laminate often fails suddenly, with little or no visible deformation beforehand. Understanding *how* composites fail is the first step to designing parts that don't.

This page covers the main failure modes, from the first tiny cracks in the resin to catastrophic structural collapse. Every composite designer — whether building a drone arm or a boat hull — needs to understand these.

## Why Composites Fail Differently from Metals

Metals are **ductile**. Pull a steel bar and it stretches visibly before breaking. Bend an aluminium bracket too far and it stays bent — it yields. That yielding is a built-in warning system.

Composites are **brittle**. The fibres carry almost all the load, and fibres do not yield. They are elastic right up to the point of failure, then they snap. There is no "bending before breaking" phase.

This has real consequences:

- A cracked steel tube on a bicycle frame usually bends first — you feel the wobble. A cracked carbon frame may show no sign until it breaks in two.
- A dented aluminium car panel absorbs energy gradually. A composite car panel can shatter.
- Metal fatigue cracks grow slowly and can be tracked with inspections. Composite damage can be hidden inside the laminate, invisible from the surface.

Because composites give fewer warnings, designers must understand each failure mode and build adequate safety margins into the laminate. Tools like [AddStack](https://addstack.addcomposites.com) let you check your laminate against multiple failure criteria before you commit to manufacturing.

## Fibre Failure

Fibre failure is the ultimate failure mode in a composite. When the fibres break, the ply has lost its primary load-carrying capability.

**In tension:** fibres simply snap when pulled beyond their ultimate strain. Carbon fibres typically fail at 1.5--1.8% strain in tension. Because millions of fibres share the load, tensile fibre failure tends to be sudden and explosive — the part fractures cleanly.

**In compression:** fibres fail by **micro-buckling** (also called kinking). Under compressive load, fibres — which are very thin columns — buckle sideways at a microscopic scale. The resin is supposed to stabilise them, but if the resin is weak, degraded, or if the fibres are even slightly misaligned, buckling starts early.

A critical design fact: **compressive fibre strength is typically only 50--60% of tensile strength** for carbon fibre composites. This asymmetry catches beginners off guard. If you design a laminate to handle tension and then flip the load direction, it may fail at barely half the expected load.

```
Fibre micro-buckling under compression:

  Load ←──  ──→ Load (compression)

  Before:           After:
  ||||||||          |/\/\/\/\|
  ||||||||          |\/\/\/\/|    ← fibres buckle sideways
  ||||||||          |/\/\/\/\|       between resin
```

## Matrix Cracking

Matrix cracking is the first type of damage to appear in a loaded composite laminate. These are cracks in the **resin** (matrix) between fibres, running parallel to the fibre direction within a single ply.

Think of a 90-degree ply in a laminate loaded in the 0-degree direction. The resin between the 90-degree fibres is being pulled apart. The fibres in that ply are not aligned with the load, so the resin alone must carry the transverse stress. Resin is weak — it cracks.

**What matrix cracks do:**

- **Reduce stiffness.** Each crack is a small interruption in load transfer. Many cracks together measurably soften the laminate.
- **Allow moisture ingress.** Cracks create pathways for water, fuel, or chemicals to seep into the laminate — bad for long-term durability, especially in boats and outdoor structures.
- **Seed delamination.** Matrix cracks can propagate to the ply interface and trigger delamination (see next section). This is the real danger.

Matrix cracks alone rarely destroy a laminate immediately. A well-designed layup tolerates some matrix cracking in off-axis plies under working loads. But ignoring them is dangerous — they are the starting point for worse damage.

```
Matrix cracks in a 90-degree ply (cross-section view):

    ─────────────────────────   0° ply  (fibres into the page ·)
    · · · ·│· · · ·│· · · ·    90° ply  (fibres left-right ─)
    ─ ─ ─ ─│─ ─ ─ ─│─ ─ ─ ─    ← cracks run parallel to fibres
    · · · ·│· · · ·│· · · ·       (vertical lines = matrix cracks)
    ─────────────────────────   0° ply

    Load direction: ←────→ (horizontal, along 0° fibres)
```

## Delamination

Delamination — the separation of adjacent ply layers — is the most common and most dangerous composite failure mode. Because the plies are held together only by the resin (no fibres cross between layers), the interface between plies is inherently weak.

**Common causes of delamination:**

- **Impact.** A dropped tool on an aircraft wing skin, a stone strike on a car panel. Even low-energy impacts can create internal delaminations.
- **Out-of-plane loads.** Composites are strong in-plane (along the fibres) but weak through-the-thickness. Peel forces, curved geometry under load, and pull-off loads at stiffener flanges all generate out-of-plane stresses.
- **Manufacturing defects.** Contamination between plies, poor cure, trapped release film — all can create regions with weak or zero bond between layers.
- **Matrix crack propagation.** Cracks within a ply reach the ply boundary and turn to run along the interface, separating the layers.

**Why delamination is so dangerous:**

A delaminated region acts like two thinner sub-laminates instead of one thick laminate. Bending stiffness drops dramatically (stiffness scales with thickness cubed). Under compression, the thin sub-laminate above the delamination buckles locally, the delamination grows, and the part fails. This sequence — delamination, local buckling, growth, collapse — happens fast.

```
Delamination between plies (side view):

    ┌──────────────────────────────┐
    │  0° ply                      │
    ├──────────────────────────────┤
    │ +45° ply                     │
    ├──────┐                ┌──────┤
    │      │  ← gap →       │      │  ← DELAMINATION
    ├──────┘                └──────┤     (plies separated)
    │ -45° ply                     │
    ├──────────────────────────────┤
    │ 90° ply                      │
    └──────────────────────────────┘

    The delaminated region has zero through-thickness bond.
    Under compressive load, the plies above it can buckle outward.
```

## Impact Damage and BVID

One of the most insidious threats to composite structures is **barely visible impact damage (BVID)**. A dropped tool, a hailstone, a runway stone — these low-energy impacts can leave the outer surface almost unmarked while creating a cone of internal delamination.

This happens because the impact energy travels through the laminate thickness, creating matrix cracks and delaminations at multiple ply interfaces. The damage zone spreads with depth, forming a pine-tree or cone pattern. The surface ply may show only a small dent or no mark at all.

**Why this matters in practice:**

- In aerospace, structures must tolerate BVID without catastrophic failure. Designs assume damage is present and unseen. This drives the requirement for damage-tolerant design — laminates that retain adequate strength even with delaminations up to a certain size.
- Inspection methods like **ultrasonic testing** (using sound waves to detect internal gaps) and **tap testing** (tapping the surface and listening for a dull sound instead of a sharp ring) are used to find hidden damage.
- For a bicycle frame or drone arm, the same physics applies. A frame that was dropped or struck may look fine but carry hidden delamination that reduces its strength, particularly under compression.

The practical takeaway: treat composite parts with respect after any impact event. When in doubt, inspect or replace.

## Buckling

Buckling is not a material failure — it is a **structural instability**. A thin panel under compression deflects sideways (out of plane) before the material itself reaches its failure stress. The panel "pops" into a buckled shape.

Buckling is relevant for:

- Thin skins on sandwich panels (drone body panels, boat hull skins)
- Unsupported panels between stiffeners (aircraft fuselage, wind turbine blade skins)
- Slender columns and struts (bicycle forks, truss members)

**Key facts about buckling in composites:**

- Buckling load depends on panel geometry (length, width, thickness), boundary conditions (how the edges are supported), and laminate stiffness — particularly the bending stiffness (D-matrix from Classical Laminate Theory).
- Adding stiffeners, increasing core thickness in a sandwich panel, or changing the stacking sequence to increase bending stiffness are all ways to push the buckling load higher.
- After a panel buckles, load redistributes. In some designs (like aircraft fuselage skin panels), post-buckling behaviour is acceptable and even designed for. In others (a drone arm, a bicycle fork), buckling is equivalent to failure.

Buckling often partners with delamination: a delamination creates a thin sub-laminate that buckles at a much lower load than the intact panel, which then causes the delamination to grow.

## How Failure Modes Interact — The Damage Cascade

In real structures, failure modes rarely act alone. They form a **damage cascade** — one mode triggers the next, accelerating toward collapse.

The typical sequence:

```
Matrix cracks form in off-axis plies (first damage, low load)
         │
         ▼
Cracks propagate to ply interfaces
         │
         ▼
Delamination initiates and grows
         │
         ▼
Delaminated sub-laminate loses compressive stability
         │
         ▼
Local buckling of the delaminated region
         │
         ▼
Rapid delamination growth + fibre failure
         │
         ▼
Catastrophic collapse
```

This cascade is why composites can appear healthy under inspection and then fail with little warning — most of the damage accumulation is internal and invisible.

Good composite design interrupts this cascade at every stage:

- **Stacking rules** (balanced, symmetric laminates; avoiding thick ply clusters) reduce matrix cracking. See [Stacking Sequences](../02-design-rules/stacking-sequences.md).
- **Tough resin systems** resist matrix cracking and slow delamination growth.
- **Adequate laminate thickness** and **stiffener spacing** prevent buckling.
- **Damage tolerance philosophy** assumes BVID is present and sizes the structure so that it still carries limit load with damage.

Use [AddStack](https://addstack.addcomposites.com) to check your laminate against failure criteria like Tsai-Wu, Hashin, or max stress — each of these criteria targets different failure modes and tells you which mode is critical for your design.

## Key Takeaways

- Composites fail with little warning — no yielding or visible bending before fracture, unlike metals
- Compressive fibre strength is roughly 50--60% of tensile strength; always check both load directions
- Matrix cracking is the first damage mode and the gateway to delamination
- Delamination is the most common and dangerous failure mode — it is often invisible from the surface and dramatically reduces compressive strength
- Impact damage (BVID) can hide severe internal delamination beneath an undamaged surface; inspect after any impact event
- Design to interrupt the damage cascade: good stacking rules, tough resins, adequate thickness, and damage tolerance margins

## Further Reading / Tools

- [What Are Composites?](what-are-composites.md) — the basics of fibres, resin, and laminates
- [Laminate Theory](laminate-theory.md) — how stacking sequence controls stiffness and strength
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — design rules that reduce failure risk
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) — Tsai-Wu, Hashin, max stress — when to use which
- [Common Defects](../03-manufacturing-processes/common-defects.md) — manufacturing problems that cause failure
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — check your laminate against multiple failure criteria
