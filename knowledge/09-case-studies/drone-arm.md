---
title: "Case Study: Carbon Fibre Drone Arm"
category: "case-study"
tags: ["case-study", "drone", "UAV", "carbon-fibre", "tube", "lightweight", "beginner"]
difficulty: "beginner"
related: ["../01-fundamentals/what-are-composites.md", "../01-fundamentals/fibre-types.md", "../02-design-rules/stacking-sequences.md", "../03-manufacturing-processes/wet-layup.md", "../08-cost-estimation/material-costs.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Case Study: Carbon Fibre Drone Arm

This walkthrough takes you from a blank sheet to a finished carbon fibre tube suitable for a quadcopter arm. Every step uses knowledge from this knowledge base and free tools. By the end you will have designed, built, and verified a composite tube that is lighter and stiffer than the aluminium tube it replaces. No aerospace degree required.

## The Brief

**What we are building:** A carbon fibre tube, 300 mm long, 15 mm outer diameter, to serve as a quadcopter motor arm.

**What it must do:**
- Carry a motor producing roughly 20 N (about 2 kg) of thrust at the tip
- Survive landing loads and vibration without excessive deflection
- Weigh less than the equivalent aluminium tube
- Be stiff enough that the motor does not wobble during flight

**Why composites?** A 6061-T6 aluminium tube with similar dimensions weighs about 30 g and deflects noticeably under thrust. A well-made carbon tube can cut that weight in half while being two to three times stiffer. For a quadcopter, every gram saved on the arms is a gram available for battery, payload, or flight time.

## Step 1: Define Requirements

Start with the loads. The arm is a cantilever beam: fixed at the central frame, free at the motor end.

```
Load diagram — cantilever drone arm:

    Fixed end                          Motor end
    (frame)                            (free)
    ╔══════════════════════════════════╗
    ║            300 mm                ║
    ╚══════════════════════════════════╝
    ^                                  ↑ F = 20 N (thrust)
    |
    Fixed support
```

**Bending moment at the root** (worst case):
- M = F x L = 20 N x 0.3 m = 6 N-m

**Apply a safety factor of 2** (standard for hobby/prototype structures):
- Design moment = 12 N-m

**Stiffness target:** Keep tip deflection under 1 mm at 20 N. For a cantilever beam, deflection = FL^3 / (3EI). We will check this against our final laminate.

**Summary of requirements:**

| Parameter | Value |
|---|---|
| Length | 300 mm |
| Outer diameter (OD) | 15 mm |
| Tip load (thrust) | 20 N |
| Design moment (with SF = 2) | 12 N-m |
| Max tip deflection | 1 mm at 20 N |
| Target wall thickness | ~1 mm |
| Target weight | < 15 g (half of aluminium equivalent) |

## Step 2: Choose Materials

For a drone arm, the decision is straightforward. Refer to [Fibre Types](../01-fundamentals/fibre-types.md) for the full comparison.

**Why carbon/epoxy:**
- Highest specific stiffness of any common fibre. A drone arm is a stiffness-driven design: if the arm flexes, the motors tilt and the flight controller fights itself.
- Standard modulus carbon (T700 class) at $15-30/kg is affordable for small parts. You need less than 20 g of fibre for one arm.

**Why not glass?** E-glass has roughly one-third the stiffness of carbon at 40% more density. A glass arm meeting the same stiffness target would weigh nearly three times as much. Glass is the better choice when cost matters more than weight; for a drone arm, weight is everything.

**Why not aluminium?** Aluminium 6061-T6 has a modulus of 69 GPa and density of 2.7 g/cm3. Carbon/epoxy UD laminate achieves 120-135 GPa in the fibre direction at 1.55 g/cm3. Carbon wins on both stiffness and weight simultaneously.

**Material selected:** T700/epoxy unidirectional prepreg or dry UD tape with room-temperature epoxy. Approximate ply properties (at ~55% fibre volume for prepreg, ~45% for wet layup):

| Property | Prepreg (Vf ~55%) | Wet layup (Vf ~45%) |
|---|---|---|
| E1 (along fibre) | 135 GPa | 110 GPa |
| E2 (across fibre) | 9 GPa | 8 GPa |
| G12 (shear) | 5 GPa | 4 GPa |
| Ply thickness | 0.125 mm | 0.15 mm |
| Density | 1.55 g/cm3 | 1.50 g/cm3 |

## Step 3: Design the Laminate

A tube in bending needs axial stiffness (0-degree plies aligned along the tube length) to resist the bending moment. It also needs off-axis plies to handle torsion from motor torque and to prevent the tube wall from splitting under impact.

**Proposed stacking sequence: [0/+45/-45/0]**

This is a 4-ply sequence repeated once to give 8 plies total (for a tube, the layup wraps around the mandrel, so the "inner" and "outer" faces are the same continuous wrap). At 0.125 mm per ply, that gives a wall thickness of approximately 1.0 mm.

```
Tube cross-section (not to scale):

         ┌─────────────────────┐
         │  0° ply (outermost) │
         │  -45° ply           │
         │  +45° ply           │
         │  0° ply             │     Wall thickness
         │  0° ply             │     ~1.0 mm
         │  +45° ply           │
         │  -45° ply           │
         │  0° ply (innermost) │
         └─────────────────────┘
              ← 15 mm OD →

    Inner diameter ≈ 13 mm
```

**Why this sequence works:**
- **50% of plies at 0 degrees** carry the bending load. The 0-degree plies run along the tube length, directly resisting the bending moment from motor thrust.
- **50% of plies at plus/minus 45 degrees** carry torsion from motor reaction torque and provide shear strength. They also resist splitting from impact loads (a dropped drone hits the arms first).
- The layup is **symmetric** (mirrored about the midplane) and **balanced** (equal +45 and -45 plies), satisfying both fundamental stacking rules. See [Stacking Sequences](../02-design-rules/stacking-sequences.md).

**Check with AddStack:** Enter the ply properties, stacking sequence, and tube geometry into [AddStack](https://addstack.addcomposites.com). Verify that the equivalent axial modulus (Ex) of the laminate is in the range of 70-80 GPa. Then calculate the tube bending stiffness EI using:

```
I (moment of inertia, thin-walled tube) = pi/4 * (Ro^4 - Ri^4)

Where:
  Ro = 7.5 mm (outer radius)
  Ri = 6.5 mm (inner radius, assuming 1 mm wall)

  I = pi/4 * (7.5^4 - 6.5^4)
    = pi/4 * (3164 - 1785)
    = pi/4 * 1379
    ≈ 1085 mm^4

EI = 75 GPa * 1085 mm^4 = 81,375 N-mm^2 = 81.4 N-m^2

Tip deflection = FL^3 / (3EI)
               = 20 * 300^3 / (3 * 81,375,000)
               = 540,000,000 / 244,125,000
               ≈ 2.2 mm
```

That is above our 1 mm target. Two options: increase the OD (more lever arm, much more stiffness) or accept 2 mm deflection (still reasonable for a hobby quadcopter). Going to 16 mm OD would bring deflection below 1.5 mm. For this walkthrough, we accept 2 mm as adequate for a 5-inch prop quadcopter.

**Strength check:** The bending stress at the outermost fibre is M/Z, where Z (section modulus) = I/Ro = 1085/7.5 = 145 mm3. At the design moment of 12 N-m: stress = 12,000 / 145 = 83 MPa. The 0-degree plies have compressive strength above 1,000 MPa, so the margin of safety is very comfortable.

## Step 4: Choose Manufacturing Process

For a small tube, three methods work. Pick based on what you have access to.

**Option A: Mandrel wrapping with prepreg (best quality)**
Wrap prepreg plies around a polished aluminium or steel mandrel. Apply shrink tape over the outside. Cure in an oven at 120-180 degrees C (follow the prepreg datasheet). The shrink tape compacts the laminate as the resin flows during cure. This produces tubes with high fibre volume and low void content.

**Option B: Mandrel wrapping with wet layup (most accessible)**
Wrap dry UD carbon tape around a mandrel, wetting with epoxy resin as you go. Apply shrink tape. Cure at room temperature (24 hours) then post-cure at 60-80 degrees C for 2-4 hours if possible. Lower fibre volume than prepreg but perfectly adequate for a drone arm.

**Option C: Filament winding (best for production)**
If you have access to a filament winding machine or an [AddComposites AFP system](https://www.addcomposites.com), the tube can be wound automatically. This gives excellent control over fibre angle and consistent quality. Overkill for a single prototype but ideal for making dozens of identical arms.

**We will use Option B (wet layup on a mandrel)** because it requires the least equipment.

## Step 5: Estimate Cost

Using values from [Material Costs](../08-cost-estimation/material-costs.md):

| Item | Quantity | Unit Cost | Cost |
|---|---|---|---|
| T700 carbon UD tape (50 mm wide) | ~0.015 m2 (for one arm) | ~$20/m2 | ~$0.30 |
| Epoxy resin (room-temp cure) | ~5 g | ~$20/kg | ~$0.10 |
| Aluminium mandrel tube (13 mm OD, reusable) | 1 (reusable for many arms) | ~$5-10 | ~$2.50 amortised |
| Shrink tape (PET, 25 mm) | ~1 m | ~$0.50/m | ~$0.50 |
| Release agent (PTFE spray) | small amount | ~$15/can (many uses) | ~$0.25 |
| Mixing cups, brushes | 1 set | ~$5 (many uses) | ~$0.50 |
| **Total per arm** | | | **~$4-5** |

**Comparison:** A ready-made carbon fibre tube (300 mm, 15 mm OD, 1 mm wall) from a hobby supplier costs $8-15 per tube. Making your own is cheaper per arm once you have the mandrel, and you control the layup exactly.

**For a full quadcopter (4 arms):** Materials cost roughly $15-20. The mandrel and consumables are one-time investments.

## Step 6: Manufacturing Procedure

### Materials and tools needed
- Aluminium tube mandrel, 13 mm OD, at least 350 mm long (available from any metals supplier)
- T700 carbon UD tape or prepreg, 50 mm wide
- Epoxy resin and hardener (slow cure, 60+ minute pot life)
- PTFE release agent spray
- PET shrink tape, 25 mm wide
- Sharp fabric scissors or rotary cutter
- Digital scale (0.1 g resolution)
- Nitrile gloves, safety glasses

### Procedure

**1. Prepare the mandrel.** Clean the aluminium tube with acetone. Apply two coats of PTFE release agent, allowing each to dry. The mandrel must be perfectly clean — any contamination and the tube will bond permanently to it.

**2. Cut the plies.** Cut eight rectangles of UD tape. Each rectangle wraps once around the mandrel circumference (pi x 13 mm = approximately 41 mm width) and runs the full 300 mm length, plus 5 mm extra at each end for trimming. Four plies at 0 degrees (fibres along the length) and four at plus/minus 45 degrees (cut on the bias).

```
Cutting layout for one arm (8 plies):

  Ply 1 (0°):    300 x 41 mm, fibres along 300 mm direction
  Ply 2 (+45°):  300 x 41 mm, fibres at 45° to 300 mm direction
  Ply 3 (-45°):  300 x 41 mm, fibres at -45° to 300 mm direction
  Ply 4 (0°):    300 x 41 mm, fibres along 300 mm direction
  Ply 5 (0°):    300 x 41 mm, fibres along 300 mm direction
  Ply 6 (-45°):  300 x 41 mm, fibres at -45° to 300 mm direction
  Ply 7 (+45°):  300 x 41 mm, fibres at 45° to 300 mm direction
  Ply 8 (0°):    300 x 41 mm, fibres along 300 mm direction
```

**3. Mix resin.** Weigh resin and hardener on the digital scale in the exact ratio specified on the bottle (typically 100:30 or 100:50 by weight for common laminating epoxies). Mix thoroughly for 2 minutes.

**4. Wrap the first ply.** Lay the 0-degree ply on a clean surface, wet it lightly with resin using a brush (thin, even coat — less is more). Place the mandrel at one edge and roll it across the ply, wrapping the ply tightly around the mandrel. Smooth out any bubbles or wrinkles with your gloved fingers.

**5. Wrap subsequent plies.** Repeat for each ply in sequence: 0, +45, -45, 0, 0, -45, +45, 0. Wet each ply lightly before wrapping. Keep tension consistent. Ensure each ply butts up to the previous one without gaps or excessive overlap.

**6. Apply shrink tape.** Starting at one end, spiral-wrap the PET shrink tape over the entire tube with about 50% overlap. The tape should be taut but not so tight that it displaces wet resin. Secure both ends with a small piece of tape.

**7. Cure.** Place the wrapped mandrel on V-blocks or hang it vertically. Cure at room temperature for 24 hours. If you have access to an oven, post-cure at 60 degrees C for 4 hours to improve the glass transition temperature and mechanical properties.

**8. Remove shrink tape and extract the mandrel.** Unwrap the shrink tape. The tube should slide off the mandrel with gentle twisting and pulling. If it sticks, cool the mandrel (aluminium contracts more than carbon) or gently tap the end with a soft mallet.

**9. Trim ends.** Mark the final 300 mm length and cut both ends square using a rotary tool with a diamond or abrasive cutting disc. Wear a dust mask — carbon dust is an irritant. Lightly sand the cut edges to remove any burrs.

## Step 7: Quality Checks

Before you fly with a home-made arm, verify it meets expectations.

**Visual inspection:** The surface should be smooth and uniformly dark. White or grey patches indicate dry spots (fibre not wetted with resin). Glossy bumps indicate resin-rich areas. Neither is ideal, but small areas are acceptable for a hobby part.

**Tap test:** Tap along the tube with a coin. A consistent, sharp ring indicates good consolidation. A dull thud suggests a void or delamination at that location. Compare the sound at different points along the length.

**Weight check:** Weigh the finished tube and compare to the prediction. A 300 mm tube with 15 mm OD, 1 mm wall, and density of 1.50-1.55 g/cm3 should weigh:

```
Volume = pi/4 * (OD^2 - ID^2) * L
       = pi/4 * (15^2 - 13^2) * 300
       = pi/4 * (225 - 169) * 300
       = pi/4 * 56 * 300
       ≈ 13,195 mm^3 = 13.2 cm^3

Weight = 13.2 cm^3 * 1.52 g/cm^3 ≈ 20 g (wet layup)
Weight = 13.2 cm^3 * 1.55 g/cm^3 ≈ 20.5 g (prepreg)
```

If the tube weighs significantly more (say 25 g+), it is resin-heavy. If significantly less (say 15 g), it may have voids. Either way, a first attempt in the 18-23 g range is a good result.

**Concentricity:** Roll the tube on a flat surface. It should roll smoothly without wobbling. Wobble indicates the wall thickness varies around the circumference or the tube is not straight.

## Weight and Performance Comparison

| Property | Aluminium 6061-T6 | Carbon/Epoxy (this design) | Advantage |
|---|---|---|---|
| Wall thickness | 1.0 mm | 1.0 mm | Same |
| Outer diameter | 15 mm | 15 mm | Same |
| Tube weight (300 mm) | 31 g | 20 g | Carbon 35% lighter |
| Axial modulus | 69 GPa | 75 GPa (laminate avg.) | Carbon 9% stiffer |
| Bending stiffness EI | 74.8 N-m2 | 81.4 N-m2 | Carbon 9% stiffer |
| Tip deflection at 20 N | 2.4 mm | 2.2 mm | Carbon stiffer |
| Material cost per arm | ~$2 (tube stock) | ~$4-5 (materials) | Aluminium cheaper |
| Specific stiffness (EI/mass) | 2.41 N-m2/g | 4.07 N-m2/g | Carbon 69% better |

The carbon tube is meaningfully lighter at comparable or better stiffness. The specific stiffness advantage (stiffness per gram) is where carbon truly shines. For a quadcopter, reducing arm mass by 11 g each (44 g for four arms) translates directly to longer flight time or more payload.

## Key Takeaways

- A carbon fibre drone arm is a practical first composites project that delivers real performance gains over aluminium
- The design process follows the same steps as any composite structure: define loads, choose materials, design the laminate, choose a process, then build and verify
- A [0/+45/-45/0]s stacking sequence gives a good balance of bending stiffness (0-degree plies) and torsion/impact resistance (plus/minus 45-degree plies)
- Mandrel wrapping with wet layup is the most accessible method and requires minimal equipment
- Material cost for one arm is under $5 — the real investment is learning the process
- Always verify your finished part: weigh it, tap-test it, and inspect it visually before flying

## Further Reading / Tools

- [What Are Composites?](../01-fundamentals/what-are-composites.md) — start here if any of this was unfamiliar
- [Fibre Types](../01-fundamentals/fibre-types.md) — why carbon was the right choice for this application
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) — the rules behind the layup design
- [Wet Layup](../03-manufacturing-processes/wet-layup.md) — detailed process guidance
- [Material Costs](../08-cost-estimation/material-costs.md) — full cost tables for fibres, resins, and consumables
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — verify laminate stiffness and run failure analysis for your own tube design
