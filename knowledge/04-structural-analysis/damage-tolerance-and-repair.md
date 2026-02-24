---
title: "Damage Tolerance, Inspection, and Repair"
category: "analysis"
tags: ["damage-tolerance", "BVID", "CAI", "repair", "knockdown"]
difficulty: "advanced"
related: ["../01-fundamentals/failure-modes.md", "failure-criteria.md", "sandwich-structures.md"]
tools: []
last_updated: "2026-02"
---

# Damage Tolerance, Inspection, and Repair

Composite structures must not only carry design loads when new — they must carry them throughout their service life, even after sustaining damage from impacts, fatigue, moisture, or manufacturing defects. Damage tolerance is the design philosophy that ensures this.

## The Damage Tolerance Philosophy

Unlike metals, which yield visibly before fracturing, composites can sustain internal damage (delaminations, matrix cracks) with little or no visible indication on the surface. This makes damage tolerance both critical and challenging.

**Two design philosophies:**

**No-growth:** Design the structure so that damage below a detectable size will not grow under service loads. This is the dominant approach for composite aircraft structures. The damage must remain stable between inspection intervals.

**Slow-growth:** Allow damage to grow, but at a rate slow enough to be detected during scheduled inspections before it reaches a critical size. Less common for composites (more typical for metals with fatigue crack growth).

## Impact Damage Categories

| Category | Energy | Surface Indication | Internal Damage | Example |
|----------|--------|-------------------|-----------------|---------|
| **BVID** (Barely Visible Impact Damage) | Low–medium (typically 1–8 J/mm thickness) | Barely detectable dent (<0.5 mm deep) | Delamination, matrix cracks | Tool drop, hail, runway debris |
| **VID** (Visible Impact Damage) | Medium–high | Clearly visible dent or surface damage | Significant delamination, possible fibre breakage | Ground vehicle collision, bird strike |
| **Penetration** | High | Through-thickness hole | Complete local failure | Ballistic impact, severe hail |

BVID is the critical design case because it causes significant internal damage while being difficult to detect visually. The structure must carry limit loads with BVID present.

## Compression After Impact (CAI)

CAI is the key metric for damage-tolerant composite design. Impact damage (delaminations) creates local buckling instabilities that dramatically reduce compressive strength.

**Typical CAI knockdowns:**
- Undamaged compression strength: 600–800 MPa (for aerospace CFRP)
- After BVID impact: 200–350 MPa (a 50–70% reduction)
- This means the structure must be sized for the damaged strength, not the pristine strength

**Factors that improve CAI:**
- Toughened resin systems (thermoplastic-toughened epoxies)
- Stitched or z-pinned laminates (through-thickness reinforcement)
- ±45° outer plies (spread the impact over a wider area)
- Thicker laminates (higher impact energy to achieve the same damage level)

## Design for Inspectability

A damage-tolerant structure is only as good as the inspection programme that supports it:

- **Access:** every structural surface must be accessible for inspection (ultrasonic, visual, or thermographic)
- **Inspection interval:** the time between inspections determines the maximum allowable damage growth rate
- **Detectable damage size:** depends on the inspection method and access — typically 6 mm diameter (detailed visual) to 25 mm (general visual)
- **Inspection zones:** the structure is divided into zones based on damage susceptibility (high-traffic areas, hail-exposed surfaces, tool contact regions)

Design the structure so that all load-critical areas can be inspected using the planned inspection method. If an area cannot be inspected, it must be designed to sustain worst-case damage without inspection (higher knockdown factors).

## Knockdown Factors

Knockdown factors account for the difference between pristine material properties and the allowable strength used in design:

| Factor | Typical Value | What It Accounts For |
|--------|--------------|---------------------|
| **BVID** | 0.40–0.65 | Impact damage effect on compression |
| **Environment** (hot/wet) | 0.80–0.90 | Moisture absorption + elevated temperature |
| **Open hole** | 0.50–0.70 | Stress concentration from bolt holes |
| **Filled hole** | 0.65–0.80 | Bolt bearing + bypass loads |
| **Manufacturing variability** | 0.85–0.95 | Fibre volume, void content, ply alignment |

These factors are cumulative in the worst case. A hot/wet BVID-damaged bolted joint might use an effective knockdown of 0.40 × 0.85 × 0.70 = 0.24 — meaning only 24% of the pristine material strength is available for design. This is why composite structures can appear over-designed compared to metals.

## Repair Approaches

When damage is found, several repair options exist:

### Bonded Scarf Repair

The strongest permanent repair:
- Material around the damage is machined away in a tapered scarf (typically 1:20 to 1:50 taper ratio)
- New prepreg plies are laid into the scarf cavity, matching the original laminate orientations
- Cured under vacuum bag with a portable heat blanket or oven
- Restores 80–100% of original strength
- Requires skilled technicians and access to both sides

```
Original laminate:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           ↓ damage

Scarf repair:
━━━━━╲                  ╱━━━━━
      ╲  repair plies  ╱
       ╲              ╱
━━━━━━━╲            ╱━━━━━━━━
        ╲__________╱
         scarf taper
```

### Stepped Lap Repair

Similar to scarf but with discrete steps:
- Each ply is exposed by removing material in steps
- Repair plies are laid into each step
- Easier to machine than a smooth scarf
- Slightly lower strength recovery than scarf (stress concentration at each step)

### Bolted Doubler Repair

The simplest and fastest structural repair:
- A metal or composite patch is bolted over the damaged area
- No special surface preparation or cure cycle needed
- Adds weight and changes local stiffness
- Recovers 60–80% of original strength depending on design
- Common for field repairs and temporary fixes

### Resin Injection Repair

For small delaminations without fibre damage:
- Drill small holes into the delaminated region
- Inject low-viscosity resin under vacuum or pressure
- Cure at room temperature or with local heat
- Restores matrix continuity but not fibre continuity
- Use case: minor BVID, cosmetic delaminations

## Repair Design Considerations

- **Match the original laminate** — repair plies should match the original orientation, material, and stacking order as closely as possible
- **Overlap length** — bonded repair patches must extend beyond the damaged region by at least 25 mm on each side (more for primary structure)
- **Cure compatibility** — repair cure temperature must not damage the parent structure (especially for 120°C cure repairs on 180°C parent laminates)
- **Moisture** — the parent laminate must be dried before bonded repair (moisture causes porosity during cure)
- **Lightning strike** — if the repair area includes LSP mesh, the mesh continuity must be restored

## Key Takeaways

- BVID is the critical design case — significant internal damage with minimal surface indication
- CAI strength can be 50–70% lower than pristine compression strength — this drives composite sizing
- Design for inspectability: if you cannot inspect it, you must assume worst-case damage
- Knockdown factors are cumulative — hot/wet + BVID + open hole can leave only 20–30% of pristine strength
- Scarf repairs provide the best strength recovery (80–100%) but require skill and access
- Bolted doublers are the fastest field repair but add weight and reduce aerodynamic smoothness

## Further Reading / Tools

- [Failure Modes](../01-fundamentals/failure-modes.md) — delamination, matrix cracking, and BVID mechanisms
- [Failure Criteria](failure-criteria.md) — analytical methods for predicting composite failure
- [Sandwich Structures](sandwich-structures.md) — damage tolerance in sandwich panels (core crushing, face sheet disbond)
- [Buckling Basics](buckling-basics.md) — local buckling from delaminations
