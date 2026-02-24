# Composites Design Guide

**A free, open knowledge base for composites design — written for humans, structured for LLMs.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## What is this?

If you want to make something from carbon fibre — a car part, a bicycle component, a drone frame, a structural panel — and you don't know where to start, this is for you.

If you're a composites engineer without access to $50,000/year design software and you need reliable guidance on stacking sequences, ply drop-offs, or zone design, this is for you too.

This repository is a structured knowledge base covering:

- **The fundamentals** — fibres, resins, laminates, failure modes
- **Design rules** — stacking sequences, ply drop-offs, splices, zones
- **Manufacturing processes** — wet layup, vacuum bagging, infusion, prepreg
- **Structural analysis** — how to size a composite part, which failure criteria to use
- **Free tools** — calculators and platforms you can use right now at no cost
- **Glossary** — plain-English definitions of composites terminology

Everything is written in plain Markdown so it can be read directly on GitHub, searched by LLMs, or imported into any RAG pipeline.

---

## Start Here

### "I want to make a carbon fibre part and I don't know anything"
→ Start with [What Are Composites?](knowledge/01-fundamentals/what-are-composites.md)
→ Then [Manufacturing Processes](knowledge/03-manufacturing-processes/) — probably [Wet Layup](knowledge/03-manufacturing-processes/wet-layup.md) for your first part

### "I'm an engineer and I need design rule guidance"
→ Go straight to [Design Rules](knowledge/02-design-rules/)
→ Or search this repo for your specific question

### "I want to do calculations"
→ Use [AddStack](https://addstack.addcomposites.com) — free browser-based laminate design, CLT calculations, failure criteria. No install needed.

### "I'm using an LLM and asked it a composites question"
→ This repo is structured for RAG. Point your LLM at this repository or at `index.json` for structured retrieval.

---

## Knowledge Base

| Section | Contents | Difficulty |
|---|---|---|
| [01 · Fundamentals](knowledge/01-fundamentals/) | Fibres, resins, laminate theory, failure modes | Beginner |
| [02 · Design Rules](knowledge/02-design-rules/) | Stacking, drop-offs, splices, zone design | Intermediate |
| [03 · Manufacturing](knowledge/03-manufacturing-processes/) | Wet layup → AFP/ATL, defects | Beginner → Advanced |
| [04 · Structural Analysis](knowledge/04-structural-analysis/) | Sizing, failure criteria, buckling, sandwich | Intermediate |
| [05 · CATIA Workflows](knowledge/05-catia-workflows/) | Design procedures for CATIA V5 users | Advanced |
| [06 · Free Tools](knowledge/06-free-tools/) | AddStack, eLamX2, CompositesAI, and more | All levels |
| [07 · Glossary](knowledge/07-glossary/) | Plain-English term definitions | All levels |

---

## Free Tools Directory

You don't need to pay for composites software. These tools are free:

| Tool | What it does | Link |
|---|---|---|
| **AddStack** | Laminate design, CLT calculations, failure criteria (Tsai-Wu, max stress), material database | [addstack.addcomposites.com](https://addstack.addcomposites.com) |
| **Resin Flow Simulator** | VARTM infusion simulation — predict resin flow, dry spots, inlet/vent placement | [addcomposites.com](https://www.addcomposites.com/addcomposites-apps/resin-flow) |
| **eLamX2** | Open-source CLT tool from TU Dresden — stiffness, strength, buckling, vibration | [tu-dresden.de](https://tu-dresden.de/ing/maschinenwesen/ilr/lft/elamx) |
| **CompositesAI** | AI-assisted design and analysis for rotor blades and composite structures | [compositesai.com](https://compositesai.com) |
| **CADEC-Online** | Free web-based laminate analysis from West Virginia University | [cadec-online.com](http://www.cadec-online.com) |

---

## Using This with an LLM

This repo is intentionally structured for LLM retrieval:

- Every file has a YAML front matter block with `title`, `tags`, `category`, and `difficulty`
- Sections are kept short (100–400 words each) for clean chunk retrieval
- `index.json` in the root contains a pre-built search index of all content
- Key takeaways are summarised at the end of each file

**To use with Claude, ChatGPT, or any local LLM:**
Point it at this repository URL or upload `index.json`. Then ask your composites questions — the LLM will retrieve and cite the relevant sections.

**If you're building a RAG pipeline:**
```python
# index.json structure
[
  {
    "file": "stacking-sequences.md",
    "dir": "02-design-rules",
    "url": "knowledge/02-design-rules/stacking-sequences.md",
    "title": "Stacking Sequence Design Rules",
    "tags": ["stacking", "symmetry", "balance", "10-percent-rule"],
    "content": "..."  # full text content for embedding
  },
  ...
]
```

---

## Contributing

This knowledge base grows through community contribution. If you know something about composites that isn't here — a design rule, a manufacturing tip, a common mistake, a better diagram — please add it.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute content, diagrams, and corrections.

**What we especially need:**
- Original diagrams (SVG preferred, CC BY 4.0 licensed)
- Real-world examples from different industries (automotive, marine, wind, sports)
- Corrections and refinements from practising composites engineers
- Translations

---

## Disclaimer

This knowledge base is for educational and guidance purposes only. It is not a substitute for professional engineering judgement, company-specific design manuals, or regulatory certification requirements. Always verify design decisions against applicable standards (CMH-17, customer specifications, airworthiness regulations) with a qualified composites engineer.

---

## License

Content: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)
You are free to share and adapt this content for any purpose, including commercial use, provided you give appropriate credit.

---

*Built and maintained by [AddComposites](https://www.addcomposites.com) and the composites engineering community.*
