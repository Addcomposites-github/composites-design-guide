---
title: "Resin Systems"
category: "fundamentals"
tags: ["resin", "epoxy", "polyester", "vinyl-ester", "thermoplastic", "matrix"]
difficulty: "beginner"
related: ["what-are-composites.md", "fibre-types.md", "../03-manufacturing-processes/wet-layup.md", "../03-manufacturing-processes/prepreg-and-autoclave.md"]
tools: []
last_updated: "2026-02"
---

# Resin Systems

The resin — also called the **matrix** — is the plastic that binds the fibres together in a composite. Fibres carry most of the load, but without the resin they are just loose threads. The resin transfers load between fibres, protects them from moisture and chemicals, holds the part's shape, and prevents the fibres from buckling under compression. Choosing the right resin affects cost, processing method, temperature resistance, and toughness of the final part.

## What the Resin Actually Does

Think of a composite like a rope bridge. The ropes (fibres) carry the tension, but the planks and lashings (resin) hold everything in position and make it usable as a structure.

The resin has four jobs:

1. **Load transfer** — when one fibre breaks or a load enters from the side, the resin channels that force into neighbouring fibres. Without the resin, each fibre would act alone.
2. **Fibre protection** — bare carbon or glass fibres are brittle and sensitive to surface damage. The resin coats each fibre and shields it from abrasion, moisture, and UV.
3. **Shape definition** — the resin gives the part its final geometry. A curved car bonnet or a drone shell holds its shape because the resin cured into that form.
4. **Compression support** — fibres are strong in tension but tend to buckle under compression. The resin acts like a continuous support, preventing individual fibres from kinking sideways.

The resin typically makes up 35--60% of the composite by volume. Too little resin leads to dry spots and poor load transfer. Too much resin adds weight without adding strength.

## Thermoset vs Thermoplastic — The Fundamental Split

All composite resins fall into one of two families, and the difference is permanent.

**Thermosets** undergo a chemical reaction during cure. The polymer chains form cross-links — permanent bonds that lock the resin into a rigid network. Once cured, a thermoset cannot be melted or reshaped. Epoxy, polyester, and vinyl ester are all thermosets.

**Thermoplastics** do not cross-link. They soften when heated and solidify when cooled. You can remelt and reshape them repeatedly, like wax. PEEK, PPS, and nylon are thermoplastics used in composites.

```
Thermoset curing (permanent):

  Liquid resin + hardener ──heat/time──► Cross-linked solid
                                          (cannot be re-melted)

Thermoplastic processing (reversible):

  Solid pellets/tape ──heat──► Softened ──cool──► Solid again
                                 (cycle repeatable)
```

This distinction drives everything: shelf life, processing temperature, recyclability, repair method, and cost. Most composites today use thermosets because they are easier to process at lower temperatures, but thermoplastics are growing fast.

## Epoxy — The Workhorse

Epoxy is the most widely used resin in high-performance composites. The carbon fibre parts on aircraft, racing cars, and high-end bicycles almost always use epoxy. It earned this position through a strong combination of mechanical properties, adhesion, and processability.

**Why engineers choose epoxy:**
- Excellent adhesion to carbon, glass, and aramid fibres
- Low shrinkage during cure (typically 1--3%), which means less residual stress and better dimensional accuracy
- Good mechanical properties — tensile strength around 60--85 MPa neat (unreinforced), with good retention at moderate temperatures
- Available in formulations from room-temperature cure to 180 C cure

**The downsides:**
- More expensive than polyester (roughly 2--5x the cost per kilogram)
- Requires careful mix ratios — get the hardener ratio wrong and the resin will not cure properly
- Higher-performance epoxies need elevated temperature cures, which means ovens or autoclaves
- Brittle compared to thermoplastics unless toughened

**Common epoxy variants by cure temperature:**
- **Room-temperature cure (20--25 C):** Used for wet layup and repair. Convenient but gives lower glass transition temperature (Tg), meaning the part softens at relatively low temperatures (50--80 C). Fine for a car body panel; not for an engine cowling.
- **120 C cure:** A common prepreg cure cycle. Good balance of properties and processing cost. Used in sporting goods, automotive, and some aerospace secondary structures.
- **180 C cure:** The aerospace standard. Highest mechanical properties and temperature resistance (Tg up to 180--200 C). Requires an autoclave or high-temperature oven. Used in primary aircraft structures.

## Polyester — Cheap and Everywhere

Polyester resin is the entry point for composites. If you have been inside a fibreglass boat, sat in a bathtub surround, or walked past a roofing panel, you have seen polyester composite. It dominates general industry because it is cheap and easy to use.

**Advantages:**
- Lowest cost of any composite resin (often under $5/kg in bulk)
- Cures at room temperature with a simple catalyst (MEKP — methyl ethyl ketone peroxide)
- Fast gel times available — you can demould parts in hours
- Wide availability worldwide

**Disadvantages:**
- High shrinkage during cure (5--8%), which can cause print-through of the fibre pattern on the surface and internal stresses
- Lower mechanical properties than epoxy — tensile strength around 40--65 MPa neat
- Strong styrene emissions during processing — health and environmental concern
- Moderate adhesion to fibres compared to epoxy
- Poor hot/wet performance — properties degrade faster in humid, warm environments

Polyester is the right choice when cost matters more than peak performance: boat hulls, swimming pools, architectural cladding, storage tanks, truck fairings. It is rarely used in aerospace or high-performance motorsport.

## Vinyl Ester — The Middle Ground

Vinyl ester sits between polyester and epoxy in both performance and cost. It processes like polyester (same catalysts, similar handling) but delivers better mechanical properties and significantly better chemical resistance.

**Where vinyl ester wins:**
- Excellent chemical resistance — it handles acids, alkalis, and solvents better than polyester or epoxy. This makes it the standard for chemical storage tanks, scrubbers, and pipes.
- Better toughness and elongation to failure than polyester (typically 3--6% vs 1--3%)
- Lower shrinkage than polyester (though still higher than epoxy)
- Good fatigue performance

**Where it falls short:**
- Costs more than polyester (roughly 1.5--2x)
- Still uses styrene as a reactive diluent, so similar odour and emission concerns
- Does not match epoxy for adhesion or peak mechanical properties

Vinyl ester is popular in marine structures (boat hulls that need osmosis resistance), infrastructure (bridge decks, rebar, wind turbine blades), and chemical processing equipment. If you need better performance than polyester but cannot justify the cost and complexity of epoxy, vinyl ester is often the answer.

## Thermoplastics — PEEK, PPS, and Nylon

Thermoplastic composites are the fastest-growing segment of the composites industry. They solve several problems that thermosets cannot: recyclability, weldability, unlimited shelf life, and high toughness.

**Key thermoplastic resins for composites:**

- **PEEK (polyether ether ketone):** The premium option. Service temperatures above 250 C, outstanding toughness, excellent chemical resistance. Used in aerospace primary structures and medical implants. Very expensive — raw PEEK resin can cost $50--100+/kg.
- **PPS (polyphenylene sulphide):** Good chemical resistance and temperature performance (service to ~200 C) at lower cost than PEEK. Used in aerospace brackets, clips, and semi-structural parts.
- **PA/Nylon (polyamide):** The workhorse thermoplastic for automotive composites. Glass-fibre-reinforced nylon is used in engine covers, structural brackets, and under-the-hood parts. Low cost, moderate properties, absorbs moisture.

**Why thermoplastics are gaining ground:**
- No cure cycle — processing is heat-and-cool, not a chemical reaction. This means no shelf life for raw materials and potentially faster cycle times.
- High toughness and impact resistance — thermoplastic composites resist damage much better than thermoset composites. A PEEK panel that would survive an impact might cause delamination in an epoxy panel.
- Weldable — you can join thermoplastic composite parts by remelting the interface (ultrasonic welding, induction welding, resistance welding). No adhesive, no fasteners.
- Recyclable — at end of life, thermoplastic composites can be reprocessed.

**The catch:**
- High processing temperatures — PEEK needs 380--400 C; PPS needs 300--330 C. This requires specialised tooling and equipment.
- High material cost, especially for aerospace-grade resins
- Existing manufacturing infrastructure is built around thermosets, so switching requires capital investment

Thermoplastics dominate short-fibre moulding (injection-moulded parts) and are steadily moving into continuous-fibre structural applications as automated placement technology matures.

## Resin Comparison Table

```
Property           | Epoxy         | Polyester     | Vinyl Ester   | PEEK (thermo) | Nylon (thermo)
────────────────── | ────────────  | ───────────── | ───────────── | ───────────── | ──────────────
Tensile strength   | 60-85 MPa     | 40-65 MPa     | 60-80 MPa     | 90-100 MPa    | 60-80 MPa
(neat resin)       |               |               |               |               |
Elongation at      | 2-6%          | 1-3%          | 3-6%          | 30-50%        | 15-80%
break              |               |               |               |               |
Glass transition   | 120-200 C     | 60-120 C      | 100-150 C     | 143 C (Tg)    | 50-80 C
(Tg) range         | (depends on   |               |               | ~250 C        | (dry)
                   |  cure temp)   |               |               | (service)     |
Cure/process temp  | 20-180 C      | 20-25 C       | 20-25 C       | 380-400 C     | 230-280 C
Shrinkage          | 1-3%          | 5-8%          | 3-5%          | ~0%           | ~0%
Relative cost      | $$            | $             | $-$$          | $$$$$         | $-$$
Shelf life (uncured)| 6-12 months  | 3-6 months    | 3-6 months    | Unlimited     | Unlimited
                   | (prepreg)     |               |               |               |
Typical            | Aerospace,    | Boats, bath-  | Chemical      | Aerospace     | Automotive
applications       | motorsport,   | tubs, panels, | tanks, marine,| primary       | structural,
                   | sporting      | general       | infrastructure| structures,   | under-hood
                   | goods, wind   | industry      |               | medical       | components
                   | energy        |               |               |               |
```

*Note: Values are approximate and vary by specific formulation. Always check the supplier datasheet for your chosen resin system.*

## How to Choose a Resin

The resin choice is rarely made in isolation. In practice, your manufacturing process narrows the options before you even think about mechanical properties.

**Start with the process:**

```
What is your manufacturing method?
│
├─ Hand/wet layup ─────────────► Polyester (lowest cost)
│                                 or Epoxy (better properties)
│
├─ Vacuum infusion (VARTM) ───► Epoxy or Vinyl ester
│                                 (low viscosity needed)
│
├─ Prepreg + oven/autoclave ──► Epoxy (120 C or 180 C cure)
│
├─ Filament winding ──────────► Epoxy or Vinyl ester
│
├─ Injection moulding ────────► Nylon, PPS, or other
│   (short fibre)                thermoplastics
│
└─ Automated fibre placement ─► Epoxy prepreg (thermoset)
    (AFP/ATL)                    or PEEK/PPS tape (thermoplastic)
```

**Then consider the application requirements:**

- **Temperature:** Will the part see sustained heat? A car body panel sitting in the sun (80 C peak) is fine with room-temp-cured epoxy. A part near an engine (150 C+) needs 180 C-cured epoxy or a thermoplastic.
- **Chemical exposure:** Fuel tanks, chemical pipes, and marine hulls need chemical resistance. Vinyl ester or PEEK are strong choices.
- **Toughness / impact:** If the part must survive impacts (aircraft leading edges, sports helmets), toughened epoxy or thermoplastics are preferred over standard epoxy or polyester.
- **Cost:** For large, non-structural parts (boat decks, panels, fairings), polyester's low cost wins. For high-performance structural parts, epoxy or thermoplastics justify the premium.
- **Production rate:** Thermosets need cure time (minutes to hours). Thermoplastics can be formed in seconds to minutes, making them attractive for high-volume automotive production.

There is no universally "best" resin. There is only the best resin for your specific combination of performance requirements, manufacturing process, and budget.

## Key Takeaways

- The resin (matrix) transfers load between fibres, protects them, gives the part its shape, and prevents fibre buckling in compression
- Thermosets (epoxy, polyester, vinyl ester) cross-link permanently during cure; thermoplastics (PEEK, PPS, nylon) can be remelted and reshaped
- Epoxy is the default for high-performance composites: good properties, low shrinkage, but higher cost and often needs elevated cure temperatures
- Polyester is the cheapest option for general-purpose applications like boats and panels; vinyl ester offers a step up in performance and chemical resistance
- Thermoplastics offer superior toughness, recyclability, and weldability, but require high processing temperatures and more expensive equipment
- Your manufacturing process is the strongest driver of resin selection — choose the process first, then match the resin to it

## Further Reading / Tools

- [What Are Composites?](what-are-composites.md) — overview of fibres, resin, and laminates
- [Fibre Types](fibre-types.md) — carbon, glass, aramid compared
- [Wet Layup](../03-manufacturing-processes/wet-layup.md) — the simplest process, typically uses polyester or epoxy
- [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md) — the aerospace process, almost always epoxy
- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — build and analyse laminates once you have chosen your resin system
