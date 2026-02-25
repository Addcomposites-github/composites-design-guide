---
title: "Fibre Types"
category: "fundamentals"
tags: ["carbon-fibre", "glass-fibre", "aramid", "basalt", "kevlar", "fibre-properties"]
difficulty: "beginner"
related: ["what-are-composites.md", "resin-systems.md", "../02-design-rules/stacking-sequences.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Fibre Types

Reinforcing fibres are the backbone of any composite. The resin holds the shape and transfers load between fibres, but the fibres themselves carry most of the stress and provide stiffness. Choosing the right fibre determines how strong, stiff, heavy, and expensive your part will be. This page covers the four main fibre families — carbon, glass, aramid, and basalt — plus a brief look at natural fibres. By the end you will know when to reach for each one.

## What Reinforcing Fibres Do

A composite is a partnership: the matrix (resin) binds everything together, and the fibres resist the loads. Think of it like reinforced concrete — the steel rebar carries the tension, and the concrete carries the compression. In a composite laminate, fibres do the heavy lifting in the direction they are aligned. This is why fibre orientation matters so much (see [stacking sequences](../02-design-rules/stacking-sequences.md)).

Two properties dominate fibre selection:

- **Tensile modulus** (stiffness) — how much the fibre resists stretching. A higher modulus means less deflection under load. Measured in gigapascals (GPa).
- **Tensile strength** — the maximum stress the fibre can take before it breaks. Measured in megapascals (MPa).

Other factors — density, cost, impact toughness, electrical conductivity, and moisture absorption — often decide the final choice just as much as raw mechanical numbers.

## Carbon Fibre

Carbon fibre is the high-performance option. It offers the best stiffness-to-weight ratio of any common reinforcing fibre, which is why it dominates aerospace, motorsport, and high-end sporting goods.

### Grades of carbon fibre

Carbon fibre comes in several grades defined by tensile modulus:

| Grade | Typical modulus | Character |
|---|---|---|
| Standard modulus (SM) | 230–240 GPa | Best balance of strength and cost. Most widely used. |
| Intermediate modulus (IM) | 270–320 GPa | Higher stiffness, still good strength. Common in primary aircraft structure. |
| High modulus (HM) | 350–600 GPa | Very stiff but more brittle and expensive. Used where deflection control is critical (satellite dishes, telescope tubes). |

Most hobby and industrial users work with standard-modulus carbon. Intermediate modulus is the workhorse of aerospace. High modulus is niche.

### Key properties

- **High specific stiffness and strength** — roughly three to five times stiffer than steel at one-fifth the density.
- **Low density** — around 1.75–1.80 g/cm³.
- **Brittle failure** — carbon fibres do not yield. They carry load right up to failure and then snap suddenly with little warning.
- **Electrically conductive** — important for lightning-strike protection in aircraft, but a nuisance when electrical insulation is needed.
- **Low coefficient of thermal expansion** — carbon parts barely change size with temperature, valuable for precision structures.

### Typical uses

Racing car monocoques, bicycle frames and forks, drone arms and frames, aircraft wing skins and fuselage panels, sporting goods (tennis rackets, golf shafts), and high-end automotive panels.

### Cost

Carbon fibre is the most expensive of the common fibres. Expect to pay roughly five to fifteen times more per kilogram than E-glass. Price drops as production volume grows, but it remains a premium material.

## Glass Fibre

Glass fibre is the workhorse of the composites industry. It handles the vast majority of composite parts produced worldwide — boats, wind turbine blades, pipes, tanks, building panels, and general industrial applications. It is cheap, well understood, and readily available.

### Types of glass fibre

| Type | Character |
|---|---|
| **E-glass** (electrical glass) | The standard. Good strength, low cost. Accounts for over 90% of all glass fibre used. |
| **S-glass** (strength glass) | About 30% stronger and stiffer than E-glass, but two to three times the price. Used where glass is preferred but more performance is needed (ballistic armour backing, aerospace secondary structure). |

### Key properties

- **Good tensile strength** — E-glass ultimate tensile strength is around 3,400 MPa, comparable to standard-modulus carbon.
- **Lower stiffness** — modulus of roughly 72 GPa for E-glass, about one-third that of carbon. Glass parts flex more under the same load.
- **Higher density** — around 2.55 g/cm³, significantly heavier than carbon (1.78 g/cm³).
- **Electrically insulating** — glass is a natural insulator, making it the default choice for radomes, circuit boards, and parts near electrical systems.
- **Good corrosion resistance** — stands up well to moisture and many chemicals, especially when paired with vinyl ester or polyester resin.

### Typical uses

Boat hulls and decks, wind turbine blades, automotive body panels (bonnets, bumpers), chemical storage tanks, construction panels, surfboards, and any application where cost matters more than minimum weight.

### Cost

E-glass is the cheapest structural fibre available. A roll of woven E-glass fabric costs a fraction of an equivalent carbon fabric. This is why glass fibre is the default starting point for most non-aerospace projects.

## Aramid Fibre (Kevlar)

Aramid fibres — best known by the DuPont trade name Kevlar — are organic polymer fibres with exceptional toughness and impact resistance. Where carbon snaps and glass cracks, aramid absorbs energy and resists penetration.

### Key properties

- **Outstanding impact resistance** — aramid absorbs more energy before failure than carbon or glass. This makes it the go-to fibre for ballistic protection and crash structures.
- **Good tensile strength** — around 3,000–3,600 MPa depending on grade.
- **Moderate stiffness** — roughly 60–130 GPa depending on grade (standard Kevlar 29 is around 70 GPa; high-modulus Kevlar 49 is around 125 GPa).
- **Poor compressive strength** — aramid fibres buckle under compression at relatively low stress. This limits their use in structures loaded in bending or compression.
- **Difficult to cut and machine** — the fibres are so tough they fuzz and fray rather than cutting cleanly. Special shears or laser cutting are needed.
- **Absorbs moisture** — aramid picks up water from the environment (up to about 4% by weight), which can degrade long-term performance if not sealed properly.
- **Low density** — around 1.44 g/cm³, the lightest of the four main fibre types.

### Typical uses

Body armour and ballistic panels, motorcycle protective clothing, kayak and canoe hulls (impact zones), helicopter blade leading edges, rope and cable, and hybrid laminates where aramid plies are added to carbon laminates for damage tolerance.

### A practical note on hybrids

Because aramid is weak in compression but superb under impact, engineers often combine it with carbon in a hybrid laminate. Carbon carries the primary loads; aramid plies on the outer surfaces catch impacts and prevent catastrophic splintering. This is common in racing car crash structures and high-end helmets.

## Basalt Fibre

Basalt fibre is made from volcanic basalt rock and sits between E-glass and S-glass in mechanical performance. It offers better temperature resistance than glass (usable up to about 650 degrees Celsius) and good chemical resistance.

Basalt is an emerging option, not yet as widely available or well characterised as glass or carbon. It is gaining traction in civil engineering (rebar replacement), fire-resistant panels, and applications where glass is adequate but a modest performance or temperature upgrade is needed without jumping to carbon pricing.

Cost is slightly above E-glass but well below carbon. Watch this space — basalt fibre production is growing.

## Natural Fibres

Flax, hemp, jute, and other plant-based fibres are attracting interest for sustainability reasons. They are renewable, biodegradable, and have lower embodied energy than glass or carbon.

Properties are modest — stiffness and strength fall below E-glass in most cases — but for non-structural or lightly loaded parts (interior panels, consumer goods casings, furniture), natural fibres can make sense. Moisture sensitivity and batch-to-batch variability remain challenges.

Natural fibre composites are common in the European automotive industry for interior door panels and trim pieces, where low weight and sustainability credentials matter more than ultimate strength.

## Fibre Forms: UD, Woven, and Non-Crimp Fabrics

Fibres are supplied in different physical forms that affect draping, layup speed, and mechanical properties:

**Unidirectional (UD) tape:** All fibres run in one direction. Provides the highest mechanical properties in that direction. Available as prepreg tape for hand layup or AFP, or as dry tape for infusion. Limited draping on doubly curved surfaces.

**Woven fabric:** Fibres interlaced in two directions (typically 0° and 90°). Good draping, easier to handle, but the interlacing (crimp) reduces stiffness by 10–15% compared to equivalent UD. Common weave styles: plain, twill (2×2), satin (5-harness, 8-harness).

**Non-crimp fabric (NCF):** Multiple layers of straight fibres stitched together without interlacing. Combines the handling advantages of fabric with mechanical properties closer to UD. See [Non-Crimp Fabrics](../02-design-rules/non-crimp-fabrics.md) for detailed design guidance.

**Fibre sizing:** All commercial fibres receive a surface treatment (sizing) during production that promotes bonding with the resin matrix. The sizing must be compatible with your chosen resin — epoxy-sized fibres may not bond well with polyester resin and vice versa. Check material datasheets for compatibility.

## Fibre Comparison Table

The table below gives typical values for dry fibres. Actual laminate properties depend on fibre volume fraction, resin type, and layup — use [AddStack](https://addstack.addcomposites.com) to calculate laminate-level properties for your specific design.

```
┌──────────────────┬─────────────┬─────────────────┬──────────────┬────────────────┐
│ Fibre            │ Tensile     │ Tensile         │ Density      │ Relative       │
│                  │ modulus     │ strength        │ (g/cm³)      │ cost           │
│                  │ (GPa)       │ (MPa)           │              │                │
├──────────────────┼─────────────┼─────────────────┼──────────────┼────────────────┤
│ Carbon (SM)      │ 230         │ 3,500–5,500     │ 1.78         │ $$$$           │
│ Carbon (IM)      │ 290         │ 4,500–6,000     │ 1.78         │ $$$$$          │
│ Carbon (HM)      │ 390–590     │ 2,500–4,000     │ 1.85–1.90    │ $$$$$$         │
│ E-glass          │ 72          │ 3,400           │ 2.55         │ $              │
│ S-glass          │ 86          │ 4,500           │ 2.49         │ $$             │
│ Aramid (Kevlar)  │ 70–125      │ 3,000–3,600     │ 1.44         │ $$$            │
│ Basalt           │ 85–90       │ 3,000–4,800     │ 2.65         │ $–$$           │
│ Flax             │ 27–80       │ 500–1,500       │ 1.40–1.50    │ $              │
└──────────────────┴─────────────┴─────────────────┴──────────────┴────────────────┘
```

> Note: These are representative fibre-level values. Laminate properties will be lower and depend on resin, fibre volume fraction, and layup. Use a laminate calculator such as [AddStack](https://addstack.addcomposites.com) for design work.

## How to Choose: A Simple Decision Guide

Picking a fibre comes down to answering a few questions about your application:

**1. Is weight your top priority?**
Use carbon fibre. Nothing else matches its stiffness-to-weight ratio. If budget allows, start with standard-modulus carbon.

**2. Is cost your top priority?**
Use E-glass. It is cheap, widely available, and strong enough for most non-aerospace applications. Boats, tanks, and wind blades are built from it for good reason.

**3. Do you need impact resistance or damage tolerance?**
Use aramid, or add aramid plies to a carbon laminate. Aramid absorbs energy that would shatter carbon or crack glass.

**4. Do you need electrical insulation?**
Use glass. Carbon is conductive and will short-circuit electrical systems or interfere with radio signals.

**5. Do you need high temperature resistance?**
Consider basalt fibre. It handles higher temperatures than glass without the cost of carbon.

**6. Is sustainability a requirement?**
Look at natural fibres (flax, hemp) for lightly loaded or non-structural parts.

```
Decision flow:

  Weight critical? ──Yes──► CARBON
       │ No
  Budget tight? ──Yes──► E-GLASS
       │ No
  Impact loads? ──Yes──► ARAMID (or carbon/aramid hybrid)
       │ No
  Electrical insulation needed? ──Yes──► GLASS
       │ No
  High temperature? ──Yes──► BASALT
       │ No
  Sustainability focus? ──Yes──► NATURAL FIBRES (flax, hemp)
       │ No
  Default ──► E-GLASS (cheapest, most forgiving to work with)
```

## Fibre Property Comparison Table

This table summarises typical fibre properties. Use it for quick comparisons during preliminary design.

| Property | E-Glass | S-Glass | Carbon (HS) | Carbon (IM) | Carbon (HM) | Aramid (Kevlar 49) | Basalt |
|----------|---------|---------|-------------|-------------|-------------|-------------------|--------|
| **Tensile modulus (GPa)** | 72 | 87 | 230 | 290 | 390 | 125 | 89 |
| **Tensile strength (MPa)** | 3,400 | 4,600 | 4,900 | 5,700 | 3,400 | 3,000 | 4,800 |
| **Density (g/cm³)** | 2.54 | 2.49 | 1.80 | 1.77 | 1.87 | 1.44 | 2.65 |
| **Specific modulus (GPa·cm³/g)** | 28 | 35 | 128 | 164 | 209 | 87 | 34 |
| **Failure strain (%)** | 4.7 | 5.3 | 2.1 | 1.9 | 0.9 | 2.4 | 3.1 |
| **Cost ($/kg)** | 2–5 | 10–20 | 15–30 | 30–80 | 80–200 | 25–40 | 5–12 |
| **Electrical conductivity** | Insulator | Insulator | Conductor | Conductor | Conductor | Insulator | Insulator |
| **Temperature limit (°C)** | 350 | 500 | 500+ | 500+ | 500+ | 250 | 700 |

*HS = high strength (T700, T300). IM = intermediate modulus (T800, IM7). HM = high modulus (M55J, M60J). Values are typical fibre properties, not laminate properties. Actual laminate performance depends on fibre volume fraction, resin system, and layup.*

## Key Takeaways

- **Carbon fibre** delivers the best stiffness and strength per unit weight but is expensive and brittle. It is the default for aerospace and performance applications.
- **Glass fibre (E-glass)** is the low-cost workhorse — lower stiffness than carbon but strong, cheap, and electrically insulating. Start here if weight is not critical.
- **Aramid (Kevlar)** excels at impact resistance and energy absorption but is weak in compression and absorbs moisture. Use it where things get hit.
- **Basalt fibre** is an emerging mid-range option between E-glass and S-glass with good temperature resistance.
- **Natural fibres** (flax, hemp) offer a sustainable alternative for non-structural or lightly loaded parts.
- Always check laminate-level properties, not just raw fibre numbers — fibre volume fraction, resin choice, and layup orientation all change the final performance.

## Further Reading / Tools

- [What Are Composites?](what-are-composites.md) — start here if you are new to composites
- [Resin Systems](resin-systems.md) — the other half of the equation: choosing the right matrix
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — how fibre orientation in a laminate affects performance
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — build laminates with real material data, run failure analysis, and compare fibre/resin combinations
