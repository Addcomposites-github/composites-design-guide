---
title: "Bolted Joints in Composite Structures"
category: "analysis"
tags: ["bolted joint", "bearing", "bypass", "fastener", "net tension", "shear-out"]
difficulty: "intermediate"
related: ["splices-and-joints.md", "failure-criteria.md", "damage-tolerance-and-repair.md"]
tools: ["addstack"]
last_updated: "2026-02"
---

# Bolted Joints in Composite Structures

Bolted joints are the primary method for assembling composite structures in aerospace, automotive, and industrial applications. Unlike metals, composites do not yield — they are brittle, notch-sensitive, and anisotropic. This means composite bolted joints require different design rules and analysis methods than metallic joints.

## Why Composite Joints Are Different from Metal Joints

In a metal part, a bolt hole creates a stress concentration, but the material yields locally and redistributes the load. Composites cannot yield. The stress concentration at the hole remains, and failure is sudden. Three consequences follow:

1. **No load redistribution** — peak stresses at the hole drive failure directly
2. **Notch sensitivity** — open-hole and filled-hole tensile strengths are significantly lower than unnotched strengths (typically 40-60% of unnotched)
3. **Fibre orientation matters** — a laminate with mostly 0-degree plies will be strong in bearing but weak in net tension if loaded transversely

## Failure Modes

A bolted joint in composite can fail in four distinct modes. Good design ensures that all four have adequate margin simultaneously.

### 1. Bearing Failure

The bolt compresses the laminate at the hole edge. The laminate crushes locally.

- **Stress:** sigma_br = P / (d * t), where P is bolt load, d is hole diameter, t is laminate thickness
- **Design goal:** sigma_br < bearing allowable (typically 400-800 MPa for CFRP, depending on layup and bolt fit)
- **Improvement:** Increase laminate thickness locally, use interference-fit bolts, add more +-45 plies

### 2. Net-Tension Failure

The laminate tears across the minimum cross-section at the bolt hole row.

- **Stress:** sigma_nt = P / ((w - d) * t), where w is the specimen/joint width
- **Design goal:** sigma_nt < filled-hole tensile allowable
- **Improvement:** Increase w/d ratio (minimum 4, prefer 6), ensure adequate 0-degree plies in the load direction

### 3. Shear-Out (Tear-Out) Failure

The bolt pulls through the end of the laminate, shearing two planes along the load direction.

- **Stress:** tau_so = P / (2 * e * t), where e is edge distance (bolt centre to free edge)
- **Design goal:** tau_so < interlaminar shear allowable
- **Improvement:** Increase edge distance (minimum 3d, prefer 4d), add +-45 plies

### 4. Cleavage Failure

A combination of tension and shear that splits the laminate from the hole to the edge. Common in narrow specimens with small e/d ratios.

- **Prevention:** Maintain e/d >= 3 and w/d >= 4 simultaneously

## Geometric Design Rules

These rules come from decades of aerospace testing and are codified in CMH-17 and MIL-HDBK-17:

| Parameter | Minimum | Preferred | Notes |
|-----------|---------|-----------|-------|
| w/d (width-to-diameter) | 4.0 | 6.0 | Below 4, net tension dominates |
| e/d (edge distance-to-diameter) | 3.0 | 4.0 | Below 3, shear-out risk |
| d/t (diameter-to-thickness) | 0.5 | 1.0-2.0 | Optimal bearing at d/t ~ 1.0 |
| Pitch (multi-bolt spacing) | 4d | 5d | Prevents interaction between holes |
| Bolt-hole clearance | +0.1 mm | Interference fit | Interference improves fatigue life |

## Bearing-Bypass Interaction

In multi-fastener joints, each bolt carries some load (bearing) and the remaining load bypasses through the laminate to the next bolt. The interaction between bearing stress and bypass stress at each hole is critical.

- **All-bearing (bypass ratio = 0):** Single bolt in a lap joint — all load transfers through the bolt
- **All-bypass (bypass ratio = 1):** Open hole with no bolt — all load passes through the net section
- **Real joints:** Each fastener in a multi-bolt row has a bypass ratio between 0 and 1

The bearing-bypass interaction envelope is typically plotted as an elliptical failure surface. Designs must fall inside this envelope with adequate margin. CMH-17 Volume 3 Chapter 14 provides detailed methods.

## Laminate Design for Bolted Joints

Bolted regions need a specific laminate design that may differ from the surrounding structure:

- **Minimum 25% of each angle family** (0, +-45, 90) in the bolt region — this ensures quasi-isotropic or near-quasi-isotropic behaviour, which maximises bearing strength
- **No more than 40% of any single angle** — highly directional laminates are weak in bearing
- **Prefer hard laminates** (high percentage of 0 and 90 plies) for tension-loaded joints
- **Prefer soft laminates** (high percentage of +-45 plies) for shear-loaded joints
- **Local pad-ups** — add extra plies around bolt holes if the main laminate is too thin

## Multi-Bolt Joint Load Distribution

In a row of bolts connecting two parts, the load does not distribute equally. The outermost bolts carry more load due to the "spring analogy":

- Each bolt acts as a spring in parallel with the laminate
- Stiffer bolts (or thinner laminate) concentrate more load in the outer bolts
- Typical distribution for 3 bolts: ~40% / 20% / 40%
- Typical distribution for 5 bolts: ~30% / 15% / 10% / 15% / 30%

For critical joints, use a spring-analogy method or FEA to determine the actual load split.

## Bolt Installation Torque

Over-torquing composite bolts can crush the laminate. Under-torquing allows gap opening and fretting.

- **Torque range:** Follow the bolt manufacturer's specification for composite applications
- **Clamp-up force:** A small clamp-up force (finger-tight + 1/4 turn for aerospace) improves bearing strength by 10-30% by constraining delamination
- **Protruding vs. countersunk heads:** Protruding heads give higher bearing strength; countersunk heads reduce aerodynamic drag but weaken the laminate locally

## Key Takeaways

- Composite bolted joints fail by bearing, net-tension, shear-out, or cleavage — design must check all four
- Maintain w/d >= 4, e/d >= 3, and d/t between 0.5 and 2.0 as minimum geometric ratios
- Use quasi-isotropic or near-quasi-isotropic laminates in bolt regions (25% minimum of each angle family)
- In multi-bolt rows, outer fasteners carry the most load — do not assume equal distribution
- Bearing strength improves with bolt clamp-up, interference fit, and +-45 ply content
- Composite joints cannot yield to redistribute load — every failure mode must have positive margin

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) for checking laminate properties at bolt locations
- CMH-17 Volume 3, Chapter 14: Mechanically Fastened Joints
- MIL-HDBK-17-3F, Section 5: Bolted Joints
- knowledge/02-design-rules/splices-and-joints.md for general joint design principles
