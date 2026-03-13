# Thriving Economy — Decision Funnel

This repo is a guided decision environment for teams working on the Thriving Economy pillar at the Richmond Civic Hackathon (March 27–29, 2026).

Journey stages
- Land → Orient → Choose → Run focused research → Compare MVP shapes → Lock scope → Build → Validate → Demo → Hand off

Three questions to answer fast
1) What problem are we actually solving? 2) Can we build something credible by Sunday? 3) What should we refuse to build?

---

## Phase 0: Landing and Framing

Goal
- Understand what this repo is and how to use it without “exploring” for two hours.

What this pillar is about
- Equitable access to City contracting opportunities and small-business formation/navigation; workforce pathways and entrepreneurship support under Thriving Economy.

What kinds of teams succeed here
- Teams that pick one user, one workflow, one credible data/doc base, and aim for a Sunday demo grounded in sources.

What this repo contains
- Pillar overview/alignment, problem statements, data/indexes, research prompts + runner, build guides, decision templates.

How to use it with a coding CLI
- Read just enough to decide, then use the Perplexity runner for evidence gathering, not research theater.

What a good project looks like
- Source-linked, narrow scope, credible demo, explicit limits.

What a bad project looks like
- Platform claims, eligibility/legal decisions, policy/integration dependencies, private data needs.

Admin quick links
- Master research hub: `research_notes.md`
- Evidence tracker: `evidence_log.md`
- Source inventory (CSV): `02_data/source_inventory.csv`
- Artifacts: `03_artifacts/`
  - Journeys: `03_artifacts/user_journeys.md`
  - Decision tree: `03_artifacts/small_business_decision_tree.md`
  - MBE data feasibility: `03_artifacts/mbe_data_feasibility.md`
  - Benchmark scan: `03_artifacts/benchmark_scan.md`
  - Prototype recommendations: `03_artifacts/prototype_recommendations.md`
  - Continuation plan: `03_artifacts/continuation_plan.md`

Verification workflow
- Add official URLs and dates in `evidence_log.md`; flip status to verified.
- Mirror verified sources into `02_data/source_inventory.csv` with access mode and key fields.
- Only after verification, promote content from research intake to the Executive Brief in `research_notes.md`.

Call to action
- Choose one: “I already know the rough problem” (Path A) or “I need help choosing” (Path B).

Path A — I already know the rough problem
- Skim Rapid Orientation (Phase 1), then go to Problem Selection (Phase 2) and Opportunity Framing (Phase 4).

Path B — I need help choosing a problem
- Start with Rapid Orientation (Phase 1) and proceed in order.

---

## Phase 1: Rapid Orientation (20–30 min)

Read just enough to build a shared mental model:
- `QUICKSTART.md`
- `00_core/00_pillar_overview.md`
- `00_core/01_map_alignment.md`
- `01_problem_space/02_targeted_problem_statements.md`

Filter for:
- user groups, pain points, what the City actually cares about
- problems that are software-shaped vs policy-shaped

Team checkpoint: draft a Working Direction note (keep it short)

```
## Working Direction
- Pillar: Thriving Economy
- Candidate problem:
- Likely user:
- Why it matters:
- Why it seems weekend-buildable:
- Biggest uncertainty:
```

You can use `99_templates/working_direction_note.md` to capture this.

---

## Phase 2: Problem Selection (30–45 min)

Files
- `01_problem_space/01_bluesky_problem_statements.md`
- `01_problem_space/02_targeted_problem_statements.md`
- `01_problem_space/03_user_personas.md`
- `00_core/04_solution_patterns.md`
- `05_prompts/01_problem_selection_prompt.md`

Decision rule — choose only if the problem has:
- a real user, an understandable workflow
- a plausible public data/document base
- a demoable artifact by Sunday

Output: a Decision Memo

```
## Chosen Problem
## User
## Why this one
## Why not the others
## Risks
```

Template: `99_templates/decision_memo.md`

---

## Phase 3: Research Spin‑Up (60–90 min)

Goal: gather just enough evidence to avoid fantasy software.

Use the runner to execute targeted prompts and capture findings:
- Perplexity runner: `05_prompts/perplexity_runner/` (see README)
- Research plan: `05_prompts/research/99_research_plan.md`
- Data index: `02_data/00_index.md`

Evidence Log format

```
## Evidence Log
### Confirmed
### Likely but unverified
### Missing
### Useful datasets
### Useful source documents
### Prior art
### Risks
```

Tip: parse URLs from API metadata; don’t ask for URLs in prompt text.

---

## Phase 4: Opportunity Framing (45–60 min)

Compare at least two MVP shapes before choosing.

Files
- `04_build_guides/01_mvp_shapes.md`
- `04_build_guides/02_recommended_architectures.md`
- `05_prompts/03_mvp_scoping_prompt.md`
- `05_prompts/06_risk_review_prompt.md`

Output

```
## MVP Options
1. …
2. …
3. …

## Recommended MVP
## Why
## What we are explicitly not building
```

---

## Phase 5: Scope Lock (45–60 min)

Pin down must‑haves, mockables, data, AI role, limits, and demo path.

Files
- `99_templates/project_one_pager_template.md`
- `04_build_guides/03_ai_usage_guidance.md`
- `00_core/03_guardrails.md`
- `04_build_guides/06_pitch_structure.md`

Key sentence
> By Sunday, we will show a prototype that helps [user] do [specific thing] using [specific data/docs], without pretending to do [dangerous overclaim].

---

## Phase 6–9: Build → Validate → Demo

Build
- Break work into FE/BE/data/content; assign source verification and demo owner.
- Keep AI constrained to explanation, retrieval, comparison, and guidance.

Validate
- Use risk review prompts and red flags; check source links and clarity.

Demo
- Follow `04_build_guides/05_demo_advice.md` and `04_build_guides/06_pitch_structure.md`.

---

## Appendix: Pillar Context and Rubric

Prepared by: Christian Markow, et al. (March 11, 2026)

Pillar Committee & Working Session
- Session: February 23, 2026, 1:30 PM – 3:30 PM
- Location: Lost Office Collaborative, 5000 Old Main St, Henrico, VA 23231

Participants
| Role               | Name                      | Organization / Title | Contact                   |
|--------------------|---------------------------|----------------------|---------------------------|
| Nonprofit Partner  | Martha Shickle            | PlanRVA              | martha@PlanRVA.org        |
| Nonprofit Partner  | Heather Lyne              | 1717 Collective      | hlyne@1717collective.org  |
| City Representative| Sharon Ebert              | DCAO                 | Sharon.Ebert@rva.gov      |
| Hack RVA           | Christian, Heather, Michael | Organizer team     | —                         |

Rubric Score Summary
| Statement                   | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Total | Band   |
|----------------------------|----|----|----|----|----|----|----|----|-------|--------|
| MBE Contracting            | 4  | 4  | 3  | 2  | 4  | 3  | 3  | 3  | 26    | Strong |
| Small Business Navigation  | 4  | 3  | 2  | 2  | 4  | 3  | 3  | 3  | 24    | Strong |

Dimension key: D1 Clarity | D2 Scope | D3 Data readiness | D4 Champion | D5 Population & impact | D6 Operating environment | D7 Success criteria | D8 Accessibility

Quick‑kill flags: both targeted statements lack a continuation pathway; Small Business Navigation has a procedural data gap.

Targeted Statement 1: Helping Minority‑Owned Businesses Identify Relevant City Contract Opportunities (Score 26/32 — Strong)
- Problem, context, constraints, success, gaps, and relevant open data are detailed in `01_problem_space/02_targeted_problem_statements.md`.

Targeted Statement 2: Small Business Navigation & Business Setup Friction (Score 24/32 — Strong)
- Problem, context, constraints, success, gaps, and relevant open data are detailed in `01_problem_space/02_targeted_problem_statements.md`.

Blue Sky Statements
- See `01_problem_space/01_bluesky_problem_statements.md`.

Prioritized Actions Before March 27, 2026
1) Document the business registration decision tree (turns Strong → Exceptional)
2) Name a departmental champion (continuation pathway)
3) Clarify procurement portal data format (API/CSV/scrape)
4) Link City Contracts Registry into the MBE statement
5) Specify expected output types in each statement
