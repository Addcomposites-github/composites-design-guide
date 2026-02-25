---
title: "Case Study: Composite Pressure Vessel"
category: "case-study"
tags: ["case-study", "pressure-vessel", "COPV", "filament-winding", "hoop", "helical", "netting-analysis"]
difficulty: "intermediate"
related: ["../03-manufacturing-processes/filament-winding.md", "../01-fundamentals/fibre-types.md", "../04-structural-analysis/failure-criteria.md", "../08-cost-estimation/process-costs.md"]
tools: ["crds", "addstack"]
last_updated: "2026-02"
---

# Case Study: Composite Overwrapped Pressure Vessel (COPV)

This case study walks through the design of a small composite overwrapped pressure vessel from requirements to testing. The techniques apply to any pressurised cylinder -- hydrogen storage for drones, portable compressed air, CNG tanks, or oxygen systems. By the end you will understand why composite pressure vessels are designed the way they are, and you will have the numbers to do a first-pass design yourself.

## The Brief

**Application:** A lightweight pressure vessel for a commercial drone compressed-air system (pneumatic actuator supply) or a portable breathing air bottle.

**Requirements:**

- Internal volume: 1 litre (roughly 80 mm inner diameter x 200 mm cylindrical length, plus domes)
- Working pressure (MAWP): 300 bar (30 MPa)
- Safety factor to burst: 2.35x working pressure (aerospace standard) = 705 bar design burst
- Construction: Type III -- aluminium liner with full carbon fibre/epoxy overwrap
- Target: at least 50% weight saving compared to an all-aluminium vessel of the same volume and burst pressure

**Why Type III?** Pressure vessel types range from Type I (all metal) to Type V (linerless composite). Type III uses a thin metal liner as the gas barrier and a composite overwrap for structural strength. The liner seals; the composite carries the load. This balances manufacturability, cost, and weight -- the liner doubles as the winding mandrel, and aluminium provides a reliable permeation barrier without the cost and complexity of a fully linerless design.

```
Pressure vessel types:

Type I    ████████████████████  All metal (steel or aluminium)
Type II   ██████████▓▓▓▓▓▓▓▓▓  Metal + composite hoop wrap (cylinder only)
Type III  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  Thin metal liner + full composite overwrap  <-- this design
Type IV   ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  Plastic (HDPE) liner + full composite overwrap
Type V    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  Linerless composite (no liner)

██ = metal    ▓▓ = composite    ░░ = plastic liner
```

## Step 1: Define Requirements and Calculate Loads

Start with thin-wall pressure vessel theory. For a cylinder under internal pressure P, with inner radius r and wall thickness t:

```
Hoop stress (circumferential):   sigma_hoop = P x r / t
Axial stress (longitudinal):     sigma_axial = P x r / (2t)
```

The key insight: **hoop stress is exactly twice the axial stress.** This 2:1 ratio drives every design decision that follows. A cylindrical pressure vessel always wants to split lengthwise before it blows apart end-to-end, which is why unlined pipes burst along their length.

**For our vessel at design burst pressure (705 bar = 70.5 MPa):**

- Inner radius: 40 mm = 0.040 m
- Hoop stress x thickness = P x r = 70.5 x 0.040 = 2.82 MPa-m = 2,820 N/mm per mm of length
- This is the running load the overwrap must carry in the hoop direction

The dome closures see a different stress state. At the equator where the dome meets the cylinder, the membrane stresses transition from the 2:1 cylinder ratio to equal biaxial stress on a spherical dome. The dome is structurally less efficient than the cylinder, which is why burst failures often initiate at the dome-cylinder transition (the knuckle region).

## Step 2: Choose Materials and Configuration

### Liner

**6061-T6 aluminium**, ~1.0 mm wall thickness.

- Yield strength: ~275 MPa. At 300 bar working pressure, the liner hoop stress is 300 x 0.040 / 0.001 = 1,200 MPa -- far beyond yield. The liner is NOT designed to carry the full pressure load. It autofrettages (yields plastically) on the first pressurisation, and the composite carries the structural load from then on.
- The liner's job: seal gas, provide the mandrel shape for winding, and contribute a small amount of structural capacity.
- Weight of liner: approximately 0.15 kg for this geometry.

### Composite Overwrap

**T700S carbon fibre / epoxy** (wet winding).

- Fibre tensile strength: ~4,900 MPa
- Fibre tensile modulus: ~230 GPa
- Density: 1.78 g/cm3
- Achievable fibre volume fraction (wet winding): 55-60%
- Ply tensile strength (UD, fibre direction): ~2,400 MPa at 60% Vf

Why carbon and not glass? At 300 bar, the required wall thickness with E-glass would be roughly 2.5 times that of carbon (because glass tensile strength is similar but at 40% higher density and lower modulus -- see [Fibre Types](../01-fundamentals/fibre-types.md)). The weight saving from carbon justifies the cost premium in any application where weight matters. For low-pressure vessels (under 50 bar), glass is often the smarter choice.

## Step 3: Design the Composite Overwrap

### Netting Analysis -- Why 54.7 Degrees

Netting analysis assumes that only the fibres carry load (the resin contributes zero). For a helical winding at angle alpha (measured from the vessel axis), the fibre tension resolves into hoop and axial stress components:

```
Hoop component:     sigma_hoop  ~ sigma_f x sin^2(alpha)
Axial component:    sigma_axial ~ sigma_f x cos^2(alpha)
```

For internal-pressure-only loading, the 2:1 hoop-to-axial stress ratio must be satisfied:

```
sigma_hoop / sigma_axial = sin^2(alpha) / cos^2(alpha) = tan^2(alpha) = 2

Therefore:  tan(alpha) = sqrt(2)
            alpha = arctan(sqrt(2)) = 54.74 degrees
```

**At +/-54.7 degrees, a single helical winding angle simultaneously resists both hoop and axial stress in the exact ratio that internal pressure demands.** This is the most efficient single angle for a pressure vessel. No excess material in either direction.

### Practical Layup

Pure 54.7-degree helical winding works in theory. In practice, designers add dedicated hoop (90-degree) layers for several reasons:

- Extra burst margin in the hoop direction (where the highest stress acts)
- Compensation for fibre strength knockdowns (impact damage, environmental degradation)
- Process requirements -- hoop layers compact and stabilise the helical layers during winding

A typical layup for a high-performance COPV:

```
Vessel cross-section (cylindrical region):

    ┌──────────────────────────────────┐
    │  90° hoop layer (outermost)      │  ~0.3 mm
    ├──────────────────────────────────┤
    │  +54.7° helical layer            │  ~0.5 mm
    ├──────────────────────────────────┤
    │  -54.7° helical layer            │  ~0.5 mm
    ├──────────────────────────────────┤
    │  90° hoop layer                  │  ~0.3 mm
    ├──────────────────────────────────┤
    │  +54.7° helical layer            │  ~0.5 mm
    ├──────────────────────────────────┤
    │  -54.7° helical layer            │  ~0.5 mm
    ├──────────────────────────────────┤
    │  90° hoop layer (innermost)      │  ~0.3 mm
    ╞══════════════════════════════════╡
    │  Aluminium liner                 │  ~1.0 mm
    └──────────────────────────────────┘

    Total composite thickness: ~2.9 mm
    Total wall (liner + composite): ~3.9 mm
```

Use [CRDS](https://www.addcomposites.com/addcomposites-apps/crds) to validate the laminate and check burst pressure against the fibre strength allowable. Use [AddStack](https://addstack.addcomposites.com) to verify ply-level stresses and run failure criteria (Tsai-Wu, max stress) on the wound laminate -- see [Failure Criteria](../04-structural-analysis/failure-criteria.md).

### Dome Winding and the Clairaut Equation

On the domes, the fibre path must follow the changing curvature. For geodesic (stable, non-slipping) paths on a surface of revolution, the Clairaut equation governs:

```
r x sin(alpha) = constant = r_boss x sin(alpha_boss)
```

Where r is the local radius and alpha is the local winding angle. As the radius decreases from the cylinder (r = 40 mm) toward the polar boss opening (r_boss, typically 10-15 mm), the winding angle must increase. At the equator, alpha = 54.7 degrees. Near the boss, alpha approaches 90 degrees -- the fibre wraps nearly circumferentially around the opening.

```
Dome fibre path (half cross-section):

    Boss opening                  Equator
    (r_boss)                      (r = R)
       │                            │
       ├────────╲                   │
       │         ╲  alpha steepens  │
       │          ╲  toward boss    │
       │           ╲                │
       │            ╲               │
       │             ╲──────────────┤  alpha = 54.7° at equator
       │              dome surface  │
       │                            │
    Fibre angle approaches 90°     Fibre angle = 54.7°
    near the boss
```

The dome is thicker near the boss (where many fibre paths converge) and thinner near the equator. This natural thickness build-up reinforces the high-stress region around the boss. However, excessive build-up causes resin-rich pockets and fibre bunching -- a common defect. Dome profile optimisation (isotensoid dome shape) can equalise fibre stress across the entire dome, but that is an advanced topic.

## Step 4: Manufacturing -- Filament Winding

The aluminium liner serves as the winding mandrel. This eliminates the need for a separate mandrel and its extraction -- a significant simplification. See [Filament Winding](../03-manufacturing-processes/filament-winding.md) for full process details.

### Winding Sequence

1. **Prepare the liner:** Clean, abrade the outer surface (sandblast or scotchbrite), apply a coupling agent or primer for aluminium-to-epoxy adhesion.
2. **Mount on the winder:** The liner's boss fittings clamp into the winder spindle. Check concentricity.
3. **Wind helical layers first:** +/-54.7 degree helical passes. These cover both the cylinder and the domes. Wet winding: fibre passes through a resin bath (epoxy mixed with hardener) and onto the liner under 20-50 N tension per tow.
4. **Add hoop layers:** 90-degree circumferential winding on the cylindrical section only. Hoop layers do not extend onto the domes (they cannot follow the curvature at 90 degrees without slipping).
5. **Repeat:** Alternate helical and hoop layers per the laminate design. Typical: 2-4 helical passes interleaved with 1-2 hoop passes.
6. **Final hoop wrap:** The outermost layer is often hoop -- it compacts the underlying helical layers and provides a smooth outer surface.

### Process Parameters

- **Fibre tension:** 20-50 N per tow (higher tension improves fibre volume fraction but risks liner buckling on thin liners)
- **Resin bath temperature:** 30-40 degrees C for reduced viscosity (improved wet-out)
- **Winding speed:** 0.3-1.0 m/s surface speed (balance speed against resin wet-out time)
- **Bandwidth:** 3-6 mm per tow, 4-12 tows in parallel

### Cure

Oven cure at 120-150 degrees C for 2-4 hours (depending on epoxy system). The aluminium liner supports the composite during cure. Post-cure at higher temperature may be used for improved glass transition temperature.

## Step 5: Cost Estimate

| Item | Quantity | Unit Cost | Total |
|------|----------|-----------|-------|
| 6061-T6 aluminium liner (spun/deep-drawn) | 1 | $40-80 | $40-80 |
| T700 carbon fibre (12K tow) | ~0.20 kg | $25/kg | $5 |
| Epoxy resin + hardener | ~0.10 kg | $20/kg | $2 |
| Consumables (release, coupling agent) | -- | -- | $3 |
| **Material subtotal** | | | **~$50-90** |
| Winding time (setup + wind + cure) | ~2 hrs | $50/hr (operator + machine) | $100 |
| Inspection (hydrostatic proof test) | 1 | $30-50 | $30-50 |
| **Total cost per vessel** | | | **~$180-240** |

At higher volumes (100+ units), liner cost drops significantly with production tooling, and winding time reduces with optimised programs. Expect $100-150 per vessel in batch production.

**Comparison with all-aluminium:** An all-aluminium 7075-T6 vessel for the same pressure and volume weighs more but costs less to manufacture at low volumes (simple machining or forging, no winding step). The COPV wins on weight; the all-metal vessel wins on simplicity. The crossover where COPV makes economic sense depends on how much weight savings is worth in your application. For a drone, every gram matters. For a workshop air bottle, it does not.

See [Process Costs](../08-cost-estimation/process-costs.md) and [Material Costs](../08-cost-estimation/material-costs.md) for broader cost estimation guidance.

## Step 6: Testing and Qualification

Composite pressure vessels require specific test protocols because they fail differently from metal vessels. Metal vessels yield visibly before bursting. Composite vessels can show no external warning -- see [Failure Modes](../01-fundamentals/failure-modes.md).

### Required Tests

1. **Hydrostatic proof test:** Pressurise with water (not gas -- water is incompressible, so a burst releases far less energy). Proof pressure is typically 1.5x MAWP = 450 bar. Every production vessel is proof-tested.
2. **Hydrostatic burst test:** Pressurise to destruction on sample vessels. Must exceed 2.35x MAWP = 705 bar. Demonstrates the design margin.
3. **Pressure cycling:** Repeatedly pressurise from zero to MAWP for 10,000-45,000 cycles (depending on the standard). Checks fatigue life. Aluminium liners are the fatigue-critical component -- the liner cycles through yield on every pressurisation.
4. **Environmental exposure:** Temperature extremes (-40 to +65 degrees C), humidity, UV, and chemical exposure followed by burst testing.
5. **Drop and impact tests:** Simulate handling damage, then proof-test to check residual strength.
6. **Bonfire / fast-heat test:** Expose the vessel to flame. The composite must not burst catastrophically before the pressure relief device activates.

### Acoustic Emission Monitoring

During proof and burst testing, acoustic emission (AE) sensors bonded to the vessel surface detect the ultrasonic signals emitted by fibre breakage, matrix cracking, and delamination. AE monitoring distinguishes healthy composite behaviour (scattered low-energy events) from damage growth (clustered high-energy events). It is one of the few ways to non-destructively assess the structural health of a COPV during its service life.

## Weight Comparison

```
All-aluminium (7075-T6) vs Type III COPV (Al liner + T700/epoxy):
1 litre volume, 300 bar working pressure, 705 bar design burst

┌────────────────────────┬──────────────────┬─────────────────────┐
│ Parameter              │ All-Aluminium    │ Type III COPV       │
│                        │ (7075-T6)        │ (6061 + T700/epoxy) │
├────────────────────────┼──────────────────┼─────────────────────┤
│ Wall thickness (cyl.)  │ ~5.5 mm          │ ~3.9 mm (1.0 + 2.9) │
│ Vessel weight          │ ~1.2 kg          │ ~0.50 kg            │
│ Weight saving          │ baseline         │ ~58%                │
│ Internal volume        │ 1.0 L            │ 1.0 L               │
│ Design burst pressure  │ 705 bar          │ 705 bar             │
│ Failure mode           │ Ductile yielding │ Fibre rupture       │
│ Approximate cost (low  │ $60-120          │ $180-240            │
│   volume, per unit)    │                  │                     │
│ Fatigue life (cycles   │ >100,000         │ 15,000-45,000       │
│   to MAWP)             │ (if no corrosion)│ (liner-limited)     │
└────────────────────────┴──────────────────┴─────────────────────┘
```

The COPV achieves roughly 58% weight savings at roughly 2x the cost. For a drone carrying a 1.2 kg metal bottle versus a 0.50 kg COPV, the 0.70 kg saving translates directly into extra payload or flight time -- often worth far more than the $100-150 cost premium.

## Key Takeaways

- Hoop stress is twice the axial stress in a pressurised cylinder -- this 2:1 ratio is the starting point for every COPV design
- The netting-analysis-optimal helical winding angle for internal pressure is +/-54.7 degrees, derived directly from the 2:1 stress ratio
- Practical designs add hoop (90-degree) layers for burst margin and process stability on top of the helical layers
- The Clairaut equation (r x sin(alpha) = constant) governs fibre paths on the domes -- the angle steepens as the radius decreases toward the polar boss
- Type III vessels (metal liner + composite overwrap) balance weight, cost, and manufacturability -- the liner seals gas and serves as the winding mandrel
- Carbon fibre is justified over glass at high pressures because the weight saving is substantial; at low pressures, glass may be more cost-effective
- Testing is critical: hydrostatic burst, pressure cycling, impact, and environmental exposure. Composite vessels do not give visible warning before failure

## Further Reading / Tools

- [CRDS -- Composite Rotor/Sleeve Design](https://www.addcomposites.com/addcomposites-apps/crds) -- free tool for designing composite wound structures, directly applicable to COPV overwrap design
- [AddStack -- free laminate calculator](https://addstack.addcomposites.com) -- verify ply stresses and run failure criteria on wound laminates
- [Filament Winding](../03-manufacturing-processes/filament-winding.md) -- full process guide for the manufacturing method used in this case study
- [Fibre Types](../01-fundamentals/fibre-types.md) -- carbon vs glass vs aramid property comparison
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) -- Tsai-Wu, Hashin, max stress for checking the overwrap
- [Failure Modes](../01-fundamentals/failure-modes.md) -- how composites fail and why COPVs need specific test protocols
- [Process Costs](../08-cost-estimation/process-costs.md) -- broader cost estimation for filament winding and other processes
- [Material Costs](../08-cost-estimation/material-costs.md) -- fibre and resin pricing data
