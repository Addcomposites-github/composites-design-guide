---
title: "Bonded Joints in Composite Structures"
category: "analysis"
tags: ["bonded joint", "adhesive", "scarf", "lap joint", "peel stress", "bond line"]
difficulty: "intermediate"
related: ["splices-and-joints.md", "bolted-joints.md", "failure-criteria.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Bonded Joints in Composite Structures

Adhesive bonding is the preferred joining method for many composite structures. It avoids drilling holes (which cut fibres and create stress concentrations), distributes load over a larger area, and produces smoother aerodynamic surfaces. However, bonded joints require careful design, surface preparation, and quality control — a weak bond can be invisible and catastrophic.

## Why Bond Composites?

- **No fibre cutting** — bolt holes reduce laminate strength by 40-60%; bonds preserve fibre continuity
- **Smooth load transfer** — shear stress distributes across the entire overlap area, not a single bolt
- **Weight savings** — no fastener weight, no local pad-ups, thinner laminates possible
- **Fatigue resistance** — bonded joints outperform bolted joints in fatigue for most configurations
- **Sealed joints** — no gap for moisture ingress or corrosion

## Joint Types

### Single Lap Joint

The simplest configuration: two adherends overlap and are bonded with adhesive. The eccentric load path creates bending (peel) stresses at the overlap ends.

- **Use for:** Low to moderate loads, secondary structure
- **Limitation:** Peel stresses at the overlap ends limit the load capacity
- **Typical overlap:** 30-50 times the thinner adherend thickness

### Double Lap Joint

A symmetric version of the single lap, with doublers on both sides. Eliminates the bending moment and peel stresses.

- **Use for:** Moderate to high loads, primary structure repairs
- **Advantage:** Higher strength than single lap (roughly 2x for the same overlap)
- **Limitation:** Requires access to both sides

### Scarf Joint

The adherends are tapered to a shallow angle and bonded along the tapered surface. The most efficient bonded joint for composites.

- **Scarf angle:** Typically 1:20 to 1:50 (3 degrees to 1.1 degrees)
- **Advantage:** Nearly uniform shear stress along the bond line; minimal peel
- **Use for:** Primary structure repairs, high-load joints
- **Limitation:** Requires precise machining of the scarf angle; long scarf lengths for thick laminates

### Stepped Lap Joint

A practical approximation of the scarf joint: each ply is stepped back to create a staircase pattern.

- **Use for:** Thick laminate repairs where a continuous scarf is impractical
- **Step length:** Typically 10-15 mm per ply step
- **Advantage:** Easier to manufacture than a true scarf; each step can be matched to a ply

## Stress Distribution in Bonded Joints

Adhesive stress in a lap joint is not uniform. Two types of stress dominate:

### Shear Stress

- Peaks at the overlap ends and is minimum in the centre
- The peak-to-average shear stress ratio depends on the stiffness ratio of the adherends and the adhesive
- Stiffer adherends or softer adhesive makes the distribution more uniform
- Volkersen's shear-lag model: tau(x) varies as cosh/sinh functions along the overlap

### Peel (Normal) Stress

- Acts perpendicular to the bond line, trying to pull the adherends apart
- Highest at the overlap ends of single lap joints
- Composites are weak in through-thickness tension (interlaminar tensile strength ~ 40-80 MPa)
- Peel stress is the most common cause of premature failure in bonded composite joints

## Design Rules

| Parameter | Guideline | Reasoning |
|-----------|-----------|-----------|
| Minimum overlap | 30t (single lap), 20t (double lap) | Ensures load is carried by shear, not peel |
| Maximum overlap | Beyond ~80t, no additional strength gain | Shear stress already near zero in the middle |
| Adhesive thickness | 0.1-0.3 mm | Too thin: voids and disbonds; too thick: low shear strength |
| Scarf angle | 1:20 to 1:50 | Shallower is better but requires more length |
| Surface preparation | Peel ply, abrade + solvent wipe, or plasma | Single most critical factor for bond quality |
| Operating temperature | Adhesive Tg minus 30 C | Bond strength drops rapidly near the glass transition temperature |

## Surface Preparation

Surface preparation is the single most important factor in bond quality. A poor surface can reduce joint strength by 80% or more.

### Methods (from least to most reliable)

1. **Solvent wipe only** — removes grease but does not activate the surface; unreliable
2. **Abrade + solvent wipe** — sanding with 180-320 grit, then acetone/IPA wipe; adequate for secondary structure
3. **Peel ply removal** — a nylon or polyester peel ply is co-cured with the laminate and peeled off before bonding; provides a consistently fresh, textured surface
4. **Plasma treatment** — atmospheric plasma activates the surface at a molecular level; highest and most consistent bond strengths
5. **Grit blast + primer** — used in aerospace; phosphoric acid anodising (PAA) or chromic acid etch followed by primer (BR-127 or equivalent)

### Critical Rules

- Bond within 24 hours of surface preparation (less for critical applications)
- Never touch the prepared surface with bare hands
- Store peel-plied surfaces in sealed bags if not bonding immediately
- Verify bond quality with witness coupons and/or NDI (ultrasonic, thermography)

## Adhesive Selection

| Adhesive Type | Shear Strength (MPa) | Peel Strength | Temperature Range | Notes |
|---------------|----------------------|---------------|-------------------|-------|
| Epoxy film (e.g. FM 300) | 30-45 | Good | -55 to 120 C | Aerospace standard, requires oven/autoclave cure |
| Epoxy paste (e.g. Hysol EA 9394) | 25-35 | Moderate | -55 to 80 C | Room-temperature cure, gap-filling |
| Methacrylate (e.g. Plexus) | 15-25 | Good | -40 to 80 C | Tolerant of poor surface prep, fast cure |
| Polyurethane | 10-20 | Excellent | -40 to 80 C | Flexible, good peel; lower shear strength |
| Cyanoacrylate | 15-25 | Poor | -30 to 80 C | Instant bond; brittle, poor durability |

## Failure Modes

1. **Cohesive failure** — crack propagates within the adhesive layer. This is the desired failure mode, as it means the bond was stronger than the adhesive itself.
2. **Adhesive failure** — the bond line separates from one adherend surface. Indicates poor surface preparation.
3. **Interlaminar failure** — the composite delaminates near the bond line. Indicates peel stress exceeded the laminate's interlaminar strength.
4. **Mixed mode** — combination of the above.

A good bonded joint should show 100% cohesive failure on destructive testing of witness coupons.

## Key Takeaways

- Bonded joints avoid fibre cutting and distribute load more evenly than bolted joints
- Peel stress at overlap ends is the primary failure driver — design to minimise it
- Surface preparation is the single most critical factor: abrade + clean, or use peel ply
- Scarf joints are the strongest configuration but require precise machining
- For single lap joints, overlap should be at least 30 times the thinner adherend thickness
- Always verify bond quality with witness coupons and NDI — a bad bond is invisible
- Adhesive thickness should be 0.1-0.3 mm; thicker bonds are weaker in shear

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) for checking interlaminar properties
- CMH-17 Volume 3, Chapter 13: Adhesive Bonded Joints
- knowledge/02-design-rules/splices-and-joints.md for splice design rules
- knowledge/04-structural-analysis/bolted-joints.md for mechanical fastening alternative
