---
title: "Manufacturing Process Costs"
category: "cost-estimation"
tags: ["cost", "labour", "equipment", "process-cost", "automation", "afp", "hand-layup"]
difficulty: "intermediate"
related: ["material-costs.md", "tooling-costs.md", "../03-manufacturing-processes/wet-layup.md", "../03-manufacturing-processes/afp-atl.md", "../03-manufacturing-processes/filament-winding.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Manufacturing Process Costs

Material is often the smallest cost in a composite part. Labour, equipment, and overhead typically dominate — especially for low-volume production. Understanding process costs helps you choose the right manufacturing method for your volume and budget.

## Cost Breakdown by Process

Every composite part cost breaks down into four categories:

```
Total part cost = Material + Labour + Tooling (amortized) + Overhead
```

The balance between these shifts dramatically with the manufacturing process:

```
Cost distribution by process:

Wet Layup:     ████████████████████░░░░░░░░░░  Material: 20%
               ░░░░░░░░░░░░░░░████████████████  Labour: 60%
               ░░░░░░░░░░░░░░░░░░░░░░░░░░████  Tooling: 10%
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  Overhead: 10%

Infusion:      ████████████████████████░░░░░░░  Material: 30%
               ░░░░░░░░░░░████████████████████  Labour: 40%
               ░░░░░░░░░░░░░░░░░░░░░░░░██████  Tooling: 15%
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░███  Overhead: 15%

Prepreg/Auto:  ████████████████████████████░░░  Material: 40%
               ░░░░░░░░░░░░░████████████░░░░░░  Labour: 20%
               ░░░░░░░░░░░░░░░░░░░░░██████████  Tooling: 20%
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░███  Overhead: 20%

AFP:           ████████████████████████████░░░  Material: 35%
               ░░░░░░░░░░░░░░░░░░████░░░░░░░░  Labour: 10%
               ░░░░░░░░░░░░░░░████████████████  Equipment: 35%
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░███  Overhead: 20%
```

## Labour Rates and Productivity

Labour cost depends on two things: the hourly rate and how many kilograms (or square metres) an operator can lay up per hour.

| Process | Layup Rate (kg/hr) | Layup Rate (m2/hr) | Typical Labour Rate (USD/hr) |
|---------|-------------------|-------------------|---------------------------|
| **Wet layup** | 0.5–1.5 | 0.5–2 | $20–50 |
| **Vacuum bagging** | 0.5–1.0 | 0.5–1.5 | $25–50 |
| **Resin infusion setup** | 0.3–0.8 (setup-heavy) | 1–5 (once flowing) | $30–60 |
| **Prepreg hand layup** | 0.3–1.0 | 0.5–2 | $30–70 |
| **AFP** | 5–20 | 5–50 | $40–80 (operator) |
| **ATL** | 10–50 | 20–100 | $40–80 (operator) |
| **Filament winding** | 2–10 | N/A (wound) | $30–60 |
| **Pultrusion** | 10–100+ | N/A (continuous) | $25–40 |

**Why automation changes the equation:**
- Hand layup: 1 operator per part, 100% attention, physical labour
- AFP: 1 operator monitors 1–3 machines, machine does the placement at 10–50× the rate
- The crossover point where AFP becomes cheaper than hand layup depends on part size and volume — typically at 50–200 parts/year for medium-sized parts (1–5 m2)

## Equipment Costs

| Equipment | Capital Cost (USD) | Hourly Operating Cost | Amortization |
|-----------|-------------------|----------------------|-------------|
| **Wet layup kit** (rollers, cups, brushes) | $100–500 | ~$0 | Negligible |
| **Vacuum pump + accessories** | $500–5,000 | $2–5/hr | 5 years |
| **Oven** (walk-in, for post-cure) | $10,000–100,000 | $10–30/hr | 10 years |
| **Autoclave** (small: 1m dia) | $100,000–500,000 | $50–200/hr | 15 years |
| **Autoclave** (large: 3m+ dia) | $500,000–5,000,000 | $100–500/hr | 15 years |
| **CNC filament winder** (lab) | $100,000–300,000 | $20–50/hr | 10 years |
| **CNC filament winder** (production) | $300,000–1,500,000 | $40–100/hr | 10 years |
| **AFP-XS** (on robot arm) | Lease from ~€2–3k/month | $30–80/hr | Lease or 7 years |
| **AFP** (traditional gantry) | $2,000,000–10,000,000 | $100–500/hr | 15 years |
| **ATL** (large) | $3,000,000–15,000,000 | $150–600/hr | 15 years |
| **Clean room** (if required) | $50,000–500,000 | $5–20/hr | 20 years |
| **Freezer** (prepreg storage) | $500–5,000 | $2–5/hr | 10 years |

**The AFP-XS advantage:** Traditional AFP cells cost $2–10M. AddComposites' AFP-XS mounts on a standard industrial robot, bringing the total cell cost to a fraction of this. For universities, startups, and small manufacturers, this changes the automation calculus entirely. [Learn more about AFP-XS leasing options →](https://www.addcomposites.com/product/afp-xs)

## Cost Per Part by Volume

The following table shows approximate total cost per part (material + labour + tooling amortized + overhead) for a **1 m2, 2 mm thick carbon/epoxy panel**:

| Volume (parts/year) | Wet Layup | Infusion | Prepreg/Autoclave | AFP |
|---------------------|-----------|----------|-------------------|-----|
| 1 | $200–400 | $300–600 | $500–1,000 | N/A (setup cost too high) |
| 10 | $150–300 | $200–400 | $350–700 | $500–1,000 |
| 100 | $120–250 | $150–300 | $250–500 | $200–400 |
| 1,000 | $100–200 | $100–200 | $200–400 | $100–200 |
| 10,000 | $80–150 | $80–150 | $150–300 | $60–120 |

**Crossover points (approximate):**
- Infusion becomes cheaper than wet layup at **~20 parts** (less labour per part despite higher setup)
- Prepreg becomes competitive with infusion at **~200 parts** (material cost offset by consistency and less rework)
- AFP becomes cheapest at **~500–2,000 parts** (high equipment cost amortized over volume)
- For **axisymmetric parts**, filament winding beats all others at almost any volume due to low capital cost and high automation

## Hidden Costs People Forget

1. **Rework and scrap** — composite parts cannot be reworked like metal. A failed infusion or a wrinkled prepreg layup is scrap. Budget 5–15% scrap rate for manual processes, 1–5% for automated.
2. **Inspection** — NDI (ultrasonic, thermography) costs $50–500 per part depending on method and part size. Required for structural parts.
3. **Post-processing** — trimming, drilling, surface finishing, and assembly add 10–30% to the cure cost.
4. **Facility costs** — temperature/humidity control for prepreg work, dust extraction, ventilation for resin fumes.
5. **Certification costs** — if the part needs airworthiness certification, testing and documentation can cost more than the manufacturing itself.
6. **Training** — skilled composites technicians are rare. Training a new operator takes 3–12 months.

## Quick Cost Estimation Formula

For a rough estimate before detailed quoting:

```
Part cost (USD) ≈ Material cost
                + (Part weight in kg × Labour hours/kg × Labour rate)
                + (Tooling cost ÷ Expected production volume)
                + 20% overhead
```

**Example — carbon fibre drone arm (0.15 kg, 4 plies, vacuum bagged, 50 parts):**
- Material: $12 (carbon fabric + epoxy + consumables)
- Labour: 0.15 kg × 4 hrs/kg × $35/hr = $21
- Tooling: $800 mould ÷ 50 parts = $16
- Overhead: 20% × ($12 + $21 + $16) = $10
- **Total: ~$59 per part**

At 500 parts with AFP? Material: $10, labour: $3, equipment: $15, tooling: $5, overhead: $7 → **~$40 per part** — and far more consistent quality.

## Key Takeaways

- Labour dominates cost for manual processes (wet layup, hand prepreg) — 40–60% of total
- Equipment and material dominate cost for automated processes (AFP, ATL, winding) — tooling and material are 60–70%
- The automation crossover point is typically 200–2,000 parts/year for medium parts
- AFP-XS brings the automation threshold much lower by reducing capital cost
- Filament winding is the most cost-effective automated process for axisymmetric parts
- Always budget 5–15% for scrap/rework and 10–30% for post-processing
- Facility, inspection, training, and certification costs are real — do not ignore them

## Further Reading / Tools

- [Material Costs](material-costs.md) — fibre, resin, prepreg, and consumables pricing
- [Tooling Costs](tooling-costs.md) — mould costs by material, complexity, and size
- [AFP and ATL](../03-manufacturing-processes/afp-atl.md) — when automated placement makes sense
- [Filament Winding](../03-manufacturing-processes/filament-winding.md) — cost-effective for axisymmetric parts
- [Wet Layup](../03-manufacturing-processes/wet-layup.md) — the lowest-cost entry point
- [AddPath — AFP path planning](https://www.addcomposites.com/all-products/addpath) — plan and simulate AFP manufacturing
- [AddStack — free laminate calculator](https://addstack.addcomposites.com)
