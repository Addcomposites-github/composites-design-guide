# composites-mcp-server

Add composites engineering knowledge to any AI assistant in 2 minutes.

An MCP (Model Context Protocol) server that gives AI assistants access to 54 composites engineering articles, material property databases, manufacturing process selection, cost estimation, and laminate stacking rule checks.

[![npm version](https://img.shields.io/npm/v/composites-mcp-server.svg)](https://www.npmjs.com/package/composites-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## Quick Install

### Claude Desktop

Add to your `claude_desktop_config.json` (Settings > Developer > Edit Config):

```json
{
  "mcpServers": {
    "composites": {
      "command": "npx",
      "args": ["-y", "composites-mcp-server"]
    }
  }
}
```

Restart Claude Desktop. You now have composites engineering tools available.

### Claude Code (CLI)

```bash
claude mcp add composites-mcp-server -- npx -y composites-mcp-server
```

### VS Code (Claude Extension / Copilot)

Add to `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "composites": {
      "command": "npx",
      "args": ["-y", "composites-mcp-server"]
    }
  }
}
```

### Cursor

Add to Cursor Settings > MCP:

```json
{
  "mcpServers": {
    "composites": {
      "command": "npx",
      "args": ["-y", "composites-mcp-server"]
    }
  }
}
```

### Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "composites": {
      "command": "npx",
      "args": ["-y", "composites-mcp-server"]
    }
  }
}
```

---

## From Source (Development)

```bash
git clone https://github.com/addcomposites/composites-design-guide.git
cd composites-design-guide/mcp-server
npm install
npm run build
```

Then use the absolute path in your MCP config:

```json
{
  "mcpServers": {
    "composites": {
      "command": "node",
      "args": ["/path/to/composites-design-guide/mcp-server/build/index.js"]
    }
  }
}
```

---

## What You Get

### 5 Engineering Tools

| Tool | What It Does | Example |
|------|-------------|---------|
| **search_composites** | Natural language search across 54 knowledge articles | "How do I design a ply drop-off?" |
| **get_material_properties** | Look up mechanical properties, cost, process compatibility | "T700 carbon epoxy" |
| **check_stacking_rules** | Validate a laminate against symmetry, balance, 10% rule, consecutive ply limits | `[0, 45, -45, 90, 90, -45, 45, 0]` |
| **recommend_process** | Rank manufacturing processes by part size, volume, quality class, geometry | "0.5 m2, 100/yr, structural, double_curve" |
| **estimate_cost** | Rough cost breakdown: material, labour, tooling, consumables | "carbon, prepreg, 2 kg, 16 plies, 50/yr" |

### 3 Guided Prompts

| Prompt | Purpose |
|--------|---------|
| **design_review** | Review a laminate design (layup + material + application) |
| **process_selection** | Choose a manufacturing process (part description + requirements + budget) |
| **photo_to_plan** | Create a manufacturing plan from a part description or photo |

### 5 Knowledge Resources

| URI | Description |
|-----|-------------|
| `composites://knowledge/index` | List all 54 knowledge articles |
| `composites://knowledge/{dir}/{filename}` | Read a specific article |
| `composites://data/materials` | 15+ material systems with full properties |
| `composites://data/processes` | 10 manufacturing processes with capability matrices |
| `composites://decision-trees/{name}` | Decision trees for process/fibre/failure-criteria selection |

---

## Knowledge Base Coverage

| Category | Articles | Topics |
|----------|----------|--------|
| Fundamentals | 5 | Fibres, resins, laminates, failure modes |
| Design Rules | 8 | Stacking sequences, ply drops, splices, zones, DFM, NCF, darts |
| Manufacturing | 11 | Wet layup, vacuum bag, VARTM, prepreg, RTM, AFP, filament winding, pultrusion |
| Structural Analysis | 5 | Panel sizing, failure criteria, buckling, sandwich, damage tolerance |
| CATIA Workflows | 8 | Ply creation, zones, stacking, flat patterns, ply books |
| Free Tools | 4 | AddStack, eLamX2, CompositesAI, other resources |
| Glossary | 1 | Plain-English composites terminology |
| Cost Estimation | 3 | Material costs, process costs, tooling costs |
| Case Studies | 4 | Bicycle fork, drone arm, pressure vessel, car body panel |
| Applications | 4 | eVTOL, automotive, wind energy, sporting goods |

**Total: 54 articles, 67,000+ words**

---

## Example Conversations

### "What material should I use for a drone arm?"

The AI will use `search_composites` to find the drone arm case study and fibre types article, then `get_material_properties` to look up T700 carbon/epoxy properties, and `recommend_process` to suggest vacuum bagging for low volume.

### "Check my laminate: [0/45/-45/90/0/0/90/-45/45/0]"

The AI will use `check_stacking_rules` to verify symmetry (PASS), balance (PASS), 10% rule, and consecutive ply limits.

### "How much would a carbon fibre car hood cost to make?"

The AI will use `estimate_cost` with carbon fibre, VARTM process, estimated weight, and volume to give a cost breakdown, then reference the car body panel case study.

---

## Free Tools Mentioned in the Knowledge Base

| Tool | URL | Purpose |
|------|-----|---------|
| **AddStack** | [addstack.addcomposites.com](https://addstack.addcomposites.com) | CLT calculator, ABD matrices, failure criteria |
| **Resin Flow Simulator** | [addcomposites.com/apps/resin-flow](https://www.addcomposites.com/addcomposites-apps/resin-flow) | VARTM infusion simulation |
| **CRDS** | [addcomposites.com/apps/crds](https://www.addcomposites.com/addcomposites-apps/crds) | Composite rotor/sleeve design |
| **eLamX2** | TU Dresden | Open-source desktop CLT tool |

---

## Development

```bash
npm run dev     # Watch mode — recompiles on change
npm run build   # One-time build
npm start       # Run the server
```

### Architecture

```
mcp-server/
  src/index.ts       -- Server: resources, tools, prompts, search engine, stacking checks
  build/             -- Compiled JS (generated by tsc)

../data/
  materials.json     -- 15+ material systems with mechanical properties and cost
  processes.json     -- 10 manufacturing processes with capabilities and cost models

../decision-trees/
  process-selection.json        -- Manufacturing process decision tree
  fibre-selection.json          -- Fibre type selection decision tree
  failure-criteria-selection.json -- Failure criterion selection decision tree

../index.json        -- Search index (54 articles, 67,000+ words)
../knowledge/        -- 54 markdown articles organized by topic
```

The server loads data files at startup using relative paths from the build directory up to the repository root.

---

## Contributing

This is part of the [Composites Design Open Knowledge Base](https://github.com/addcomposites/composites-design-guide) — an open-source composites engineering resource. Contributions welcome.

## License

MIT — the server code.
CC BY 4.0 — the knowledge base content.

## Disclaimer

This knowledge base is for educational and guidance purposes only. It is not a substitute for professional engineering judgement, company-specific design manuals, or regulatory certification requirements. Always verify design decisions against applicable standards (CMH-17, customer specs, airworthiness regulations) with a qualified composites engineer.

---

Built by [AddComposites](https://www.addcomposites.com) — Making composites accessible to everyone.
