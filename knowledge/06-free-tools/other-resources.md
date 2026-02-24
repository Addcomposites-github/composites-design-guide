---
title: "Other Free Composites Resources"
category: "tools"
tags: ["resources", "CMH-17", "ESDU", "databases", "open-source", "reference"]
difficulty: "beginner"
related: ["addstack.md", "elamx2.md", "compositesai.md"]
tools: []
last_updated: "2026-02"
---

# Other Free Composites Resources

Beyond the dedicated calculators covered in this section, there are numerous free resources for learning and practising composites design. This page collects the most useful ones — databases, reference documents, university tools, and learning materials.

## Standards and Reference Documents

### CMH-17 (Composite Materials Handbook)

CMH-17 (formerly MIL-HDBK-17) is the primary reference for composite material properties and design methodology in aerospace. It is a multi-volume handbook covering:
- Volume 1: Polymer matrix composites — guidelines for characterisation and testing
- Volume 2: Polymer matrix composites — design and analysis
- Volume 3: Polymer matrix composites — material properties (allowables database)
- Volume 4: Metal matrix composites
- Volume 5: Ceramic matrix composites
- Volume 6: Structural sandwich composites

**Access:** CMH-17 is administered by SAE International. The full handbook requires a subscription, but summary tables and selected data are available through various public sources. The methodology chapters (design guidelines, analysis approaches) are the most broadly useful for engineers without access to the full database.

### ESDU Data Sheets

ESDU (Engineering Sciences Data Unit) publishes engineering data sheets on a wide range of topics including composite design. Selected sheets on composite laminate analysis, buckling, and joint design are available through institutional subscriptions. Some universities provide free access.

### NASA Technical Reports

NASA's Technical Reports Server (NTRS) hosts thousands of free reports on composite materials, manufacturing, and structural analysis. Key historic reports include foundational work on:
- Laminate theory and failure prediction
- Composite panel buckling
- Damage tolerance methodology
- Bolted joint analysis in composites

Search NTRS for "composite" plus your topic of interest.

## Free Software Tools

### ABAQUS Student Edition

A free student edition of ABAQUS is available — a general-purpose finite element analysis (FEA) package widely used for composite structural analysis. The student edition has model-size limits but is sufficient for learning composite FEA modelling.

### OpenFOAM (for Resin Flow Simulation)

OpenFOAM is a free, open-source computational fluid dynamics (CFD) package. It can be configured to simulate resin flow in infusion processes. Requires significant CFD knowledge to set up, but is powerful for research and advanced manufacturing simulation.

### Python Libraries

Several open-source Python libraries exist for composites analysis:
- **composites** — basic CLT calculations
- **pynite** — structural analysis with composite beam elements
- Various individual scripts shared on GitHub for ABD matrix computation, failure analysis, and laminate optimisation

These are useful for scripting parametric studies, optimisation loops, or integrating CLT into larger analysis workflows.

## Learning Resources

### Textbooks (Selected Free or Low-Cost Options)

While comprehensive composites textbooks are expensive, several resources are freely available:

- **MIT OpenCourseWare** — mechanics of composite materials courses with lecture notes, problem sets, and solutions
- **University lecture notes** — many universities publish composites course notes freely. TU Delft, Stanford, and others have open-access materials
- **DoD Composite Materials Handbook** — the older MIL-HDBK-17 revisions are in the public domain and contain substantial design guidance

### Online Courses

Several platforms offer free or low-cost composites courses:
- edX and Coursera occasionally host composite materials courses from universities
- YouTube has extensive composites manufacturing and design video content — particularly useful for visual learners wanting to see manufacturing processes

## Material Databases

### Free Material Property Sources

Finding composite material properties without a CMH-17 subscription is a common challenge. These sources help:

- **Material supplier datasheets** — Hexcel, Toray, Solvay, and other prepreg manufacturers publish material datasheets with typical (not design-allowable) properties. These are adequate for preliminary sizing.
- **MatWeb** — a free online database with mechanical properties for thousands of materials including composite systems
- **AddStack material library** — [AddStack](https://addstack.addcomposites.com) includes a built-in material database with common fibre/resin combinations
- **Campus plastics database** — primarily for thermoplastics but includes some composite data

**Important distinction:** Datasheet "typical" values are mean properties. Design allowables (A-basis, B-basis) used for structural certification are statistically reduced values, typically 10–30% lower. Do not use typical values as design allowables for structural applications.

## Industry Organisations and Communities

- **SAMPE** (Society for the Advancement of Material and Process Engineering) — publishes technical papers and hosts conferences. Student memberships are affordable.
- **ICCM** (International Committee on Composite Materials) — organises the ICCM conference series
- **CompositesWorld** — online magazine with free articles on composites technology and industry news
- **r/composites** (Reddit) — active community forum for makers and engineers

## Key Takeaways

- CMH-17 is the definitive composite materials handbook; NASA technical reports are freely available and cover similar ground
- Material supplier datasheets provide free "typical" properties suitable for preliminary design — not for certification
- eLamX2 and AddStack are the best free CLT tools; ABAQUS student edition covers FEA
- MIT OpenCourseWare and university lecture notes provide free structured learning
- Python libraries allow scripting of CLT calculations for parametric studies

## Further Reading / Tools

- [AddStack — free laminate calculator](https://addstack.addcomposites.com) — built-in material database and CLT analysis
- [eLamX2](elamx2.md) — open-source CLT tool from TU Dresden
- [CompositesAI](compositesai.md) — composite beam cross-section analysis
- [Resin Flow Simulator — free infusion simulation](https://www.addcomposites.com/addcomposites-apps/resin-flow)
