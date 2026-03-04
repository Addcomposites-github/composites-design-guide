# HANDOVER.md — Session Continuity Guide

> **Last updated:** 2026-02-25
> **Sessions so far:** 3 (context ran out twice)
> **Status:** All features built. Uncommitted. Needs git commit + push.

---

## 1. What Is This Project?

**OpenComposites** is a free, open-source composites design platform built by
[Addcomposites](https://www.addcomposites.com). It has two parts:

1. **Knowledge Base** — 56 Markdown articles covering composites design
   (fibres, resins, manufacturing, analysis, CATIA workflows, cost estimation,
   case studies). Structured for LLM retrieval (RAG).

2. **Web Application** — A React + FastAPI app that lets users:
   - Search the knowledge base (TF-IDF full-text search)
   - Browse a materials database (carbon, glass, aramid composites)
   - Analyze composite parts using AI (Claude API — BYOK model)
   - Run engineering calculators (CLT, sandwich panel, bolted joints)
   - Get process recommendations and cost estimates

**Who it's for:** Makers, students, startup engineers, drone builders — anyone
without access to expensive aerospace composites tools.

**Repo:** `github.com/addcomposites/composites-design-guide`

---

## 2. Repository Structure

```
composites-design-guide/
├── CLAUDE.md                    ← Project instructions for Claude Code
├── HANDOVER.md                  ← YOU ARE HERE — session continuity
├── README.md                    ← Public-facing project intro
├── CONTRIBUTING.md              ← How to contribute
├── CHANGELOG.md                 ← Version history
├── PRODUCT_ROADMAP.md           ← Future features
├── SETUP_GUIDE.md               ← Dev setup instructions
├── index.json                   ← Auto-generated search index for all articles
├── llm-instructions.md          ← Instructions for LLMs consuming this repo
│
├── knowledge/                   ← 56 Markdown articles (the knowledge base)
│   ├── 01-fundamentals/         ← Fibres, resins, laminates, failure modes
│   ├── 02-design-rules/         ← Stacking, ply drop-offs, splices, DFM
│   ├── 03-manufacturing-processes/ ← Wet layup, vacuum bag, infusion, prepreg, AFP, RTM, etc.
│   ├── 04-structural-analysis/  ← Sizing, failure criteria, buckling, sandwich, joints
│   ├── 05-catia-workflows/      ← Ply creation, zones, stacking, flat patterns
│   ├── 06-free-tools/           ← AddStack, eLamX2, CompositesAI
│   ├── 07-glossary/             ← Composites terminology
│   ├── 08-cost-estimation/      ← Cost models, drivers, estimation methods
│   ├── 09-case-studies/         ← Car body panel, drone frame, wind turbine blade
│   └── 10-applications/         ← Aerospace, automotive, marine, sporting goods
│
├── data/
│   ├── materials.json           ← Material property database (E1, E2, strengths, cost)
│   └── processes.json           ← Manufacturing process database
│
├── decision-trees/
│   ├── fibre-selection.json     ← Guides fibre choice based on requirements
│   ├── process-selection.json   ← Guides manufacturing process choice
│   └── failure-criteria-selection.json
│
├── diagrams/
│   ├── README.md
│   └── svg/                     ← 11 original SVG diagrams (CC BY 4.0)
│
├── scripts/
│   ├── build_index.py           ← Regenerates index.json from knowledge/ articles
│   └── build.sh                 ← Full build script (index + frontend + copy dist)
│
├── web-app/
│   ├── backend/                 ← FastAPI (Python)
│   │   ├── app/
│   │   │   ├── main.py          ← FastAPI app, CORS, SPA serving, routers
│   │   │   ├── config.py        ← Settings (paths, API keys, pydantic-settings)
│   │   │   ├── routes/          ← API endpoints:
│   │   │   │   ├── analysis.py      POST /api/analyze (Claude AI — needs API key)
│   │   │   │   ├── knowledge.py     GET  /api/search?query=...&top_n=...
│   │   │   │   ├── materials.py     GET  /api/materials?query=...
│   │   │   │   ├── processes.py     POST /api/processes/recommend
│   │   │   │   ├── cost.py          POST /api/estimate-cost
│   │   │   │   ├── clt.py           POST /api/clt/calculate
│   │   │   │   ├── sandwich.py      POST /api/sandwich/analyze
│   │   │   │   └── bolted_joint.py  POST /api/bolted-joint/analyze
│   │   │   ├── services/        ← Business logic for each route
│   │   │   └── models/          ← Pydantic request/response models
│   │   ├── requirements.txt
│   │   └── .env                 ← Backend env (ANTHROPIC_API_KEY goes here)
│   │
│   └── frontend/                ← React + Vite + Tailwind CSS v4
│       ├── src/
│       │   ├── App.tsx          ← Single-page app with page state routing
│       │   ├── main.tsx         ← React entry point
│       │   ├── index.css        ← Global styles (Inter font, glass, gradients, mesh bg)
│       │   ├── pages/
│       │   │   ├── HomePage.tsx          ← Hero, features, stats, tools, What's New
│       │   │   ├── KnowledgeBasePage.tsx ← Search, browse topics, materials browser
│       │   │   ├── AnalyzePage.tsx       ← AI analysis form with BYOK
│       │   │   └── ResultsPage.tsx       ← Analysis results display
│       │   ├── components/
│       │   │   ├── Header.tsx            ← Sticky nav with backdrop blur
│       │   │   ├── Footer.tsx            ← Clean minimal footer
│       │   │   ├── AnalysisForm.tsx      ← Part description + options form
│       │   │   ├── ApiKeyInput.tsx       ← BYOK Claude API key input
│       │   │   ├── ResultsDisplay.tsx    ← Renders analysis results
│       │   │   ├── FeedbackButton.tsx    ← GitHub issue feedback link
│       │   │   └── ... (MaterialCard, ProcessCard, charts, etc.)
│       │   ├── api/
│       │   │   └── client.ts    ← API client (fetch wrapper, all endpoints)
│       │   └── types/
│       │       └── index.ts     ← TypeScript interfaces for all API types
│       ├── .env                 ← VITE_API_URL= (empty = relative URLs for prod)
│       ├── vite.config.ts       ← Dev proxy /api -> localhost:8000
│       ├── tailwind.config.ts   ← Custom colors (primary=red, secondary=slate)
│       └── dist/                ← Production build output (served by FastAPI)
│
├── mcp-server/                  ← MCP server (for LLM tool integration)
│
└── .claude/
    └── launch.json              ← Dev server configs for Claude Code preview
```

---

## 3. Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | React 19 + TypeScript | Single-page app (no router — state-based nav) |
| Styling | Tailwind CSS v4 + `@tailwindcss/vite` | Inter font, custom `primary`/`secondary` scales |
| Build | Vite 6.4 | Dev server on port 5173, proxies /api to backend |
| Backend | FastAPI (Python) | Uvicorn, port 8000 |
| AI | Anthropic Claude API | BYOK — user provides their own key via header |
| Search | TF-IDF (scikit-learn) | Searches index.json built from knowledge/ articles |
| Data | JSON files | materials.json, processes.json, decision trees |
| Deployment | Replit (planned) | SPA mode: FastAPI serves frontend dist/ |

---

## 4. How the App Runs

### Development (two servers)
```bash
# Terminal 1: Backend
cd web-app/backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2: Frontend
cd web-app/frontend
npm install
npm run dev    # Vite on port 5173, proxies /api to :8000
```

### Production (single server)
```bash
cd web-app/frontend && npm run build     # Outputs to dist/
cd web-app/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
# FastAPI serves dist/ as static files + SPA fallback
```

### Claude Code preview
The `.claude/launch.json` is configured. Use `preview_start` with name `backend` or `frontend`.
Note: On Windows, the frontend uses `node node_modules/vite/bin/vite.js` because `npm`/`npx` don't resolve properly through the preview system.

---

## 5. Key API Endpoints

| Method | Path | What it does |
|--------|------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/search?query=...&top_n=10` | Full-text search knowledge base |
| GET | `/api/materials?query=...` | Search material database |
| POST | `/api/analyze` | AI part analysis (needs `X-Anthropic-Key` header) |
| POST | `/api/processes/recommend` | Process recommendation |
| POST | `/api/estimate-cost` | Cost estimation |
| POST | `/api/calculate-laminate` | CLT: ABD matrices and effective moduli |
| POST | `/api/check-failure` | CLT: failure analysis (max stress, Tsai-Wu, etc.) |
| POST | `/api/optimize-laminate` | CLT: lightest passing laminate |
| POST | `/api/sandwich/analyze` | Sandwich panel analysis |
| POST | `/api/sandwich/optimize` | Sandwich panel optimisation |
| GET | `/api/sandwich/cores` | List core materials |
| POST | `/api/bolted-joint/analyze` | Bolted joint analysis |
| POST | `/api/bolted-joint/recommend` | Joint sizing recommendation |
| GET | `/api/bolted-joint/bolts` | List bolt database |
| POST | `/api/check-stacking` | Stacking sequence rule check |
| GET | `/api/article/{dir}/{file}` | Retrieve article markdown content |

### Search API response shape (important!)
```json
{
  "results": [
    {
      "title": "Vacuum Bagging",
      "file": "vacuum-bagging.md",
      "dir": "03-manufacturing-processes",
      "url": "knowledge/03-manufacturing-processes/vacuum-bagging.md",
      "category": "manufacturing",
      "difficulty": "beginner",
      "tags": ["vacuum-bag", "compaction", "bleeder"],
      "score": 49.77,
      "snippet": "Vacuum bagging is the most impactful..."
    }
  ],
  "count": 10
}
```
**Note:** Fields are `url` (not `path`), `snippet` (not `excerpt`), and `score` is already a percentage (not 0-1). The frontend `SearchResult` type in `types/index.ts` has been updated to match.

---

## 6. What Was Built Across 3 Sessions

### Session 1 — Knowledge Base Foundation
- Created 56 knowledge articles across 10 topic areas
- Built index.json search index
- Created SVG diagrams
- Set up data files (materials.json, processes.json, decision trees)

### Session 2 — Web Application
- Built full FastAPI backend with all API routes and services
- Built React frontend with all pages and components
- Implemented AI analysis with BYOK (Bring Your Own Key) model
- Added CLT calculator, sandwich panel, bolted joint analyzers
- Set up Replit deployment config

### Session 3 (current) — Polish and Bug Fixes
- **Fixed "Failed to fetch" bug** — Frontend `.env` had `VITE_API_URL=http://localhost:8000` baked into production build. Fixed to empty string (relative URLs).
- **Modernized UI** — Complete redesign from flat 2010-era look to modern 2025 aesthetic:
  - Inter font from Google Fonts
  - Gradient mesh backgrounds, glass-morphism effects
  - Pill-shaped buttons, rounded-2xl cards
  - Sticky header with backdrop blur
  - Gradient text for hero "with AI"
  - Micro-animations (hover translate, fade-up)
  - Custom color scheme: primary (red/orange), secondary (slate)
- **Fixed search results not clickable** — Changed `SearchResultCard` from `<div>` to `<a>` linking to GitHub article URLs.
- **Fixed SearchResult type mismatch** — Frontend type used `path`/`excerpt` but API returns `url`/`snippet`. Updated `types/index.ts` and `KnowledgeBasePage.tsx`.
- **Fixed score display** — Was showing `4977%` (score * 100). Now shows `50%` (score as-is).
- **Set up `.claude/launch.json`** for dev server preview.
- **Rebuilt production frontend** — `npm run build` succeeds, no localhost in output.

---

## 7. Current State — What's Uncommitted

Everything from sessions 2 and 3 is uncommitted. `git status` shows:

**Modified files:**
- `.gitignore`, `README.md`, `index.json`
- Several knowledge articles (expanded content)

**New files (untracked):**
- `web-app/` — entire web application (backend + frontend)
- `data/` — materials.json, processes.json
- `decision-trees/` — fibre, process, failure criteria selection
- `diagrams/svg/` — 11 SVG diagrams
- `mcp-server/` — MCP server for LLM integration
- `scripts/build.sh`
- New knowledge articles (manufacturing, analysis, cost, case studies, applications)
- `CHANGELOG.md`, `PRODUCT_ROADMAP.md`, `SETUP_GUIDE.md`, `llm-instructions.md`
- `.replit`, `replit.nix` — Replit deployment config

---

## 8. What Needs to Happen Next

### Immediate (start of next session)
1. **Git commit all changes** — Stage everything, write a good commit message
2. **Git push** to GitHub
3. **Verify on Replit** — The deployment should work with SPA mode

### Future enhancements (from PRODUCT_ROADMAP.md)
- Dark mode toggle
- Image upload for AI analysis (vision)
- Interactive CLT calculator page in frontend
- PDF report export
- User accounts and saved analyses
- More knowledge articles

---

## 9. Known Issues and Gotchas

1. **Port 8000 ghost process on Windows** — Sometimes `python.exe` holds port 8000 after being killed. Use `netstat -ano | grep ":8000"` and `taskkill //F //PID <pid>`. If stuck, wait or use a different port temporarily.

2. **Vite proxy in dev mode** — `vite.config.ts` proxies `/api` to `localhost:8000`. If backend is on a different port, update this. The proxy only affects dev mode.

3. **Frontend `.env`** — Must be `VITE_API_URL=` (empty) for production. Any value gets baked into the JS at build time.

4. **Windows + Claude preview** — `npm` and `npx` don't resolve as `runtimeExecutable` in `.claude/launch.json`. Use `node` with direct path to `node_modules/vite/bin/vite.js`.

5. **Search result types** — The `SearchResult` TypeScript interface must match the actual API response. Fields: `url`, `snippet`, `score` (percentage), `category`, `difficulty`, `file`, `dir`, `tags`.

---

## 10. Files You'll Read Most Often

| File | Why |
|------|-----|
| `web-app/frontend/src/pages/KnowledgeBasePage.tsx` | Search UI + results display |
| `web-app/frontend/src/pages/HomePage.tsx` | Landing page |
| `web-app/frontend/src/api/client.ts` | All API calls |
| `web-app/frontend/src/types/index.ts` | TypeScript interfaces |
| `web-app/frontend/src/index.css` | Global styles and utilities |
| `web-app/backend/app/main.py` | FastAPI app setup + SPA serving |
| `web-app/backend/app/routes/knowledge.py` | Search endpoint |
| `web-app/backend/app/config.py` | All path and env config |
| `CLAUDE.md` | Project guidelines and content rules |

---

## 11. Commands Cheat Sheet

```bash
# Rebuild search index after editing knowledge/ articles
python scripts/build_index.py

# Build frontend for production
cd web-app/frontend && npm run build

# Start backend
cd web-app/backend && python -m uvicorn app.main:app --reload --port 8000

# Start frontend dev server
cd web-app/frontend && npm run dev

# Full build (index + frontend + copy)
bash scripts/build.sh

# Check for localhost leaks in production build
grep -r "localhost" web-app/frontend/dist/assets/*.js
```
