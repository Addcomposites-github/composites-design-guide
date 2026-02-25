---
title: "Case Study: Carbon Fibre Car Body Panel"
category: "case-study"
tags: ["case-study", "automotive", "body-panel", "cosmetic", "woven", "vacuum-bagging", "infusion"]
difficulty: "beginner"
related: ["../03-manufacturing-processes/vacuum-bagging.md", "../03-manufacturing-processes/resin-infusion-vartm.md", "../01-fundamentals/resin-systems.md", "../02-design-rules/design-for-manufacture.md", "../08-cost-estimation/tooling-costs.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Case Study: Carbon Fibre Car Body Panel

This walkthrough covers the full process of designing and manufacturing a carbon fibre front splitter (air dam) for a track-day car. It is aimed at makers, small-shop fabricators, and junior engineers who want a practical, start-to-finish reference. Every design decision is explained so you can adapt the approach to a bonnet, diffuser, wing endplate, or any other cosmetic-structural car panel.

## The Brief

**Part:** Front splitter / air dam for a track car.
**Size:** Approximately 500 mm wide by 300 mm deep (0.15 m2 plan area).
**Loads:** Aerodynamic pressure at 200 km/h produces roughly 200 N of downforce distributed across the panel. Mounting point loads at three bolt locations. Occasional stone impacts on the leading edge.
**Cosmetic requirement:** Visible carbon weave on the top surface (single-sided cosmetic finish).
**Stiffness target:** Maximum 2 mm deflection at the centre under the 200 N aero load.
**Weight target:** Under 500 g finished.
**Production volume:** 1-20 parts (personal use or small-run club supply).

## Step 1: Define Requirements

Before touching any materials, write down every requirement the part must satisfy. Skipping this step is how splitters crack on track or flex embarrassingly at speed.

**Structural requirements:**
- Aero load: ~200 N distributed over 0.15 m2 gives an average pressure of roughly 1.3 kPa. Not high, but the panel is thin and unsupported between mounting points.
- Mounting: three M6 bolts along the rear edge. Each bolt carries roughly 67 N in shear plus any peel loads from uneven pressure distribution.
- Stiffness: 2 mm maximum deflection at the centre of the unsupported span (~350 mm between mounts). This drives the laminate thickness more than strength does.

**Impact and durability:**
- Stone strikes from the front wheels at 100-200 km/h. The leading edge must resist minor impacts without delaminating or crazing the visible surface.
- Temperature: sitting in direct sunlight a black carbon panel can reach 80-90 degrees Celsius. The resin must handle this.

**Cosmetic requirements:**
- Visible 2x2 twill carbon weave on the top surface. No print-through (fibre pattern telegraphing through from lower plies), no pinholes, no dry spots.
- The mould-side surface (facing down on the car) does not need to be cosmetic.

**Weight:**
- Under 500 g. A 0.15 m2 panel at 1.5 mm thickness with carbon/epoxy at ~1,550 kg/m3 weighs roughly 350 g, well within budget.

## Step 2: Choose Materials

### Fibre

Use two types of [carbon fibre](../01-fundamentals/fibre-types.md):

**Woven 2x2 twill, 200 g/m2, standard modulus (T300/T700 class):** This goes on the cosmetic surface. The twill weave drapes well over mild curvature, resists impact better than UD because fibres run in two directions, and displays the classic carbon weave pattern buyers expect. A 200 g/m2 areal weight keeps each woven ply thin enough to avoid excessive resin pockets.

**Unidirectional (UD) tape, 150 g/m2, standard modulus:** UD plies carry the structural load. They are stiffer and stronger per unit weight than woven fabric because the fibres are straight, not crimped over and under each other. Use UD for the inner plies where nobody sees them.

### Resin

Use [epoxy resin](../01-fundamentals/resin-systems.md) -- specifically a room-temperature-cure laminating epoxy with a post-cure capability.

**Why epoxy over polyester?**
- Lower shrinkage (1-3% vs 5-8%), which prevents print-through of the fibre pattern on the cosmetic surface.
- Better adhesion to carbon fibre.
- Higher mechanical properties.

**Room-temp cure vs elevated cure:**
A room-temp epoxy (cure at 20-25 degrees Celsius, post-cure at 60-80 degrees Celsius in an oven) gives a glass transition temperature (Tg) around 65-85 degrees Celsius after post-cure. That is adequate for a car body panel exposed to sunlight. If you skip the post-cure, Tg drops to about 50-60 degrees Celsius, which is marginal -- a black panel in summer sun can reach that temperature and begin to soften.

Post-cure in a household oven at 60-80 degrees Celsius for 6-8 hours is strongly recommended for any part that will see sustained heat.

### Bill of materials summary

| Material | Quantity needed | Approx. cost |
|----------|----------------|-------------- |
| Carbon 2x2 twill 200 g/m2 | 0.4 m2 (two plies + waste) | $12-20 |
| Carbon UD 150 g/m2 | 0.5 m2 (three plies + waste) | $10-18 |
| Laminating epoxy + hardener | ~200 g mixed | $5-10 |
| Consumables (peel ply, release film, breather, bag, tape) | One set | $8-15 |
| Release agent | Shared across parts | $2-5 per part |

See [Material Costs](../08-cost-estimation/material-costs.md) for broader pricing data.

## Step 3: Design the Laminate

The layup is a five-ply symmetric laminate:

```
Laminate cross-section (mould side at bottom):

    ┌──────────────────────────────┐
    │  Woven 0/90  (200 g/m2)     │  ← cosmetic face (against mould)
    ├──────────────────────────────┤
    │  UD 0°       (150 g/m2)     │  ← primary bending stiffness
    ├──────────────────────────────┤
    │  UD +/-45°   (150 g/m2)     │  ← torsional stiffness + shear
    ├──────────────────────────────┤
    │  UD 0°       (150 g/m2)     │  ← primary bending stiffness
    ├──────────────────────────────┤
    │  Woven 0/90  (200 g/m2)     │  ← back face (bag side)
    └──────────────────────────────┘

    Total areal weight: ~850 g/m2 dry fibre
    Estimated cured thickness: ~1.4-1.6 mm
    Estimated cured panel weight: ~300-350 g
```

### Why this layup works

**Woven outer plies** serve three purposes. First, the mould-side woven ply gives the cosmetic carbon weave appearance. Second, woven fabric on both faces provides impact resistance -- the interlocked fibres hold together under stone strikes instead of splitting like UD. Third, the woven plies protect the UD core from edge damage.

**0-degree UD plies placed away from the midplane** maximise bending stiffness. In a beam or panel, the material farthest from the neutral axis contributes the most to bending rigidity. Placing the stiff 0-degree plies as the second and fourth layers (close to the outer faces) is the most weight-efficient way to resist deflection. This is basic [laminate theory](../01-fundamentals/laminate-theory.md).

**+/-45-degree UD ply at the centre** adds torsional stiffness and in-plane shear resistance. Without it, the panel would be stiff front-to-back but weak in twist. The 45-degree fibres also help distribute load around the mounting bolt holes.

### Verify with AddStack

Enter this layup in [AddStack](https://addstack.addcomposites.com) with standard-modulus carbon/epoxy properties. Check the D-matrix (bending stiffness) and run a simple plate deflection estimate. For a 350 mm span, 200 N distributed load, and this laminate, deflection should be well under 2 mm. Also run a [failure criteria](../04-structural-analysis/failure-criteria.md) check -- the margins will be large because this panel is stiffness-driven, not strength-driven.

See [Sizing a Panel](../04-structural-analysis/sizing-a-panel.md) for the full sizing workflow.

## Step 4: Choose Manufacturing Process

Two viable options for a small cosmetic carbon panel:

| Factor | Wet layup + vacuum bag | Resin infusion (VARTM) |
|--------|----------------------|----------------------|
| Equipment | Vacuum pump, bag, consumables | Vacuum pump, bag, flow media, catch pot |
| Cosmetic quality | Good (mould surface) | Good (mould surface) |
| Fibre volume fraction | ~50-55% | ~55-60% |
| Complexity | Lower | Higher (resin flow path design) |
| Risk of dry spots | Low (each ply is wetted individually) | Moderate (depends on flow front) |
| Best for | Small parts, low volume | Larger parts, higher fibre content |

**For a 0.15 m2 splitter, wet layup plus vacuum bagging wins.** The part is small enough to wet out by hand in 15-20 minutes. Infusion adds complexity (flow media, spiral tubing, resin feed/bleed lines) that does not pay off at this scale. Save infusion for parts above ~0.5 m2 where hand wet-out becomes inconsistent.

See [Vacuum Bagging](../03-manufacturing-processes/vacuum-bagging.md) and [Resin Infusion / VARTM](../03-manufacturing-processes/resin-infusion-vartm.md) for detailed process descriptions.

## Step 5: Tooling

A cosmetic carbon surface requires a **female mould** -- the part lays up inside the mould so the mould surface defines the visible face.

### Making the mould

1. **Start with a plug.** If you have the original plastic splitter, use it as the plug directly. If not, carve a plug from high-density foam (Divinycell or rigid PU) or shape it from MDF, then fill, sand, and polish to a smooth finish.
2. **Apply gelcoat** to the plug surface. This creates the hard, glossy surface that transfers to every part.
3. **Lay up a fibreglass mould** over the plug. Use 4-6 plies of woven E-glass with polyester or epoxy tooling resin. Include flanges (50-75 mm wide flat edges around the part perimeter) for the vacuum bag sealant tape.
4. **Demould and finish** the fibreglass mould. Sand and polish the mould cavity if needed.

```
Mould cross-section:

                    Flange for bag seal
                   ┌────┐          ┌────┐
                   │    │          │    │
    ───────────────┘    └──────────┘    └───────────────
                        ▼
              Mould cavity (concave)
              This surface defines the
              cosmetic face of every part

    Material: 4-6 plies woven E-glass / polyester
    Gelcoat inner surface for gloss finish
```

### Cost estimate for tooling

For a small splitter mould (~0.15 m2 cavity plus flanges):
- Foam or MDF plug material: $20-40
- Gelcoat: $15-25
- E-glass fabric + polyester resin for mould: $30-60
- Sanding and finishing supplies: $10-20
- **Total mould cost: $75-150**

The mould should last 20-50 parts before the gelcoat surface degrades. See [Tooling Costs](../08-cost-estimation/tooling-costs.md) for more detail.

## Step 6: Manufacturing Procedure

### Preparation (30 minutes)

1. Clean the mould cavity. Wipe with solvent (acetone or isopropyl alcohol).
2. Apply three coats of PVA release agent or paste wax, buffing between coats. This is what lets you remove the cured part without destroying the mould.
3. Pre-cut all plies to shape. Label them in layup order. Pre-cutting avoids rushed trimming while the resin clock is ticking.
4. Mix epoxy resin and hardener per the datasheet ratio. Measure by weight, not by volume.

### Layup (20-30 minutes)

5. **Ply 1 (cosmetic woven):** Lay the first 2x2 twill ply face-down into the mould. This ply contacts the gelcoat surface and becomes the visible face of the finished part. Wet it out thoroughly with a brush and stipple roller. Work out all air bubbles against the mould surface. Take your time here -- every air bubble trapped against the mould will show as a pinhole on the finished part.
6. **Ply 2 (UD 0 degrees):** Lay the first UD ply on top of the wetted woven ply. Wet out. Roll with a ribbed aluminium roller to consolidate.
7. **Ply 3 (UD +/-45 degrees):** Lay the +/-45 ply. Wet out and consolidate.
8. **Ply 4 (UD 0 degrees):** Second UD 0-degree ply. Wet out and consolidate.
9. **Ply 5 (woven 0/90):** Final woven ply on the bag side. Wet out. This ply gives a clean finish on the back face and adds impact protection.

### Vacuum bag stack (15-20 minutes)

10. Apply **peel ply** over the entire laminate. Press it down with a dry brush.
11. Apply **perforated release film** over the peel ply.
12. Apply **breather fabric** extending to the vacuum port location on the flange.
13. Apply **sealant tape** around the mould flange perimeter.
14. Drape the **vacuum bag film** over everything and press it onto the sealant tape. Pleat the bag at corners to avoid bridging.
15. Install the **vacuum fitting** through the bag on the flange area.

```
Complete vacuum bag stack (cross-section):

    ┌──────────────────────────────────┐  ← Vacuum bag (nylon film)
    │  Breather                        │
    ├──────────────────────────────────┤
    │  Perforated release film         │
    ├──────────────────────────────────┤
    │  Peel ply                        │
    ├──────────────────────────────────┤
    │  Woven 0/90                      │ ─┐
    │  UD 0°                           │  │
    │  UD +/-45°                       │  ├─ Laminate (your part)
    │  UD 0°                           │  │
    │  Woven 0/90 (cosmetic face)      │ ─┘
    ├──────────────────────────────────┤
    │  Release agent                   │
    └══════════════════════════════════┘  ← Mould surface (gelcoat)
```

### Cure (12-24 hours + post-cure)

16. Connect the vacuum pump and pull full vacuum. Check the gauge: you want 850-950 mbar below atmospheric. Listen for hissing leaks and fix immediately.
17. Leave under vacuum at room temperature for the resin manufacturer's recommended cure time (typically 12-24 hours at 20-25 degrees Celsius).
18. **Post-cure:** Place the mould (with the part still inside, under vacuum if possible) into an oven at 60-80 degrees Celsius for 6-8 hours. This raises the Tg and fully cross-links the epoxy. If you do not have an oven large enough, a heat blanket or an insulated box with a heat gun on a thermostat works.

### Demould and trim (30 minutes)

19. Release vacuum. Remove consumable layers (bag, breather, release film, peel ply).
20. Gently demould the part using plastic wedges along the flange. Never use metal tools against the mould surface.
21. Trim the edges with a diamond-coated cutting disc or oscillating multi-tool. Wear a dust mask -- carbon fibre dust is a respiratory irritant.
22. Drill mounting holes using a carbide or diamond drill bit. Back the part with a sacrificial board to prevent exit-side delamination.

## Step 7: Cost Estimate

### Per-part material cost

| Item | Cost per part |
|------|---------------|
| Carbon twill fabric (2 plies) | $8-12 |
| Carbon UD fabric (3 plies) | $7-12 |
| Epoxy resin + hardener | $5-10 |
| Consumables (peel ply, release film, breather, bag, tape) | $8-15 |
| Release agent (amortized) | $2-3 |
| **Material subtotal** | **$30-52** |

### Labour and tooling

| Item | 1 part | 5 parts | 20 parts |
|------|--------|---------|----------|
| Mould cost (amortized) | $75-150 | $15-30 | $4-8 |
| Labour (2.5 hrs at $25/hr) | $63 | $63 | $63 |
| Material | $30-52 | $30-52 | $30-52 |
| **Total per part** | **$168-265** | **$108-145** | **$97-123** |

Labour dominates for one-off parts. At 20 parts the mould cost becomes negligible. A hand-laid carbon fibre splitter at $100-120 per part compares favourably to aftermarket prices of $200-400 for similar panels. See [Process Costs](../08-cost-estimation/process-costs.md) for a broader comparison.

## Step 8: Finishing

**Clear coat for UV protection:** Bare epoxy degrades under UV exposure -- it yellows and chalks within months of outdoor use. Apply two coats of automotive-grade 2K clear coat (polyurethane) over the cosmetic surface. Sand lightly with 800-grit between coats. This protects the resin and gives a deep, glossy finish over the visible carbon weave.

**Mounting tabs:** For a bolted splitter, bond aluminium or steel captive nut plates on the back face using structural epoxy adhesive (e.g., 3M DP420 or similar). Alternatively, drill through the panel and use stainless steel bolts with large washers to spread the bearing load. Reinforce around bolt holes with a small doubler patch (one or two extra plies, 30-40 mm diameter) during layup. See [Splices and Joints](../02-design-rules/splices-and-joints.md) for bolted joint guidance.

**Edge sealing:** Exposed cut edges allow moisture to wick into the laminate along the fibre/resin interface. Seal all trimmed edges with a thin coat of neat epoxy or the same 2K clear coat used on the face.

## Key Takeaways

- A carbon fibre car splitter is stiffness-driven, not strength-driven. The laminate design is governed by the 2 mm deflection limit, not by material failure.
- Use woven fabric on the cosmetic face for appearance and impact tolerance. Use UD plies internally for structural efficiency.
- Room-temperature-cure epoxy works for car body panels, but always post-cure to raise the Tg above the temperatures the part will see in service.
- Wet layup plus vacuum bagging is the simplest and most cost-effective process for small panels under ~0.5 m2.
- A fibreglass female mould costs $75-150 for a small part and lasts 20-50 pulls.
- Material cost per part is $30-52. Labour and tooling dominate the total cost at low volume.

## Further Reading / Tools

- [Vacuum Bagging](../03-manufacturing-processes/vacuum-bagging.md) -- the manufacturing process used in this case study
- [Resin Infusion / VARTM](../03-manufacturing-processes/resin-infusion-vartm.md) -- alternative process for larger panels
- [Resin Systems](../01-fundamentals/resin-systems.md) -- epoxy selection and cure temperature trade-offs
- [Fibre Types](../01-fundamentals/fibre-types.md) -- carbon vs glass vs aramid for automotive panels
- [Design for Manufacture](../02-design-rules/design-for-manufacture.md) -- DFM rules that apply to this part
- [Sizing a Panel](../04-structural-analysis/sizing-a-panel.md) -- the full sizing workflow for flat panels
- [Failure Criteria](../04-structural-analysis/failure-criteria.md) -- checking laminate strength margins
- [Tooling Costs](../08-cost-estimation/tooling-costs.md) -- mould cost estimation for different production volumes
- [Material Costs](../08-cost-estimation/material-costs.md) -- fibre, resin, and consumables pricing
- [AddStack -- free laminate calculator](https://addstack.addcomposites.com) -- design and verify the laminate before manufacturing
