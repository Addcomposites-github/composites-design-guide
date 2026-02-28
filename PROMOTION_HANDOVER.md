# PROMOTION_HANDOVER.md — OpenComposites Marketing Agent

> **For:** A new Claude Code agent taking over promotion work
> **Date:** 2026-02-27
> **Build status:** Complete. App is live. Your job is promotion only.

---

## What You Are Promoting

**OpenComposites** — a free, open-source AI composites design platform.

- **Live app:** https://opencomposites.addcomposites.com
- **Knowledge base repo:** https://github.com/Addcomposites-github/composites-design-guide
- **App repo:** https://github.com/Addcomposites-github/opencomposites-app

### One-line pitch
> "Free AI composites design platform — material selection, laminate design, cost estimation,
> and a 56-article open-source knowledge base. No Fibersim, no CATIA, no paywall."

### Why people care
99% of people interested in composites — makers, drone engineers, students, startup engineers
— have no access to the $15k–$150k/year tools that aerospace companies use.
OpenComposites fills that gap, for free, forever.

### Built by
[Addcomposites](https://www.addcomposites.com) — a company that makes AFP (automated fibre
placement) robots. They know composites. This is credible.

---

## What the App Does (know this before you write anything)

| Feature | What it does |
|---------|-------------|
| AI part analysis | Describe or photo a part → get material + process recommendation |
| Knowledge base | 56 plain-language articles, searchable, CC BY 4.0 |
| CLT calculator | Classical Laminate Theory — ABD matrices, effective moduli |
| Sandwich panel analyser | Core + face sheet design and optimisation |
| Bolted joint analyser | Joint sizing and bearing/bypass analysis |
| Cost estimator | Per-part cost including materials, labour, tooling |
| Materials browser | 15 material systems (carbon, glass, aramid, basalt, thermoplastics) — properties and recommendations |

AI uses Claude (Anthropic) via **BYOK** — users bring their own API key.
Everything else works without an API key.

---

## Target Audiences

| Audience | Pain point | Message |
|----------|-----------|---------|
| **Makers / hobbyists** | No idea where to start with carbon fibre | "Design your first CF part without a $15k software licence" |
| **Drone / eVTOL engineers** | No composites background, tight budgets | "AI-guided laminate design for your airframe — open source" |
| **Junior engineers / students** | No access to institutional knowledge or tools | "Reference-grade composites knowledge base, free forever" |

---

## Your Task List

Work through these in order. Each section below has the content ready to post or produce.

---

## Task 1 — Reddit Posts

Post to each subreddit below. Use the template, customise the opening line per community.
Do NOT post all on the same day — spread over 5–7 days.

### Base template (adapt opening for each sub)

```
Title: [see per-subreddit titles below]

[Opening line tailored to the community]

What it does:
- Describe or upload a photo of your composite part → AI gives you material selection,
  process recommendation, and step-by-step layup instructions
- 56 plain-language knowledge articles (fibres, resins, manufacturing, failure analysis)
  — CC BY 4.0, structured for LLM search
- CLT calculator, sandwich panel analyser, bolted joint tool, cost estimator

Why free: most composites knowledge is locked behind $15k–$150k/year software.
We think that's wrong. So this is free, open source, forever.

Try it: https://opencomposites.addcomposites.com
Source: https://github.com/Addcomposites-github/composites-design-guide

Would love feedback — especially from people who've actually tried to design
composite parts before.
```

### Per-subreddit customisation

**r/DIYComposites**
- Title: `Free AI tool for composite part design — material selection, process rec, and a 56-article knowledge base`
- Opening: `Been building composites tools at Addcomposites for a while. Kept getting questions from makers who had no idea where to start — and no budget for Fibersim. So we built this.`

**r/compositesmanufacturing**
- Title: `Open-source composites knowledge base + AI design tool — CC BY 4.0, free forever`
- Opening: `We've open-sourced a 56-article composites knowledge base (CLT, ply drop-offs, AFP, infusion, failure criteria, cost estimation) and wrapped an AI design tool around it. Structured for LLM retrieval (RAG) so any model can search it.`

**r/AerospaceEngineering**
- Title: `Free CLT calculator + composites knowledge base — 56 articles, CC BY 4.0, open source`
- Opening: `Built a free composites design platform for people without access to Fibersim or CATIA. Includes a CLT calculator (ABD matrices, failure criteria), sandwich panel analyser, bolted joint tool, and a full knowledge base.`

**r/Multicopter**
- Title: `Free AI tool to design carbon fibre drone frames and arms — material selection + laminate calculator`
- Opening: `Designing a custom carbon frame or arm and not sure which layup to use? Built a free tool that gives you material recommendations, fibre orientation, and manufacturing process for your specific geometry and loads.`

**r/DIY**
- Title: `Built a free AI tool to help design carbon fibre parts — no expensive software needed`
- Opening: `Carbon fibre is amazing but the design knowledge is locked behind $15,000/year software. We built a free alternative.`

**r/engineering**
- Title: `Open-sourced a composites design platform — free AI analysis, CLT calculator, 56-article knowledge base`
- Opening: `My team builds AFP robots at Addcomposites. We kept seeing small teams and individual engineers struggle with composites design questions that we could answer in 5 minutes — but the tools to answer them properly cost $15k+/year. So we built this.`

---

## Task 2 — Hacker News (Show HN)

Submit at: https://news.ycombinator.com/submit

**Title:**
`Show HN: OpenComposites – free AI composites design tool with open-source knowledge base`

**URL:** `https://opencomposites.addcomposites.com`

**First comment (post immediately after submitting as OP):**
```
I work at Addcomposites (we make AFP robots for industrial composites manufacturing).

We kept getting the same questions from makers and small startups: "What fibre should
I use?", "How thick does my laminate need to be?", "What's the cheapest process for
my part size?" — questions that take 5 minutes to answer if you know composites, but
require $15k+/year software to answer properly.

So we built this:

**OpenComposites** — free AI composites design platform
- Describe or upload a part photo → get material selection, process recommendation,
  layup sequence, and cost estimate
- 56-article open-source knowledge base (plain language, CC BY 4.0, RAG-ready)
- CLT calculator (ABD matrices, failure criteria: Tsai-Wu, Hashin, max stress)
- Sandwich panel and bolted joint analysis
- Materials browser (carbon, glass, aramid — properties and cost)

The AI uses Claude (BYOK — bring your own key). Everything else works without one.

The knowledge base is structured specifically for LLM retrieval — each section is
100–400 words, tagged, and indexed. The idea is that any LLM (not just Claude) can
search it and give reliable composites answers.

Knowledge base repo (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide
App repo: https://github.com/Addcomposites-github/opencomposites-app

Happy to talk composites or architecture questions.
```

**Best time to submit:** Tuesday, Wednesday, or Thursday between 9–11am US Eastern time.

---

## Task 3 — LinkedIn Post

Post from Pravin Luthada's personal profile AND the Addcomposites company page.

```
We just open-sourced a composites design platform — and it's completely free.

The problem: 99% of people interested in composites have zero access to the tools
aerospace companies use. Fibersim, CATIA Composites, HyperFiber — great software,
but $15,000–$150,000 per year. Out of reach for makers, drone startups, and junior
engineers at Tier 2/3 suppliers.

So we built OpenComposites:

→ AI-guided material selection and process recommendation
→ CLT calculator with failure criteria (Tsai-Wu, Hashin, max stress)
→ Sandwich panel and bolted joint analysis
→ Cost estimator
→ 56-article knowledge base in plain language — CC BY 4.0, free to use anywhere

The knowledge base is also structured for LLM retrieval (RAG) — so Claude, ChatGPT,
Gemini, any LLM can search it and give reliable composites answers. We think that
matters as AI assistants become the first place engineers look things up.

Live app (no account needed): https://opencomposites.addcomposites.com
GitHub (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide

What composites questions are you seeing go unanswered?

#composites #carbonfibre #opensource #manufacturing #aerospace #eVTOL #drones #engineering
```

---

## Task 4 — GitHub Awesome Lists

Find and submit PRs to add OpenComposites to relevant awesome lists.

Search GitHub for these repos and open a PR adding the link:
- `awesome-engineering` (multiple exist — search GitHub)
- `awesome-cae` (computer-aided engineering)
- `awesome-selfhosted`
- `awesome-mechanical-engineering`

PR format (one line addition in the relevant section):
```markdown
- [OpenComposites](https://github.com/Addcomposites-github/opencomposites-app) - Free AI composites design platform with CLT calculator, material browser, and 56-article open-source knowledge base.
```

---

## Task 5 — Tutorial Article (Medium / LinkedIn Article)

Write and publish this article. Aim for 600–900 words with screenshots.

**Title:** `How to design a carbon fibre drone arm — for free, in 10 minutes`

**Structure:**
1. The problem (brief — 2 sentences on cost of composites tools)
2. What we need to design (simple: a 200mm arm, takes 50N lateral load)
3. Step 1 — open OpenComposites, describe the part
4. Step 2 — review the AI recommendation (material, fibre orientation, process)
5. Step 3 — use the CLT calculator to verify the laminate
6. Step 4 — check the knowledge base article on AFP or wet layup
7. Conclusion — link to the repo, CC BY 4.0 note, invite contributions

**Where to publish:**
- Medium (under Addcomposites publication if one exists, or personal)
- Cross-post to LinkedIn as an article
- Share the Medium link to the relevant Reddit communities above

---

## Task 6 — "Why We Open-Sourced This" Article

**Title:** `Why we open-sourced a composites knowledge base`

**Structure:**
1. Who we are (Addcomposites — AFP robots)
2. The questions we kept getting (makers, drone startups, junior engineers)
3. The 99% problem — why the knowledge is paywalled
4. What we built and why CC BY 4.0
5. The RAG angle — designed for LLMs to search
6. Invite: contribute an article, submit a correction, use it in your project

**Where to publish:**
- Medium
- LinkedIn article
- Dev.to (good audience for open source tools)

---

## Tone and Style Notes

- **Don't be corporate.** Write like an engineer talking to another engineer.
- **Lead with the problem**, not the product.
- **Include specifics.** "56 articles", "CC BY 4.0", "CLT calculator" — concrete details build trust.
- **Don't oversell.** The AI output is preliminary guidance. Always include this caveat when relevant.
- **Invite feedback.** End posts with a question or "what would you add?" — drives comments.

---

## Pre-Posting Checklist

Before posting anywhere, open the app and verify:

- [ ] App loads at https://opencomposites.addcomposites.com in **light mode**
- [ ] Type "carbon fibre drone arm 200mm 50N load" in the Analyze page → reasonable AI output
- [ ] Search "ply drop-off" in Knowledge Base → relevant articles appear
- [ ] Click an article → opens and renders correctly
- [ ] Footer links (GitHub, Contribute, Report an Error) all work

---

## Context Files in This Repo

If you need more detail on the product:

| File | Contents |
|------|---------|
| `MARKETING_HANDOVER.md` | Extended marketing strategy with more detail |
| `HANDOVER.md` | Full technical handover (build sessions, architecture) |
| `README.md` | Public-facing project intro |
| `CONTRIBUTING.md` | Contribution guide |
| `knowledge/` | The 56 articles themselves — read these for content ideas |
| `PRODUCT_ROADMAP.md` | Upcoming features |
