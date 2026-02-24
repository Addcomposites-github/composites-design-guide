---
title: "Design for Manufacture"
category: "design-rules"
tags: ["manufacturability", "tooling", "ply-shape", "drape", "accessibility", "DFM"]
difficulty: "intermediate"
related: ["stacking-sequences.md", "ply-drop-offs.md", "zone-design.md", "splices-and-joints.md", "../03-manufacturing-processes/common-defects.md"]
tools: []
last_updated: "2026-02"
---

# Design for Manufacture

A laminate that looks perfect on paper can be impossible — or ruinously expensive — to actually build. Design for manufacture (DFM) means shaping your design decisions around the realities of the shop floor: material widths, tool access, draping limits, layup time, and inspection requirements. The best composites engineers think about manufacturing from the very first sketch.

## Why DFM Matters for Composites

Composites are uniquely sensitive to manufacturing quality. A metal part machined 0.5 mm off-nominal still works; a composite ply laid up with a wrinkle loses 30–50% of its compressive strength. The gap between "designed" and "as-built" performance is larger for composites than for any other structural material.

DFM reduces this gap by ensuring the designed part can be built consistently, with known quality, at acceptable cost.

## Ply Shape and Draping

Every ply starts as a flat sheet. That flat sheet must conform to a curved tool surface. The ability of a ply to follow a curved surface without wrinkling, bridging, or tearing is called **draping** (or drapability).

### Flat Surfaces and Single Curvature

Flat panels and gently curved surfaces (cylinders, cones) are easy. A flat sheet can wrap around a cylinder without any distortion. Single-curvature surfaces drape without issues for all fibre orientations.

### Double Curvature

Surfaces that curve in two directions simultaneously — like a car bonnet, a helmet, or a wing leading edge — are the challenge. A flat sheet cannot conform to a doubly curved surface without either stretching, compressing, or shearing. Fabric (woven) plies can shear to accommodate moderate double curvature. Unidirectional (UD) tape has almost no shear tolerance and will wrinkle or bridge on doubly curved surfaces.

```
Draping comparison:

    Single curvature (cylinder):     Double curvature (sphere):
    ┌─────────────────────┐          ╭─────────────────────╮
    │  ← flat sheet wraps │          │   ← flat sheet      │
    │     perfectly       │          │     must distort     │
    └─────────────────────┘          ╰─────────────────────╯

    UD tape: OK                      UD tape: wrinkles likely
    Woven fabric: OK                 Woven fabric: OK if curvature is moderate
```

### DFM Rules for Draping

1. **Use woven fabric on highly curved regions** — especially the first ply against the tool, which sees the most curvature.

2. **Dart or slit UD plies** on double curvature — cut relief slits (darts) into the ply edge so the material can spread or overlap to follow the surface. Each dart creates a small butt splice or overlap that must follow splice rules.

3. **Avoid 0° plies over tight convex curvature** — fibres under tension on a convex curve try to lift off the surface (bridging). Use a ply angle that runs along the curve rather than across it.

4. **Keep minimum bend radii in mind** — UD prepreg tape typically cannot follow inside radii tighter than about 3–6 mm without fibre buckling. Fabric handles tighter radii (down to ~2 mm).

## Tooling Considerations

The **tool** (or mould) is the surface the part is laid up on. Tool design directly constrains laminate design.

### Tool Surface Determines One Face of the Part

- **Outer mould line (OML) tool:** The tool defines the external surface. The inner surface varies with laminate thickness. Common for aerodynamic surfaces.
- **Inner mould line (IML) tool:** The tool defines the internal surface. The outer surface varies. Common for structural closeout surfaces.

**Design implication:** Ply drop-offs create steps. If the tool is OML, drops must be internal (the inner surface has steps). If the tool is IML, drops appear on the outer surface.

### Draft Angles

For parts that must be removed from a mould, the side walls need a slight angle (draft) to allow demoulding. Typical draft angles: 1–3° minimum. A vertical wall with 0° draft in a concave mould will trap the cured part.

### Thermal Expansion Mismatch

Tools expand when heated to cure temperature. If the tool material's thermal expansion differs significantly from the composite, the part will be the wrong size or have residual stresses.

| Tool material | Thermal expansion relative to CFRP | Notes |
|---|---|---|
| Invar (low-expansion steel) | Very close match | Expensive, used for precision aerospace parts |
| Steel | Moderate mismatch | Common, requires compensation |
| Aluminium | Large mismatch | Cheap for short runs; part will be undersized |
| Composite (CFRP tool) | Near-zero mismatch | Matched expansion; limited tool life |

## Minimum Ply Dimensions

Plies that are too small are difficult to handle, position accurately, and inspect:

- **Minimum ply width:** ~10 mm for manual layup, ~6.35 mm (1/4 inch) for AFP tow width
- **Minimum ply area:** Small isolated reinforcement patches (less than ~25 × 25 mm) are hard to position and hold in place. Consider extending the ply to a larger zone.
- **Very narrow plies** tend to shift during cure, especially under vacuum bag pressure. Anchor them with adjacent plies or use a wider ply instead.

## Layup Accessibility

The person or machine laying up the part must be able to physically reach every area of the tool:

- **Enclosed or deep channels** are difficult — reaching the bottom of a narrow C-channel to smooth a ply against the radius is impractical if the channel is deeper than an arm's length.
- **Interior corners (female radii)** tend to bridge — the ply spans across the corner rather than conforming to it. Use debulk cycles (intermediate vacuum compaction) to press plies into tight corners.
- **Long narrow features** (like hat stiffeners) require layup along the feature — consider pre-forming the plies on a separate mandrel and then co-bonding them to the skin.

```
Bridging in an interior corner:

    What happens:                 What you want:
    ┌──────────┐                  ┌──────────┐
    │          │                  │          │
    │    ╲     │ ← ply bridges   │    │     │ ← ply conforms
    │     ──── │   across        │    └──── │   to radius
    └──────────┘                  └──────────┘
```

## Debulk Cycles

**Debulking** is applying vacuum to the partially-completed layup — typically every 3 to 5 plies — to compact the plies, remove trapped air, and ensure conformance to the tool surface.

**When debulking is essential:**
- Thick laminates (more than ~15–20 plies)
- Parts with tight radii or deep features
- When using prepreg at room temperature (the tack makes plies resist conforming)

**Design implication:** Plan for debulk cycles in the manufacturing time estimate. A 60-ply laminate might need 10–15 debulks, each taking 15–30 minutes.

## Material Widths and Roll Planning

The width of your material roll determines where splices fall. Planning this up front avoids surprises:

- **Standard prepreg tape widths:** 75 mm, 150 mm, 300 mm, 600 mm
- **AFP tow widths:** 3.175 mm (1/8″), 6.35 mm (1/4″), 12.7 mm (1/2″)
- **Dry fabric rolls:** 1000–1500 mm typical

For a 2-metre-wide panel using 300 mm prepreg tape, you need at least 7 courses per ply — meaning at least 6 splices per ply. These must all be staggered per the [splice rules](splices-and-joints.md).

## Design Choices That Simplify Manufacturing

| Design choice | Manufacturing benefit |
|---|---|
| Use standard ply angles (0°, ±45°, 90°) | Easy to cut and orient, automated nesting is straightforward |
| Fewer zones with rounded-up thickness | Fewer ply boundaries, fewer drop-offs, faster layup |
| Constant-width ply shapes | Simpler nesting, less material waste |
| Symmetric layup | Part stays flat after cure — no costly shimming |
| Woven outer plies | Better surface quality, easier handling |
| Avoid joggles (steps in the tool) | Fewer bridging and wrinkle risks |
| Co-cure rather than co-bond when possible | Eliminates a bonding step and surface preparation |

## Design Choices That Complicate Manufacturing

| Design choice | Manufacturing consequence |
|---|---|
| Many ply angles beyond 0/±45/90 (e.g., ±30°, ±60°) | Custom cutting, harder to verify orientation, more scrap |
| Very tight radii (< 3 mm) | Bridging, fibre buckling, needs extra debulks |
| Highly tailored layups (many zones) | Long layup times, more inspection points |
| Large doubly curved parts with UD tape | Wrinkles, darts required, slower layup |
| Asymmetric laminates | Warping, need compensating tooling |

## Mirror and Symmetric Part Strategy

Many composite structures are symmetric about a plane — left and right wing skins, paired fuselage panels, mirror-image fairings. Rather than designing both independently, design one and mirror it.

**When to use mirroring:**
- The part geometry is symmetric about a plane (left/right, upper/lower)
- The laminate design is intended to be identical on both sides
- Shared tooling reduces manufacturing cost

**Associative vs non-associative mirror:**
- **Associative** — changes to the master part automatically propagate to the mirror. Preferred for production designs where the master evolves.
- **Non-associative** — a one-time copy. The mirror part is independent after creation. Use for parts that will diverge after the initial design.

**What gets mirrored correctly:**
- Ply contours and stacking order
- Fibre directions (+45° becomes -45° in the mirror — this is structurally correct)
- Reference surfaces and rosettes (axis systems are reflected)

**Manufacturing benefits:**
- Shared tooling (same tool, flipped) or mirrored tool halves the tooling cost
- Halved programming effort for AFP/ATL
- Consistent quality between left and right parts

**Verify after mirroring:** The mirrored stacking must still satisfy all design rules (symmetry, balance, 10%). A balanced laminate [+45/-45/0/90]s remains balanced after mirroring, but an unbalanced one will have its imbalance reversed.

## Key Takeaways

- Design for manufacture from the start — a laminate that cannot be built well is a bad laminate
- Draping limits determine whether UD tape or woven fabric is appropriate for curved regions
- Keep ply dimensions practical — nothing too small to handle or position
- Plan for debulk cycles in thick or complex layups
- Match your material width to the part geometry to control splice locations
- Minimise the number of zones and non-standard ply angles to reduce layup time and cost
- Ensure the tool design supports demoulding, thermal expansion, and layup accessibility

## Further Reading / Tools

- [Stacking Sequences](stacking-sequences.md) — the structural rules that DFM must satisfy
- [Ply Drop-offs](ply-drop-offs.md) — manufacturing constraints on ply terminations
- [Splices and Joints](splices-and-joints.md) — how material widths drive splice design
- [Zone Design](zone-design.md) — how zones translate structural needs into layup instructions
- [Common Defects](../03-manufacturing-processes/common-defects.md) — what goes wrong when DFM rules are ignored
