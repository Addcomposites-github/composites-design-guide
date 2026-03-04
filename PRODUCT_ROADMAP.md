# Product Roadmap: Composites Design Platform
## From Open Knowledge Base to AI-Powered Composites Engineering Tool

**Version:** 1.1 — February 2026
**Owner:** AddComposites
**Vision:** Anyone with an idea for a composite part — from a maker with a photo to a startup
engineer with a napkin sketch — should be able to get a grounded, practical manufacturing
plan without needing $150k/year software or 20 years of aerospace experience.

---

## Table of Contents

1. [Where We Are Today](#1-where-we-are-today)
2. [The Opportunity](#2-the-opportunity)
3. [Open-Source Ecosystem to Integrate](#3-open-source-ecosystem-to-integrate)
4. [AddComposites Assets to Leverage](#4-addcomposites-assets-to-leverage)
5. [Product Phases](#5-product-phases)
   - [Phase 0: Foundation — Agent-Ready Knowledge Base](#phase-0-foundation--agent-ready-knowledge-base-now--3-months)
   - [Phase 1: MCP Server — Universal AI Access](#phase-1-mcp-server--universal-ai-access-months-1-3)
   - [Phase 2: Composites AI Agent — Photo to Plan](#phase-2-composites-ai-agent--photo-to-plan-months-3-8)
   - [Phase 3: Integrated Engineering Tools](#phase-3-integrated-engineering-tools-months-6-12)
   - [Phase 4: Marketplace and Ecosystem](#phase-4-marketplace-and-ecosystem-months-12-24)
6. [Business Model](#6-business-model)
7. [Technical Architecture](#7-technical-architecture)
8. [Competitive Landscape](#8-competitive-landscape)
9. [Risk Assessment](#9-risk-assessment)
10. [Key Open-Source Dependencies](#10-key-open-source-dependencies)

---

## 1. Where We Are Today

### Knowledge Base (This Repository)
- **54 markdown files, ~67,000 words** across 10 categories
- Covers fundamentals, design rules, manufacturing, analysis, CATIA workflows, free tools, glossary, cost estimation, case studies, applications
- **index.json** (289 KB) with full-text content for RAG retrieval
- **11 original SVG diagrams** for key concepts (laminate cross-sections, process schematics, failure envelopes)
- **3 decision tree JSON files** for guided AI reasoning (process, fibre, failure criteria selection)
- **MCP server** with 5 tools, 5 resources, 3 prompts — ready for npm publishing
- **Web app scaffold** — FastAPI backend + React frontend for photo-to-plan AI agent
- Structured with YAML front matter, tags, difficulty levels, cross-references
- Designed from the ground up for LLM consumption (100-400 word chunks per section)
- License: CC BY 4.0 (content) + MIT (code) — free forever

### AddComposites Free Tools Already Live
| Tool | URL | What It Does |
|------|-----|--------------|
| **AddStack** | addstack.addcomposites.com | CLT calculator, ABD matrices, failure criteria (Tsai-Wu, Hashin, max stress), material database |
| **Resin Flow Simulator** | addcomposites.com/addcomposites-apps/resin-flow | VARTM infusion simulation, flow front prediction |
| **CRDS** | addcomposites.com/addcomposites-apps/crds | Composite rotor/sleeve design, hoop stress, burst pressure, filament winding angle optimization |

### AddComposites Commercial Products
| Product | What It Is | Pricing Model |
|---------|-----------|---------------|
| **AFP-XS** | Compact AFP head for standard industrial robots | Purchase or lease (€2-3k/month) |
| **AFP-X** | Multi-tow production AFP system | Custom pricing |
| **AddPath** | AFP path planning, simulation, digital twin | Free trial license available, subscription |

### What's Missing
The knowledge base exists. The tools exist. The hardware exists. What's missing is the
**intelligent orchestration layer** that connects a user's intent to the right knowledge,
the right calculations, and the right manufacturing path — automatically.

---

## 2. The Opportunity

### The Problem (quantified)
- **99% of people** interested in composites cannot access the tools and knowledge that
  aerospace OEMs use daily
- Enterprise composites software costs **$15k–$150k/year per seat** (Fibersim, CATIA
  Composites, ANSYS ACP, HyperSizer, VERICUT Composite)
- Traditional AFP systems cost **$2–10M** (Electroimpact, Coriolis, Automated Dynamics)
- Composites knowledge is locked in:
  - Senior engineers' heads (not searchable, not scalable)
  - Internal design manuals at Boeing/Airbus (proprietary)
  - CMH-17 handbook (3,000+ pages, expensive subscription)
  - Enterprise software documentation (not public)

### Who Needs This (user segments, prioritized)

**Segment 1: Makers and Enthusiasts** (largest volume, lowest ARPU)
- Building carbon fibre parts for cars, bikes, drones, furniture, sporting goods
- Zero composites background, learn from YouTube and trial-and-error
- Need: "I have a photo of what I want to build. What do I need? How much will it cost?"
- Willingness to pay: $0–$20/project

**Segment 2: Startup Engineers** (high growth, medium ARPU)
- eVTOL, drone, EV, marine, renewable energy startups
- Some engineering background but no composites specialist on staff
- Need: "Design a laminate for this load case, check failure, plan manufacturing"
- Willingness to pay: $50–$500/month for tools

**Segment 3: Small/Medium Manufacturers** (Tier 2/3 suppliers) (medium volume, high ARPU)
- Making composite parts for larger OEMs
- Have shop floor capability but lack design/analysis software
- Need: "Automate our design-to-manufacturing workflow without Fibersim"
- Willingness to pay: $500–$5,000/month for integrated tools

**Segment 4: Universities and Research Labs** (brand building, pipeline)
- Teaching composites courses, running AFP research
- Need: Free/affordable tools for education, research-grade simulation
- Willingness to pay: $0–$2,000/year (educational pricing)

### Why Now
1. **Multi-modal AI is mature**: Claude, GPT-4o, Gemini can all analyze photos and reason
   about engineering problems with high reliability
2. **MCP protocol is standardized**: One server makes the knowledge base accessible to
   every major AI assistant simultaneously
3. **Open-source composites tools have reached critical mass**: Enough Python libraries
   and FEA tools exist to build real engineering pipelines
4. **AddComposites has the trust**: Active blog, AFP-XS installations at universities
   worldwide, free tools already in use — the brand is established in the community
5. **No competitor has done this**: Zero products combine "composites knowledge base +
   AI agent + calculation tools + manufacturing planning" in one place

---

## 3. Open-Source Ecosystem to Integrate

### Python CLT / Laminate Analysis Libraries

| Library | GitHub | Features | Integration Value |
|---------|--------|----------|-------------------|
| **composipy** | rafaelpsilva07/composipy | CLT, stress/strain, plate buckling, lamination parameter optimization. Pip installable, NumPy/SciPy based | High — wrap as MCP tool for server-side calculations |
| **lamipy** | joaopbernhardt/lamipy | CLT, Tsai-Wu/Hashin/Max Stress/Max Strain failure criteria, progressive failure (ply discount) | Medium — failure criteria breadth, but not fully validated |
| **Classical-CLT-Calculator** | AJJLagerweij/Classical-Composite-Laminate-Theory-Calculator | Full ABD matrix, documented | Medium — good reference implementation |
| **ICLC** | FranciSessa/ICLC | Interactive CLT with Tkinter GUI, thickness optimization | Low — GUI-focused, less API-friendly |
| **lamprop** | rsmith-nl/lamprop | Laminate properties calculator, lightweight | Medium — simple, well-tested |
| **bjsfm** | BYU-composites/bjsfm | Bolted joint stress field model | High — fills a gap (no other free bolted joint tool) |

### Open-Source FEA with Composites Capability

| Tool | What It Does | Composites Capability |
|------|-------------|----------------------|
| **CalculiX** | General-purpose FEA (ABAQUS input format) | Shell elements with composite layup, coupled with NASA MAC/GMC for micromechanics |
| **OpenRadioss** | Explicit dynamics FEA (Altair open-sourced) | Composite material models, impact/crash simulation, progressive damage |
| **Elmer FEM** | Multi-physics FEA | Basic composite material definition, thermal analysis |
| **FEniCS / FEniCSx** | Python-based FEA framework | Programmable — can implement custom composite models |
| **Code_Aster** | General-purpose FEA (French nuclear industry heritage) | Composite plate/shell elements, progressive damage |

### Specialized Composites Tools

| Tool | Source | What It Does |
|------|--------|-------------|
| **cdmHUB** | cdmhub.org (Purdue) | Cloud-based composites simulation hub, hosts multiple tools |
| **ABAQUS-VABS GUI** | cdmHUB open source | Cross-sectional analysis for composite beams |
| **ANSYS-SwiftComp GUI** | cdmHUB open source | Micromechanics analysis interface |
| **CompositesAI** | compositesai.com | AI-assisted rotor blade / composite structure design (free tier) |
| **CADEC-Online** | cadec-online.com | WVU laminate analysis, material property database |
| **eLamX2** | TU Dresden | Desktop CLT with Puck/Hashin criteria, buckling, hygrothermal |
| **b3p** | GitHub | Wind turbine blade parametric modelling |
| **Hashin_3D_UMAT** | GitHub | ABAQUS subroutine for 3D Hashin progressive damage |

### AI/ML Frameworks for Building the Agent

| Framework | Stars | Best For | Our Use Case |
|-----------|-------|----------|-------------|
| **LangChain** | 127k | RAG pipelines, tool integration | Primary RAG + tool-calling framework |
| **LlamaIndex** | ~40k | Data ingestion, knowledge serving | Alternative RAG framework, strong on structured data |
| **CrewAI** | 44k | Role-based multi-agent teams | Specialist agents (materials, manufacturing, analysis) |
| **AutoGen** (Microsoft) | 55k | Multi-agent conversation | Complex collaborative workflows |
| **LangGraph** | ~10k | Stateful workflows, human-in-the-loop | Engineering review workflows with approval steps |
| **Chroma** | ~16k | Vector database | Embedding storage for semantic search |
| **Qdrant** | ~22k | Vector database | Production-grade alternative to Chroma |

### 3D/CAD Open Source

| Tool | What It Does | Integration Path |
|------|-------------|-----------------|
| **FreeCAD** | Parametric 3D CAD (Python scriptable) | Agent generates FreeCAD scripts from user descriptions |
| **Blender** | 3D modelling (has MCP server already) | Agent creates surface models via Blender MCP |
| **Meshroom/AliceVision** | Photogrammetry — multi-photo to 3D mesh | Photo-to-geometry pipeline |
| **OpenCascade (OCCT)** | CAD kernel (used by FreeCAD) | Programmatic geometry creation |
| **CadQuery** | Python parametric CAD (built on OCCT) | Most natural for agent-generated geometry |

---

## 4. AddComposites Assets to Leverage

### Free Tools (top-of-funnel, brand building)
1. **AddStack** — Already the most accessible CLT calculator. Wrap as API/MCP tool.
2. **Resin Flow Simulator** — Unique free offering. Integrate into manufacturing planning.
3. **CRDS** — Niche but valuable for cylindrical composites (motors, pressure vessels, flywheels).

### Commercial Tools (monetization, upsell)
1. **AddPath** — AFP path planning. Free trial → paid subscription. The agent recommends
   AFP manufacturing → user tries AddPath → conversion.
2. **AFP-XS** — Hardware. The agent's manufacturing plan says "AFP recommended" → user
   explores AFP-XS leasing options.

### Content Assets
1. **Blog** — Extensive technical blog covering AFP, composites manufacturing, sustainability,
   case studies. Can be ingested into the knowledge base as additional RAG content.
2. **This knowledge base** — 40,000 words of structured, RAG-optimized composites knowledge.
3. **CATIA documentation mirror** — 165 pages of CATIA V5 composites workflows (already
   distilled into original content in the repo).

### Brand and Community
- AFP-XS installations at universities worldwide
- Projecting 200+ installations by 2026
- Effman partnership for turnkey manufacturing cells at 1/5th traditional cost
- CompositesWorld coverage, industry recognition
- Active community of makers, researchers, and engineers using the free tools

---

## 5. Product Phases

---

### Phase 0: Foundation — Agent-Ready Knowledge Base (NOW – 3 months)

**Goal:** Make the knowledge base the single best composites reference that any AI agent
can access. Expand content, add structured data, prepare for tool integration.

#### 0.1 Knowledge Base Completion
- [x] 39 files, ~40,000 words (DONE)
- [x] index.json with full-text content (DONE)
- [x] YAML front matter on every file (DONE)
- [x] **Add structured data tables** — fibre property comparison table, resin comparison table, failure criteria selection table, common laminate families table added to key knowledge pages
- [x] **Add filament winding page** (`knowledge/03-manufacturing-processes/filament-winding.md`)
  - Winding patterns (hoop, helical, polar), wet vs dry winding, mandrel design
  - Geodesic vs non-geodesic paths, dome design, Clairaut equation
  - Cost comparison with AFP, defect catalogue, CRDS tool integration
- [x] **Add cost estimation section** (`knowledge/08-cost-estimation/`)
  - `material-costs.md` — fibre, resin, prepreg, consumables pricing with tables
  - `process-costs.md` — labour rates, equipment costs, cost-vs-volume curves
  - `tooling-costs.md` — mould material selection, cost by volume, mandrel costs
- [x] **Add case studies section** (`knowledge/09-case-studies/`)
  - `bicycle-fork.md` — full walkthrough: load analysis → laminate design → manufacturing
  - `drone-arm.md` — lightweight structural member design
  - `car-body-panel.md` — large cosmetic + structural panel
  - `pressure-vessel.md` — filament wound, CRDS-relevant
- [x] **Cost estimation data** — completed in `knowledge/08-cost-estimation/` (see above)
- [x] **Enhance process selection content** — added Mermaid decision trees to all 8 manufacturing process pages, plus a master `process-selection-guide.md`

#### 0.2 Diagram Creation
- [x] Create SVG diagrams for the top 10 most-viewed concepts (all in `diagrams/svg/`):
  1. ~~Symmetric laminate cross-section~~ `symmetric-laminate-cross-section.svg`
  2. ~~Ply drop-off with ramp ratio~~ `ply-drop-off-ramp-ratio.svg`
  3. ~~Manufacturing process comparison flowchart~~ `manufacturing-process-flowchart.svg`
  4. ~~Failure envelope (Tsai-Wu)~~ `failure-envelope-tsai-wu.svg`
  5. ~~Sandwich structure anatomy~~ `sandwich-structure-anatomy.svg`
  6. ~~Vacuum bagging setup~~ `vacuum-bagging-setup.svg`
  7. ~~Resin infusion schematic~~ `resin-infusion-schematic.svg`
  8. ~~AFP/ATL tow placement illustration~~ `afp-tow-placement.svg`
  9. ~~Zone map example~~ `zone-map-example.svg`
  10. ~~Splice types comparison~~ `splice-types-comparison.svg`
  11. ~~Filament winding patterns~~ `filament-winding-patterns.svg` (bonus)

#### 0.3 Blog Content Ingestion
- [ ] Identify top 20 AddComposites blog posts with unique technical content
- [ ] Extract key technical information (in original words) into new knowledge pages
  or expansions of existing pages
- [x] Add `knowledge/10-applications/` section covering:
  - `evtol-composites.md` — eVTOL airframe design considerations
  - `automotive-lightweighting.md` — EV body panels, battery enclosures
  - `wind-energy-blades.md` — blade design, scaling, manufacturing
  - `sporting-goods.md` — bikes, tennis rackets, golf shafts, skis

#### 0.4 Structured Material Database
- [x] Create `data/materials.json` — 15 material systems with full properties (E1, E2, G12, nu12, Xt, Xc, Yt, Yc, S, density, cost, process compatibility)
- [x] Create `data/processes.json` — 10 manufacturing processes with capability matrices, cost models, geometry compatibility, and quality classes

**Deliverable:** A knowledge base that is not just prose but also contains structured,
machine-queryable data tables that an AI agent can use for calculations and recommendations.

---

### Phase 1: MCP Server — Universal AI Access (Months 1-3)

**Goal:** Build an MCP server so that any AI assistant (Claude, ChatGPT via plugins, Cursor,
VS Code Copilot, custom apps) can access the composites knowledge base and run calculations.

#### 1.1 Core MCP Server (`composites-mcp-server`)

**Resources exposed:**
```
composites://knowledge/{category}/{filename}  → Individual knowledge pages
composites://index                             → Full search index
composites://materials                         → Material property database
composites://processes                         → Process capability matrix
```

**Tools exposed:**

| Tool | Input | Output | Backend |
|------|-------|--------|---------|
| `search_composites` | Natural language query | Top 5 matching knowledge chunks with citations | Semantic search over index.json |
| `get_material_properties` | Material name or type | Full property table (E1, E2, strengths, cost) | materials.json lookup |
| `calculate_laminate` | Layup sequence + material | ABD matrix, effective moduli, thermal coefficients | composipy or AddStack API |
| `check_failure` | Layup + material + loads | Failure index per criterion (Tsai-Wu, Hashin, Max Stress) | composipy or AddStack API |
| `check_stacking_rules` | Layup sequence | Pass/fail for symmetry, balance, 10% rule, consecutive ply limit | Custom rule engine |
| `recommend_process` | Part description (size, volume, performance class, geometry) | Ranked manufacturing processes with rationale (includes filament winding for axisymmetric parts) | Decision tree from knowledge base |
| `estimate_cost` | Part size, process, material, volume | Cost breakdown (material, labour, tooling, overhead) | Parametric model from cost-data |
| `get_design_rules` | Topic (e.g., "ply drop-offs") | Relevant design rules with explanations | Knowledge base retrieval |

**Prompts exposed:**
```
composites://prompts/design-review     → "Review this laminate for a {application}"
composites://prompts/process-selection → "Help me choose a manufacturing process for..."
composites://prompts/failure-analysis  → "Analyze this composite failure..."
composites://prompts/photo-to-plan    → "I want to build this part in composites..."
```

#### 1.2 AddStack API Integration
- [ ] If AddStack has an API: wrap it as an MCP tool for CLT calculations
- [ ] If AddStack is browser-only: use composipy as the backend, validate against AddStack
- [ ] Long term: build a proper REST API for AddStack that the MCP server calls

#### 1.3 Publishing and Distribution
- [x] Prepare package.json for npm publishing (author, repository, keywords, engines, files, prepublishOnly)
- [x] Create comprehensive README.md with install instructions for Claude Desktop, Claude Code, VS Code, Cursor, Windsurf
- [x] Create `.npmignore` for clean package distribution
- [x] Create Claude Desktop configuration snippet (`npx -y composites-mcp-server`)
- [x] Write `SETUP_GUIDE.md` — "Add composites engineering to your AI assistant in 2 minutes"
- [ ] Publish to npm registry (`npm publish`)
- [ ] Register on the MCP server directory (mcp.so)
- [ ] Add to the Anthropic MCP servers list (github.com/modelcontextprotocol/servers)

#### 1.4 Agent-Friendly Knowledge Enhancement
- [x] Add `llm-instructions.md` to repo root — tells any LLM how to use this knowledge base
- [x] Add structured "decision tree" files that agents can follow step-by-step:
  - `decision-trees/process-selection.json`
  - `decision-trees/fibre-selection.json`
  - `decision-trees/failure-criteria-selection.json`

**Deliverable:** `composites-mcp-server` published and installable. Any Claude Desktop /
Cursor / VS Code user can `npm install composites-mcp-server` and immediately get
composites engineering assistance in their AI tool of choice.

**Impact:** Instant penetration to every sector where engineers use AI coding assistants —
aerospace, automotive, marine, sporting goods, construction, energy. The knowledge base
becomes a "skill" that any agent can pick up.

---

### Phase 2: Composites AI Agent — Photo to Plan (Months 3-8)

**Status:** Web app scaffold built — FastAPI backend + React/Vite/Tailwind frontend

**Goal:** Build the flagship product — a user uploads a photo (or describes) a part they
want to make in composites, and the AI agent produces a complete, grounded manufacturing
plan.

#### 2.0 Web Application (IN PROGRESS)
- [x] **FastAPI backend** (`web-app/backend/`) — API routes for analysis, materials, processes, cost, knowledge search
  - Knowledge service (TF-IDF search ported from MCP server TypeScript)
  - Material service (materials.json query engine)
  - Process service (recommendation engine ported from MCP server)
  - Cost service (parametric estimation ported from MCP server)
  - Stacking service (rule checks ported from MCP server)
  - Vision service (Claude API integration for photo analysis)
  - Report service (markdown + PDF report generation)
- [x] **React frontend** (`web-app/frontend/`) — Vite + TypeScript + TailwindCSS
  - Photo upload with drag-and-drop
  - Analysis form (part description, intended use, skill level)
  - Results display with collapsible sections
  - Stacking sequence visualizer (colour-coded plies)
  - Cost breakdown chart
  - Process recommendation cards
  - Material property cards
  - Download report button
- [ ] Wire up frontend to backend (API integration)
- [ ] End-to-end testing with real part scenarios
- [ ] Deploy to Vercel (frontend) + Railway/Fly.io (backend)

#### 2.1 The Core User Flow

```
USER JOURNEY:
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  1. USER INPUT                                                          │
│     📷 Photo of desired part                                            │
│     OR ✏️ Text description ("I want to make a carbon fibre bike fork")  │
│     OR 📐 Sketch/drawing upload                                        │
│                                                                         │
│  2. AI ANALYSIS                                                         │
│     🔍 Identify part geometry, size, application context                │
│     📊 Estimate structural requirements (loads, environment)            │
│     🏗️ Classify complexity (simple flat panel → complex 3D shape)      │
│                                                                         │
│  3. DESIGN RECOMMENDATIONS                                              │
│     🧵 Fibre type selection (carbon/glass/aramid) with reasoning        │
│     🧪 Resin system recommendation with reasoning                       │
│     📋 Preliminary layup schedule (orientations, ply count)             │
│     ✅ Stacking rule compliance check                                   │
│     ⚠️ DFM warnings (minimum radius, draft angles, accessibility)      │
│                                                                         │
│  4. MANUFACTURING PLAN                                                  │
│     🏭 Process recommendation (wet layup / vacuum bag / infusion /     │
│        prepreg / AFP) with reasoning                                    │
│     📦 Bill of materials (fibre, resin, consumables, quantities)       │
│     🛠️ Tooling requirements (mould material, complexity)               │
│     📝 Step-by-step manufacturing procedure                            │
│                                                                         │
│  5. COST ESTIMATE                                                       │
│     💰 Material cost breakdown                                          │
│     👷 Labour estimate (hours × rate)                                   │
│     🔧 Tooling cost (one-time)                                         │
│     📊 Total per-part cost at 1, 10, 100, 1000 units                  │
│     📈 Where AFP-XS becomes economical (if applicable)                 │
│                                                                         │
│  6. RISK ASSESSMENT                                                     │
│     ⚠️ Key failure modes for this design                               │
│     🔍 Critical inspection points                                       │
│     🛡️ Design margins and safety factors                               │
│     📋 "Things that could go wrong" checklist                          │
│                                                                         │
│  7. SHAREABLE OUTPUT                                                    │
│     📄 PDF report (or markdown) that can be shared with a              │
│        manufacturer, mentor, or team for review                         │
│     🔗 Links to relevant AddStack calculations to verify               │
│     📚 References to knowledge base pages for deeper learning          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### 2.2 Technical Architecture

```
                    ┌──────────────────┐
                    │   Web Frontend   │
                    │   (React/Svelte) │
                    └───────┬──────────┘
                            │
                    ┌───────▼──────────┐
                    │   API Gateway    │
                    │   (FastAPI)      │
                    └───────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
     ┌────────▼───┐  ┌─────▼─────┐  ┌───▼──────────┐
     │  Vision    │  │   RAG     │  │  Calculation │
     │  Analysis  │  │  Engine   │  │  Engine      │
     │  (Claude/  │  │(LlamaIdx/ │  │ (composipy/  │
     │   GPT-4V)  │  │ LangChain)│  │  AddStack)   │
     └────────────┘  └─────┬─────┘  └──────────────┘
                           │
                    ┌──────▼──────┐
                    │  Knowledge  │
                    │  Base       │
                    │  (this repo │
                    │  + vectors) │
                    └─────────────┘
```

**Option A — Single-agent (simpler, ship faster):**
- One LLM call with tools (MCP server from Phase 1)
- The LLM orchestrates: vision analysis → knowledge retrieval → calculations → output
- Works well for Claude and GPT-4o which handle multi-step tool use

**Option B — Multi-agent (more capable, more complex):**
Using CrewAI or AutoGen:
- **Geometry Agent**: Analyzes photo/description, estimates dimensions and curvature
- **Materials Agent**: Selects fibre/resin system based on requirements
- **Design Agent**: Creates laminate schedule, checks stacking rules
- **Manufacturing Agent**: Selects process, creates step-by-step plan
- **Cost Agent**: Estimates costs at different volumes
- **Quality Agent**: Identifies risks, inspection points, failure modes

**Recommendation:** Start with Option A (single agent + MCP tools). Move to Option B
when the single agent hits quality limits.

#### 2.3 Key Features to Build

**2.3.1 Photo Analysis Module**
- Accept photos of: existing parts, sketches, CAD screenshots, similar products
- Extract: approximate geometry, curvature, size (with reference objects or user input)
- Classify: structural vs cosmetic, load-bearing vs fairing, flat vs curved vs complex
- Output: structured JSON with geometry parameters for downstream tools

**2.3.2 Laminate Design Module**
- Input: geometry classification + structural requirements + environment
- Processing:
  1. Select fibre type from decision tree (knowledge base)
  2. Select resin system from decision tree (knowledge base)
  3. Generate initial layup using the 10% rule + quasi-isotropic starting point
  4. Check against failure criteria (composipy or AddStack)
  5. Iterate if needed (add plies, change orientations)
  6. Validate stacking rules (symmetry, balance, consecutive ply limit)
- Output: layup schedule with rationale for each decision

**2.3.3 Manufacturing Process Selector**
- Input: part size, volume, performance class, budget, available equipment
- Decision logic: encoded from knowledge base process pages
- Output: ranked process list with pros/cons/cost implications
- Upsell hook: when AFP is recommended, link to AddPath trial and AFP-XS leasing

**2.3.4 Cost Estimator**
- Parametric model based on:
  - Material: cost/kg × weight (fibre + resin + consumables)
  - Labour: hours × rate (varies by process: hand layup ~4-8 hrs/kg, AFP ~1-2 hrs/kg)
  - Tooling: one-time cost amortized over volume
  - Equipment: hourly rate for autoclave, oven, vacuum pump, AFP system
  - Overhead: facility, utilities, quality, scrap factor
- Output: cost breakdown table + cost-vs-volume chart showing where automation pays off

**2.3.5 Report Generator**
- Generates a professional PDF/markdown report with:
  - Part description and requirements
  - Recommended laminate schedule (table format)
  - Manufacturing process and step-by-step procedure
  - Bill of materials with costs
  - Risk assessment and inspection checklist
  - References to knowledge base pages
  - "Verified with AddStack" badge where calculations were run
- Shareable: user can email the PDF to a manufacturer for quoting

#### 2.4 Data Flows

```
Photo/Description
    │
    ▼
┌─────────────────┐     ┌────────────────────┐
│ Vision Analysis  │────▶│ Geometry Parameters │
└─────────────────┘     └────────┬───────────┘
                                 │
                                 ▼
┌─────────────────┐     ┌────────────────────┐
│ Knowledge Base   │────▶│ Material Selection  │
│ (fibre-types.md, │     │ + Resin Selection   │
│  resin-systems)  │     └────────┬───────────┘
└─────────────────┘              │
                                 ▼
┌─────────────────┐     ┌────────────────────┐
│ Design Rules     │────▶│ Laminate Schedule   │
│ (stacking-seq,   │     │ + Stacking Checks   │
│  ply-drop-offs)  │     └────────┬───────────┘
└─────────────────┘              │
                                 ▼
┌─────────────────┐     ┌────────────────────┐
│ composipy /      │────▶│ Failure Analysis    │
│ AddStack         │     │ + Iteration         │
└─────────────────┘     └────────┬───────────┘
                                 │
                                 ▼
┌─────────────────┐     ┌────────────────────┐
│ Manufacturing    │────▶│ Process Selection   │
│ Knowledge        │     │ + Step-by-Step Plan │
│ (wet-layup.md,   │     └────────┬───────────┘
│  vacuum-bag...)   │             │
└─────────────────┘              ▼
                        ┌────────────────────┐
┌─────────────────┐     │ Cost Estimate       │
│ Cost Data        │────▶│ + Risk Assessment   │
│ (material-costs, │     └────────┬───────────┘
│  process-costs)  │             │
└─────────────────┘              ▼
                        ┌────────────────────┐
                        │ Shareable Report    │
                        │ (PDF / Markdown)    │
                        └────────────────────┘
```

---

### Phase 3: Integrated Engineering Tools (Months 6-12)

**Goal:** Go beyond recommendations into actual engineering — wrap open-source tools so
users can do real analysis without $50k/year software.

#### 3.1 Web-Based Laminate Designer
- Visual laminate builder: drag plies, set orientations, see ABD matrix update in real-time
- Built on composipy backend, modern web frontend
- Features:
  - Ply-by-ply stacking sequence editor
  - Real-time failure criterion calculation (Tsai-Wu, Hashin, Max Stress, Puck)
  - Automatic stacking rule checking (symmetric, balanced, 10% rule)
  - Polar stiffness plots
  - Export to PDF, CSV, JSON
- **This is AddStack 2.0** — a major upgrade to the existing free tool

#### 3.2 Process Simulation Integration
- **Resin Flow**: Enhanced version of existing simulator with AI-recommended inlet/vent placement
- **Draping Simulation**: Wrap an open-source kinematic draping model (or build one based on
  knowledge base producibility analysis concepts)
- **Cure Cycle**: Basic cure simulation for common resin systems (degree of cure vs time/temp)

#### 3.3 Bolted Joint Analysis
- Wrap bjsfm (BYU bolted joint stress field model) as web tool
- Input: hole pattern, laminate schedule, bolt loads
- Output: bearing/bypass stress ratios, failure prediction
- Fills a major gap — no free bolted joint analysis tool exists today

#### 3.4 Sandwich Panel Designer
- Web tool for sandwich structure design
- Core material selection (honeycomb types, foams by density)
- Face sheet laminate design
- Wrinkling, dimpling, core crush checks
- Weight optimization (core thickness vs face sheet thickness trade-off)

#### 3.5 AFP Path Planning Preview
- Lightweight web-based visualization of AFP paths on simple geometries
- Shows tow gaps, overlaps, steering radii
- Demonstrates the value of AddPath — serves as upsell gateway
- "Want to do this on your actual part? Try AddPath free for 30 days"

#### 3.6 FEA Lite — Cloud-Based Composites Analysis
- Wrap CalculiX or OpenRadioss in a serverless backend
- Simple geometry input (flat panel, cylinder, curved panel)
- Apply loads and boundary conditions via web UI
- Run composite-specific analysis: buckling, failure, impact
- **This is the most ambitious tool** — defer to later in Phase 3

---

### Phase 4: Marketplace and Ecosystem (Months 12-24)

**Goal:** Connect the design tool to the manufacturing ecosystem. The AI agent's output
(manufacturing plan, BOM, layup schedule) becomes a "request for quote" that goes to
qualified manufacturers.

#### 4.1 Manufacturing Marketplace
- Users generate a manufacturing plan in Phase 2
- Click "Get quotes from manufacturers"
- Plan is sent to a curated network of composites manufacturers
- Manufacturers respond with quotes, lead times, and questions
- Think: **Xometry for composites** but starting with the design layer
- Revenue model: transaction fee (5-15%) on manufactured parts

#### 4.2 Material Sourcing
- Link to material suppliers from the BOM
- Negotiated discounts for platform users (fibre, resin, consumables)
- Revenue: affiliate commission or wholesale margin

#### 4.3 AFP-as-a-Service
- For users whose parts are recommended for AFP manufacturing:
- Option 1: Try it at a university with AFP-XS (connect to nearest installation)
- Option 2: Use an AFP-XS service bureau
- Option 3: Lease an AFP-XS system (€2-3k/month)
- Option 4: Buy AFP-XS for production
- Revenue: hardware sales, leasing, service bureau margins

#### 4.4 Certification Support
- Templates for material qualification test plans
- Process specification templates
- Quality documentation generators
- Connection to testing laboratories
- Note: NOT providing certification advice (legal risk), but tools for managing the
  paperwork and connecting to qualified professionals

#### 4.5 Community and Education
- Forum / Discord for composites community
- Certification courses: "Composites Design Fundamentals" (badge/certificate)
- AFP training courses (tied to AFP-XS installations)
- User-contributed case studies (like GitHub repos — open, forkable)
- Revenue: course fees, employer-sponsored certifications

---

## 6. Business Model

### Revenue Streams by Phase

```
PHASE 0-1: FREE EVERYTHING                      Cost: ~$0/month hosting
├── Knowledge base (CC BY 4.0)                   Revenue: $0 (brand building)
├── MCP server (open source)                     Revenue: $0 (penetration)
├── AddStack (free web tool)                     Revenue: $0 (lead gen)
└── Resin Flow Simulator (free web tool)         Revenue: $0 (lead gen)

PHASE 2: PAY-PER-USE AI                         Cost: ~$500-2k/month (API + hosting)
├── Basic Q&A over knowledge base                FREE (drives adoption)
├── Photo-to-Plan (full report)                  $5-20 per plan
├── Detailed cost estimation                     $5-15 per estimate
├── Custom laminate optimization                 $5-15 per optimization
├── DFM review                                   $5-15 per review
└── Monthly subscription (unlimited)             $49-99/month

PHASE 3: ENGINEERING TOOLS                       Cost: ~$2-5k/month
├── Laminate Designer (basic)                    FREE (AddStack evolution)
├── Laminate Designer (advanced features)        $29-99/month
├── FEA Lite (cloud compute)                     $2-10 per analysis run
├── AFP Path Preview                             FREE (AddPath gateway)
├── AddPath trial → subscription                 $X/month (existing pricing)
└── Bolted Joint / Sandwich tools                $19-49/month

PHASE 4: MARKETPLACE                            Cost: variable
├── Manufacturing quotes (transaction fee)       5-15% of order value
├── Material sourcing (margin/affiliate)         3-8% of material cost
├── AFP-XS leasing                              €2-3k/month
├── Certification courses                        $200-500 per course
└── Enterprise consulting                        Custom pricing
```

### Unit Economics (Phase 2)

Assuming Claude/GPT-4o API costs:
- Average photo-to-plan session: ~10k input tokens + 5k output tokens ≈ $0.15-$0.40 API cost
- Selling price: $10-20 per plan
- **Gross margin: 95%+** (after API costs, before infrastructure)
- Break-even at ~100 paid plans/month (infrastructure + maintenance costs)

### Flywheel

```
Open knowledge base (free)
    │
    ▼ attracts community (SEO, AI agent discovery, GitHub stars)
    │
    ▼ community uses free tools (AddStack, MCP server)
    │
    ▼ some users need more (photo analysis, cost estimation, DFM)
    │
    ▼ paid AI features convert power users
    │
    ▼ revenue funds more content, more tools, more R&D
    │
    ▼ manufacturers join marketplace (for the qualified leads)
    │
    ▼ AFP-XS/AddPath sales from "AFP recommended" plans
    │
    ▼ more knowledge, more tools → more users → repeat
```

---

## 7. Technical Architecture

### Infrastructure Choices

| Component | Recommended | Why |
|-----------|------------|-----|
| **MCP Server** | Python (FastMCP SDK) | Team likely already Python-proficient, composipy is Python |
| **RAG Framework** | LlamaIndex or LangChain | Both mature; LlamaIndex better for structured knowledge |
| **Vector DB** | Chroma (start) → Qdrant (scale) | Chroma is simplest to start, Qdrant for production |
| **LLM** | Claude API (primary), GPT-4o (fallback) | Claude for reasoning quality; GPT-4o for vision diversity |
| **Backend** | FastAPI (Python) | Async, fast, well-documented, type-safe |
| **Frontend** | Svelte or React | Svelte for speed; React for ecosystem |
| **Hosting** | Vercel (frontend) + Railway/Fly.io (backend) | Low-ops, scale on demand |
| **Calculations** | composipy (primary), AddStack API (validation) | Open source + proprietary validation |
| **FEA (Phase 3)** | CalculiX in Docker container | Most composites-capable open FEA |
| **PDF Generation** | WeasyPrint or Playwright PDF | Professional report output |

### MCP Server Architecture (Detail)

```python
# composites-mcp-server/server.py (conceptual)

from mcp.server import Server
from mcp.types import Resource, Tool, TextContent

server = Server("composites-engineering")

# --- RESOURCES ---
# Expose all 39+ knowledge base files
@server.list_resources()
async def list_resources():
    return [
        Resource(uri=f"composites://knowledge/{f['dir']}/{f['file']}",
                 name=f['title'],
                 description=f"Category: {f['category']}, Difficulty: {f['difficulty']}")
        for f in index_entries
    ]

# --- TOOLS ---
@server.list_tools()
async def list_tools():
    return [
        Tool(name="search_composites",
             description="Search the composites knowledge base by topic or question",
             inputSchema={"type":"object","properties":{
                 "query":{"type":"string","description":"Natural language search query"}}}),

        Tool(name="calculate_laminate",
             description="Calculate laminate properties using Classical Lamination Theory",
             inputSchema={"type":"object","properties":{
                 "layup":{"type":"array","items":{"type":"object","properties":{
                     "angle":{"type":"number"}, "thickness":{"type":"number"},
                     "material":{"type":"string"}}}},
                 "loads":{"type":"object","properties":{
                     "Nx":{"type":"number"}, "Ny":{"type":"number"},
                     "Nxy":{"type":"number"}}}}}),

        Tool(name="check_stacking_rules",
             description="Validate a laminate stacking sequence against design rules",
             inputSchema={"type":"object","properties":{
                 "angles":{"type":"array","items":{"type":"number"}}}}),

        Tool(name="recommend_process",
             description="Recommend a manufacturing process based on requirements",
             inputSchema={"type":"object","properties":{
                 "part_size_m2":{"type":"number"},
                 "annual_volume":{"type":"integer"},
                 "performance_class":{"type":"string","enum":["hobby","structural","aerospace"]},
                 "budget":{"type":"string","enum":["minimal","moderate","high"]}}}),

        Tool(name="estimate_cost",
             description="Estimate manufacturing cost for a composite part",
             inputSchema={"type":"object","properties":{
                 "fibre_type":{"type":"string"},
                 "process":{"type":"string"},
                 "part_weight_kg":{"type":"number"},
                 "volume":{"type":"integer"}}}),
    ]
```

---

## 8. Competitive Landscape

### Who Could Build This (But Hasn't)

| Potential Competitor | Why They Haven't | Our Advantage |
|---------------------|-----------------|---------------|
| **Siemens (Fibersim)** | Sells $100k/yr licenses, no incentive to democratize | We give away the knowledge for free |
| **Dassault (CATIA)** | Same — enterprise model, composites is a niche module | We're building for the 99% they don't serve |
| **ANSYS** | FEA-focused, not manufacturing-process-oriented | We cover design → manufacturing → cost holistically |
| **Altair (HyperSizer)** | Sizing optimization, not full workflow | We start from "I have a photo" |
| **Xometry** | Manufacturing marketplace, no composites design intelligence | We start at design, they start at quoting |
| **Markforged** | 3D printed composites only (chopped fibre, not true laminate) | We cover all manufacturing processes |
| **eLamX2 (TU Dresden)** | Academic tool, no AI, no manufacturing planning | We wrap their concepts in an AI agent |
| **CompositesAI** | Rotor blades only, niche application | We're general-purpose composites |

### Defensibility

1. **Knowledge base depth**: 40,000+ words of structured composites knowledge, growing
   with community contributions. Hard to replicate quickly.
2. **Agent-first design**: Built for AI retrieval from day one. Competitors would need to
   restructure their content.
3. **Tool integration**: MCP server + calculation tools + manufacturing knowledge in one
   package. No one else has this stack.
4. **Community**: Open source builds trust and contributions. Proprietary tools can't match this.
5. **Hardware tie-in**: AFP-XS gives a unique hardware-software-knowledge flywheel that
   pure software companies can't replicate.

---

## 9. Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| **AI recommendations are wrong** → user makes bad part, gets hurt | HIGH | Prominent disclaimers, "verify with qualified engineer" on every output, conservative safety factors, link to professional consultation |
| **Liability from engineering advice** | HIGH | Clear terms of service: "educational guidance only, not engineering sign-off", insurance, legal review |
| **LLM costs spike** | MEDIUM | Cache common queries, use smaller models for simple lookups, open-source LLM fallback (Llama, Mistral) |
| **Competitor builds similar tool** | MEDIUM | Move fast, build community moat, hardware integration differentiator |
| **Knowledge base quality degrades** with community contributions | MEDIUM | Audit script (already built), review process, expert review board |
| **Users expect precision** that AI can't deliver | MEDIUM | Set expectations clearly: "preliminary design guidance, not final analysis" |
| **Open-source tools break** or become unmaintained | LOW | Multiple fallbacks (composipy OR lamipy OR lamprop), contribute patches upstream |
| **Material property data is wrong** | MEDIUM | Only use published datasheets, cite sources, user can override with own data |

### Liability Framework

```
WHAT THE TOOL SAYS:                      WHAT IT MEANS:
"Preliminary design guidance"        →   NOT a final structural analysis
"Educational purposes"               →   NOT a substitute for qualified engineers
"Verify with AddStack / eLamX2"     →   Cross-check with established tools
"Consult CMH-17 for allowables"     →   We don't provide design allowables
"Safety factor of X applied"        →   We're being conservative
"Estimated cost: $X ± 30%"          →   This is a range, not a quote
```

---

## 10. Key Open-Source Dependencies

### Critical Path (must work for the product to function)

| Dependency | License | Risk | Mitigation |
|-----------|---------|------|------------|
| **composipy** | MIT | Active maintainer, but single-person project | Contribute upstream, fork if abandoned |
| **MCP SDK** | MIT | Backed by Anthropic, actively developed | Low risk |
| **LlamaIndex / LangChain** | MIT | Massive communities, well-funded companies | Low risk |
| **Chroma** | Apache 2.0 | Venture-backed, active development | Low risk |

### Nice-to-Have (enhance the product but not required)

| Dependency | License | Use |
|-----------|---------|-----|
| **bjsfm** | MIT | Bolted joint analysis (Phase 3) |
| **CalculiX** | GPL v2 | Cloud FEA (Phase 3) — GPL means server must be careful about distribution |
| **OpenRadioss** | AGPL v3 | Explicit dynamics — AGPL requires source disclosure for server use |
| **FreeCAD** | LGPL v2 | CAD generation — LGPL allows use as library |
| **Meshroom** | MPL v2 | Photogrammetry (future: multi-photo to 3D) |
| **CadQuery** | Apache 2.0 | Programmatic CAD generation |

### License Considerations

- **GPL/AGPL tools (CalculiX, OpenRadioss)**: Cannot be distributed in a proprietary
  product. Use them as server-side computation engines only (user uploads data → server
  runs analysis → returns results). The AGPL issue with OpenRadioss means the server
  code interfacing with it may need to be open-sourced.
- **MIT/Apache tools**: No restrictions. Can be used freely.
- **Knowledge base (CC BY 4.0)**: Anyone can use, even commercially, with attribution.
  This is intentional — it drives adoption.

---

## Appendix A: Implementation Priority Matrix

| Feature | Impact | Effort | Phase | Priority |
|---------|--------|--------|-------|----------|
| MCP server (basic search + retrieval) | Very High | Low | 1 | **P0** |
| Material properties database (JSON) | High | Low | 0 | **P0** |
| Stacking rule checker tool | High | Low | 1 | **P0** |
| Process recommendation tool | High | Medium | 1 | **P1** |
| CLT calculation tool (composipy wrapper) | High | Medium | 1 | **P1** |
| Photo-to-plan agent (basic) | Very High | High | 2 | **P1** |
| Cost estimation model | High | Medium | 2 | **P1** |
| Report generator (PDF) | Medium | Medium | 2 | **P2** |
| Web laminate designer (AddStack 2.0) | High | High | 3 | **P2** |
| Bolted joint analysis (bjsfm wrapper) | Medium | Medium | 3 | **P2** |
| Sandwich panel designer | Medium | Medium | 3 | **P2** |
| Cloud FEA (CalculiX) | High | Very High | 3 | **P3** |
| Manufacturing marketplace | Very High | Very High | 4 | **P3** |
| AFP path preview (AddPath gateway) | Medium | High | 3 | **P3** |

---

## Appendix B: 30-60-90 Day Action Plan

### Days 1-30: Foundation
- [x] Create `data/materials.json` with 15 material systems
- [x] Create `data/processes.json` with 10 processes capability matrix
- [x] Write 4 case studies (bicycle fork, drone arm, pressure vessel, car body panel)
- [x] Build MCP server with `search_composites`, `get_material_properties`, `check_stacking_rules`, `recommend_process`, `estimate_cost`
- [x] Add RTM and pultrusion knowledge pages
- [x] Test MCP server build (TypeScript compiles clean)
- [x] Prepare MCP server for npm (package.json metadata, README, .npmignore, config snippets)
- [x] Create 11 SVG diagrams in `diagrams/svg/`
- [x] Create `SETUP_GUIDE.md` with instructions for 6 AI clients
- [x] Create 4 applications pages (eVTOL, automotive, wind energy, sporting goods)
- [x] Create 3 decision tree JSON files (process, fibre, failure criteria selection)
- [x] Create `llm-instructions.md` for AI agent onboarding
- [x] Add structured comparison tables to 4 key knowledge pages
- [x] Add Mermaid decision trees to all 8 manufacturing process pages
- [x] Create master `process-selection-guide.md`
- [ ] Publish MCP server to npm registry

### Days 31-60: AI Agent MVP
- [x] Build `recommend_process` decision engine (in MCP server + FastAPI backend)
- [x] Build `estimate_cost` parametric model (in MCP server + FastAPI backend)
- [x] Create web frontend scaffold (React + Vite + TypeScript + TailwindCSS) with photo upload, analysis form, results display
- [x] Create FastAPI backend with vision service (Claude API), knowledge search, material lookup, process recommendation, cost estimation, stacking checks, report generation
- [ ] Integrate composipy for CLT calculations via MCP tool or backend API
- [ ] Wire up: photo → Claude vision analysis → knowledge retrieval → calculations → output
- [ ] Generate first end-to-end "photo to plan" demo
- [ ] Internal testing with 10 real-world part scenarios

### Days 61-90: Polish and Launch
- [ ] Add PDF report generation
- [ ] Refine cost model with real-world data points
- [ ] Add failure criteria checking to the agent workflow
- [ ] Launch beta to AddComposites community (blog announcement)
- [ ] Collect feedback, iterate on top 5 user requests
- [ ] Set up pay-per-use billing (Stripe)
- [ ] Submit MCP server to Anthropic's MCP directory

---

## Appendix C: Success Metrics

| Metric | Phase 1 Target | Phase 2 Target | Phase 4 Target |
|--------|---------------|---------------|---------------|
| MCP server installs | 500 | 2,000 | 10,000 |
| Monthly active users (all tools) | 1,000 | 5,000 | 50,000 |
| Paid plans generated/month | — | 500 | 5,000 |
| Monthly recurring revenue | $0 | $5,000 | $100,000 |
| Knowledge base pages | 45 | 60 | 100+ |
| Community contributors | 5 | 20 | 100+ |
| AddPath trial → subscription conversion | baseline | +20% | +50% |
| AFP-XS inquiries from platform | baseline | +10% | +30% |
| GitHub stars | 100 | 500 | 5,000 |

---

## Appendix D: Sources and References

### Open-Source Tools Found in Research
- [composipy](https://github.com/rafaelpsilva07/composipy) — Python CLT library
- [lamipy](https://github.com/joaopbernhardt/lamipy) — Python CLT with failure criteria
- [Classical-CLT-Calculator](https://github.com/AJJLagerweij/Classical-Composite-Laminate-Theory-Calculator)
- [ICLC](https://github.com/FranciSessa/ICLC---Interactive-Composite-Laminate-Calculator)
- [bjsfm](https://github.com/BYU-composites/bjsfm) — Bolted joint stress field model
- [lamprop](https://github.com/rsmith-nl/lamprop) — Laminate properties calculator
- [b3p](https://github.com/WISDEM/b3p) — Wind turbine blade modelling
- [OpenRadioss](https://github.com/OpenRadioss/OpenRadioss) — Open-source explicit FEA
- [CalculiX](http://www.dhondt.de/) — Open-source general FEA
- [cdmHUB](https://cdmhub.org/) — Composites simulation hub (Purdue)
- [eLamX2](https://tu-dresden.de/ing/maschinenwesen/ilr/lft/elamx2) — CLT tool (TU Dresden)
- [MCP Protocol](https://modelcontextprotocol.io/) — Model Context Protocol specification
- [kb-mcp-server](https://github.com/Geeksfino/kb-mcp-server) — Reference knowledge base MCP server
- [MCP Servers Directory](https://github.com/modelcontextprotocol/servers)

### AddComposites Products
- [AddStack](https://addstack.addcomposites.com) — Free laminate calculator
- [AddPath](https://www.addcomposites.com/all-products/addpath) — AFP path planning
- [AFP-XS](https://www.addcomposites.com/product/afp-xs) — Compact AFP system
- [Resin Flow Simulator](https://www.addcomposites.com/addcomposites-apps/resin-flow)
- [CRDS](https://www.addcomposites.com/addcomposites-apps/crds) — Rotor design simulator

### Industry Context
- [CompositesWorld on AddComposites](https://www.compositesworld.com/products/addcomposites-releases-free-professional-composites-design-software-suite)
- [Tulip: MCP for Manufacturing](https://tulip.co/blog/model-context-protocol-mcp-for-manufacturing/)
- [GitHub: composite-materials topic](https://github.com/topics/composite-materials)
- [GitHub: composites topic](https://github.com/topics/composites)
