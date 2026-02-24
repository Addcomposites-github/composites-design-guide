---
title: "Common Defects in Composite Manufacturing"
category: "manufacturing"
tags: ["defects", "voids", "wrinkles", "delamination", "dry-spots", "porosity"]
difficulty: "beginner"
related: ["wet-layup.md", "vacuum-bagging.md", "resin-infusion-vartm.md", "prepreg-and-autoclave.md", "afp-atl.md", "../01-fundamentals/failure-modes.md"]
tools: []
last_updated: "2026-02"
---

# Common Defects in Composite Manufacturing

Composite parts can look perfect on the outside and be riddled with hidden problems on the inside. Unlike metals, where defects like cracks are usually visible or detectable with simple methods, many composite defects are internal and invisible to the naked eye. Knowing what defects exist, what causes them, and how to prevent them is essential — whether you are making a car panel in a garage or a wing skin in a factory.

## Voids and Porosity

**What it is:** Small gas-filled cavities trapped within the cured laminate. Individual discrete cavities are called voids; distributed fine porosity is many tiny voids spread through a region.

**What causes it:**
- Trapped air between plies during layup
- Volatiles released from the resin during cure (moisture, solvents)
- Insufficient vacuum or compaction pressure
- Expired or moisture-contaminated prepreg

**How bad is it:**
- Void content below 1% is aerospace-acceptable
- 1–2% causes measurable reduction in interlaminar shear strength and fatigue life
- Above 5% is typically rejectable — strength can drop 20–40%

**Prevention:**
- Debulk every 3–5 plies during layup
- Ensure good vacuum bag integrity (no leaks)
- Store prepreg at correct temperature and humidity
- Use adequate autoclave pressure or vacuum compaction

```
Void in a laminate (cross-section):

    ─────────────────────────────   ← ply
    ─────────────────────────────   ← ply
    ──────────── ○ ──────────────   ← void (gas pocket)
    ─────────────────────────────   ← ply
    ─────────────────────────────   ← ply
```

## Wrinkles (Fibre Waviness)

**What it is:** An out-of-plane distortion where fibres bend or buckle instead of lying flat. Can be localised (a single sharp fold) or distributed (gentle waviness over a broad area).

**What causes it:**
- Excess material in a ply that cannot drape flat on a curved surface
- Ply bridging that collapses under vacuum pressure, forcing material to bunch up
- Thermal expansion mismatch between the tool and the laminate during cure
- Poor debulking allowing inter-ply slippage

**How bad is it:**
- Severe wrinkles reduce compressive strength by 30–50% or more
- Even gentle waviness (fibre misalignment of 5–10°) degrades compression performance
- Wrinkles are one of the most structurally damaging composite defects

**Prevention:**
- Use darts or slits in plies over doubly curved surfaces
- Debulk frequently during layup
- Design the tool to minimise thermal mismatch
- For AFP: respect minimum steering radii

## Delamination

**What it is:** Separation between adjacent ply layers. The resin bond between two plies fails, creating a planar crack.

**What causes it (during manufacture):**
- Contamination between plies (release film left in, dust, moisture)
- Poor tack or insufficient compaction during layup
- Tooling radius too tight — plies peel apart at the bend
- Thermal stress during cooldown from cure temperature

**How bad is it:**
- Delamination dramatically reduces compressive and buckling strength
- Under fatigue loading, delaminations grow
- Often undetectable visually — requires ultrasonic inspection (C-scan)

**Prevention:**
- Clean layup environment — control dust, moisture, and contamination
- Debulk at tight radii to ensure ply conformance
- Avoid excessive cure temperature ramp rates that create thermal gradients
- Verify that peel plies and release materials are correctly placed (not left inside the laminate!)

## Dry Spots

**What it is:** Regions where fibres are not fully wetted with resin. The dry fibres have no structural contribution — they are held in place by surrounding cured resin but carry no load through matrix transfer.

**What causes it:**
- Inadequate resin application during wet layup
- Flow front bypassing a region during resin infusion (race-tracking)
- Insufficient resin volume mixed (ran out before the part was fully wet)
- Blocked flow paths in infusion (pinched tubes, collapsed flow media)

**How bad is it:**
- Dry spots are typically scrap-level defects — the region cannot carry design load
- Even small dry patches compromise environmental protection (moisture enters through dry fibres)

**Prevention:**
- In wet layup: work methodically, section by section, and inspect before bagging
- In infusion: plan inlet/outlet positions carefully, monitor flow front, prepare extra resin
- In infusion: pack fabric to mould edges to prevent race-tracking

## Bridging

**What it is:** A ply spans across an internal corner or concavity rather than conforming to the tool surface, leaving a void underneath.

```
Bridging at an internal corner:

    What happens:                 What you want:
    │          │                  │          │
    │    ╲     │ ← ply bridges   │    │     │ ← ply pressed
    │     ──── │   across corner │    └──── │   into corner
    │          │   (void under)  │          │   (no void)
```

**What causes it:**
- Ply stiffness too high relative to the corner radius
- Insufficient vacuum pressure or debulking
- Thick laminate stack resists conforming to tight radii

**Prevention:**
- Debulk before the stack becomes too thick to press into corners
- Use a smaller corner radius on the tool (within design limits)
- Apply hand pressure or shaped caul plates at corners before bagging

## Foreign Object Debris (FOD)

**What it is:** Any foreign material trapped inside the laminate — backing paper, release film, tape, glove fragments, tools, hair, or shop debris.

**How bad is it:**
- Creates a local delamination or resin-rich pocket
- Non-structural FOD (paper, plastic) creates a weak plane
- Metallic FOD can cause galvanic corrosion with carbon fibre

**Prevention:**
- Strict shop-floor cleanliness protocols
- FOD checks at every debulk cycle
- Tool accountability (count tools in and out)
- Clean room or controlled environment for aerospace parts

## Resin-Rich and Resin-Starved Areas

**Resin-rich:** Too much resin in a local area — typically at ply drop-offs, corners, or around inserts. Resin-rich areas are brittle, prone to micro-cracking, and heavier than necessary.

**Resin-starved:** Too little resin — fibres are visible on the surface, or the laminate feels rough and dry to the touch. Insufficient resin means poor fibre-to-fibre load transfer.

Both are controlled by proper vacuum bag consumables (bleeder and release film) and resin management during layup or infusion.

## Defect Summary Table

| Defect | Typical cause | Structural impact | Detection method |
|---|---|---|---|
| Voids / porosity | Trapped air, poor vacuum | Reduced shear strength | Ultrasonic, X-ray |
| Wrinkles | Draping issues, bridging | Severe compression loss | Visual, ultrasonic |
| Delamination | Contamination, peel stress | Loss of compressive strength | Ultrasonic C-scan |
| Dry spots | Resin starvation | No load transfer locally | Visual, ultrasonic |
| Bridging | Tight corners, poor debulk | Void at radius | Visual, ultrasonic |
| FOD | Cleanliness failure | Local weak zone | Visual, X-ray |
| Resin-rich area | Ply drops, poor bleed | Micro-cracking, weight | Ultrasonic, micrograph |

## Key Takeaways

- Many composite defects are internal and invisible — inspection (ultrasonic, X-ray) is essential for structural parts
- Voids above 1–2% measurably degrade strength; above 5% is typically rejectable
- Wrinkles are among the most damaging defects — 30–50% compressive strength loss is common
- Debulking frequently during layup prevents or reduces most defects (voids, bridging, wrinkles)
- Cleanliness prevents FOD and contamination-driven delamination
- Prevention through good process design is always cheaper than inspection and repair after the fact

## Further Reading / Tools

- [Vacuum Bagging](vacuum-bagging.md) — the primary defence against voids and porosity
- [Wet Layup](wet-layup.md) — where many defects originate if technique is poor
- [Failure Modes](../01-fundamentals/failure-modes.md) — how manufacturing defects translate into structural failure
- [Design for Manufacture](../02-design-rules/design-for-manufacture.md) — designing parts to avoid defect-prone geometry
