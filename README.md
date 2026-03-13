<div align="center">

# Thriving Economy — Decision Funnel

Richmond Civic Hackathon • March 27–29, 2026

[![Pillar](https://img.shields.io/badge/Pillar-Thriving_Economy-4c68d7)](#)  
[![Stage](https://img.shields.io/badge/Stage-Decision_Funnel-00a38f)](#)  
[![Focus](https://img.shields.io/badge/Focus-From_Idea_%E2%86%92_MVP-ff7a59)](#)

</div>

This is a guided decision environment for teams working on the Thriving Economy pillar. It’s designed to help you quickly choose a credible, source‑linked, weekend‑buildable MVP—and avoid fantasy software.

Journey stages: Land → Orient → Choose → Research → Compare MVPs → Lock Scope → Build → Validate → Demo → Hand‑off

Three questions to answer fast: 1) What problem are we actually solving? 2) Can we credibly demo by Sunday? 3) What should we refuse to build?

---

## Table of Contents

1. Quick Start
2. Repo Map
3. Guardrails
4. Decision Phases
   - Phase 0: Landing & Framing
   - Phase 1: Rapid Orientation
   - Phase 2: Problem Selection
   - Phase 3: Research Spin‑Up
   - Phase 4: Opportunity Framing
   - Phase 5: Scope Lock
   - Phases 6–9: Build → Validate → Demo
5. Verification Workflow
6. Hackbot Helper
7. Appendix: Pillar Context & Rubric

---

## Quick Start

Do these first 15–30 minutes to get moving:

1) Read: `QUICKSTART.md`  
2) Skim: `00_core/00_pillar_overview.md` and `01_problem_space/02_targeted_problem_statements.md`  
3) Capture a 5‑bullet “Working Direction” using `99_templates/working_direction_note.md`  
4) Decide your path:
   - Path A — already have a rough problem: jump to Phase 2 and Phase 4
   - Path B — need help choosing: start at Phase 1 and proceed in order

---

## Repo Map

- Research hub: `research_notes.md`
- Evidence tracker: `evidence_log.md`
- Data index: `02_data/00_index.md`
- Source inventory (CSV): `02_data/source_inventory.csv`
- Artifacts: `03_artifacts/`
  - Journeys: `03_artifacts/user_journeys.md`
  - Decision tree: `03_artifacts/small_business_decision_tree.md`
  - MBE data feasibility: `03_artifacts/mbe_data_feasibility.md`
  - Benchmark scan: `03_artifacts/benchmark_scan.md`
  - Prototype recommendations: `03_artifacts/prototype_recommendations.md`
  - Continuation plan: `03_artifacts/continuation_plan.md`
- Build guides: `04_build_guides/`
- Prompts + runners: `05_prompts/`
- Templates: `99_templates/`

---

## Guardrails

- Pick one user, one workflow, and one credible data/doc base.
- Avoid eligibility/legal determinations and policy/integration dependencies.
- Always cite official sources. Log every claim in `evidence_log.md`.
- Keep AI constrained to explanation, retrieval, comparison, and guidance.

---

## Decision Phases

<details open>
<summary><strong>Phase 0 — Landing & Framing</strong></summary>

Goal: understand what this repo is and how to use it without “exploring” for two hours.

What this pillar is about:
- Equitable access to City contracting opportunities and small‑business formation/navigation; workforce pathways and entrepreneurship support under Thriving Economy.

Success patterns:
- Source‑linked, narrow scope, credible demo, explicit limits.

Anti‑patterns:
- Platform claims; eligibility/legal decisions; policy/integration dependencies; private data needs.

Admin quick links:
- Research hub: `research_notes.md`
- Evidence tracker: `evidence_log.md`
- Source inventory (CSV): `02_data/source_inventory.csv`
- Artifacts: see Repo Map below

Call to action: choose Path A or Path B.

</details>

<details open>
<summary><strong>Phase 1 — Rapid Orientation (20–30 min)</strong></summary>

Read just enough to build a shared mental model:
- `QUICKSTART.md`
- `00_core/00_pillar_overview.md`
- `00_core/01_map_alignment.md`
- `01_problem_space/02_targeted_problem_statements.md`

Filter for:
- user groups; pain points; what the City actually cares about
- problems that are software‑shaped vs policy‑shaped

Team checkpoint — Working Direction (use `99_templates/working_direction_note.md`):

```
## Working Direction
- Pillar: Thriving Economy
- Candidate problem:
- Likely user:
- Why it matters:
- Why it seems weekend‑buildable:
- Biggest uncertainty:
```

</details>

<details>
<summary><strong>Phase 2 — Problem Selection (30–45 min)</strong></summary>

Files:
- `01_problem_space/01_bluesky_problem_statements.md`
- `01_problem_space/02_targeted_problem_statements.md`
- `01_problem_space/03_user_personas.md`
- `00_core/04_solution_patterns.md`
- `05_prompts/01_problem_selection_prompt.md`

Decision rule — choose only if the problem has:
- a real user and understandable workflow
- a plausible public data/document base
- a demoable artifact by Sunday

Output: Decision Memo (`99_templates/decision_memo.md`)

```
## Chosen Problem
## User
## Why this one
## Why not the others
## Risks
```

</details>

<details>
<summary><strong>Phase 3 — Research Spin‑Up (60–90 min)</strong></summary>

Goal: gather just enough evidence to avoid fantasy software.

Use the runner to execute targeted prompts and capture findings:
- Perplexity runner: `05_prompts/perplexity_runner/` (see its README)
- Research plan: `05_prompts/research/99_research_plan.md`
- Data index: `02_data/00_index.md`

Evidence Log structure (log in `evidence_log.md`):

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

</details>

<details>
<summary><strong>Phase 4 — Opportunity Framing (45–60 min)</strong></summary>

Compare at least two MVP shapes before choosing.

Files:
- `04_build_guides/01_mvp_shapes.md`
- `04_build_guides/02_recommended_architectures.md`
- `05_prompts/03_mvp_scoping_prompt.md`
- `05_prompts/06_risk_review_prompt.md`

Output:

```
## MVP Options
1. …
2. …
3. …

## Recommended MVP
## Why
## What we are explicitly not building
```

</details>

<details>
<summary><strong>Phase 5 — Scope Lock (45–60 min)</strong></summary>

Pin down must‑haves, mockables, data, AI role, limits, and demo path.

Files:
- `99_templates/project_one_pager_template.md`

Key sentence:

> By Sunday, we will show a prototype that helps [user] do [specific thing] using [specific data/docs], without pretending to do [dangerous overclaim].

</details>

<details>
<summary><strong>Phases 6–9 — Build → Validate → Demo</strong></summary>

Build:
- Break work into FE/BE/data/content; assign source verification and demo owner.
- Keep AI constrained to explanation, retrieval, comparison, and guidance.

Validate:
- Use risk review prompts and red flags; check source links and clarity.

Demo:
- Follow `04_build_guides/05_demo_advice.md`.

</details>

---

## Verification Workflow

1) Add official URLs and dates in `evidence_log.md`; flip status to Verified.  
2) Mirror verified sources into `02_data/source_inventory.csv` with access mode and key fields.  
3) After verification, promote findings into the Executive Brief inside `research_notes.md`.

---

## Hackbot Helper

You can use Hackbot to reconstruct context, run research, and shape an MVP.

- Boot prompt: `HACKBOT_BOOT_PROMPT.md`
- Skills: `skills/**/SKILL.md` (repo_memory, problem_scoping, research_runner, dataset_mapper, opportunity_mapper, mvp_designer, risk_review, demo_coach, repo_librarian, continuity_planner)
- Team profile (recommended): `99_templates/team_profile_template.md`

Notes:
- Hackbot never invents government programs or legal eligibility. It cites official sources and encourages verification.
- For best results, create a team profile so Hackbot can map tasks to roles and follow your communication preferences.

---

## Appendix: Pillar Context & Rubric

<details>
<summary>Open context from the Pillar Committee session (March 11, 2026)</summary>

Prepared by: Christian Markow, et al. (March 11, 2026)

Pillar Committee & Working Session
- Session: February 23, 2026, 1:30 PM – 3:30 PM
- Location: Lost Office Collaborative, 5000 Old Main St, Henrico, VA 23231

Participants
| Role               | Name                        | Organization / Title | Contact                  |
|--------------------|-----------------------------|----------------------|--------------------------|
| Nonprofit Partner  | Martha Shickle              | PlanRVA              | martha@PlanRVA.org       |
| Nonprofit Partner  | Heather Lyne                | 1717 Collective      | hlyne@1717collective.org |
| City Representative| Sharon Ebert                | DCAO                 | Sharon.Ebert@rva.gov     |
| Hack RVA           | Christian, Heather, Michael | Organizer team       | —                        |

Rubric Score Summary
| Statement                  | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Total | Band   |
|---------------------------|----|----|----|----|----|----|----|----|-------|--------|
| MBE Contracting           | 4  | 4  | 3  | 2  | 4  | 3  | 3  | 3  | 26    | Strong |
| Small Business Navigation | 4  | 3  | 2  | 2  | 4  | 3  | 3  | 3  | 24    | Strong |

Dimension key: D1 Clarity | D2 Scope | D3 Data readiness | D4 Champion | D5 Population & impact | D6 Operating environment | D7 Success criteria | D8 Accessibility

Quick‑kill flags: both targeted statements lack a continuation pathway; Small Business Navigation has a procedural data gap.

Targeted Statement 1: Helping Minority‑Owned Businesses Identify Relevant City Contract Opportunities (Score 26/32 — Strong)
- Problem, context, constraints, success, gaps, and relevant open data are in `01_problem_space/02_targeted_problem_statements.md`.

Targeted Statement 2: Small Business Navigation & Business Setup Friction (Score 24/32 — Strong)
- Problem, context, constraints, success, gaps, and relevant open data are in `01_problem_space/02_targeted_problem_statements.md`.

Blue Sky Statements
- See `01_problem_space/01_bluesky_problem_statements.md`.

Prioritized Actions Before March 27, 2026
1) Document the business registration decision tree (turns Strong → Exceptional)  
2) Name a departmental champion (continuation pathway)  
3) Clarify procurement portal data format (API/CSV/scrape)  
4) Link City Contracts Registry into the MBE statement  
5) Specify expected output types in each statement

</details>
