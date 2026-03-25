<div align="center">

# Thriving Economy Pillar

**Richmond Civic Hackathon · March 27–29, 2026**

[![Pillar](https://img.shields.io/badge/Pillar-Thriving_Economy-4c68d7)](#)  [![Stage](https://img.shields.io/badge/Stage-Decision_Funnel-00a38f)](#)  [![Focus](https://img.shields.io/badge/Focus-From_Idea_%E2%86%92_MVP-ff7a59)](#)

*A guided environment for choosing a credible, source-linked, weekend-buildable MVP — and avoiding fantasy software.*

</div>

---

## The Three Questions

> **1. What problem are we actually solving?**
> **2. Can we credibly demo this by Sunday?**
> **3. What should we refuse to build?**

Answer these before writing a line of code.

---

## The Challenge

**→ Full detail in [`CHALLENGE.md`](CHALLENGE.md).** Read it before anything else — it defines the two problems, the top blue sky vision, data constraints, and exactly how judges will score your solution.

### Problem 1: Helping Minority-Owned Businesses Identify Relevant City Contract Opportunities — 26/32 — Strong

> How might we use technology to help minority-owned businesses in Richmond more easily identify and understand City contracting opportunities that match their capabilities?

Build toward: Procurement opportunity finder with plain-language descriptions · Procurement jargon translator for first-time vendors · Vendor readiness guide · Business-type-to-opportunity matching interface

⚠ Existing procurement portal must remain the official source — surface it, don't replace it. Confirm data format (API, CSV, or scraping) before building. Must not make eligibility determinations.

---

### Problem 2: Small Business Navigation & Business Setup Friction — 24/32 — Strong

> How might we improve how emerging and home-based entrepreneurs start and register a business in Richmond so they understand the right steps, complete them in the right order, and connect to relevant City services?

Build toward: Small business setup navigator (step-by-step, plain language, correct sequence) · Business type wizard (answer questions → get your specific steps) · Staff or nonprofit workflow helper for referrals

⚠ The business registration decision tree (which permits apply to which business types, in what order) does not exist in this repository and must be built before a navigator can work. Start here.

---

### Top Blue Sky: Rebuilding the Pathway Into the Trades — 22/27 — Strong ★ Recommended

> How might we use technology to help more Richmond residents — especially from underrepresented communities — discover, prepare for, and persist in high-opportunity trades and technical careers?

Pick one phase of the lifecycle: **discover** (what trades careers exist and pay), **prepare** (what training programs are available), or **persist** (navigate apprenticeship barriers). Do not try to cover all three in a weekend.

---

### Pillar Award Rubric

| Category | Weight | Dominant question |
|----------|--------|-------------------|
| **Impact** | **5** | Does this directly address one of the two problems above? |
| User Value | 4 | Is there a specific real user? Does the prototype improve their experience? |
| Feasibility | 3 | Could this be piloted by a City department or economic development partner? |
| Innovation | 3 | Fresh thinking on procurement access or business navigation? |
| Execution | 3 | Does a working demo exist? Is the flow coherent? |
| Equity | 3 | Does it specifically reach minority-owned businesses and first-time entrepreneurs? |

Full rubric with scoring anchors and judge instructions: [`../RUBRIC.md`](../RUBRIC.md)

---

## Journey

```
Land → Orient → Choose → Research → Frame MVPs → Lock Scope → Build → Validate → Demo → Hand-off
```

**New team?** Start at [Quick Start](#quick-start).
**Already have a problem?** Jump to [Phase 4 — Opportunity Framing](#).

---

## Quick Start

*First 15–30 minutes:*

| Step | Action |
|------|--------|
| 1 | Read `CHALLENGE.md` — the two problems, top blue sky, and rubric (start here, not QUICKSTART.md) |
| 2 | Read `QUICKSTART.md` for the minimal path |
| 2 | Skim `00_core/00_pillar_overview.md` to understand the problem space |
| 3 | Read `01_problem_space/02_targeted_problem_statements.md` — two strong, scored problems ready to go |
| 4 | Fill out a 5-bullet Working Direction using `99_templates/working_direction_note.md` |
| 5 | **Choose your path:** already have a problem → Phase 2 & 4 · still exploring → start at Phase 1 |

---

## Repo Map

| Folder / File | What's in it |
|---------------|-------------|
| `00_core/` | Pillar overview, MAP alignment |
| `01_problem_space/` | Blue-sky + targeted problem statements (scored) |
| `02_data/` | Data index, source inventory |
| `03_artifacts/` | User journeys, decision trees, prototype recommendations, research notes |
| `04_build_guides/` | MVP shapes, architectures, demo advice |
| `research/` | 51 deep research reports (sections A–I + cross-cutting) |
| `skills/` | Hackbot skill modules (14 skills) |
| `99_templates/` | Working direction, decision memo, project one-pager, team profile |
| `getting-started/` | Event-day OpenCode + Featherless setup |
| `_admin/` | Internal tracking, evidence log, research prompts |

**Navigation files:**
| File | Purpose |
|------|---------|
| `CORPUS_GUIDE.md` | How to use the research corpus (humans + AI agents) |
| `manifest.json` | Machine-readable index of all significant files |
| `research/index.json` | Machine-readable index of all 51 research reports |
| `research/README.md` | Human-readable research table of contents |
| `MAINTENANCE.md` | How to add and update reports and metadata |

---

## Guardrails

| Rule | Why |
|------|-----|
| One user, one workflow, one data source | Scope that fits a weekend |
| No eligibility or legal determinations | Civic-tech liability trap |
| Cite official sources for every claim | Credibility with judges |
| AI = explanation, retrieval, comparison, guidance | Not a decision-maker |
| No policy changes or City system integrations | Out of scope for a hackathon |

---

## Decision Phases

<details open>
<summary><strong>Phase 0 — Landing & Framing</strong></summary>

**Goal:** Understand what this repo is and how to use it — without "exploring" for two hours.

**This pillar covers:**
- Equitable access to City contracting opportunities for minority-owned businesses
- Small business formation and navigation friction
- Workforce pathways into trades and technical careers
- Entrepreneurship support and ecosystem visibility

**Patterns that win:**
- Source-linked · Narrow scope · Credible demo · Explicit limits

**Patterns that lose:**
- Platform claims · Eligibility/legal decisions · Policy dependencies · Private data needs

**→ Choose Path A (have a problem) or Path B (need help choosing).**

</details>

<details open>
<summary><strong>Phase 1 — Rapid Orientation (20–30 min)</strong></summary>

Read just enough to build a shared mental model:

1. `QUICKSTART.md`
2. `00_core/00_pillar_overview.md`
3. `00_core/01_map_alignment.md`
4. `01_problem_space/02_targeted_problem_statements.md`

Filter for: user groups · pain points · what the City actually cares about · problems that are software-shaped vs. policy-shaped.

**Team checkpoint — Working Direction** (use `99_templates/working_direction_note.md`):

```
Pillar: Thriving Economy
Candidate problem:
Likely user:
Why it matters:
Why it seems weekend-buildable:
Biggest uncertainty:
```

</details>

<details>
<summary><strong>Phase 2 — Problem Selection (30–45 min)</strong></summary>

**Files:**
- `01_problem_space/01_bluesky_problem_statements.md`
- `01_problem_space/02_targeted_problem_statements.md`
- `_admin/05_prompts/01_problem_selection_prompt.md`

**Decision rule — choose only if the problem has:**
- A real user with an understandable workflow
- A plausible public data or document base
- A demoable artifact by Sunday

**Output:** Decision Memo (`99_templates/decision_memo.md`)

```
Chosen Problem:
User:
Why this one:
Why not the others:
Risks:
```

</details>

<details>
<summary><strong>Phase 3 — Research Spin-Up (60–90 min)</strong></summary>

**Goal:** Gather just enough evidence to avoid fantasy software.

| Resource | Location |
|----------|----------|
| Perplexity runner | `_admin/05_prompts/perplexity_runner/` |
| Research plan | `_admin/05_prompts/research/99_research_plan.md` |
| Data index | `02_data/00_index.md` |

**Evidence log structure** (`_admin/evidence_log.md`):

```
Confirmed · Likely but unverified · Missing
Useful datasets · Useful source documents · Prior art · Risks
```

> **Tip:** Parse URLs from API metadata — don't ask for URLs in prompt text.

</details>

<details>
<summary><strong>Phase 4 — Opportunity Framing (45–60 min)</strong></summary>

**Compare at least two MVP shapes before choosing.**

| Resource | Location |
|----------|----------|
| MVP shape templates | `04_build_guides/01_mvp_shapes.md` |
| Recommended architectures | `04_build_guides/02_recommended_architectures.md` |
| Risk review prompt | `_admin/05_prompts/06_risk_review_prompt.md` |

**Output:**

```
MVP Options:
1. …
2. …
3. …

Recommended MVP:
Why:
What we are explicitly NOT building:
```

</details>

<details>
<summary><strong>Phase 5 — Scope Lock (45–60 min)</strong></summary>

Use `99_templates/project_one_pager_template.md` to pin down must-haves, mockables, data sources, AI role, limits, and demo path.

**The key sentence:**

> *By Sunday, we will show a prototype that helps **[user]** do **[specific thing]** using **[specific data/docs]**, without pretending to do **[dangerous overclaim]**.*

</details>

<details>
<summary><strong>Phases 6–9 — Build → Validate → Demo</strong></summary>

**Build:** Break work into FE / BE / data / content. Assign source verification and demo owner. Keep AI constrained to explanation, retrieval, comparison, and guidance.

**Validate:** Use `_admin/05_prompts/06_risk_review_prompt.md`. Check source links and clarity.

**Demo:** Follow `04_build_guides/05_demo_advice.md`. 90 seconds: problem → user → flow → sources → limits → next.

</details>

---

## Verification Workflow

1. Add official URLs and dates in `_admin/evidence_log.md` → flip status to **Verified**
2. Mirror verified sources into `02_data/source_inventory.csv` with access mode and key fields
3. Promote verified findings into the Executive Brief in `03_artifacts/research_notes.md`

---

## Hackbot

Hackbot is the AI assistant built for this repo. It reconstructs context, runs research, and helps shape an MVP without inventing government programs or making legal claims.

| Resource | Location |
|----------|----------|
| Boot prompt | `HACKBOT_BOOT_PROMPT.md` |
| Agent spec | `AGENTS.md` |
| Team profile template | `99_templates/team_profile_template.md` |
| Skills | `skills/**/SKILL.md` |
| Corpus guide | `CORPUS_GUIDE.md` |
| Full file manifest | `manifest.json` |

**Team skills:** `repo_memory` · `problem_scoping` · `research_runner` · `dataset_mapper` · `opportunity_mapper` · `mvp_designer` · `risk_review` · `demo_coach` · `repo_librarian` · `continuity_planner`

**Research corpus skills:** `research_corpus_navigation` · `cross_report_synthesis` · `evidence_grounded_answering` · `report_update_protocol`

> For best results, create a team profile (`99_templates/team_profile_template.md`) so Hackbot can map tasks to roles and match your communication preferences.

---

## Appendix: Pillar Committee Context

<details>
<summary>Session notes — March 11, 2026</summary>

*Prepared by Christian Markow et al.*

**Working Session:** February 23, 2026, 1:30–3:30 PM · Lost Office Collaborative, 5000 Old Main St, Henrico, VA 23231

**Participants**

| Role | Name | Organization | Contact |
|------|------|-------------|---------|
| Nonprofit Partner | Martha Shickle | PlanRVA | martha@PlanRVA.org |
| Nonprofit Partner | Heather Lyne | 1717 Collective | hlyne@1717collective.org |
| City Representative | Sharon Ebert | DCAO | Sharon.Ebert@rva.gov |
| Hack RVA | Christian, Heather, Michael | Organizer team | — |

**Rubric Scores**

| Problem Statement | Score | Band |
|------------------|-------|------|
| MBE Contracting | 26/32 | Strong |
| Small Business Navigation | 24/32 | Strong |

*Dimensions: Clarity · Scope · Data readiness · Champion · Population & impact · Operating environment · Success criteria · Accessibility*

**Quick-kill flags:** Both statements lack a continuation pathway. Small Business Navigation has a procedural data gap.

**Prioritized actions before March 27:**
1. Document the business registration decision tree (Strong → Exceptional)
2. Name a departmental champion (continuation pathway)
3. Clarify procurement portal data format (API/CSV/scrape)
4. Link City Contracts Registry into the MBE statement
5. Specify expected output types in each statement

Full problem detail: `01_problem_space/02_targeted_problem_statements.md`

</details>
