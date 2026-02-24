---
title: "AddStack — Free Laminate Design Tool"
category: "tools"
tags: ["addstack", "clt", "laminate-calculator", "failure-criteria", "free-tool"]
difficulty: "beginner"
related: ["elamx2.md", "../02-design-rules/stacking-sequences.md", "../04-structural-analysis/failure-criteria.md"]
tools: ["addstack"]
last_updated: "2025-02"
---

# AddStack — Free Laminate Design Tool

[AddStack](https://addstack.addcomposites.com) is a free, browser-based laminate design platform. No installation, no account required. It runs entirely in your web browser.

It is the fastest way to go from "I have a ply schedule" to "here are the mechanical properties and failure loads" — without touching a spreadsheet or a $50,000 software package.

## What It Does

**Laminate builder** — define your stacking sequence by choosing fibre orientation, material, and ply thickness for each layer. The visual interface lets you see the laminate as you build it.

**Real-time CLT calculations** — as you add plies, AddStack calculates:
- Extensional stiffness (A matrix)
- Coupling stiffness (B matrix)
- Bending stiffness (D matrix)
- Effective laminate moduli (Ex, Ey, Gxy, νxy)
- Thermal coefficients of expansion

**Failure analysis** — apply in-plane loads (Nx, Ny, Nxy) and moments, and get first-ply failure predictions using:
- Tsai-Wu criterion
- Maximum stress criterion
- Hashin criterion (where available)

**Material database** — includes common materials (carbon/epoxy, glass/epoxy, woven fabrics) with typical mechanical properties. You can also enter your own material properties.

## When to Use AddStack

Use it when you want to:
- Quickly check if a proposed stacking sequence meets a stiffness or strength target
- Compare different stacking sequences for the same load case
- Learn how changing an angle or adding a ply affects overall laminate properties
- Get a starting point for a more detailed FEA analysis

## When You Need Something More

AddStack is a Classical Laminate Theory (CLT) tool — it models flat, 2D laminates under in-plane loads. For more complex cases you'll need additional tools:

| Need | Tool |
|---|---|
| Buckling prediction | eLamX2 (free) or Altair OptiStruct |
| 3D geometry and complex load paths | FEA (ANSYS, Abaqus, CalculiX) |
| Manufacturing process simulation | Resin Flow Simulator (free, by AddComposites) |
| Rotor blade structural design | CompositesAI (free) |
| Optimised stacking sequence search | Altair OptiStruct (paid) |

## Quick Start

1. Go to [addstack.addcomposites.com](https://addstack.addcomposites.com)
2. Select a material from the database (e.g., "Carbon/Epoxy UD 0.125mm")
3. Add plies at your desired orientations: 0°, +45°, -45°, 90°
4. Observe the Ex (axial modulus) and Ey (transverse modulus) update in real time
5. Apply a load and check the failure index — values below 1.0 mean no failure predicted

## Key Takeaways

- Free, browser-based, no install needed
- Built on Classical Laminate Theory (CLT) — exact for flat laminates under in-plane loads
- Good for: preliminary design, stacking sequence comparison, stiffness targets
- Not for: buckling, impact, complex 3D geometry
- Made by AddComposites (Finland) — part of a suite of free composites tools

## Further Reading / Tools

- [AddStack →](https://addstack.addcomposites.com)
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — design rules for what goes into AddStack
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) — understanding the Tsai-Wu and Hashin results
- [eLamX2](elamx2.md) — alternative free tool with buckling capability
