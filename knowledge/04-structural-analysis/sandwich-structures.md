---
title: "Sandwich Structures"
category: "analysis"
tags: ["sandwich", "honeycomb", "foam-core", "face-sheet", "core", "bending-stiffness"]
difficulty: "intermediate"
related: ["buckling-basics.md", "sizing-a-panel.md", "../01-fundamentals/failure-modes.md", "../02-design-rules/stacking-sequences.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Sandwich Structures

A sandwich panel is one of the most weight-efficient structural concepts in engineering. Take two thin, stiff face sheets (composite laminates), separate them with a thick, lightweight core (honeycomb or foam), and bond them together. The result has dramatically higher bending stiffness than a solid laminate of equivalent weight. This is the same principle as an I-beam — the flanges (face sheets) carry the bending loads, and the web (core) keeps them apart and carries the shear.

## Why Sandwich?

Consider a flat panel that must resist buckling under compression. You could make it from a solid 6 mm laminate — heavy and material-intensive. Or you could use two 1 mm face sheets separated by a 10 mm core — total thickness 12 mm but total weight is often less than the solid 6 mm panel, and the bending stiffness is dramatically higher.

```
Solid laminate vs. sandwich:

    Solid (6 mm):           Sandwich (1+10+1 = 12 mm):
    ┌──────────────┐        ┌──────────────┐  ← face sheet (1 mm)
    │              │        ├──────────────┤
    │  All composite│       │              │
    │  (heavy)     │        │  Core (10mm) │  ← lightweight core
    │              │        │  (light)     │
    └──────────────┘        ├──────────────┤
                            └──────────────┘  ← face sheet (1 mm)

    Weight: 100%            Weight: ~50%
    Bending stiffness: 1×   Bending stiffness: ~12×
```

The bending stiffness of a sandwich panel scales roughly with the square of the core thickness. Double the core → roughly 4× the bending stiffness, with only a small weight increase from the extra core.

## Core Materials

The core's job is to keep the face sheets apart and carry shear loads. It needs to be light, stiff in shear, and bondable to the face sheets.

### Honeycomb Core

Hexagonal cells made from aluminium, Nomex (aramid paper), or thermoplastic. The cells are filled with air — the material density is very low (30–130 kg/m³ depending on cell size and material).

```
Honeycomb cell geometry (top view):

     ╱╲    ╱╲    ╱╲
    ╱  ╲  ╱  ╲  ╱  ╲
    ╲  ╱  ╲  ╱  ╲  ╱
     ╲╱    ╲╱    ╲╱
     ╱╲    ╱╲    ╱╲
    ╱  ╲  ╱  ╲  ╱  ╲
    ╲  ╱  ╲  ╱  ╲  ╱
     ╲╱    ╲╱    ╲╱
```

**Types:**
| Core type | Density range | Strengths | Common use |
|---|---|---|---|
| Aluminium honeycomb | 30–130 kg/m³ | Highest shear strength/weight, good thermal conductivity | Aerospace floors, fairings |
| Nomex honeycomb | 30–96 kg/m³ | Good damage tolerance, fire resistant | Aircraft interiors, radomes |
| Thermoplastic honeycomb | 60–200 kg/m³ | Moisture resistant, thermoformable | Marine, automotive |

**Key properties:** Cell size (typically 3–6 mm) and density determine the shear strength and stiffness. Smaller cells and higher density = stronger but heavier.

### Foam Core

Closed-cell rigid foams — PVC (Divinycell), PET, polyurethane (PU), or syntactic foams. Foam is easier to handle than honeycomb because it is continuous (no open cells) and can be thermoformed to curved shapes.

| Foam type | Density range | Strengths | Common use |
|---|---|---|---|
| PVC (cross-linked) | 40–250 kg/m³ | Good all-round, excellent fatigue | Marine, wind energy |
| PET | 70–200 kg/m³ | Recyclable, good mechanical | Wind turbine blades |
| PU (polyurethane) | 30–200 kg/m³ | Cheap, easy to shape | Insulation, non-structural |
| Balsa wood | 100–250 kg/m³ | High shear strength, natural | Marine, wind energy |

### Honeycomb vs. Foam: When to Use Which

| Factor | Honeycomb | Foam |
|---|---|---|
| Weight efficiency | Better (lighter for same shear performance) | Slightly heavier |
| Ease of handling | Difficult (fragile, hard to cut to shape) | Easy (continuous, machineable) |
| Curved surfaces | Difficult (must be pre-formed or scored) | Easy (thermoformable) |
| Moisture ingress | Risky (open cells absorb water if skin is damaged) | Resistant (closed cells) |
| Cost | Higher | Lower |
| Flatwise tension | Lower (dependent on bond area) | Higher (continuous bond surface) |

## Sandwich Failure Modes

Sandwich structures have their own set of failure modes beyond those of solid laminates:

### 1. Face Sheet Failure

The face sheet fails in tension, compression, or under impact — the same failure modes as any composite laminate. The face sheets are sized just like a solid laminate panel (see [Sizing a Panel](sizing-a-panel.md)).

### 2. Core Shear Failure

The core carries all the transverse shear load. If the shear stress exceeds the core's shear strength, the core cracks or collapses. Lightweight cores (low density) are the weakest link in many sandwich designs.

```
Core shear failure:

    ────────────────────────   ← face sheet
    ┊  ╱  ┊  ╱  ┊  ╱  ┊
    ┊╱    ┊╱    ┊╱    ┊       ← core cells shearing
    ┊  ╱  ┊  ╱  ┊  ╱  ┊
    ────────────────────────   ← face sheet
```

### 3. Face Sheet Wrinkling

A thin face sheet on a compressible core can buckle locally — the face sheet wrinkles into the core. This is controlled by the face sheet thickness, core stiffness, and adhesive strength.

### 4. Core Crushing (Flatwise Compression)

Concentrated loads (e.g., under a fastener insert or support point) can crush the core. Honeycomb cores are particularly vulnerable to localised crushing. Potted inserts (core filled with structural adhesive around the fastener) are used to distribute these loads.

### 5. Debonding

The adhesive bond between face sheet and core fails. Often caused by:
- Poor surface preparation during manufacture
- Impact damage breaking the bond
- Moisture degrading the adhesive over time

Debonding is as dangerous to a sandwich panel as delamination is to a solid laminate.

## Design Considerations

**Core thickness selection:** Driven by bending stiffness requirements and buckling resistance. Typical range: 5–50 mm depending on panel size and loads.

**Face sheet thickness:** Driven by in-plane loads (tension, compression) and impact resistance. Minimum practical face sheet thickness: 2–3 plies (~0.25–0.4 mm) for very lightly loaded parts; 4–8 plies for structural applications.

**Core density selection:** Higher density = stronger in shear and compression but heavier. Match the core density to the shear loads — don't use a 200 kg/m³ core where a 50 kg/m³ core provides adequate shear strength.

**Inserts and hard points:** Any location where a fastener or concentrated load attaches to a sandwich panel needs a local reinforcement — a potted insert (core cavity filled with adhesive and an insert moulded in), a through-bolt with backing plates, or a local solid laminate region (core replaced with solid composite).

## Key Takeaways

- Sandwich panels achieve very high bending stiffness at low weight by separating thin face sheets with a lightweight core
- Bending stiffness scales roughly with the square of core thickness — doubling the core quadruples stiffness
- Honeycomb cores are lightest; foam cores are easier to handle and more moisture-resistant
- Sandwich-specific failure modes include core shear, face wrinkling, core crushing, and debonding
- Concentrated loads require potted inserts or local solid laminate reinforcement
- Sandwich design is the go-to solution when buckling drives the design of a thin composite panel

## Further Reading / Tools

- [Buckling Basics](buckling-basics.md) — sandwich panels exist primarily to solve the buckling problem
- [Sizing a Panel](sizing-a-panel.md) — sizing face sheets using the same CLT workflow
- [Failure Modes](../01-fundamentals/failure-modes.md) — face sheet failure modes are the same as solid laminate failure
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — design face sheet layups
