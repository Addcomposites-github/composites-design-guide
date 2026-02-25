---
title: "eVTOL and UAM Composites Design"
category: "applications"
tags: ["eVTOL", "UAM", "urban-air-mobility", "drone", "aircraft", "lightweight", "certification"]
difficulty: "intermediate"
related: ["../01-fundamentals/fibre-types.md", "../02-design-rules/stacking-sequences.md", "../03-manufacturing-processes/prepreg-and-autoclave.md", "../03-manufacturing-processes/afp-atl.md", "../03-manufacturing-processes/filament-winding.md", "../08-cost-estimation/process-costs.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# eVTOL and UAM Composites Design

Electric vertical take-off and landing (eVTOL) aircraft are reshaping urban transportation. These vehicles carry passengers or cargo across cities using electric power and vertical flight, a concept known as urban air mobility (UAM). Composites are not optional for eVTOL -- they are the enabling technology. Every kilogram saved in the airframe translates directly into extra range, extra payload, or fewer battery cells. This page covers why composites dominate eVTOL design, what materials and processes the industry uses, and the unique engineering challenges these aircraft present.

## Why eVTOL Needs Composites

Weight is the single most important design driver for any eVTOL aircraft. Battery energy density today sits around 250-300 Wh/kg at the cell level, which is roughly 40-50 times less energy per kilogram than jet fuel. That brutal physics reality means every gram of airframe weight directly steals range or payload capacity.

A typical four-seat eVTOL has a maximum take-off weight of around 2,000-3,000 kg. Of that, batteries consume 30-40%, leaving a tight budget for structure, systems, and passengers. If you build the airframe from aluminium, it weighs roughly 30-40% more than an equivalent composite airframe. On an aircraft where the total structural mass might be 400-600 kg, that difference could be 120-180 kg -- enough for one fewer passenger or 50-80 km less range.

Carbon fibre reinforced polymer (CFRP) composites offer the best strength-to-weight and stiffness-to-weight ratios of any practical structural material. A CFRP laminate can achieve a specific strength (strength divided by density) five to six times that of aluminium alloys. This is why companies like Joby, Lilium, Archer, Wisk, EHang, and Volocopter all build their primary structures from composites.

Beyond weight, composites offer three additional advantages critical for eVTOL:

- **Shape freedom.** Complex aerodynamic surfaces, nacelle fairings, and integrated structures are easier to mould than to machine from metal.
- **Fatigue tolerance.** Composites do not develop fatigue cracks the way metals do. They degrade differently (more on this below), but for high-cycle applications like rotors, this behaviour is favourable.
- **Part consolidation.** A composite airframe can integrate stiffeners, skins, and attachment features into a single co-cured assembly, reducing fastener count and assembly labour.

## Typical eVTOL Composite Structures

Nearly every structural element of an eVTOL is a candidate for composite construction. Here is a simplified structural breakdown:

```
eVTOL Structural Breakdown
===========================

                     ┌─────────────┐
                     │   Rotors /  │  High-performance CFRP
                     │  Propellers │  (fatigue-critical)
                     └──────┬──────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
   ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐
   │   Booms /   │  │   Fuselage  │  │  Nacelles / │
   │    Wings    │  │  (cabin +   │  │   Motor     │
   │             │  │   tailcone) │  │   Housings  │
   └──────┬──────┘  └──────┬──────┘  └─────────────┘
          │                │
   ┌──────┴──────┐  ┌──────┴──────┐
   │  Landing    │  │  Battery    │
   │   Gear      │  │  Enclosures │
   └─────────────┘  └─────────────┘
```

**Fuselage and cabin.** The passenger-carrying structure. Typically a semi-monocoque (a shell that carries loads through its skin and internal frames) built from CFRP skins with sandwich core in lightly loaded areas. Joby's aircraft uses a smooth composite fuselage pod. Lilium's jet has a composite cabin integrated with the wing structure.

**Booms and wings.** These carry the rotor thrust loads back into the fuselage. Booms on multi-rotor designs (Joby, Archer, Wisk) are hollow CFRP tubes or box beams. Wings on lift-plus-cruise designs carry aerodynamic loads in forward flight. These are the most structurally demanding composite parts, often requiring high-modulus carbon fibre and carefully designed stacking sequences.

**Rotors and propellers.** High-cycle fatigue-critical components. Typically built from unidirectional CFRP with a spar (the main load-carrying beam inside the blade) and aerodynamic skins. Volocopter's 18-rotor design uses many small, relatively simple propellers. Joby uses fewer, larger tilt-rotors with variable pitch.

**Nacelles and fairings.** Aerodynamic housings for motors, tilt mechanisms, and wiring. Often glass fibre or hybrid glass/carbon laminates -- weight is less critical here than in primary structure, so lower-cost glass fibre is acceptable.

**Battery enclosures.** Must contain thermal runaway events (battery fires). These use specialised composite layups with fire-resistant resins or additional protective layers.

**Landing gear.** Energy-absorbing composite structures, sometimes using glass fibre for its higher strain-to-failure (it bends more before breaking), which helps absorb crash energy.

## Material Selection for eVTOL

Material choices in eVTOL reflect a balance between performance, cost, and certification readiness.

**Carbon fibre for primary structure.** The workhorse fibres are intermediate modulus grades like T700S and T800S (Toray designation). These offer an excellent balance of strength (4,900-5,500 MPa tensile strength), stiffness (230-294 GPa modulus), and cost. T700S is the most widely used carbon fibre in aerospace and has extensive material qualification data, which matters enormously for certification.

Higher-modulus fibres like M55J or M60J appear in specific applications where stiffness drives the design -- for example, rotor blade spars where deflection limits are tight. But these cost three to five times more than T700S and are more brittle, so their use is targeted.

**Glass fibre for secondary structure.** E-glass and S-glass appear in fairings, interior panels, and some landing gear components. Glass is cheaper, more damage-tolerant (it resists impact better), and transparent to radar (useful for structures housing antennas). The penalty is roughly 40% more weight for the same stiffness compared to carbon.

**Resin systems.** Epoxy dominates eVTOL composite structures, just as it does in traditional aerospace. Toughened epoxy prepregs (like Hexcel 8552 or Toray 3900 series) provide good damage tolerance and have extensive allowables databases. For fire-critical areas such as battery enclosures, phenolic resins or intumescent (swelling when heated) epoxy systems provide fire resistance at the cost of lower mechanical properties.

**Thermoplastics -- the production-rate play.** For high-rate production, thermoplastic composites (using resins like PEEK, PEKK, or PPS reinforced with carbon fibre) offer a game-changing advantage: parts can be stamp-formed in minutes rather than cured in hours. Lilium has invested heavily in thermoplastic composite structures for their production aircraft. The trade-off is higher material cost and the need for high-temperature tooling, but the faster cycle times can make the economics work at volume.

**Core materials.** Sandwich structures (two thin composite face sheets bonded to a lightweight core) are common in eVTOL for panels, doors, and lightly loaded skins. Typical cores include Nomex honeycomb (aramid paper, excellent strength-to-weight), PMI foam (Rohacell -- closed-cell foam, good for complex shapes), and PET foam (lower cost, recyclable).

## Design Challenges Unique to eVTOL

### High-Cycle Fatigue from Rotor Loads

A commercial helicopter might fly 500-1,500 hours per year. An eVTOL air taxi making short urban hops could fly 2,000-3,000 hours per year, accumulating far more load cycles on rotor components. A rotor spinning at 2,000 RPM subjects the blade root to roughly 10^9 load cycles over a 20-year service life.

Composites handle fatigue differently from metals. Metals develop discrete cracks that grow predictably (which is actually useful for inspection-based maintenance). Composites instead accumulate distributed damage -- matrix micro-cracking, fibre-matrix debonding, delamination -- that degrades stiffness and strength gradually. The good news is that well-designed CFRP laminates retain 60-80% of their static strength even after millions of load cycles, provided the peak strains stay below the fatigue threshold (typically 0.3-0.4% strain for a tension-tension fatigue case).

The design approach for eVTOL rotor blades is to keep operating strains well below the fatigue threshold and to use damage-tolerant layup designs with sufficient off-axis plies to arrest any micro-cracking.

### Crashworthiness and Energy Absorption

eVTOL aircraft must protect passengers in a survivable crash. Regulatory targets typically require survival at vertical impact velocities of 7-9 m/s (roughly equivalent to a fall from 2.5-4 metres). The structure must absorb kinetic energy in a controlled way -- crushing progressively rather than shattering catastrophically.

Composites can be excellent energy absorbers when designed correctly. Composite crush tubes and sine-wave beam sections can achieve specific energy absorption (SEA) values of 50-120 kJ/kg, compared to 15-30 kJ/kg for aluminium. The key is triggering a stable progressive crushing mode rather than brittle fracture:

```
Composite crush tube behaviour
===============================

  GOOD: progressive crush        BAD: brittle fracture
  (high energy absorption)       (low energy absorption)

  ║████████║  ← intact           ║████████║  ← intact
  ║████████║                     ║████████║
  ║▓▓▓▓▓▓▓▓║  ← crush zone      ║        ║
  ║▓▓░░░░▓▓║    (fronds splay    ║   ──── ║  ← single crack
  ╚══╗  ╔══╝    and fragment)    ╚════════╝    (sudden failure)
     ║  ║
   ground                        ground
```

Design features that promote progressive crushing include chamfered (bevelled) trigger ends, fabric plies on the outer surface (to form stable fronds), and tulip-shaped or sine-wave cross-sections. Landing gear legs, subfloor beams, and seat support structures all use these principles.

### Battery Enclosure Fire Resistance

Lithium-ion battery thermal runaway is one of the most serious safety concerns in eVTOL design. A single cell failure can produce temperatures exceeding 1,000 degrees C and generate toxic, flammable gases. The battery enclosure must contain this event long enough for passengers to evacuate (typically 5 minutes minimum) and prevent fire from spreading to the rest of the airframe.

Standard CFRP with epoxy resin begins to lose mechanical properties above 150-180 degrees C (near the glass transition temperature of the resin). For battery enclosures, designers use several strategies:

- **Phenolic resin composites.** Phenolics char rather than burn, providing excellent fire resistance. Mechanical properties are lower than epoxy systems, but the fire performance is far superior. Common in helicopter fire walls and now adapted for eVTOL battery boxes.
- **Intumescent protection layers.** Coatings or interlayers that swell dramatically when heated, forming an insulating char layer. These can be applied to standard CFRP structures to add fire resistance.
- **Ceramic fibre blankets.** Added as thermal barriers between battery modules and composite structure.
- **Metal liners.** Some designs use a thin stainless steel or titanium inner liner for thermal containment, with the composite providing structural support.

### Lightning Strike Protection

Any aircraft flying in or near weather must survive a lightning strike. Lightning attachment to a composite structure is more damaging than to a metal one because composites are poor electrical conductors. Without protection, a lightning strike can vaporise resin, delaminate plies, and puncture skins.

Lightning strike protection (LSP) for composite eVTOL structures typically uses one or more of the following:

- **Expanded copper foil (ECF).** A thin layer of perforated copper bonded to the outer surface. This is the most common approach in aerospace and adds roughly 0.05-0.15 kg/m2.
- **Conductive mesh.** Bronze or copper wire mesh embedded in the outer ply. Slightly heavier but more robust to handling damage.
- **Conductive surfacing film.** A resin film loaded with conductive particles, providing a path for lightning current while adding minimal weight.

The protection layers must be electrically bonded to the airframe grounding network, and fastener locations need careful attention to prevent arcing.

### Vibration and Acoustic Management

eVTOL aircraft operate over populated areas, making noise a critical design constraint. Composite structures can be tailored for vibration damping through:

- **Constrained layer damping.** A viscoelastic (rubbery) layer sandwiched between two composite plies converts vibration energy into heat.
- **Stiffness tailoring.** Adjusting fibre orientations to shift natural frequencies away from rotor harmonics.
- **Acoustic treatments.** Composite sandwich panels with micro-perforated face sheets can act as acoustic absorbers in nacelles and cabin linings.

Rotor blade design directly affects noise. Composite blades allow the complex twist distributions and swept tip geometries that reduce blade-vortex interaction noise -- one of the loudest sources in helicopter and eVTOL flight.

## Manufacturing Approach by Volume

The right manufacturing process depends entirely on how many aircraft you plan to build per year. eVTOL companies progress through distinct phases:

### Prototype and Certification Phase (1-10 aircraft/year)

**Process:** Hand layup of prepreg (pre-impregnated fibre sheets) into moulds, cured in an autoclave (a large pressure oven, typically at 180 degrees C and 6 bar pressure).

**Why:** This process has decades of aerospace heritage and certification precedent. Regulatory authorities understand it, material databases exist for it, and the process produces high-quality, repeatable parts. Almost every eVTOL company starts here because the certification risk is lowest.

**Limitations:** Slow (8-24 hour cure cycles), labour-intensive, and autoclaves are expensive capital equipment. Fine for prototypes, unsustainable at production rates.

### Low-Rate Production (50-500 aircraft/year)

**Process:** Resin transfer moulding (RTM), compression moulding, and out-of-autoclave (OOA) prepreg cured in ovens.

**Why:** RTM places dry fibre preforms into a closed mould and injects resin under pressure. This produces near-net-shape parts with good surface finish on both sides, reduces hand labour, and eliminates the autoclave. Cycle times drop to 1-4 hours per part. OOA prepregs are formulated to cure at lower pressures (vacuum only, no autoclave needed) while still meeting aerospace quality standards.

**Relevant for:** Companies transitioning from certification to early commercial operations. Archer and Joby have both invested in RTM capabilities.

### High-Rate Production (1,000+ aircraft/year)

**Process:** Automated fibre placement (AFP), thermoplastic stamp forming, high-pressure RTM (HP-RTM).

**Why:** At 1,000+ aircraft per year (the target for profitable air taxi operations), manual processes cannot keep up. AFP uses a robotic head to place narrow strips of prepreg tape onto a mould, building up the laminate automatically. Thermoplastic stamp forming heats a pre-consolidated thermoplastic composite sheet above its melt point and presses it into shape in under a minute. HP-RTM injects resin at high pressure for fast fill and cure times under 10 minutes.

**AFP-XS relevance:** Traditional AFP machines cost $2-10 million and require large facilities. AFP-XS (a compact, affordable automated layup system from AddComposites) makes automated fibre placement accessible for startup-scale production volumes. It mounts on a standard industrial robot arm and can lay up parts with aerospace-quality precision at a fraction of the capital cost, making it relevant for eVTOL companies in the 100-1,000 units/year range where hand layup is too slow but a full-scale AFP cell is too expensive.

```
Manufacturing approach vs. production volume
=============================================

Volume/yr:   1    10    50   100   500  1,000  5,000
             |     |     |     |     |     |      |
Hand layup   |=====|=====|     |     |     |      |
+ autoclave  |  prototypes &   |     |     |      |
             |  certification  |     |     |      |
             |     |     |     |     |     |      |
OOA prepreg  |     |=====|=====|=====|     |      |
RTM          |     |     |=====|=====|=====|      |
             |     |     |     |     |     |      |
AFP-XS       |     |     |=====|=====|=====|      |
             |     |     |     |     |     |      |
Full AFP     |     |     |     |     |=====|======|
HP-RTM       |     |     |     |     |=====|======|
TP stamping  |     |     |     |     |     |======|
```

## Certification Considerations

eVTOL certification is evolving rapidly. The two main regulatory paths are:

- **EASA SC-VTOL (Special Condition for VTOL).** The European framework specifically designed for eVTOL aircraft. It defines categories based on passenger count and operational concept.
- **FAA Part 23 (amended) / proposed Part 21 powered-lift category.** In the United States, eVTOL aircraft are being certified under amended small aeroplane rules or emerging powered-lift rules.

For composite structures, certification requires:

1. **Material qualification.** Proving that the material system (fibre + resin + process) produces consistent, predictable properties. This involves extensive coupon testing (thousands of small specimens) to establish design allowables -- the statistically derived strength values used in structural analysis. This process alone can take 2-3 years and cost several million dollars.

2. **Building-block approach.** Testing progresses from coupons to elements (simple structural features) to sub-components to full-scale structure. Each level validates the analysis methods used at the level below. This is the same approach used for all aerospace composite certification (per CMH-17 guidelines) and is not unique to eVTOL, but the timeline and cost can be challenging for startups.

3. **Damage tolerance and durability.** Demonstrating that the structure can sustain expected damage (tool drops, hail, bird strike) and still carry limit loads. This drives the design to use impact-resistant layups and establishes inspection intervals.

4. **Fatigue and damage growth.** Showing that under repeated loading, any damage does not grow to a critical size within the inspection interval. Particularly important for rotor components as discussed above.

One advantage for eVTOL companies: several material systems (T700/8552, T800/3900-2, etc.) already have shared databases from previous aerospace programmes (such as NCAMP -- the National Center for Advanced Materials Performance), which can significantly reduce material qualification time and cost.

## Cost and Weight Targets

Understanding the cost and weight landscape helps frame design decisions:

**Structural weight fraction.** For a typical eVTOL, the airframe (all composite and metallic structure, excluding systems, batteries, and motors) represents roughly 25-35% of the empty weight. On a 2,500 kg MTOW aircraft with 1,500 kg empty weight, that is 375-525 kg of structure.

**Cost targets.** The aerospace composite industry typically produces structure at $300-1,000/kg depending on complexity and volume. For eVTOL to be commercially viable (air taxi ticket prices competitive with ground transport), airframe costs need to reach $50-200/kg at production rates -- a significant reduction from traditional aerospace but achievable with automotive-influenced processes like HP-RTM and thermoplastic stamping.

**The weight-cost trade-off.** Not every gram of weight reduction is worth pursuing at any cost. A useful rule of thumb for eVTOL: each kilogram of structural weight saved is worth roughly $200-500/year in reduced battery and energy costs over the aircraft life. This sets the economic justification for more expensive materials or processes.

## eVTOL vs Helicopter vs Automotive Composites

| Characteristic | eVTOL | Traditional Helicopter | Automotive (sports car) |
|---|---|---|---|
| **Primary fibre** | T700/T800 carbon | T700/T300 carbon | T300 carbon or glass |
| **Primary resin** | Toughened epoxy, thermoplastics | Toughened epoxy | Epoxy, vinyl ester, thermoplastics |
| **Typical fibre volume** | 55-60% | 55-62% | 45-55% |
| **Design strain limit** | 0.4-0.5% (damage tolerant) | 0.4-0.5% | 0.6-1.0% (less conservative) |
| **Fatigue cycles (life)** | 10^8 - 10^9 (rotors) | 10^7 - 10^8 (rotors) | 10^5 - 10^6 |
| **Production volume** | 100-5,000/yr (target) | 10-200/yr | 1,000-100,000/yr |
| **Primary process** | Prepreg/RTM evolving to AFP/TP | Prepreg + autoclave | HP-RTM, compression moulding, TP stamping |
| **Cost target ($/kg)** | $50-200 | $300-1,000 | $20-100 |
| **Certification basis** | SC-VTOL / Part 23 | Part 27/29 | Crash test standards (NCAP) |
| **Lightning protection** | Required (ECF/mesh) | Required (ECF/mesh) | Rarely required |
| **Crashworthiness** | Passenger protection (7-9 m/s) | Passenger protection (9-13 m/s) | Occupant protection (50-64 km/h frontal) |
| **Fire resistance** | Battery enclosure critical | Fuel system containment | Battery enclosure (EVs) |
| **Inspection approach** | Scheduled + SHM (structural health monitoring) | Scheduled calendar/flight hours | Crash repair or replace |

The eVTOL composites challenge sits squarely between aerospace and automotive: it demands aerospace-grade quality and certification rigour but needs automotive-grade production rates and costs. Companies that can bridge this gap -- using processes like AFP-XS for the transition zone, then scaling to full automation -- will have a significant competitive advantage.

## Key Takeaways

- Every kilogram of eVTOL airframe weight directly reduces range or payload due to the low energy density of current batteries. Composites are not a luxury -- they are a necessity.
- T700/T800 carbon fibre with toughened epoxy is the baseline material system for primary eVTOL structure, with thermoplastics emerging for high-rate production.
- High-cycle fatigue, crashworthiness, battery fire containment, and lightning strike protection are the four design challenges that differentiate eVTOL composites from other aerospace applications.
- Manufacturing strategy must evolve with production volume: hand layup prepreg for certification, RTM and AFP-XS for low-rate production, full AFP and thermoplastic stamping for high-rate.
- Certification follows the same building-block approach as traditional aerospace composites but benefits from shared material databases (NCAMP) that can reduce qualification time.
- The cost target of $50-200/kg for airframe structure requires automotive-influenced manufacturing processes, which is a fundamental shift from traditional aerospace economics.

## Further Reading / Tools

- [AddStack -- free laminate calculator](https://addstack.addcomposites.com) for sizing eVTOL composite panels and checking stacking sequence rules
- [Stacking Sequences](../02-design-rules/stacking-sequences.md) for symmetry, balance, and the 10% rule applied to eVTOL structures
- [Fibre Types](../01-fundamentals/fibre-types.md) for detailed properties of carbon, glass, and aramid fibres
- [Prepreg and Autoclave](../03-manufacturing-processes/prepreg-and-autoclave.md) for the baseline eVTOL manufacturing process
- [AFP/ATL](../03-manufacturing-processes/afp-atl.md) for automated fibre placement at production scale
- CMH-17 (Composite Materials Handbook) for material qualification and design allowables methodology
- EASA SC-VTOL documentation for the European eVTOL certification framework

> Structural concepts and design principles in this article are drawn from publicly available industry knowledge, conference papers (SAMPE, AHS/VFS), and regulatory guidance documents.
