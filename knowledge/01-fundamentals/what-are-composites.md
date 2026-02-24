---
title: "What Are Composites?"
category: "fundamentals"
tags: ["composites", "carbon-fibre", "fibres", "resin", "laminate", "introduction"]
difficulty: "beginner"
related: ["fibre-types.md", "resin-systems.md", "laminate-theory.md"]
tools: []
last_updated: "2025-02"
---

# What Are Composites?

A composite material is made by combining two or more materials that, together, perform better than either could alone. In structural composites, you combine **fibres** (which are strong but fragile on their own) with a **resin** (a plastic that holds everything in shape) to create something that is both strong *and* handleable.

The most familiar example is carbon fibre reinforced polymer (CFRP) — what people usually mean when they say "carbon fibre". The black fibres you see are incredibly strong in tension; the resin binds them, transfers load between them, and gives the part its final shape.

## Why Use Composites?

The main reasons engineers choose composites over metals:

**Specific strength and stiffness** — composites offer high strength-to-weight and stiffness-to-weight ratios. A well-designed carbon fibre laminate can be 5× stronger than steel at a fraction of the weight.

**Design freedom** — you lay fibres exactly where the load goes, and in the orientation that carries it best. A metal plate is equally strong in all directions; a composite panel can be engineered to be stiff in one direction and flexible in another.

**Corrosion resistance** — carbon and glass fibre composites do not rust.

**Fatigue performance** — under cyclic loading, well-designed composites often outlast metals.

The trade-offs: composites are more expensive, require skilled manufacturing, are difficult to repair, and their anisotropy (direction-dependence) means design mistakes are penalised harshly.

## The Basic Building Block: A Ply

The fundamental unit of a composite structure is a **ply** (also called a lamina or layer). A single ply is a thin sheet of fibres — aligned in one direction (unidirectional, UD) or woven — embedded in cured resin.

```
Single unidirectional ply — fibres all running left to right (0°):

  →→→→→→→→→→→→→→→→→→→
  →→→→→→→→→→→→→→→→→→→   ← fibres (0° direction)
  →→→→→→→→→→→→→→→→→→→
  ───────────────────     ← resin matrix holding fibres together
```

A single ply is strong along the fibre direction but weak at 90° to it. Stack multiple plies at different angles and you get a **laminate** — a structure that can handle loads from multiple directions.

## The Laminate

A laminate is a stack of plies, bonded together through the resin. The stacking sequence — the order and angles of the plies — determines the laminate's structural behaviour.

```
Example laminate: [0° / +45° / -45° / 90°]s
(The 's' means the sequence is mirrored about the midplane — symmetric)

    ──────────────────   0°
    ──────────────────   +45°
    ──────────────────   -45°
    ──────────────────   90°
    ══════════════════   midplane
    ──────────────────   90°
    ──────────────────   -45°
    ──────────────────   +45°
    ──────────────────   0°
```

This [0/±45/90]s laminate is called a **quasi-isotropic** laminate — it behaves almost like an isotropic material (same stiffness in all in-plane directions) because the angles are evenly distributed.

## What Controls the Performance?

Four things determine how a composite laminate performs:

1. **Fibre type** — carbon, glass, aramid (Kevlar), basalt. Each has different stiffness, strength, density, and cost. See [Fibre Types](fibre-types.md).

2. **Resin type** — epoxy, polyester, vinyl ester, thermoplastic. Controls the manufacturing process, temperature resistance, and toughness. See [Resin Systems](resin-systems.md).

3. **Fibre volume fraction** — the proportion of the laminate that is fibre (vs. resin). Higher fibre fraction = stronger, stiffer, lighter. A good hand layup gets ~40–50%; autoclave prepreg gets ~55–65%.

4. **Stacking sequence** — the order and angles of the plies. This is where most of the engineering design work happens. See [Stacking Sequences](../02-design-rules/stacking-sequences.md).

## Key Takeaways

- A composite = fibres + resin, engineered to work together
- Strength comes from the fibres; the resin holds them in place and transfers load
- A ply is a single layer of fibres; a laminate is a stack of plies
- The stacking sequence (angles and order of plies) is the primary design variable
- Composites are strong and light but require careful design — mistakes are punished more than in metals

## Further Reading / Tools

- [Fibre Types](fibre-types.md) — carbon, glass, aramid compared
- [Resin Systems](resin-systems.md) — choosing the right matrix
- [Laminate Theory](laminate-theory.md) — the math behind stiffness and strength
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — start calculating once you've chosen your fibres and resin
