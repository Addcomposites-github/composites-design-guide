---
title: "Post-Processing, Trimming, and Inspection"
category: "manufacturing"
tags: ["trimming", "NDI", "inspection", "assembly", "finishing"]
difficulty: "intermediate"
related: ["common-defects.md", "../02-design-rules/material-excess-and-boundaries.md", "../02-design-rules/design-for-manufacture.md"]
tools: []
last_updated: "2026-02"
---

# Post-Processing, Trimming, and Inspection

Curing a composite part is only the midpoint of the manufacturing process. What follows — demoulding, trimming, inspection, and assembly — determines whether the part meets its design intent and is fit for service.

## Demoulding

After cure, the part must be separated from the tool:

- **Release agent** applied before layup enables clean separation. Failure to apply release agent can bond the part permanently to the tool.
- **Thermal mismatch** between the composite and the tool (especially steel or aluminium tools) helps separation as the assembly cools — the tool contracts more than the part.
- **Draft angles** (1°–3° on vertical surfaces) prevent the part from locking onto male tool features.
- **Wedge and air blast** assist separation for stubborn parts. Never use metal wedges directly on the composite surface — use plastic or Teflon-coated tools.

After demoulding, remove all consumable materials: peel ply, breather, release film, vacuum bag, and sealant tape.

## Trimming

Most composite parts are cured with excess material beyond the engineering boundary (the MEOP). Trimming removes this excess to achieve the final part dimensions (EOP).

### CNC 5-Axis Routing

The most common method for aerospace and high-precision applications:
- **Accuracy:** ±0.1 mm
- **Edge quality:** clean, consistent, minimal delamination
- **Tool:** diamond-coated or PCD (polycrystalline diamond) router bits
- **Feed rate:** depends on material and thickness; typically 1–5 m/min
- **Dust extraction** is mandatory — carbon fibre dust is conductive and can damage electronics, and all composite dust is a respiratory hazard

### Waterjet Cutting

Abrasive waterjet uses a high-pressure water stream (3000–4000 bar) with garnet abrasive:
- **Accuracy:** ±0.2 mm
- **Advantages:** no heat-affected zone, works on any thickness, cuts CFRP and GFRP equally
- **Disadvantages:** requires drying after cutting, can cause moisture ingress at cut edges
- **Best for:** thick laminates (>10 mm), materials sensitive to heat

### Laser Cutting

CO2 or fibre lasers cut composites by vaporising material:
- **Accuracy:** ±0.05 mm
- **Speed:** very fast for thin laminates
- **Disadvantage:** creates a heat-affected zone (HAZ) that can degrade the resin and fibre near the cut edge
- **Best for:** thin laminates (<3 mm), non-structural trim, prepreg cutting before cure

### Manual Trimming

Using diamond-coated abrasive discs, oscillating tools, or routers:
- **Accuracy:** ±1–2 mm (operator dependent)
- **Use case:** prototypes, low-volume production, field repairs
- **Safety:** full PPE required — respiratory protection, eye protection, gloves. Composite dust is hazardous.

### Trimming Best Practices

- Use a backing support or sacrificial layer to prevent delamination at the exit side of the cut
- Trim from the tool side (smooth surface) whenever possible
- Inspect cut edges for delamination, fraying, or fibre pull-out
- Deburr edges with fine abrasive — sharp edges are stress concentrations and handling hazards

## Non-Destructive Inspection (NDI)

Every structural composite part must be inspected to verify that the internal quality meets acceptance criteria.

### Ultrasonic Testing (UT)

The primary inspection method for composites:
- **Pulse-echo** — a single transducer sends and receives ultrasonic waves. Defects reflect the signal back before it reaches the back wall.
- **Through-transmission** — two transducers on opposite sides; defects attenuate the signal passing through. Requires access to both sides.
- **C-scan** — automated scanning over the part surface produces a 2D map of defect locations and sizes. The industry standard for production inspection.
- **Detects:** voids, porosity, delaminations, inclusions, dry spots

### Thermography

Infrared cameras detect heat flow anomalies:
- **Flash thermography** — a brief heat pulse is applied; defects cause local temperature differences
- **Advantages:** fast, non-contact, large area coverage
- **Detects:** delaminations, voids, disbonds, water ingress in sandwich structures

### Tap Testing

The simplest inspection method:
- Tap the surface with a coin or specialised tap hammer
- A solid laminate produces a sharp, clear sound
- A delaminated or void-rich area produces a dull, flat sound
- **Limitations:** operator-dependent, only detects near-surface defects, not quantitative
- **Use case:** quick screening, field inspection, incoming goods check

### X-Ray and Computed Tomography (CT)

- **X-ray:** reveals fibre orientation, voids, inclusions, and foreign objects
- **CT scanning:** 3D reconstruction of internal structure — the most detailed inspection method
- **Limitations:** expensive, slow, radiation safety requirements
- **Use case:** critical components, root cause analysis, R&D

## Assembly

Composite parts rarely exist in isolation — they are assembled into structures using mechanical fastening, bonding, or a combination.

### Mechanical Fastening

- **Drilling:** use specialised drill bits (brad point or dagger) designed for composites. Standard twist drills cause delamination.
- **Countersinking:** controlled depth is critical — over-countersinking damages the outer plies
- **Fastener installation:** titanium or stainless steel fasteners (no aluminium in contact with carbon fibre — galvanic corrosion)
- **Hole tolerance:** typically H9 for clearance fits; interference fits require reaming

### Adhesive Bonding

Three bonding strategies:

**Co-curing:** parts are cured together in a single autoclave cycle. Strongest bond, but requires all parts to be in the uncured state simultaneously. Complex tooling.

**Co-bonding:** one part is cured, the other is uncured. The adhesive (or the uncured prepreg itself) bonds them during the cure cycle of the uncured part. Good balance of strength and manufacturing flexibility.

**Secondary bonding:** both parts are fully cured; an adhesive film or paste bonds them in a separate operation. Most flexible, but requires careful surface preparation (abrasion, solvent wipe, primer).

### Surface Preparation for Bonding

- **Peel ply removal** creates a ready-to-bond surface (if the peel ply is compatible with the adhesive)
- **Abrasion** with Scotch-Brite or grit blasting removes contamination
- **Solvent wipe** with MEK or isopropanol removes oils and release agent residue
- **Bond within the open time** — surface preparation degrades with exposure to shop atmosphere (humidity, contaminants)

## Surface Finishing

- **Gel coat** — applied to the tool surface before layup; provides a smooth, paintable exterior (common in marine and automotive)
- **Primer and paint** — aerospace and automotive parts are primed and painted after trimming
- **Lightning strike protection (LSP)** — expanded copper or aluminium mesh embedded in the outer ply; required for aircraft composite structures exposed to lightning
- **UV protection** — composites degrade under UV exposure; paint or UV-resistant clear coat is essential for outdoor applications

## Key Takeaways

- CNC routing is the standard for precision trimming; waterjet for thick parts; laser for thin, non-structural trim
- Ultrasonic C-scan is the industry standard for production NDI of composites
- Drill composites with specialised bits — standard drill bits cause delamination
- Never use aluminium fasteners with carbon fibre — galvanic corrosion will occur
- Surface preparation is the single most important factor in bonded joint quality
- Always plan for inspection access during design — a part that cannot be inspected cannot be certified

## Further Reading / Tools

- [Common Defects](common-defects.md) — the defects that inspection is looking for
- [Material Excess and Boundaries](../02-design-rules/material-excess-and-boundaries.md) — why parts are cured oversize
- [Design for Manufacture](../02-design-rules/design-for-manufacture.md) — designing for post-processing access
- [Sandwich Structures](../04-structural-analysis/sandwich-structures.md) — NDI considerations for sandwich panels
