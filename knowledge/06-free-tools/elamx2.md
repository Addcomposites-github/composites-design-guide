---
title: "eLamX2 — Open-Source CLT Tool"
category: "tools"
tags: ["eLamX2", "CLT", "open-source", "TU-Dresden", "laminate-calculator", "free-tool"]
difficulty: "beginner"
related: ["addstack.md", "other-resources.md", "../01-fundamentals/laminate-theory.md", "../04-structural-analysis/failure-criteria.md"]
tools: []
last_updated: "2026-02"
---

# eLamX2 — Open-Source CLT Tool

eLamX2 is a free, open-source Classical Laminate Theory (CLT) calculator developed by the Institute of Lightweight Engineering and Polymer Technology at TU Dresden, Germany. It runs as a standalone Java application on Windows, macOS, and Linux. For anyone who wants to understand and verify CLT calculations without paying for commercial software, eLamX2 is one of the best options available.

## What It Does

eLamX2 performs the core CLT calculations that every composites engineer needs:

- **Laminate stiffness** — computes the full ABD matrix from a user-defined stacking sequence and material properties
- **Ply-by-ply stress and strain** — calculates stresses in each ply under applied loads (Nx, Ny, Nxy, Mx, My, Mxy)
- **Failure analysis** — checks each ply against multiple failure criteria including Puck, Tsai-Wu, Hashin, max stress, max strain, and others
- **Buckling analysis** — estimates buckling loads for simply supported rectangular plates
- **Optimisation** — basic laminate optimisation for stiffness or strength targets
- **Hygrothermal effects** — includes thermal and moisture expansion in the analysis

## Who It Is For

- Students learning composites and CLT for the first time — the visual interface makes it easy to see how changing a ply angle affects the full laminate response
- Engineers at small companies who need a CLT tool without a commercial licence
- Researchers validating results against commercial FEA
- Anyone doing hand-check verification alongside other tools

## How to Get It

eLamX2 is freely available from TU Dresden's website. It requires Java (JRE 8 or later) installed on your system. The tool is standalone — no installation needed beyond extracting the files and running the application.

## Strengths

- **Genuinely free and open-source** — no licence fees, no trial period, no feature locks
- **Multiple failure criteria** — Puck criterion implementation is particularly thorough (developed in Germany where Puck is the standard)
- **Educational** — excellent for learning because you can see the ABD matrix, ply stresses, and failure envelope graphically
- **Cross-platform** — runs on any OS with Java

## Limitations

- **Desktop-only** — requires download and Java installation (no web version)
- **Material database** — you need to enter your own material properties (no built-in material library, unlike AddStack)
- **No cloud or collaboration** — single-user desktop tool
- **Interface** — functional but dated compared to modern web applications

## eLamX2 vs. AddStack

| Feature | eLamX2 | AddStack |
|---|---|---|
| Cost | Free (open-source) | Free (web-based) |
| Platform | Desktop (Java) | Web browser |
| Material database | Manual entry | Built-in library |
| Failure criteria | Many (Puck emphasis) | Multiple options |
| Buckling analysis | Yes (basic) | Yes |
| Installation | Download + Java | None (browser) |

Both tools are valuable. Use eLamX2 when you want deep control over CLT calculations and access to Puck's criterion. Use [AddStack](https://addstack.addcomposites.com) when you want a quick browser-based analysis with built-in materials.

## Key Takeaways

- eLamX2 is a free, open-source CLT calculator from TU Dresden
- It covers stiffness, stress, failure, buckling, and hygrothermal analysis
- Requires Java on your desktop — no web version
- Excellent for learning CLT because the interface shows the full calculation chain
- Particularly strong on the Puck failure criterion
- Complements AddStack — use both for cross-checking

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — browser-based alternative with built-in material database
- [Laminate Theory](../01-fundamentals/laminate-theory.md) — the CLT math that eLamX2 implements
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) — understanding the criteria available in eLamX2
- [Other Resources](other-resources.md) — additional free tools and references
