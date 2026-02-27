# MARKETING_HANDOVER.md — OpenComposites Promotion Guide

> **Created:** 2026-02-27
> **For:** Marketing agent taking over from the build agent
> **Status:** App is fully built, deployed, and live. Your job is to get eyes on it.

---

## 1. What Is OpenComposites?

**OpenComposites** is a free, open-source composites design platform built by
[Addcomposites](https://www.addcomposites.com). It solves a real problem: 99% of
people interested in composites (makers, startup engineers, students, drone builders)
have zero access to the $15k–$150k/year tools that large aerospace companies use.

### The product has two parts:

**1. Knowledge Base** — 56+ plain-language articles covering:
- Composites fundamentals (fibres, resins, laminates, failure modes)
- Design rules (stacking sequences, ply drop-offs, splices, zone design)
- Manufacturing processes (wet layup, vacuum bagging, infusion, prepreg, AFP)
- Structural analysis (sizing, failure criteria, buckling, sandwich structures)
- CATIA V5 composites workflows
- Cost estimation, case studies, real-world applications
- Full glossary

All content is CC BY 4.0 (free to use, forever). Structured for LLM retrieval (RAG).

**2. Web Application** — AI-powered design tool:
- Describe or upload a photo of your part → get a complete manufacturing plan
- Material selection (carbon, glass, aramid, hybrid)
- Process recommendation + cost estimation
- CLT (Classical Laminate Theory) calculator
- Sandwich panel analyser
- Bolted joint analyser
- Full knowledge base search

The AI analysis uses Claude (Anthropic) via a **BYOK model** — users bring their own API key. This keeps the app free to run with no backend AI cost.

---

## 2. Live URLs

| URL | Purpose |
|-----|---------|
| **https://opencomposites.addcomposites.com** | Primary custom domain (use this in all promotions) |
| https://opencomposites-app.replit.app | Replit backup domain |
| https://github.com/Addcomposites-github/opencomposites-app | App source code |
| https://github.com/Addcomposites-github/composites-design-guide | Knowledge base source |

**Always link to `opencomposites.addcomposites.com`** — it's the cleanest URL.

---

## 3. The Audiences (in priority order)

### Audience 1 — Makers and hobbyists
- Building carbon fibre parts for cars, bikes, drones, boats
- No formal composites training
- Budget-sensitive — love anything free
- **Where they are:** Reddit (r/DIYComposites, r/compositesmanufacturing, r/racing, r/DIY), YouTube, Discord

### Audience 2 — Drone and eVTOL engineers
- Small startups, no access to Fibersim or CATIA
- Technically skilled but not composites specialists
- Need quick answers on laminate design
- **Where they are:** LinkedIn, drone builder forums (RCGroups, IntoFPV), eVTOL Insights, Slack communities

### Audience 3 — Junior engineers and students
- Tier 2/3 suppliers, university labs
- Looking for reference material and free tools
- **Where they are:** University subreddits (r/AerospaceEngineering, r/MechanicalEngineering), ResearchGate, engineering Discord servers

---

## 4. The Core Message (use this in every post)

> **"99% of people interested in composites have no access to the tools aerospace companies
> use. OpenComposites gives them the knowledge and AI design tools — for free, forever."**

Variations by audience:
- **Makers:** "Design your first carbon fibre part without buying a $15,000 software licence"
- **Drone builders:** "AI-guided composites design for your airframe — open source, no paywalls"
- **Students:** "Free reference-grade composites knowledge base — 56 articles, CC BY 4.0"

---

## 5. Phase 1 — Seed Organic Reach (Week 1–2, zero cost)

### 5.1 Reddit Posts

Post to these subreddits in this order (most relevant first):

**r/DIYComposites**
- Tone: casual, enthusiastic, builder-to-builder
- Angle: "I built a free tool because I was frustrated by paywalls"
- Include a screenshot of the AI analysis on a real part

**r/compositesmanufacturing**
- Tone: professional but accessible
- Angle: the knowledge base and its CC BY 4.0 licence
- Mention the LLM/RAG structure — this community will appreciate it

**r/AerospaceEngineering**
- Tone: engineering-focused
- Angle: CLT calculator + failure criteria + open-source knowledge base

**r/Multicopter or r/fpv**
- Tone: drone-builder specific
- Angle: design your own carbon frame / arm with AI-guided laminate selection

**r/DIY**
- Tone: very accessible, non-technical opening
- Angle: "Built a free AI tool to help with carbon fibre parts"

**r/engineering**
- Tone: "here's something useful I/we made"

**Suggested post structure for Reddit:**
```
Title: I built a free open-source AI tool for composites design — no Fibersim or CATIA needed

Body:
Background: [short personal/company context]

What it does:
- Upload/describe your part → AI gives you material + process recommendation
- Full knowledge base (56 articles, plain language, CC BY 4.0)
- CLT calculator, sandwich panel analyser, cost estimator

Why free: [the 99% problem — composites knowledge is locked behind expensive tools]

Link: https://opencomposites.addcomposites.com
GitHub: [link]

Feedback welcome — especially from people who've actually tried to design with composites before.
```

---

### 5.2 Hacker News (Show HN)

Submit as a **Show HN** post. HN loves:
- Open source
- Free tools solving real problems
- RAG-ready knowledge bases
- Anything that democratises expensive professional tools

**Suggested title:**
`Show HN: OpenComposites – free AI composites design tool with open-source knowledge base`

**Body (first comment from OP):**
```
I work at Addcomposites (we make AFP robots). We kept getting asked composites design questions by makers and small startups who didn't have access to tools like Fibersim or CATIA — software that costs $15k–$150k/year.

So we built this: a free AI-powered composites design platform with a plain-language knowledge base (56 articles, CC BY 4.0, structured for LLM retrieval).

You can:
- Describe or upload a photo of your composite part → get a manufacturing plan
- Use the CLT calculator, sandwich panel analyser, or bolted joint tool
- Search 56 knowledge base articles covering fibres, resins, manufacturing, failure analysis

The AI analysis uses Claude (BYOK — bring your own API key).

Knowledge base repo: [link] — structured specifically for RAG, feel free to use it.
Live app: https://opencomposites.addcomposites.com

Happy to answer questions about the composites side or the architecture.
```

---

### 5.3 LinkedIn

Post from both the **Addcomposites company page** and **Pravin's personal profile**.

**Suggested post:**
```
We just open-sourced a composites design platform — and it's free.

Why? Because most people interested in composites (makers, drone startups, junior engineers) have zero access to the tools aerospace companies use. Fibersim, CATIA Composites — great software, but $15,000+ per year.

OpenComposites gives them:
→ AI-guided material selection and process recommendation
→ CLT calculator and laminate design tools
→ 56 knowledge base articles in plain language (CC BY 4.0)
→ Cost estimator, sandwich panel and bolted joint analysis

It's built on an open-source knowledge base structured specifically for LLM retrieval — so Claude, ChatGPT, Gemini, any LLM can search it and give reliable composites answers.

Try it free: https://opencomposites.addcomposites.com
GitHub: [link]

What composites questions are you seeing go unanswered?

#composites #carbonfibre #opensource #manufacturing #aerospace #eVTOL #drones
```

---

## 6. Phase 2 — Community Integrations (Week 2–4)

### 6.1 GitHub
- Add the live app URL prominently to the README of both repos
- Submit to `awesome-engineering` and `awesome-composites` lists (search GitHub for these)
- Add to `awesome-selfhosted` if applicable
- Star the repo yourself + ask team to star

### 6.2 Specific Forums and Communities
| Community | Platform | Approach |
|-----------|----------|----------|
| CompositesWorld | Web forum | Post about the knowledge base specifically |
| eVTOL Insights | Newsletter/community | Pitch for a feature or mention |
| RCGroups | Forum | Drone frame design angle |
| IntoFPV | Forum | Carbon frame design tool |
| Engineering Discord servers | Discord | Share in #resources or #tools channels |
| ResearchGate | Social | Share as a project page |

### 6.3 YouTube Demo Video
Even a 2-minute Loom/screen recording works. Show:
1. Open the app — it opens in light mode, clean UI
2. Type: "I want to design a carbon fibre drone arm, 200mm long, takes 50N lateral load"
3. Show the AI output — material recommendation, process, layup
4. Click into a knowledge base article — show the depth of content

Upload to YouTube with title: `Free AI tool for carbon fibre part design (no Fibersim needed)`

---

## 7. Phase 3 — Credibility Content (Month 2+)

Write 2–3 short articles to build trust and drive ongoing traffic:

**Article 1 — "Why we open-sourced a composites knowledge base"**
- Tell the story: Addcomposites builds AFP robots, kept getting questions from small teams
- The 99% problem
- Why CC BY 4.0 and LLM-ready structure
- Publish on Medium + LinkedIn + company blog

**Article 2 — Tutorial: "Design a carbon fibre drone arm — free, from scratch"**
- Walk through using the app end to end
- Include the knowledge base article on fibre types for context
- Show the CLT output
- Screenshot-heavy, practical
- Publish on Medium + share to drone communities

**Article 3 — "What the 10% rule in composites actually means"**
- Thought leadership — pull from the knowledge base article
- Short, educational, links back to the full article on the app
- Good for LinkedIn engagement

---

## 8. Before You Post Anywhere — Checklist

Before any public promotion, verify these manually:

- [ ] App opens in **light mode** by default (fixed — confirmed)
- [ ] AI analysis on a **simple test case** gives a good answer (try: "carbon fibre bicycle seatpost, takes 200N in bending")
- [ ] Knowledge base search for **"ply drop-off"** returns relevant results
- [ ] All links in the footer work (GitHub, Contribute, Report an Error)
- [ ] The GitHub repos are **public** (not private)
- [ ] README on both repos has the live app link front and centre

---

## 9. Key Differentiators to Emphasise

These are what make OpenComposites genuinely different — use them in messaging:

| Differentiator | Why it matters |
|---|---|
| **Free forever** | No freemium trap, no trial, no credit card |
| **Open source** | Engineers trust it more; can self-host |
| **CC BY 4.0 knowledge base** | Can be used in other projects, LLM training, RAG pipelines |
| **LLM/RAG structured** | Any AI can use it — this is a unique technical angle |
| **BYOK model** | Users control their own AI spend; no API cost for Addcomposites |
| **Built by AFP experts** | Addcomposites makes industrial robots — credibility matters |
| **Covers the full workflow** | Not just a calculator; material → process → laminate → cost |

---

## 10. What NOT to Say

- Don't oversell the AI output as "engineering-grade" — it's preliminary guidance
- Don't promise it replaces a composites engineer — the disclaimer is intentional
- Don't claim it competes with Fibersim/CATIA feature-for-feature — different market
- Don't post generic "check out my tool!" without providing value in the post itself

---

## 11. Company Context for Agent

- **Company:** Addcomposites (https://www.addcomposites.com)
- **Core business:** AFP (automated fibre placement) software and hardware
- **Founder:** Pravin Luthada
- **GitHub org:** Addcomposites-github
- **Other free tools to cross-promote:**
  - AddStack — free CLT/laminate calculator: https://addstack.addcomposites.com
  - Resin Flow Simulator: https://resin-flow-simulator.addcomposites.com/
  - CRDS (rotor/sleeve design): https://composite-rotor-system.addcomposites.com/

OpenComposites sits at the awareness/education layer — it brings new users into the Addcomposites ecosystem and demonstrates expertise.

---

## 12. Files Relevant to Marketing

| File | What's in it |
|------|-------------|
| `README.md` | Public-facing project intro — review before linking |
| `CONTRIBUTING.md` | How people contribute — mention in community posts |
| `knowledge/` | The 56 articles — source material for content ideas |
| `PRODUCT_ROADMAP.md` | What's coming — useful for "what's next" posts |

---

## 13. Quick Summary of Actions for Agent

```
Week 1:
  [ ] Post on r/DIYComposites
  [ ] Post on r/compositesmanufacturing
  [ ] Submit Show HN to Hacker News
  [ ] Post on LinkedIn (company + personal)
  [ ] Post on r/AerospaceEngineering

Week 2:
  [ ] Post on r/Multicopter / r/fpv
  [ ] Post on r/DIY and r/engineering
  [ ] Submit to GitHub awesome lists
  [ ] Post in 2–3 Discord engineering servers
  [ ] Record a 2-minute Loom demo

Week 3–4:
  [ ] Reach out to CompositesWorld forum
  [ ] Reach out to eVTOL Insights for a mention
  [ ] Post on RCGroups and IntoFPV
  [ ] Draft "Why we open-sourced..." article

Month 2+:
  [ ] Publish tutorial article on Medium
  [ ] Publish thought leadership piece on LinkedIn
  [ ] Follow up on best-performing Reddit/HN posts
```

---

> **The single most important post is the Show HN.** If it gets traction, everything
> else follows. Write that one carefully and time it for a Tuesday–Thursday morning
> (9–11am US Eastern time) for maximum visibility.
