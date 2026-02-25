---
title: "Automotive Composites and Lightweighting"
category: "applications"
tags: ["automotive", "lightweighting", "EV", "body-panels", "battery-enclosure", "crash", "HP-RTM"]
difficulty: "intermediate"
related: ["../01-fundamentals/fibre-types.md", "../03-manufacturing-processes/rtm.md", "../03-manufacturing-processes/prepreg-and-autoclave.md", "../03-manufacturing-processes/resin-infusion-vartm.md", "../08-cost-estimation/process-costs.md", "../09-case-studies/car-body-panel.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Automotive Composites and Lightweighting

Composites let car designers cut weight without sacrificing strength or stiffness. In battery-electric vehicles (EVs), every kilogram removed from the body extends driving range, shrinks the battery, and lowers total vehicle cost. This page explains where composites are used on a car, which manufacturing processes suit automotive production volumes, and when the cost trade-off actually makes sense.

## Why Weight Matters More Than Ever

Internal-combustion vehicles benefit from lightweighting too, but the payoff is transformative for EVs. A commonly cited industry rule of thumb: **every 10 % reduction in vehicle mass delivers a 6--8 % increase in driving range** (all else equal). That range gain compounds because a lighter car needs a smaller, cheaper battery pack, which itself weighs less, which means the suspension, brakes, and structure can all be downsized.

Consider a mid-size EV with a 500 kg battery. Saving 50 kg of body mass could let the manufacturer trim 10--15 kg of battery capacity while keeping range constant. Battery cells cost roughly $100--130/kWh at the pack level (2025 figures), so even a modest mass saving translates into real dollar savings on the most expensive single component of the car.

Aluminium already saves around 40 % over steel for equivalent structural performance. Carbon-fibre composites can save 50--70 %. The question is never "can composites save weight?" -- it is "can they do it at a cost and production rate the vehicle programme can tolerate?"

## Carbon vs Glass: Picking the Right Fibre

Not every composite part on a car needs carbon fibre. Glass fibre composites are far cheaper and often good enough.

| Property | Carbon Fibre (CF) | Glass Fibre (GF) |
|---|---|---|
| Tensile modulus | 230--400 GPa | 70--85 GPa |
| Density | 1.75--1.80 g/cm3 | 2.5--2.6 g/cm3 |
| Raw fibre cost | $15--30/kg (standard modulus) | $1.50--4/kg (E-glass) |
| Typical automotive use | Structural parts, premium body panels, wheels | Semi-structural panels, underbody shields, leaf springs |

**Use carbon when** stiffness-to-weight ratio dominates the design -- roof panels that affect centre of gravity, structural floor modules, performance suspension arms, and anywhere a few kilograms save real money downstream (battery sizing).

**Use glass when** the part is semi-structural or cosmetic and cost is the primary constraint -- fender liners, underbody aero shields, interior structural carriers, seat back shells. Glass-fibre SMC (sheet moulding compound) has been in volume automotive production for decades and is well understood by Tier 1 suppliers.

Many real-world parts use **hybrid layups** -- carbon plies on the outer skins for stiffness, glass plies in the core or low-stress areas to control cost.

## Applications by Vehicle Area

### Body Panels

Body panels -- bonnets (hoods), roofs, boot lids (trunk lids), fenders, door skins -- are the most visible composite application. They are primarily cosmetic and semi-structural: they must resist denting, support their own weight, and carry aerodynamic loads, but they rarely form part of the crash structure.

```
Typical composite bonnet cross-section:

    ┌──────────────────────────────┐  ← Class-A outer skin (woven CF or GF, 0.8-1.2 mm)
    │  ╲    ╱  ╲    ╱  ╲    ╱     │
    │   ╲  ╱    ╲  ╱    ╲  ╱      │  ← Inner reinforcement (hat-section ribs or sandwich core)
    │    ╲╱      ╲╱      ╲╱       │
    └──────────────────────────────┘  ← Inner skin or adhesive bonded stiffener
```

BMW uses carbon-fibre-reinforced plastic (CFRP) roof panels on the M3/M4 to lower the centre of gravity. McLaren moulds entire body panels from prepreg carbon. At the volume end, Corvette has used glass-fibre SMC body panels since the 1950s.

Weight saving for a bonnet: a steel bonnet at roughly 12--15 kg becomes 5--7 kg in CFRP, or 8--10 kg in aluminium. The composite version also allows more complex curvature in a single piece, eliminating spot-welded assemblies.

### Structural Members

Structural composites carry crash loads, torsional stiffness, and suspension forces. This is where composites deliver the most engineering value -- and where design gets hardest.

- **B-pillars** (the vertical post between front and rear doors) must resist roof crush and side impact. BMW developed hybrid B-pillars with a CFRP outer reinforcement bonded to a steel inner, saving about 2 kg per pillar while meeting Euro NCAP roof crush requirements.
- **Floor pans and tunnel structures** in the BMW i3 used a full CFRP passenger cell ("Life Module") bonded to an aluminium drive module. This was the most ambitious automotive CFRP structure in series production.
- **Crash structures** (front and rear crush cans) can absorb 3--5 times more energy per kilogram than steel or aluminium tubes. The energy is absorbed through progressive fragmentation (the composite breaks into small pieces in a controlled way) rather than plastic folding. Formula 1 crash structures have used this principle for decades; road cars like the McLaren P1 and Lamborghini Aventador use composite crash boxes.

Designing composite crash structures requires careful layup design and extensive physical testing because composites do not behave like metals in a crash -- there is no simple "fold line." The failure mode (splaying, fragmentation, or catastrophic fracture) depends heavily on fibre architecture, trigger geometry, and loading rate.

### Battery Enclosures

The battery enclosure is one of the fastest-growing composite applications in automotive. It must do several jobs at once:

1. **Structural** -- the enclosure often serves as the floor of the vehicle, carrying bending and torsion loads.
2. **Fire resistance** -- it must protect passengers and contain a thermal runaway event (a battery cell fire) for a defined period (typically 5+ minutes per regulation).
3. **EMI shielding** -- the high-voltage battery generates electromagnetic interference that can affect vehicle electronics. Carbon fibre, being electrically conductive, provides inherent shielding; glass fibre does not.
4. **Crash protection** -- the enclosure must resist ground impact (road debris, kerb strikes) and intrusion in a side crash.

A composite battery enclosure can be 30--40 % lighter than an equivalent steel/aluminium design. Polestar and several Chinese EV manufacturers are industrialising composite enclosure programmes. The trade-off is cost and the need for integrated fire-resistant barriers (intumescent coatings, ceramic blankets, or mica layers embedded in the laminate).

### Wheels

Carbon fibre wheels save 30--50 % versus forged aluminium. Because this is unsprung mass (weight below the suspension springs), the handling and ride benefit is amplified -- reducing unsprung mass improves tyre contact, braking response, and suspension compliance.

- **BMW** offers carbon wheels on the M4 (manufactured by Carbon Revolution or Thyssenkrupp) using a resin transfer moulding process with woven preforms.
- **Porsche** offers braided carbon wheels on the 911 Turbo S.
- **Lamborghini** pioneered "forged composite" (chopped carbon fibre in a compression mould) for structural wheel elements.

Carbon wheels are expensive ($2,000--6,000 per wheel at retail) and remain a premium option. The manufacturing challenge is producing a part with no voids and consistent mechanical properties under the extreme fatigue loads a wheel experiences.

### Interior Components

Interior composites rarely get headlines but represent high-volume applications:

- **Seat structures** -- glass-fibre or hybrid seat back frames replace stamped steel, saving 2--4 kg per seat row.
- **Dashboard carriers / instrument panel beams** -- long-glass-fibre thermoplastic (LGF-PP) injection moulded parts are standard in many OEMs.
- **Trim pieces** -- visible carbon-weave trim panels in premium vehicles (mostly cosmetic, often a thin decorative veneer over a substrate).

These are often the entry point for a Tier 1 supplier learning composites because the structural requirements are modest and the cycle times align with existing injection moulding infrastructure.

### Suspension Components

Composite leaf springs have been in production since the 1980s (the Corvette mono-leaf rear spring). A single glass-fibre-epoxy leaf spring replaces a multi-leaf steel assembly, cutting weight by 60--70 % while improving ride quality through better control of spring rate.

More recently, carbon fibre control arms, anti-roll bars, and subframe components have appeared on premium and performance vehicles. Ford developed a carbon-fibre-reinforced subframe for the Mustang GT500. These parts exploit the tailored stiffness property of composites -- you can orient fibres to be stiff in the load direction and compliant elsewhere, something impossible with isotropic metals.

## Manufacturing Processes for Automotive Scale

Aerospace composites production is measured in parts per day. Automotive composites production is measured in parts per minute. Bridging that gap requires different processes.

### HP-RTM (High-Pressure Resin Transfer Moulding)

HP-RTM is the process that enabled series production of CFRP car parts. BMW and its Tier 1 suppliers (SGL Carbon, Dieffenbacher, KraussMaffei) developed it for the i3 programme.

How it works:
1. A dry fibre preform (cut and shaped from woven or non-crimp fabric) is placed in a heated steel mould.
2. The mould closes under high clamping force (1,000--3,000 tonnes).
3. Resin (typically a fast-cure epoxy or polyurethane) is injected at high pressure (50--150 bar) to wet out the fibres.
4. The part cures in the hot mould in 2--5 minutes.
5. The mould opens and the part is demoulded.

Cycle time: **2--5 minutes** per part, depending on size and resin system. This is 10--20 times faster than traditional autoclave processing. The BMW i3 CFRP components were produced at a rate compatible with roughly 100 cars per day per press cell.

### Compression Moulding: SMC, BMC, and Prepreg Compression

**SMC (Sheet Moulding Compound)** is a sheet of chopped glass fibres (typically 25 mm long) pre-impregnated with polyester or vinyl ester resin. The sheet is cut into charges, stacked in a heated steel mould, and pressed. Cycle times are 1--3 minutes. SMC has been used for decades in bonnets, tailgates, and structural cross-members. It is quasi-isotropic (roughly equal properties in all directions) because the fibres are randomly oriented.

**Prepreg compression moulding** uses continuous-fibre pre-impregnated material in a press rather than an autoclave. This gives better mechanical properties than SMC but at a higher material cost. Used for structural parts that need directional stiffness.

### Wet Compression (Forged Composite)

Developed by Lamborghini in partnership with Callaway Golf and the University of Washington. Chopped carbon fibre tow segments (typically 25--50 mm) are placed in a mould with resin and compressed at high pressure and temperature. The result is a part with randomly oriented short fibres, lower mechanical properties than continuous-fibre composites, but the ability to fill complex 3D geometries in a single press cycle.

```
Forged composite vs continuous fibre:

  Continuous fibre:       Forged composite:
  ════════════════       ╱╲ ── ╲  ╱─╲
  ════════════════       ─╱  ╲╱  ──╱╲
  ════════════════       ╲──  ╱╲ ╱  ──
  (High strength along   (Lower peak strength,
   fibre direction)       but fills complex shapes)
```

Cycle time: **2--5 minutes**. Used by Lamborghini for suspension turrets, structural inserts, and wheel elements.

### Thermoplastic Stamping and Overmoulding

Organosheet (a thermoplastic-matrix composite sheet, typically glass or carbon fibre in a polyamide or polypropylene matrix) is heated in an infrared oven, transferred to a press, stamp-formed into shape, and optionally overmoulded with short-fibre injection moulding in the same tool.

Cycle time: **under 60 seconds**. This is the fastest route to structural composite parts at high volume. The thermoplastic matrix also enables welding to other thermoplastic parts and end-of-life recycling by remelting.

Used for seat structures, front-end carriers, underbody shields, and battery enclosure sub-components.

### Process Comparison for Automotive Volumes

| Process | Cycle Time | Fibre Type | Annual Volume Suitability | Typical Use |
|---|---|---|---|---|
| HP-RTM | 2--5 min | Continuous CF/GF | 20,000--60,000 parts/yr | Structural CFRP panels |
| SMC compression | 1--3 min | Chopped GF (or CF) | 50,000--500,000 parts/yr | Semi-structural panels, closures |
| Prepreg compression | 3--10 min | Continuous CF | 10,000--50,000 parts/yr | High-performance structural parts |
| Wet compression | 2--5 min | Chopped CF | 10,000--50,000 parts/yr | Complex 3D structural parts |
| Thermoplastic stamping | 30--60 sec | Continuous or woven GF/CF | 100,000+ parts/yr | Seat structures, carriers |
| VARTM / infusion | 30--90 min | Continuous CF/GF | 500--5,000 parts/yr | Low-volume, large parts |
| Prepreg + autoclave | 2--8 hrs | Continuous CF | 100--2,000 parts/yr | Motorsport, hypercars |

## Cost Reality Check

Composites are expensive compared to metals on a per-kilogram basis, and there is no point pretending otherwise.

| Material System | Approximate Cost ($/kg finished part) |
|---|---|
| Mild steel (stamped) | $2--5 |
| Aluminium (stamped or cast) | $5--15 |
| Glass fibre SMC | $8--20 |
| Carbon fibre HP-RTM | $30--80 |
| Carbon fibre prepreg (autoclave) | $80--200 |

The business case for automotive composites rests on **total system cost**, not part-for-part replacement:

1. **Battery cost offset** -- a 50 kg body mass saving in an EV might allow a 5--8 kWh smaller battery, saving $500--1,000 at the pack level.
2. **Part consolidation** -- a single composite moulding can replace an assembly of 5--15 steel stampings plus spot welds, brackets, and fasteners. The tooling, assembly labour, and logistics cost all drop.
3. **No corrosion protection** -- composites do not rust. Eliminating e-coat, phosphate wash, and cavity wax is a real saving in body-in-white (BIW) production.
4. **Lower tooling cost at low volume** -- composite moulds (especially for RTM and infusion) cost far less than steel stamping dies. For vehicles under 10,000 units/year, composites can be cheaper even at higher part cost.

The break-even point depends heavily on volume. Below roughly 5,000--10,000 units per year, CFRP body panels can compete with aluminium on total cost. Above 50,000 units per year, steel and aluminium usually win unless the mass saving has an outsized value (EVs, performance vehicles).

## Joining and Assembly

A composite body panel cannot simply be spot-welded to a steel frame. Joining composites to metals -- and to other composites -- is one of the biggest practical challenges in mixed-material automotive design.

**Adhesive bonding** is the preferred method for large composite panels. Structural adhesives (epoxy or polyurethane) distribute load over a large area and avoid drilling holes in the composite (which cuts fibres and creates stress concentrations). BMW bonds the CFRP Life Module to the aluminium Drive Module of the i3 using structural adhesive. Bond-line design, surface preparation, and cure time are critical.

**Mechanical fastening** (rivets, bolts, flow-drill screws) is used where disassembly is required or where bond-alone is insufficient. Self-piercing rivets (SPRs) work well for joining composite panels to metal structures. Bolt holes in composites must be properly designed with adequate edge distance and bearing-to-bypass stress ratios.

**Hybrid joining** combines adhesive with mechanical fasteners. The adhesive carries the primary load; the fasteners provide peel resistance, alignment during cure, and a fail-safe load path.

```
Hybrid bonded/bolted joint:

    Composite panel
    ═══════╤════════╤═══════
           │ bolt   │ bolt
    ───────┤adhesive├───────  ← adhesive bond line
           │ layer  │
    ───────┴────────┴───────
    Metal substructure
```

**Crash compatibility** between composite and metal zones requires careful transition design. At the interface between a CFRP crush can and an aluminium rail, a metallic "trigger" or attachment flange translates the progressive fragmentation of the composite into a load path the metal structure can absorb.

## Recycling and Sustainability

Composites have historically been difficult to recycle, and this is a legitimate concern. The automotive industry faces increasing regulatory pressure, particularly the EU End-of-Life Vehicle (ELV) directive, which requires 95 % of a vehicle by mass to be recoverable.

**Thermoset composites** (epoxy, polyester, vinyl ester matrix) cannot be remelted. Recycling routes include:

- **Mechanical grinding** -- the composite is ground into filler material. This downcycles the fibres (short length, damaged) and is low-value but functional for non-structural moulding compounds.
- **Pyrolysis** -- heating in the absence of oxygen burns off the resin and recovers the carbon fibres. The recovered fibres retain 85--95 % of their original tensile strength but are typically short and have a degraded surface. Several companies (ELG Carbon Fibre / Gen 2 Carbon, Vartega) operate at commercial scale.
- **Solvolysis** -- using a chemical solvent at elevated temperature and pressure to dissolve the resin and recover clean fibres. This can produce higher-quality recovered fibres than pyrolysis but is less mature commercially.

**Thermoplastic composites** (PA6, PP, PPS, PEEK matrix) can be remelted and reformed. This is a major driver behind the automotive industry's shift toward thermoplastic matrix composites for high-volume parts. End-of-life thermoplastic composite parts can be shredded, remelted, and injection moulded into new parts -- a true closed-loop recycling path, though the fibres shorten with each cycle.

BMW established a closed-loop recycling system for i3 CFRP production scrap: offcuts from the cutting and preforming stages are collected, processed, and reused in non-structural parts like roof and interior components.

## Aftermarket and Motorsport

For many companies and individuals, aftermarket and motorsport are the entry point to automotive composites. The economics are different from OEM production: volumes are low (tens to hundreds of parts), margins are high, and customers accept higher prices for performance and aesthetics.

**Motorsport** has always driven composite technology into automotive. Formula 1 monocoques have been carbon fibre since 1981 (McLaren MP4/1). Today, even grassroots racing series (Formula SAE, clubman racing, hillclimb) use CFRP body panels, wings, and structural components. The design freedom is enormous because certification requirements are less onerous than for road vehicles, and hand layup or low-volume infusion processes are perfectly viable.

**Aftermarket body panels** (bonnets, splitters, diffusers, wings, mirror covers) are a large market. Most are produced by wet layup or vacuum-bag prepreg cure in simple moulds. Quality varies enormously. Key considerations for aftermarket composite parts:

- **Fitment** -- the part must match OEM mounting points. Shrinkage and dimensional variation in composite moulding can make this challenging.
- **UV resistance** -- a clear-coated visible carbon-weave part needs UV-stable resin and proper clear coat to prevent yellowing.
- **Crash safety** -- aftermarket structural parts (roll cages, crash bars) require careful engineering. A poorly made CFRP part can be more dangerous than the steel part it replaces.

For a maker or small business considering automotive composites, aftermarket parts are the lowest-barrier, highest-learning opportunity. Start with a non-structural cosmetic part (a mirror cover, a dashboard trim piece), learn the moulding process, and work up to semi-structural components.

## Key Takeaways

- Every 10 % mass saving in an EV yields roughly 6--8 % more driving range and enables a smaller, cheaper battery -- this system-level argument is what makes the business case for automotive composites.
- Carbon fibre is not always the answer: glass fibre SMC and thermoplastic composites cover the majority of automotive composite applications at far lower cost.
- HP-RTM and compression moulding are the workhorse processes for automotive-volume CFRP, delivering 1--5 minute cycle times that align with assembly line takt.
- Battery enclosures are the fastest-growing application, combining structural, fire-resistance, and EMI-shielding requirements in a single composite part.
- Joining composites to metals (adhesive bonding, hybrid joints) and end-of-life recycling remain the two biggest practical challenges for wider adoption.
- Aftermarket and motorsport offer a low-volume, high-margin entry point for learning automotive composite design and manufacturing.

## Further Reading / Tools

- [AddStack -- free laminate calculator](https://addstack.addcomposites.com) -- use it to design and compare layups for automotive panels, check failure criteria, and explore material options.
- [Fibre Types](../01-fundamentals/fibre-types.md) -- detailed comparison of carbon, glass, aramid, and basalt fibres.
- [Resin Infusion / VARTM](../03-manufacturing-processes/resin-infusion-vartm.md) -- the low-volume process most accessible to small shops and aftermarket manufacturers.
- [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md) -- the aerospace-grade process used in motorsport and hypercars.
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) -- symmetry, balance, and orientation rules that apply to every automotive composite layup.
