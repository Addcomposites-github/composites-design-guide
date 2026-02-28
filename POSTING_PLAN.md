# POSTING_PLAN.md — OpenComposites Launch Promotion

> **Voice standard:** Engineer-to-engineer, problem-first, cost-aware, unpretentious.
> Informed by: Composites Central forum, Talk Composites forum, CompositesWorld,
> Easy Composites YouTube, Composites Weekly podcast.
> Core authentic vocabulary: wet out, dry spot, fibre volume, ramp ratio, racetracking,
> bridging, void, stacking sequence, hand layup, prepreg, CMH-17.

---

## Facts to use (verified)

| Claim | Value |
|-------|-------|
| Articles | **56** (10 topic areas) |
| Material systems | **15** (carbon, glass, aramid, basalt, thermoplastics) |
| In-app engineering tools | **8** (CLT, sandwich, bolted joint, stacking checker, cost estimator, materials browser, AI analysis, process selection) |
| License | **CC BY 4.0** |
| AI | **Claude via BYOK** (user brings own Anthropic key) |
| Built by | **Addcomposites** — AFP robot company, credible domain experts |
| Price | **Free forever** |

---

## Reddit Reality Check (verified via browser)

These subreddits from the original plan **do NOT exist**:
- ~~r/DIYComposites~~ — community does not exist on Reddit
- ~~r/compositesmanufacturing~~ — community does not exist on Reddit

**Key finding from community voice research:** The composites community primarily uses dedicated forums
(Composites Central, Talk Composites) rather than Reddit. Reddit audiences are engineers and makers
who are NOT composites specialists — useful for reach, but manage expectations.

**Verified real subreddits and sizes:**

| Subreddit | Subscribers | Audience fit |
|-----------|------------|-------------|
| r/Composites | 4,940 | ★★★★★ Most targeted, small |
| r/AerospaceEngineering | 131,281 | ★★★★☆ Good fit, professional |
| r/Multicopter | 118,393 | ★★★☆☆ Good for drone angle |
| r/engineering | 725,637 | ★★★☆☆ Broad, large |
| r/DIY | ~11M | ★★☆☆☆ Very broad, large |

**Also post to dedicated composites forums (better engaged audience than Reddit):**
- **Composites Central** — forum.compositescentral.org (practitioners, manufacturers)
- **Talk Composites** — talkcomposites.com ("The Forum for Advanced Composites")

---

## Platform Sequence and Dates

Post in this order. Do not post all at once.

| Day | Platform | Account | Post |
|-----|----------|---------|------|
| Day 1 (Tue) | **Reddit — r/Composites** | Personal Reddit | See post A below |
| Day 2 (Wed) | **Composites Central forum** | Forum account | See post G below |
| Day 3 (Thu) | **Reddit — r/Multicopter** | Personal Reddit | See post B below |
| Day 4 (Fri) | **Talk Composites forum** | Forum account | See post H below |
| Day 5 (Sat) | **LinkedIn** — Personal | Pravin Luthada | See LinkedIn personal below |
| Day 6 (Sun) | **LinkedIn** — Company | Addcomposites page | See LinkedIn company below |
| Day 8 (Tue) | **Reddit — r/AerospaceEngineering** | Personal Reddit | See post C below |
| Day 10 (Thu) | **Hacker News — Show HN** | HN account | See HN post below |
| Day 15 (Tue) | **Reddit — r/DIY** | Personal Reddit | See post E below |
| Day 18 (Fri) | **Reddit — r/engineering** | Personal Reddit | See post F below |
| Day 21+ | **Medium/LinkedIn article** | Personal | See article outline below |
| Day 21+ | **Twitter/X thread** | @addcomposites | See thread below |

---

## POST A — r/Composites (4,940 subscribers — most targeted)

**Audience:** Composites practitioners, hobbyists, and researchers. They know "wet out", "dry spot",
"ramp ratio". This is the most on-target Reddit audience even if small.
**What they care about:** Practical knowledge, reliable references, not marketing fluff.

**Flair:** Check sidebar for available flair when posting.

**Title:**
```
We open-sourced a composites design platform — 56 articles, CLT calc, AI analysis. Built by the AFP robot people.
```

**Body:**
```
I work at Addcomposites (we make AFP robots). We kept getting the same questions from people in
communities like this one:

"Which fibres should I use for a car diffuser?"
"My layup keeps getting dry spots — is it the infusion setup or the resin?"
"I want 0/45/-45/90 but I can't find anyone to check if my stacking sequence is right."

The people asking are completely capable of making good parts. They just don't have access to
the reference material — because most of it is locked inside $15,000-$150,000/year software
that no maker or small team can justify.

So we built OpenComposites and open-sourced the whole knowledge base.

**What it has:**

- **AI part analysis** — describe your part (geometry, load, budget) → get material recommendation,
  fibre orientation, process recommendation, and per-part cost estimate. AI is Claude via BYOK
  so you bring your own API key.

- **56 knowledge articles** — fibres, resin systems, wet layup, vacuum bagging, VARTM, AFP,
  stacking rules, ply drop-offs, failure modes, failure criteria, cost estimation. Plain English,
  no textbook walls. CC BY 4.0 so use it however you want.

- **CLT calculator** — ABD matrices, effective moduli, Tsai-Wu / Hashin / max stress failure checks

- **Sandwich panel analyser** — foam and honeycomb core design

- **Bolted joint tool** — bearing and bypass analysis

- **Materials database** — 15 material systems with E1, E2, strength properties
  (T300, IM7/8552, E-glass, S-glass, Kevlar 49, AS4/PEEK, basalt, NCF — all with source citations)

- **Cost estimator** — materials, labour, tooling

No account. No credit card. The knowledge base is on GitHub (CC BY 4.0 — fork it, quote it,
use it in your own project).

**Try it:** https://opencomposites.addcomposites.com
**Knowledge base:** https://github.com/Addcomposites-github/composites-design-guide

Genuinely would love feedback from people who've actually tried to design composite parts —
what's missing, what's wrong, what you wish existed.
```

---

## POST B — r/Multicopter

**Audience:** Drone builders, FPV pilots, multicopter engineers.
**What they care about:** Weight, stiffness, crash resistance, DIY builds.

**Title:**
```
Built a free AI tool for designing carbon fibre drone arms and frames — material selection, laminate calc, cost estimate
```

**Body:**
```
If you've ever tried to design a custom carbon frame or arm from scratch and not just buy
a tube off AliExpress, you've probably hit the same wall I kept seeing:

The knowledge is scattered, the tools are expensive, and nobody explains *why* certain
layups work better than others.

We built a free tool for this: https://opencomposites.addcomposites.com

**For drone/FPV use specifically:**

Type something like: "200mm arm, 50N lateral load at root, carbon fibre, lightest possible"

It gives you:
- Material recommendation (why IM7 vs T300 for your application)
- Fibre orientation + stacking sequence
- Manufacturing process (wet layup vs prepreg vs infusion for your part size)
- Per-arm cost estimate

There's also a CLT calculator so you can verify the laminate yourself —
stiffness (EI), failure margin, weight per metre.

And a 56-article knowledge base covering everything from "what actually is a woven
vs UD ply" to "how to design for minimum ply drop-off stress concentration."
CC BY 4.0, no account needed.

I know most drone frames are just pultruded or cut tube — but for anyone actually
designing custom structural parts (eVTOL, larger craft, custom monocoques),
this fills a real gap.

https://opencomposites.addcomposites.com
GitHub: https://github.com/Addcomposites-github/composites-design-guide

What layup failures have you run into on custom arms? Curious what's actually going wrong out there.
```

---

## POST C — r/AerospaceEngineering

**Audience:** Professional engineers, students, researchers.
**What they care about:** Technical rigour, proper references, not wasting their time.

**Title:**
```
Open-sourced a composites knowledge base and design tool — CLT calculator, 56 articles, CC BY 4.0
```

**Body:**
```
My team builds AFP systems at Addcomposites. We've open-sourced two things:

**1. Knowledge base** — 56 plain-English articles on composites design and manufacturing.
Covers CLT basics, stacking rules (symmetry, balance, 10% rule, ply drop-offs, splices),
failure criteria (Tsai-Wu, Hashin, max stress — when to use which), manufacturing processes
(wet layup through AFP/ATL), damage tolerance, sandwich structures, bolted and bonded joints,
and CATIA workflow concepts rewritten in tool-independent terms. CC BY 4.0.

Structured specifically for LLM retrieval — 100–400 word sections, front matter, tagged,
JSON-indexed — so any model (Claude, GPT, Gemini, local) can search it and give reliable answers.

**2. Web app** — https://opencomposites.addcomposites.com
- CLT calculator: ABD matrices, effective moduli, failure analysis
- Sandwich panel analyser
- Bolted joint analysis (bearing/bypass)
- AI part analysis using Claude (BYOK)
- 15-material database (T300, T700S, IM7/8552, AS4/3501-6, AS4/PEEK, E-glass, S-glass,
  Kevlar 49, basalt, NCF biaxial — with published property sources)

Everything is free. No paywall.

**GitHub:** https://github.com/Addcomposites-github/composites-design-guide

The target audience is people who don't have access to Fibersim, CATIA Composites, or HyperFiber
— makers, drone/eVTOL startups, junior engineers at Tier 2/3 suppliers, students. If you find
an error, open a PR. If a topic is missing, submit an article. Property sources are cited to
published datasheets and CMH-17 where available.

Happy to answer questions about the CLT implementation or knowledge base structure.
```

---

## POST D — r/compositesmanufacturing

**Audience:** Manufacturing engineers, process engineers, industry professionals.
**What they care about:** Process reliability, defect avoidance, practical knowledge.

**Title:**
```
Open-sourced a 56-article composites knowledge base — manufacturing, design rules, AFP/ATL, defects — CC BY 4.0
```

**Body:**
```
We've open-sourced a composites knowledge base that covers manufacturing from the
process-design side. Intended for people who need reliable reference material
without enterprise software access.

**Manufacturing coverage includes:**
- Wet layup, vacuum bagging, VARTM/resin infusion, prepreg + autoclave, RTM, filament
  winding, pultrusion, AFP/ATL (separate articles for each)
- Common defects — voids, dry spots, bridging, wrinkling, racetracking in infusion,
  spring-back — and how to mitigate them
- Post-processing: CNC trimming, inspection (NDT), assembly joining methods
- Manufacturing preparation: engineering-to-manufacturing model split, skin swapping,
  stagger origins, chimney effect avoidance
- Design for manufacture: ply shapes, accessibility, tool surface, mirror strategy

**Design rules:**
- Stacking sequences: symmetry, balance, 10% rule, consecutive ply limits
- Ply drop-offs: ramp ratios (1:8–1:20), limit contours, ETBS workflow
- Splice design: overlap/gap, no-splice zones, 3D multi-splice on curved surfaces
- Zone design: iso-thickness, rosette systems, transition zones
- Darts: when they're needed (double curvature), sizing, quality risks

**Also:**
- Failure modes and failure criteria (Tsai-Wu, Hashin, max stress)
- Damage tolerance: BVID, CAI, scarf vs stepped lap repair

CC BY 4.0. The whole thing is on GitHub.

Knowledge base: https://github.com/Addcomposites-github/composites-design-guide
Free web app (CLT, sandwich, bolted joint, AI analysis): https://opencomposites.addcomposites.com

What topics are under-documented that people actually keep getting wrong? Happy to add content.
```

---

## POST E — r/DIY

**Audience:** General DIY community. Many have never touched composites.
**Keep it simple. Don't assume any composites knowledge.**

**Title:**
```
Built a free tool to help people design their own carbon fibre parts — no expensive software needed
```

**Body:**
```
Carbon fibre is an incredible material — stiff, light, and not as hard to work with as
people think once you know the basics.

The problem is that the design knowledge is locked inside software that costs
$15,000–$150,000 per year. Out of reach for anyone doing DIY.

So I built a free alternative: https://opencomposites.addcomposites.com

You describe what you're making (a car splitter, a bike fork, a drone arm) and it gives you:
- Which fibres and resin to use, and why
- How to orient and stack the plies
- Which manufacturing method fits your setup (wet layup for most DIY, infusion for
  bigger parts, prepreg if you have oven access)
- A rough cost estimate

There's also a 56-article knowledge base in plain English — covering fibres, resins,
wet layup, vacuum bagging, defects and how to avoid them. No account needed, all free.

If you've been curious about trying carbon fibre but didn't know where to start —
this is where I'd point you.

https://opencomposites.addcomposites.com
```

---

## POST F — r/engineering

**Audience:** Mixed engineering disciplines. Respectful of technical depth.
**Frame as: open-source tool from domain experts, not a startup announcement.**

**Title:**
```
Open-sourced a composites design platform — CLT calculator, 56-article knowledge base, AI analysis (BYOK)
```

**Body:**
```
My team makes AFP robots at Addcomposites. We built an open-source composites design
platform and want to share it with the engineering community.

**The gap we're filling:**
Most composites design knowledge lives in Fibersim, CATIA Composites, and similar tools
at $15k–$150k/year. Engineers at startups, Tier 2/3 suppliers, and students have no access
to it. We wrote and open-sourced the knowledge layer.

**What it includes:**

Knowledge base (CC BY 4.0, GitHub):
- 56 articles across 10 topic areas
- Fundamentals (CLT, failure modes, fibre types, resin systems)
- Design rules (stacking sequences, ply drop-offs, splice design, zone design)
- Manufacturing (every major process from wet layup to AFP)
- Structural analysis (sizing, failure criteria, buckling, sandwich, joints)
- Cost estimation and applications

Web app (free, no account):
- CLT calculator — ABD matrices, effective moduli, failure analysis
- Sandwich panel and bolted joint analysis
- AI part analysis using Claude (BYOK)
- 15-material database with published property sources
- Process selection guide and cost estimator

**Links:**
App: https://opencomposites.addcomposites.com
GitHub (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide

If you work in composites and find anything wrong, open an issue or PR.
Property citations are linked to published datasheets and CMH-17 where available.
```

---

---

## POST G — Composites Central Forum (forum.compositescentral.org)

**Audience:** Working composites professionals and experienced practitioners. This is where
people post "Infusion Dry Spot Repair" and "Tooling for prepreg" — real hands-on problems.
**Tone:** Peer-to-peer, technically honest. They will spot any inaccuracy.
**Where to post:** Create a new thread in the most relevant section (Resources / Tools / General).

**Subject:**
```
Free open-source composites knowledge base + design app — 56 articles, CLT calc, AI analysis (BYOK)
```

**Body:**
```
Hi all — I work at Addcomposites (AFP robot company). We've open-sourced a composites
knowledge base and built a free web app around it. Sharing here because this community
is exactly who it's designed for.

The problem that drove this: composites design knowledge — stacking rules, ply drop-off
ratios, failure criteria, manufacturing constraints — lives inside Fibersim and CATIA at
$15–150k/year. Small teams and individuals have no reliable reference. We wrote 56
plain-English articles and open-sourced them (CC BY 4.0).

**Knowledge base topics:**
- Fibre types and resin systems
- Stacking sequences (symmetry, balance, 10% rule, consecutive angle limits)
- Ply drop-offs (ramp ratios 1:8–1:20, ETBS workflow, no-drop-off zones)
- Splice design (overlap/gap, no-splice zones, 3D multi-splice on curved surfaces)
- Zone design (rosette systems, iso-thickness zones, transition zones)
- Dart design (double curvature, sizing, quality risks)
- Manufacturing processes: wet layup, vacuum bagging, VARTM, prepreg, RTM, AFP/ATL,
  filament winding, pultrusion
- Common defects: voids, dry spots, racetracking, bridging, wrinkling
- Failure criteria: Tsai-Wu, Hashin, max stress — when to use which
- Damage tolerance, repair (scarf, stepped lap, bolted doubler)
- Cost estimation (material, labour, tooling)
- Case studies: drone arm, bicycle fork, pressure vessel, car body panel

**Web app (free):**
- AI part analysis using Claude (BYOK — you bring your own Anthropic key)
- CLT calculator: ABD matrices, effective moduli, Tsai-Wu/Hashin/max stress
- Sandwich panel analyser
- Bolted joint analyser
- 15-material database (T300, T700S, IM7/8552, AS4/3501-6, AS4/PEEK, E-glass,
  S-glass, Kevlar 49, basalt, NCF biaxial — all with published property source citations)
- Cost estimator

App: https://opencomposites.addcomposites.com
GitHub (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide

Property values are sourced from published datasheets and CMH-17 where available.
If you find anything wrong or missing, open an issue — we want this to be accurate.

Happy to discuss the CLT implementation, knowledge base structure, or take questions
on composites design.
```

---

## POST H — Talk Composites Forum (talkcomposites.com)

**Audience:** "The Forum for Advanced Composites" — members at all levels, very practical.
Example threads there: "Hand Layup + Vacuum Bagging Techniques (doubts)" — unpretentious,
problem-solving tone. New members and veterans on the same thread.
**Tone:** Match their direct, helpful style. Acknowledge you're sharing something you built.

**Subject:**
```
Free composites design tool + knowledge base — 56 articles, CLT calc, AI analysis
```

**Body:**
```
Hi — sharing something we built that might be useful here.

I work at Addcomposites (we make AFP machines). Over the past few years we kept getting
the same questions from makers and small teams: which fibres, what stacking, which process,
how do I check if this laminate passes? All answerable questions — but the tools that
answer them properly are $15k+/year.

So we wrote a knowledge base (56 articles, CC BY 4.0) and built a free app around it.

**What the knowledge base covers:**
Fibre types, resin systems, wet layup, vacuum bagging, VARTM, prepreg, AFP/ATL,
stacking sequences, ply drop-offs, splices, zone design, darts, failure modes,
failure criteria (Tsai-Wu, Hashin, max stress), damage tolerance, repair methods,
cost estimation. 10 topic areas, plain English throughout.

**What the app does:**
- Describe your part → AI gives material recommendation, stacking sequence,
  process rec, cost estimate (uses Claude AI — BYOK)
- CLT calculator with ABD matrices and failure criteria
- Sandwich panel and bolted joint analysis
- 15-material database with published properties
- Cost estimator

Everything free. No account. CC BY 4.0 on the knowledge base.

App: https://opencomposites.addcomposites.com
GitHub: https://github.com/Addcomposites-github/composites-design-guide

If something is wrong in the articles, please say — property values are from published
datasheets and CMH-17. We want it to be reliable, not just plentiful.
```

---

## HACKER NEWS — Show HN

> **What is HN?** Hacker News (news.ycombinator.com) is the main community for tech founders,
> engineers, and open-source builders — ~5M+ monthly readers. A good "Show HN" post can drive
> thousands of technical visitors in a day and get the project indexed by AI training sets.
>
> **Best time to post:** Tuesday, Wednesday, or Thursday, 9–11am US Eastern time.
>
> **How to post:** Go to https://news.ycombinator.com/submit
> Select "Show HN" prefix in the title. Add the URL. Post immediately at the right time.
> Then reply to your own submission within 5 minutes with the first comment below.

**Title (must start with "Show HN:"):**
```
Show HN: OpenComposites – free AI composites design tool, open-source knowledge base (56 articles, CC BY 4.0)
```

**URL:** `https://opencomposites.addcomposites.com`

**First comment — post as OP immediately after submitting:**
```
Hi HN. I work at Addcomposites (we make AFP robots for industrial composites manufacturing).

The problem we kept seeing: engineers at startups and Tier 2/3 suppliers — and makers
building carbon fibre parts in their garage — have no access to the design tools that
aerospace companies rely on. Fibersim: ~$15k/year. CATIA Composites: ~$50k/year.
The knowledge lives inside those tools and doesn't get out.

So we built two things:

**1. An open-source knowledge base** — 56 plain-English articles on composites design
and manufacturing, CC BY 4.0, structured specifically for LLM retrieval
(100–400 word chunks, front matter, JSON-indexed). The idea is that Claude, ChatGPT,
Gemini, or any local model can search it reliably and answer composites questions.
GitHub: https://github.com/Addcomposites-github/composites-design-guide

**2. A free web app** — wraps the knowledge base with:
- AI part analysis: describe your part → material selection, stacking sequence,
  process rec, cost estimate. Uses Claude (BYOK — users bring their own Anthropic key,
  zero backend AI cost on our end)
- CLT calculator (ABD matrices, effective moduli, Tsai-Wu / Hashin / max stress)
- Sandwich panel analyser and bolted joint analyser
- 15-material database with published property sources
- Cost estimator

Stack: FastAPI backend, React + Vite + Tailwind CSS frontend, scikit-learn TF-IDF for
knowledge search, JSON data files for materials and processes.
App repo: https://github.com/Addcomposites-github/opencomposites-app

The BYOK model means we have no AI costs, no subscription, no reason to put up a paywall.
Everything else is static data and a Python backend.

We specifically designed the knowledge base chunks (100–400 words each, tagged, indexed
in JSON) to be usable as a RAG source by any LLM. If you're building an engineering
assistant and want reliable composites retrieval, feel free to use it.

Happy to answer questions about composites, the architecture, or the knowledge base structure.
```

---

## LINKEDIN — Pravin's Personal Profile

**Tone:** Personal, founder perspective, engineer who has seen the problem first-hand.

```
I spent years watching engineers get stuck on composites questions that I could answer
in five minutes.

The problem wasn't the engineers. It was that the answers lived inside software that
costs $15,000–$150,000 a year. Out of reach for anyone who doesn't work at a major
aerospace company.

A maker wanting to build a carbon fibre part for their car.
A drone startup with no composites person on the team.
A junior engineer at a Tier 2 supplier without access to institutional knowledge.

All of them would hit the same wall — and then either guess, or give up, or email
me with "what do I even do here?"

So we built something to fix that.

Today we're launching OpenComposites:

→ AI-guided material selection and process recommendation (describe your part, get a plan)
→ 56-article open-source knowledge base — fibres, resins, manufacturing, failure analysis,
  stacking rules — written in plain English, CC BY 4.0
→ CLT calculator with full ABD matrices and failure criteria (Tsai-Wu, Hashin, max stress)
→ Sandwich panel and bolted joint analysis
→ 15-material database with published property sources
→ Cost estimator

No account. No paywall. No subscription.

The knowledge base is also structured specifically for LLM retrieval — so Claude, ChatGPT,
Gemini, or any local model can search it and give reliable composites answers. As AI
assistants become how engineers actually look things up, the knowledge has to be findable.

App (free): https://opencomposites.addcomposites.com
GitHub (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide

If you know someone in composites who needs this — a student, a maker, an engineer at
a startup — please share it. This is the resource I wish had existed when I started.

#composites #carbonfibre #opensource #engineering #eVTOL #drones #aerospace #manufacturing
```

---

## LINKEDIN — Addcomposites Company Page

**Tone:** Slightly more formal than personal, but still direct. Company as institution, not corporate.

```
We just open-sourced a composites design platform. Here's why, and what's in it.

The composites industry has an access problem. The software that supports professional
design — Fibersim, CATIA Composites, HyperFiber — costs $15,000–$150,000 per year.
That puts design-grade knowledge out of reach for most of the people who want it:
makers, startups, students, junior engineers at Tier 2/3 suppliers.

At Addcomposites, we build AFP (Automated Fibre Placement) robots. We've spent years
in this domain. And we kept getting questions we could answer in five minutes — from
people who just didn't have anywhere reliable to look.

So we built OpenComposites and open-sourced the entire knowledge layer.

What it includes:

▸ 56-article knowledge base (CC BY 4.0) — composites fundamentals, design rules,
  manufacturing processes (wet layup through AFP), structural analysis, cost estimation,
  case studies. Written in plain English. Structured for LLM retrieval.

▸ AI-guided design — describe your part, get material selection, fibre orientation,
  process recommendation, and cost estimate. Powered by Claude (BYOK model).

▸ CLT calculator — ABD matrices, effective moduli, Tsai-Wu / Hashin / max stress
  failure analysis

▸ Sandwich panel and bolted joint analysis

▸ 15-material database with published property sources

▸ Cost estimator — materials, labour, tooling, consumables

Free. No account required. No paywall.

The knowledge base is also structured specifically for LLM retrieval — every article
is chunked, tagged, and JSON-indexed so any AI assistant can search it reliably.
As engineers increasingly use AI for technical lookup, composites knowledge needs
to be findable.

Try the app: https://opencomposites.addcomposites.com
GitHub (CC BY 4.0): https://github.com/Addcomposites-github/composites-design-guide

#composites #carbonfibre #opensource #AFP #advancedmanufacturing #aerospace #eVTOL
```

---

## TWITTER / X THREAD

**Post as a thread — reply to your own first tweet.**

**Tweet 1:**
```
We just open-sourced a composites design platform.

56 articles, CLT calculator, AI analysis, 15-material database.
No paywall. No account. CC BY 4.0.

Here's why we built it 🧵
```

**Tweet 2:**
```
The problem: composites design knowledge is locked inside software that costs
$15,000–$150,000/year.

Fibersim. CATIA Composites. HyperFiber.

99% of people who need it — makers, drone startups, junior engineers —
can't access it. So they guess. Or ask on forums and get inconsistent answers.
```

**Tweet 3:**
```
We make AFP robots at @addcomposites.

We kept getting the same five questions from people outside the industry:

"Which fibres should I use?"
"Is my stacking sequence OK?"
"What does this failure mode mean?"
"How much will this cost to make?"

Questions we could answer in 5 minutes. But no reliable free resource existed.
```

**Tweet 4:**
```
So we wrote 56 articles, open-sourced them CC BY 4.0, and built a free app around them.

Topics: fibres, resins, wet layup, vacuum bagging, VARTM, prepreg, AFP, RTM,
stacking rules, ply drop-offs, failure criteria, damage tolerance, cost estimation,
sandwich structures, bolted joints, case studies.

Structured for LLM retrieval — Claude, GPT, Gemini, local models can all search it.
```

**Tweet 5:**
```
The app:

→ AI part analysis (describe part → get material + process rec + cost estimate)
→ CLT calculator with ABD matrices and failure criteria (Tsai-Wu, Hashin, max stress)
→ Sandwich panel analyser
→ Bolted joint analyser
→ 15-material database with published property sources

AI uses Claude — BYOK, users bring their own key.
```

**Tweet 6:**
```
Free. Forever.

No account. No credit card. No subscription.

The knowledge base is CC BY 4.0 — use it in your thesis, fork it for your domain,
have your AI assistant index it, contribute an article.

App: https://opencomposites.addcomposites.com
GitHub: https://github.com/Addcomposites-github/composites-design-guide
```

---

## MEDIUM / LINKEDIN ARTICLE — Tutorial

**Title:** `How to design a carbon fibre drone arm — for free, in 10 minutes`

**Outline (write ~800 words):**

1. **Setup** (50 words): you want a custom arm, tubes off AliExpress don't fit your layout,
   and you have no idea what layup you need. That's where this starts.

2. **The usual wall** (80 words): the software that does this properly costs more than
   your whole drone budget. Fibersim. CATIA. Not an option.

3. **What we'll use** (30 words): OpenComposites. Free. Link. No account.

4. **Step 1 — Describe the part** (150 words):
   Walk through what to type. "200mm arm, root takes 50N lateral load from prop thrust
   plus motor weight, carbon fibre, I want it as light as possible without going past
   1% failure margin in Tsai-Wu."
   Show what happens when you submit.

5. **Step 2 — Read the AI recommendation** (150 words):
   Walk through the output: why it picked T700S/Epoxy, why [0/45/-45/90]s, why VARTM
   vs wet layup for this geometry, what the cost estimate means in practice.
   Note: this is preliminary guidance — verify the laminate yourself.

6. **Step 3 — Verify with the CLT calculator** (150 words):
   Open the CLT calculator. Enter the suggested layup. Check EI (bending stiffness),
   effective Ex, failure margins. Explain what each number means in plain English.

7. **Step 4 — Check the knowledge base** (80 words):
   Search "ply drop-off" — show the article. This is where you'd look up how to taper
   the arm toward the tip without creating a stress concentration.

8. **What next** (80 words):
   You now have a layup to start from, a manufacturing process to try, and a budget estimate.
   Link to wet layup article. Link to vacuum bagging article.
   Link to the GitHub repo (CC BY 4.0 — contribute if you find something wrong or missing).

---

## Pre-Posting Verification Checklist

Run through this **before posting on any platform:**

- [ ] App loads at https://opencomposites.addcomposites.com in a fresh browser window
- [ ] Type "carbon fibre drone arm 200mm 50N load" in Analyze → reasonable output appears
- [ ] Search "ply drop-off" in Knowledge Base → results appear and are clickable
- [ ] Open the CLT calculator → enters a simple input and runs
- [ ] GitHub repo is public and README matches what we say in posts
- [ ] All URLs in the posts work (open every link before posting)
- [ ] Slide numbers and article count claim = 56 (count if uncertain)
- [ ] Materials claim = 15 material systems (not "40+")

---

## Post-Posting Monitoring

After each post, check within 48 hours:

- **Reddit:** Sort by "New" in the subreddit — is the post visible? Any comments? Reply to every comment within 24 hours.
- **HN:** Check https://news.ycombinator.com/submitted?id=YOUR_USERNAME — any upvotes? Reply to all top-level comments within an hour of posting.
- **LinkedIn:** Reply to every comment within 24 hours. Note anyone tagging others in comments — those people are your next conversations.

---

## What's Prepared (files in this repo)

| File | Contents |
|------|---------|
| `POSTING_PLAN.md` | This file — all post copy + timeline |
| `PROMOTION_HANDOVER.md` | Original promotion brief (overview) |
| `VISUAL_CONTENT_HANDOVER.md` | Carousel slide scripts, video scripts, design specs |
| `marketing/opencomposites-carousel.pptx` | 10-slide PowerPoint carousel (ready to export to images) |
| `scripts/create_carousel.py` | Script to regenerate the carousel |
