---
title: "Case Study: Carbon Fibre Bicycle Fork"
category: "case-study"
tags: ["case-study", "bicycle", "fork", "prepreg", "structural", "tube", "intermediate"]
difficulty: "intermediate"
related: ["../01-fundamentals/fibre-types.md", "../02-design-rules/stacking-sequences.md", "../02-design-rules/ply-drop-offs.md", "../03-manufacturing-processes/prepreg-and-autoclave.md", "../04-structural-analysis/failure-criteria.md", "../08-cost-estimation/process-costs.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Case Study: Carbon Fibre Bicycle Fork

A bicycle fork is one of the most iconic carbon fibre consumer products. It is also a demanding structural design: it must be light (under 400g), stiff enough for precise handling, strong enough to survive potholes and crashes, and pass fatigue testing standards. This walkthrough covers the full design-to-manufacturing journey.

## The Brief

Design a straight-blade road bicycle fork for a performance road bike.

| Requirement | Target |
|-------------|--------|
| Weight (uncut steerer) | < 380g |
| Steerer tube | 1-1/8" (28.6mm OD), carbon, 200mm minimum |
| Dropout spacing | 100mm, quick release |
| Rake (offset) | 45mm |
| Max rider + bike weight | 120 kg |
| Test standard | ISO 4210 / EN 14781 (static + fatigue) |
| Finish | Cosmetic clear coat over visible carbon weave |

## Step 1: Define the Loads

A bicycle fork sees complex, combined loading:

```
Fork loading modes:

    Vertical (braking + road loads)     Lateral (cornering)
         ↓ ↓ ↓                              ← →
    ┌────────────┐                    ┌────────────┐
    │  Steerer   │                    │  Steerer   │
    │  tube      │                    │  tube      │
    ├────┐  ┌────┤                    ├────┐  ┌────┤
    │    │  │    │                    │    │  │    │
    │    │  │    │  Blades            │    │  │    │
    │    │  │    │  carry             │    │  │    │
    └────┘  └────┘  bending          └────┘  └────┘
      ▲        ▲                       ▲        ▲
     dropout  dropout                 lateral   lateral
     loads    loads                    loads     loads
```

**Critical load cases (from ISO 4210):**
- **Vertical fatigue:** 1,200N at dropout, 100,000 cycles — simulates road bumps
- **Lateral fatigue:** ±500N at dropout, 100,000 cycles — simulates cornering
- **Forward impact:** 1,000N forward at dropout, static — simulates braking/impact
- **Static strength:** 3× vertical load, no failure

The steerer-to-crown junction is the highest-stress region. The blade mid-section sees the highest bending moment during vertical loading (M = F × L, where L is the effective blade length, ~350mm).

**Approximate peak bending moment:** 1,200N × 0.35m = 420 N·m per blade (vertical fatigue case). With a safety factor of 3× for static strength: 1,260 N·m.

## Step 2: Choose Materials

| Option | Specific Stiffness (E/ρ) | Specific Strength (σ/ρ) | Decision |
|--------|-------------------------|------------------------|----------|
| Aluminium 6061-T6 | 26 GPa/(g/cm3) | 115 MPa/(g/cm3) | Baseline — stiff enough but heavy |
| T700/Epoxy UD | 87 GPa/(g/cm3) | 1,600 MPa/(g/cm3) | 3× stiffer per gram, 14× stronger per gram |
| T800/Epoxy UD | 105 GPa/(g/cm3) | 1,900 MPa/(g/cm3) | Higher performance, higher cost |

**Selection:** T700/epoxy UD prepreg for the structural plies (best price-performance), T300/epoxy 2×2 twill woven for the outermost cosmetic ply (visible carbon weave finish). This is the same material strategy used by most production carbon forks.

**Material properties (T700/epoxy UD, 0.125mm ply):**
- E1 = 135 GPa, E2 = 10 GPa, G12 = 5 GPa
- Xt = 2,100 MPa, Xc = 1,200 MPa, Yt = 50 MPa, Yc = 200 MPa, S = 75 MPa

## Step 3: Design the Laminate

The fork has three distinct zones, each with a different layup:

### Steerer Tube
Round tube, 28.6mm OD, ~20mm ID. Must resist combined bending and torsion from headset loads.

Layup: **[Woven / 0₂ / ±45 / 0₂ / ±45 / 0₂ / Woven]** — 14 plies, ~1.75mm wall

- 0° plies carry bending (steering loads)
- ±45° plies carry torsion (braking torque)
- Woven outer ply for cosmetics and impact tolerance

### Fork Blades
Tapered tubes, ~22mm OD at crown to ~14mm OD at dropout. Highest bending loads.

Layup: **[Woven / 0₂ / ±45 / 0₂ / ±45 / Woven]** — 12 plies at crown, dropping to 8 plies at dropout

- 0° plies aligned with blade axis carry vertical bending
- ±45° carry lateral bending and torsion
- Ply drop-offs from crown to dropout (thicker where moment is highest)

### Crown Junction
The critical zone where steerer meets blades. Additional reinforcement plies wrap around the junction.

Layup: Add **4–6 extra ±45° plies** wrapping steerer-to-blade transition, plus unidirectional patches on the high-stress areas.

### Stacking Rule Check

Taking the blade layup [0/0/+45/-45/0/0/+45/-45] (one side, symmetric assumed):

| Rule | Check | Result |
|------|-------|--------|
| Symmetry | [W/0/0/+45/-45/0/0/+45/-45/-45/+45/0/0/-45/+45/0/0/W] | PASS |
| Balance | 4× (+45°) and 4× (-45°) | PASS |
| 10% rule | 0°: 50%, ±45°: 50%, 90°: 0% | FAIL — no 90° |
| Consecutive ply limit | Two consecutive 0° plies max | PASS |

The 90° rule is intentionally violated — the fork blade is a beam, not a panel, and 90° plies (circumferential) add weight without benefiting bending stiffness. This is a common, accepted practice for tubular structures. Document the engineering justification.

## Step 4: Choose Manufacturing Process

| Process | Suitability | Why |
|---------|------------|-----|
| **Internal bladder moulding** | Best | Industry standard for fork blades — inflatable bladder inside matched metal moulds |
| Prepreg + shrink tape | Good for hobbyist | Wrap prepreg around mandrel, shrink tape compaction, oven cure |
| Filament winding | Poor | Fork blades are not axisymmetric (tapered, curved, offset) |
| Wet layup | Poor | Insufficient fibre volume fraction for structural performance |

**Production method:** Internal bladder moulding with matched CNC-machined aluminium moulds. Prepreg plies are laid into the female mould halves, a nylon bladder tube is inserted, moulds are closed, bladder is inflated to 6–10 bar during cure (130°C for 60 min).

**Hobbyist method:** Prepreg wrap on a tapered aluminium mandrel + shrink tape + oven cure at 130°C. Lower quality than bladder moulding but feasible for one-offs.

## Step 5: Estimate Cost

### Production Fork (1,000 units/year, bladder moulding)

| Item | Cost per Fork |
|------|--------------|
| T700/epoxy prepreg (~40g per fork) | $4–6 |
| T300 woven prepreg (cosmetic ply, ~10g) | $2–3 |
| Bladder, consumables | $2–4 |
| Aluminium dropouts (machined) | $5–10 |
| Labour (20 min layup + 10 min trim/finish) | $10–20 |
| Tooling (CNC alu moulds, ~$15,000 ÷ 1,000) | $15 |
| Oven/press energy | $2–3 |
| Finishing (paint, decals, clear coat) | $5–10 |
| **Total manufacturing cost** | **$45–70** |

### One-Off Hobbyist Fork (shrink tape method)

| Item | Cost |
|------|------|
| T700 prepreg (small order, higher price) | $30–50 |
| Aluminium mandrel + dropout | $20–40 |
| Shrink tape + consumables | $10–15 |
| Labour (4–6 hours) | Your time |
| **Total** | **$60–105 + your time** |

## Step 6: Weight Budget

| Component | Weight |
|-----------|--------|
| Steerer tube (200mm) | 80g |
| Crown junction | 60g |
| Left blade | 65g |
| Right blade | 65g |
| Dropouts (aluminium) | 40g |
| Paint + clear coat | 30g |
| **Total** | **340g** ✓ (under 380g target) |

**Comparison with aluminium:**
| Property | Aluminium 6061 Fork | Carbon Fork |
|----------|-------------------|-------------|
| Weight | 650–800g | 330–380g |
| Lateral stiffness | Baseline | 1.2–1.5× higher |
| Vibration damping | Low | 2–3× higher |
| Material cost | $5–10 | $35–50 |
| Fatigue life | Finite (aluminium fatigues) | Effectively infinite (below threshold) |

Carbon saves 300–450g (45–55%) while delivering better stiffness, better vibration damping, and superior fatigue performance.

## Step 7: Testing

Before riding, the fork must pass:

1. **Static strength test** — 3× rated vertical load applied at dropout, no failure
2. **Fatigue test** — 100,000 vertical cycles at rated load, 100,000 lateral cycles
3. **Impact test** — drop weight onto blade, check for catastrophic failure
4. **Steerer pull-out** — verify steerer-to-crown bond strength

Non-destructive inspection: visual inspection for wrinkles and voids, tap test along blade length (dull sound = potential delamination), weight check against prediction (±10% acceptable).

## Key Takeaways

- A bicycle fork is a complex composite structure with multiple load cases, ply drop-offs, and a critical junction zone
- Carbon fibre delivers 50%+ weight savings over aluminium with better stiffness and fatigue life
- The 0° plies carry bending loads, ±45° plies carry torsion — the layup is tailored to the load path
- The 10% rule for 90° plies is intentionally violated for tubular structures — document your engineering justification
- Internal bladder moulding is the industry-standard process for hollow composite parts like fork blades
- Production cost per fork is $45–70 at 1,000 units — competitive with high-end aluminium forks
- Testing to ISO 4210 is essential — composites fail differently from metals (no visible yielding before fracture)

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — verify your fork layup stiffness and failure loads
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — symmetry, balance, and the 10% rule
- [Ply Drop-Offs](../02-design-rules/ply-drop-offs.md) — how to taper from crown to dropout
- [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md) — the material system used for forks
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) — Tsai-Wu and Hashin checks for your laminate
- [Material Costs](../08-cost-estimation/material-costs.md) — prepreg pricing and consumables
- [Process Costs](../08-cost-estimation/process-costs.md) — labour and equipment cost breakdown
