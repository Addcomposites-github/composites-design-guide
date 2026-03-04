# Add Composites Engineering to Your AI Assistant in 2 Minutes

This guide shows you how to give any AI assistant access to a composites engineering knowledge base with 54 articles, material databases, manufacturing process selection, cost estimation, and laminate design tools.

**No composites experience required. No paid software required.**

---

## What You Get

Once installed, your AI assistant can:

- **Answer composites design questions** using 54 expert articles (67,000+ words)
- **Look up material properties** for 15+ composite material systems (carbon, glass, aramid, basalt)
- **Check your laminate design** against symmetry, balance, 10% rule, and consecutive ply limits
- **Recommend manufacturing processes** based on your part geometry, volume, and quality needs
- **Estimate costs** for material, labour, tooling, and consumables
- **Guide you through decision trees** for fibre selection, process selection, and failure criteria

---

## Choose Your AI Tool

### Option A: Claude Desktop

1. Open Claude Desktop
2. Go to **Settings > Developer > Edit Config**
3. Add this to your `claude_desktop_config.json`:

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

4. Restart Claude Desktop
5. You should see the composites tools icon in the chat input area

**Try it:** Ask Claude *"What stacking sequence should I use for a quasi-isotropic carbon fibre panel?"*

---

### Option B: Claude Code (Terminal)

```bash
claude mcp add composites-mcp-server -- npx -y composites-mcp-server
```

That's it. Claude Code will now have composites tools available in every session.

**Try it:** Ask Claude *"Check this laminate: [0, 45, -45, 90, 90, -45, 45, 0]"*

---

### Option C: VS Code (Claude Extension)

1. Create a file `.vscode/mcp.json` in your project root:

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

2. Reload VS Code
3. The composites tools are now available through the Claude extension

---

### Option D: Cursor

1. Open Cursor Settings
2. Navigate to the **MCP** section
3. Add a new server with this configuration:

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

4. Save and restart Cursor

---

### Option E: Windsurf

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

### Option F: Any MCP-Compatible Client

The server runs on stdio transport. Any MCP client can use it:

```bash
npx composites-mcp-server
```

Or install globally:

```bash
npm install -g composites-mcp-server
composites-mcp-server
```

---

## Verify It Works

After installation, try these prompts with your AI assistant:

| Prompt | What happens |
|--------|-------------|
| *"What carbon fibre material should I use for a drone arm?"* | Searches knowledge base + material database |
| *"Check this laminate: [0, 45, -45, 90, 0, 0, 90, -45, 45, 0]"* | Runs stacking rule checks |
| *"What manufacturing process should I use for a 0.3 m2 curved panel, 50 parts/year, structural quality?"* | Runs process recommendation |
| *"How much would a 1.5 kg carbon fibre part cost with vacuum bagging?"* | Runs cost estimation |
| *"What is the difference between Tsai-Wu and Hashin failure criteria?"* | Searches knowledge base |

---

## Prerequisites

- **Node.js 18+** — [Download](https://nodejs.org/)
- **An MCP-compatible AI client** — Claude Desktop, Claude Code, VS Code, Cursor, Windsurf, or any MCP client

No Python, no Docker, no API keys needed for the knowledge base and tools.

---

## What's Inside

### 5 Tools

| Tool | Description |
|------|-------------|
| `search_composites` | Natural language search across 54 knowledge articles |
| `get_material_properties` | Look up material mechanical properties, cost, and compatibility |
| `check_stacking_rules` | Validate a laminate against 4 standard design rules |
| `recommend_process` | Rank manufacturing processes by suitability |
| `estimate_cost` | Rough per-part cost breakdown |

### 54 Knowledge Articles

Covering: fibre types, resin systems, laminate theory, stacking sequences, ply drop-offs, splices, zone design, wet layup, vacuum bagging, resin infusion, prepreg, RTM, AFP, filament winding, pultrusion, failure criteria, buckling, sandwich structures, damage tolerance, CATIA workflows, free tools, cost estimation, and real-world case studies (bicycle fork, drone arm, pressure vessel, car body panel).

### Structured Databases

- **15+ material systems** with E1, E2, G12, strengths, density, cost, process compatibility
- **10 manufacturing processes** with fibre volume fraction, void content, cycle times, cost models
- **3 decision trees** (process selection, fibre selection, failure criteria selection)

---

## Free Composites Tools (No Installation Needed)

These browser-based tools complement the knowledge base:

| Tool | URL | What it does |
|------|-----|-------------|
| **AddStack** | [addstack.addcomposites.com](https://addstack.addcomposites.com) | CLT calculator, ABD matrices, failure criteria |
| **Resin Flow Simulator** | [addcomposites.com](https://www.addcomposites.com/addcomposites-apps/resin-flow) | VARTM infusion simulation |
| **CRDS** | [addcomposites.com](https://www.addcomposites.com/addcomposites-apps/crds) | Composite rotor/sleeve design |

---

## Troubleshooting

**"npx: command not found"**
Install Node.js 18+ from [nodejs.org](https://nodejs.org/).

**"Server failed to start"**
Make sure you're using Node.js 18 or higher: `node --version`

**"No tools showing up in Claude Desktop"**
1. Check your config file path (Settings > Developer > Edit Config)
2. Make sure the JSON is valid (no trailing commas)
3. Restart Claude Desktop completely (quit and reopen)

**"index.json not found" error**
If running from source, make sure you cloned the full repository (the server needs the knowledge/ directory).

---

## Contributing

This is an open-source project. Contributions welcome:
- [GitHub Repository](https://github.com/addcomposites/composites-design-guide)
- [Contributing Guide](https://github.com/addcomposites/composites-design-guide/blob/main/CONTRIBUTING.md)
- License: MIT (server) + CC BY 4.0 (knowledge base)

---

## Disclaimer

This knowledge base is for educational and guidance purposes only. It is not a substitute for professional engineering judgement, company-specific design manuals, or regulatory certification requirements. Always verify design decisions against applicable standards (CMH-17, customer specs, airworthiness regulations) with a qualified composites engineer.

---

Built by [AddComposites](https://www.addcomposites.com) — Making composites accessible to everyone.
