---
title: "Prepreg and Autoclave Processing"
category: "manufacturing"
tags: ["prepreg", "autoclave", "out-of-autoclave", "OOA", "cure-cycle", "aerospace"]
difficulty: "intermediate"
related: ["vacuum-bagging.md", "afp-atl.md", "common-defects.md", "../01-fundamentals/resin-systems.md"]
tools: []
last_updated: "2026-02"
---

# Prepreg and Autoclave Processing

Prepreg (pre-impregnated) material is composite reinforcement — usually unidirectional carbon fibre tape or woven fabric — that comes with the resin already mixed into it at the factory. The resin is partially cured (B-staged) so the material is tacky but not liquid. You lay it up dry-handed (no mixing, no brushes), bag it, then cure it in an autoclave or oven under heat and pressure. This process delivers the highest, most repeatable composite quality — and is the standard for aerospace structures.

## What Is Prepreg?

A roll of prepreg looks and feels like a slightly sticky, flexible tape or fabric. The resin is uniformly distributed through the fibres at a precisely controlled ratio (typically 32–42% resin by weight). Because the resin content is controlled at the factory rather than on the shop floor, part-to-part variation is dramatically lower than wet layup or infusion.

**Storage:** The partially cured resin continues to advance slowly at room temperature. Prepreg must be stored frozen (typically -18°C / 0°F) to preserve its shelf life (6–12 months frozen, 2–4 weeks at room temperature). This is a significant logistics constraint.

## The Autoclave

An autoclave is a pressurised oven — essentially a large pressure vessel that can apply both heat and gas pressure simultaneously.

```
Autoclave cross-section:

    ╔══════════════════════════════════════╗
    ║                                      ║
    ║    Heated pressurised gas (N₂)       ║
    ║    ┌────────────────────────┐        ║
    ║    │    Vacuum bag           │        ║
    ║    │    ┌──────────────┐    │        ║
    ║    │    │  LAMINATE     │    │        ║
    ║    │    └──────────────┘    │        ║
    ║    │    MOULD / TOOL        │        ║
    ║    └────────────────────────┘        ║
    ║                                      ║
    ╚══════════════════════════════════════╝

    Vacuum inside bag:  removes air and volatiles
    Pressure outside bag: 0.3–0.7 MPa (3–7 atm), compacts the laminate
```

**Why both vacuum AND pressure?**
- The vacuum inside the bag removes trapped air and volatile gases from the resin.
- The external gas pressure (typically nitrogen to prevent fire risk) compacts the laminate far beyond what vacuum alone can achieve.
- The combination produces void contents below 1% and fibre volume fractions of 55–65%.

## The Cure Cycle

A cure cycle is a controlled time-temperature-pressure profile. Different prepreg systems require different cycles, but a typical aerospace 180°C cure looks like:

```
Temperature and pressure vs. time:

    180°C  ─────────────────────────────────
           /                                 \
    120°C /   ← optional dwell (hold)         \
         /     to equalise temperature         \
        /                                       \
    RT ──                                        ──── RT

    Ramp up    Hold at 180°C       Ramp down
    (1-3°C/min)  (2 hours)         (2-3°C/min)

    Pressure applied at ~0.7 MPa throughout heating
    Vacuum held until pressure reaches ~0.15 MPa, then vented
```

**Common cure temperatures:**
| Prepreg class | Cure temp | Typical use |
|---|---|---|
| Low-temperature | 80–120°C | Tooling, non-structural, repair |
| Standard aerospace | 120°C (250°F) | Secondary structure, interiors |
| High-performance | 177–180°C (350°F) | Primary structure, hot/wet environments |

**Cure time:** Typically 1–2 hours at the dwell temperature. The resin supplier specifies the exact cycle.

## Layup Process for Prepreg

1. **Remove from freezer** — let the roll warm to room temperature (30–60 min) before opening the sealed bag. Opening cold prepreg causes condensation, which introduces moisture.
2. **Cut plies** — using a ply cutter (manual or CNC). Prepreg is backed with a release paper/film that is removed during layup.
3. **Lay up on the tool** — place each ply on the mould, using the tack (stickiness) of the resin to hold it in position. Press down with a hand roller.
4. **Debulk every 3–5 plies** — apply a vacuum bag and pull vacuum for 10–15 minutes to compact the stack, remove trapped air, and ensure ply conformance to the tool shape. This is critical for thick laminates.
5. **Complete the layup** — continue until all plies are placed.
6. **Final bag** — apply the full vacuum bag stack (peel ply, release film, breather, bag, sealant tape).
7. **Load into autoclave** — connect vacuum lines, seal the autoclave door, run the cure cycle.
8. **Demould after cooling** — open the autoclave after the part has cooled below ~60°C.

## Out-of-Autoclave (OOA) Prepreg

Autoclaves are expensive — a large aerospace autoclave costs millions of dollars and consumes enormous energy per cycle. Out-of-Autoclave (OOA) prepregs are a newer class of material designed to achieve near-autoclave quality using vacuum pressure alone (cured in a standard oven).

**How OOA prepregs differ:**
- Resin formulated to flow and consolidate at vacuum-only pressure
- Engineered air pathways in the prepreg that allow trapped air to evacuate more effectively
- Slightly lower fibre volume fraction than autoclave-processed material (~55% vs ~60%) but still far better than wet layup

**OOA has opened prepreg quality to:**
- Smaller companies without autoclave access
- Large structures that don't fit in available autoclaves (e.g., large wind turbine spars, marine structures)
- Cost-sensitive aerospace programmes

## Cost and Trade-offs

| Factor | Prepreg/autoclave | Wet layup | Infusion |
|---|---|---|---|
| Material cost | High (prepreg premium) | Low | Low |
| Equipment cost | Very high (autoclave) | Minimal | Moderate |
| Fibre volume fraction | 55–65% | 35–50% | 50–60% |
| Void content | < 1% | 3–10% | 1–3% |
| Repeatability | Excellent | Poor | Good |
| Shelf life concern | Yes (frozen storage) | No | No |
| Suitable for | Aerospace, high-performance | Prototypes, makers | Medium-performance |

## Key Takeaways

- Prepreg is fibre with resin already applied at a controlled ratio — no mixing on the shop floor
- Autoclave processing adds 3–7 atm of pressure beyond vacuum, achieving < 1% void content and 55–65% fibre volume fraction
- Prepreg must be stored frozen and has limited out-time at room temperature
- Debulking every 3–5 plies is essential for thick laminates
- Out-of-Autoclave (OOA) prepregs deliver near-autoclave quality using oven cure and vacuum-only pressure
- This process delivers the highest quality but at the highest cost — choose it when performance justifies the investment

## Further Reading / Tools

- [Vacuum Bagging](vacuum-bagging.md) — the vacuum side of autoclave processing
- [AFP / ATL](afp-atl.md) — automated layup of prepreg tape for large or complex parts
- [Common Defects](common-defects.md) — defects that even prepreg processing can produce
- [Resin Systems](../01-fundamentals/resin-systems.md) — the matrix chemistry behind cure cycles
