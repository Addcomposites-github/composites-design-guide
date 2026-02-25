---
title: "Composite Material Costs"
category: "cost-estimation"
tags: ["cost", "material-cost", "carbon-fibre", "glass-fibre", "resin", "prepreg", "budget"]
difficulty: "beginner"
related: ["process-costs.md", "tooling-costs.md", "../01-fundamentals/fibre-types.md", "../01-fundamentals/resin-systems.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Composite Material Costs

The single most common question from anyone starting in composites: "How much will the material cost?" The answer depends on three things — what fibre you use, what resin you use, and what form you buy them in. This page gives practical cost ranges so you can estimate your bill of materials before committing to a design.

## Fibre Costs

Fibre is usually the largest material cost in a composite part. Prices vary by fibre type, grade, and purchasing volume.

| Fibre | Cost (USD/kg) | Cost Driver | Typical Applications |
|-------|--------------|-------------|---------------------|
| **E-Glass roving** | $2–5 | Commodity, very high global production | Boats, pipes, wind blades, general industry |
| **E-Glass woven fabric** | $5–15 | Weaving adds cost | Panels, moulds, general structural |
| **S-Glass** | $15–30 | Higher strength glass, smaller production runs | Ballistic, aerospace secondary structure |
| **Standard modulus carbon (T300/T700)** | $15–30 | High volume carbon grades | Automotive, sporting goods, drones, wind |
| **Intermediate modulus carbon (IM7, T800)** | $30–80 | Tighter fibre specs, lower production volume | Aerospace primary structure |
| **High modulus carbon (M55J, M60J)** | $100–500+ | Very specialized, low volume | Space structures, satellite, antenna |
| **Aramid (Kevlar 49)** | $25–40 | DuPont/Teijin production | Ballistic protection, pressure vessels |
| **Basalt** | $5–10 | Newer market, growing production | Fire-resistant panels, rebar, pipes |
| **Natural fibres (flax, hemp)** | $3–8 | Agricultural product | Interior panels, eco-friendly consumer goods |

**Key insight:** Standard modulus carbon fibre (T300/T700 class) has dropped significantly in price over the past decade due to automotive and wind energy demand. For most non-aerospace applications, this grade provides excellent performance at reasonable cost.

## Resin Costs

| Resin | Cost (USD/kg) | Pot Life | Typical Vf with Fibre |
|-------|--------------|----------|----------------------|
| **Polyester** | $3–6 | 15–45 min | 30–45% |
| **Vinyl ester** | $6–12 | 15–45 min | 35–50% |
| **Epoxy (room-temp cure)** | $10–25 | 30 min–several hours | 40–55% |
| **Epoxy (elevated-temp cure)** | $15–40 | Hours (stored cold) | 50–65% |
| **PEEK (thermoplastic)** | $100–200 | N/A (melt-processed) | 55–65% |
| **PPS (thermoplastic)** | $40–80 | N/A (melt-processed) | 55–65% |

**Resin-to-fibre ratio matters:** A typical laminate is 50–60% fibre by volume. By weight, the resin content ranges from 30% (high-Vf prepreg) to 55% (wet layup). So for a 1 kg laminate at 40% resin by weight, you need ~0.6 kg fibre + ~0.4 kg resin.

## Pre-Impregnated (Prepreg) Costs

Prepreg combines fibre and resin into a ready-to-use sheet. The price premium over dry fibre + resin reflects the manufacturing, quality control, and cold-chain logistics.

| Prepreg Type | Cost (USD/m2) | Cost (USD/kg) | Notes |
|-------------|--------------|--------------|-------|
| **Carbon/epoxy UD (standard)** | $30–60 | $50–100 | Most common aerospace prepreg |
| **Carbon/epoxy woven (standard)** | $40–80 | $60–120 | Cosmetic or quasi-isotropic layups |
| **Glass/epoxy prepreg** | $10–25 | $20–50 | Lower cost, tooling or secondary structure |
| **Carbon/PEEK UD** | $150–300 | $200–500 | Thermoplastic, high-performance |
| **Carbon/BMI UD** | $80–150 | $120–250 | High temperature (>200°C service) |

**The hidden costs of prepreg:**
- Cold storage (-18°C freezer): $500–$5,000/year for a small freezer
- Out-time tracking: prepreg has limited room-temperature life (typically 30 days)
- Shelf life: typically 6–12 months in the freezer
- Minimum order quantities: often 50–100 m2 from major suppliers
- Shipping: temperature-controlled freight is expensive

## Consumables Cost

Every composite part requires consumables that are used once and discarded. These add up fast.

| Consumable | Cost Range | Used In |
|-----------|-----------|---------|
| **Release agent** (liquid/spray) | $20–50/litre (covers many parts) | All processes |
| **Peel ply** (nylon/polyester) | $3–8/m2 | Vacuum bag, infusion, prepreg |
| **Release film** (perforated) | $3–10/m2 | Vacuum bag, prepreg |
| **Breather/bleeder** | $2–5/m2 | Vacuum bag, prepreg |
| **Vacuum bag film** | $2–6/m2 | Vacuum bag, infusion |
| **Sealant tape** | $1–3/metre | Vacuum bag, infusion |
| **Flow media** (infusion mesh) | $3–8/m2 | VARTM/infusion only |
| **Spiral tubing** (infusion lines) | $1–3/metre | VARTM/infusion only |
| **Mixing cups, brushes, rollers** | $5–20/set | Wet layup |

**Rule of thumb:** For vacuum bagging or infusion, consumables typically add $15–30/m2 on top of fibre and resin costs.

## Estimating Your Material Bill

A simple formula for material cost per part:

```
Material cost = (Fibre cost/kg × fibre weight)
              + (Resin cost/kg × resin weight)
              + (Consumables cost/m2 × part area)
              + Waste factor (typically 1.1–1.3×)
```

**Example — carbon fibre car splitter (0.3 m2, 4 plies of woven carbon, vacuum bagged):**
- Carbon woven fabric: 0.3 m2 × 4 plies × 300 g/m2 = 0.36 kg fibre → ~$10
- Epoxy resin: ~0.24 kg → ~$5
- Consumables (peel ply, release film, breather, bag, tape): ~$8
- Waste factor (1.2×): multiply by 1.2
- **Total material cost: ~$28**

The fibre and resin are cheap. The labour, tooling, and equipment are where the real cost is — see [Process Costs](process-costs.md).

## Key Takeaways

- Glass fibre is 5–10× cheaper than carbon fibre per kilogram — use glass unless you specifically need carbon's stiffness or weight savings
- Standard modulus carbon (T300/T700) is the sweet spot for most applications at $15–30/kg
- Prepreg adds a 2–3× cost premium over dry fibre + resin but delivers higher and more consistent quality
- Consumables add $15–30/m2 per cure cycle — budget for them
- Waste factor of 10–30% is normal (offcuts, trim, mixing losses)
- For small parts, material cost is often less than tooling and labour cost

## Further Reading / Tools

- [Process Costs](process-costs.md) — labour, equipment, and overhead costs by process
- [Tooling Costs](tooling-costs.md) — mould and fixture costs
- [Fibre Types](../01-fundamentals/fibre-types.md) — properties and selection guide
- [Resin Systems](../01-fundamentals/resin-systems.md) — choosing the right resin
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — design your laminate, then estimate material weight
