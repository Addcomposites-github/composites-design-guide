---
title: "CompositesAI (AnalySwift / VABS)"
category: "tools"
tags: ["CompositesAI", "AnalySwift", "VABS", "beam-analysis", "rotor-blade", "cross-section"]
difficulty: "intermediate"
related: ["addstack.md", "elamx2.md", "other-resources.md", "../04-structural-analysis/sizing-a-panel.md"]
tools: []
last_updated: "2026-02"
---

# CompositesAI (AnalySwift / VABS)

CompositesAI is a cloud-based composite beam and cross-section analysis tool developed by AnalySwift (with roots in Purdue University research). It goes beyond flat-panel CLT analysis into the realm of composite beams, blades, shafts, and other elongated structures. If you are designing a wind turbine blade, a helicopter rotor blade, a drone spar, or any composite beam-like structure, this tool fills a gap that basic CLT calculators cannot.

## What It Does

Standard CLT tools (AddStack, eLamX2) analyse flat laminates under in-plane and bending loads. CompositesAI analyses **composite cross-sections** — the full 2D geometry of a beam's cross-section, with multiple materials, layups, and complex shapes.

Key capabilities:
- **Cross-sectional stiffness** — computes the full 6×6 stiffness matrix of a composite beam section (extension, bending in two axes, torsion, and couplings)
- **Stress and strain recovery** — calculates 3D stresses within the cross-section under applied beam loads
- **Complex geometries** — handles multi-cell closed sections, open sections, built-up structures with webs, spar caps, and skins
- **Material mixing** — different laminates in different regions of the cross-section (e.g., carbon spar caps with glass skins)

## Who It Is For

- Engineers designing rotor blades (wind, helicopter, eVTOL)
- Drone designers sizing composite spars and booms
- Anyone working with composite tubes, shafts, or elongated structures
- Researchers needing validated beam cross-section properties

## When to Use It vs. CLT Tools

| What you are analysing | Use |
|---|---|
| Flat panel under Nx, Ny, Nxy | AddStack or eLamX2 (CLT) |
| Flat panel buckling | AddStack or eLamX2 |
| Composite tube / shaft | CompositesAI |
| Rotor blade cross-section | CompositesAI |
| Composite I-beam or C-channel | CompositesAI |
| Spar cap + web + skin assembly | CompositesAI |

**Rule of thumb:** If the structure is elongated (length >> cross-section dimensions) and has a complex cross-section, CompositesAI is the right tool. If it is a flat or gently curved panel, use CLT.

## How to Access

CompositesAI is available as a cloud platform through AnalySwift. It has both free and paid tiers — the free tier covers basic cross-section analysis. Check the AnalySwift website for current access options and capabilities.

## Underlying Theory: VABS

CompositesAI is based on VABS (Variational Asymptotic Beam Sectional Analysis), a theory developed at Purdue University by Professor Wenbin Yu. VABS uses variational asymptotic methods to rigorously reduce a 3D beam problem to a 1D beam analysis plus a 2D cross-sectional analysis. This is mathematically rigorous — not an approximation like assuming thin-wall theory — and has been validated against full 3D finite element analysis for a wide range of composite beam geometries.

## Key Takeaways

- CompositesAI analyses composite beam cross-sections — tubes, blades, spars, shafts
- It computes the full 6×6 beam stiffness matrix and recovers 3D stresses from beam loads
- Use it when the structure is beam-like (length >> width); use CLT tools for flat panels
- Based on the VABS theory from Purdue — rigorously validated
- Free tier available for basic analysis

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — for flat panel CLT analysis
- [eLamX2](elamx2.md) — another free CLT tool for flat laminates
- [CRDS — Composite Rotor/Sleeve Design](https://www.addcomposites.com/addcomposites-apps/crds) — free tool for rotor and sleeve design
- [Other Resources](other-resources.md) — additional free tools and references
