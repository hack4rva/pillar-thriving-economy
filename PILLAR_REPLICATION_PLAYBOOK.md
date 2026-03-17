# Pillar Repo Replication Playbook

How to bootstrap a new hackathon pillar repository from nothing but a rubric evaluation document.

Pillar 4 (Thriving Economy) is the canonical template. All other pillar repos follow this structure.

---

## What exists in a complete pillar repo

```
00_core/
  00_pillar_overview.md        — Purpose, framing, useful/less-useful prototype directions
  01_map_alignment.md          — How this pillar connects to the MAP framework

01_problem_space/
  01_bluesky_problem_statements.md   — Aspirational/expansive framings with scores
  02_targeted_problem_statements.md  — 2 highest-scoring targeted problems, full detail

02_data/
  00_index.md                  — Guide to datasets relevant to this pillar
  source_inventory.csv         — Registry of all data sources (name, url, format, notes)

03_artifacts/
  user_journeys.md             — Journey maps for primary users
  prototype_recommendations.md — 3 seeded solution concepts with pros/cons
  benchmark_scan.md            — Comparable tools found nationally
  continuation_plan.md         — Post-hackathon partner pathways
  [pillar-specific].md         — One additional pillar-specific artifact

04_build_guides/
  01_mvp_shapes.md             — 4-5 MVP patterns with tradeoffs
  02_recommended_architectures.md — Tech stack options by MVP shape
  05_demo_advice.md            — Demo strategy guidance

05_prompts/
  01_problem_selection_prompt.md
  06_risk_review_prompt.md
  research/
    00_pillar_summary_context.txt
    01_master_research_prompt.txt
    90_top_10_research_questions.txt
    91_top_10_hypotheses_to_test.txt
    92_red_flags.txt
    93_missing_information_gaps.txt
    A1-A5_problem_landscape_*.txt    (5 files)
    B1-B5_users_*.txt                (5 files)
    C1-C5_services_*.txt             (5 files)
    D1-D5_data_*.txt                 (5 files)
    E1-E5_prior_art_*.txt            (5 files)
    F1-F5_opportunities_*.txt        (5 files)
    G1-G5_risks_*.txt                (5 files)
    H1-H5_mvp_feasibility_*.txt      (5 files)
    I1-I5_demo_guidance_*.txt        (5 files)
  perplexity_runner/
    config.yaml
    .env.example
    px_client.py
    run_one.py
    run_all.py
    Makefile
    README.md

99_templates/
  team_profile_template.md
  project_one_pager_template.md
  decision_memo.md
  working_direction_note.md

skills/
  repo_memory/SKILL.md
  problem_scoping/SKILL.md
  research_runner/SKILL.md
  research_search/SKILL.md
  dataset_mapper/SKILL.md
  opportunity_mapper/SKILL.md
  mvp_designer/SKILL.md
  risk_review/SKILL.md
  demo_coach/SKILL.md
  repo_librarian/SKILL.md
  continuity_planner/SKILL.md

scripts/
  list_skills.py
  run_all_deep_research.py
  test_px_deep_research.py

getting-started/
  (team onboarding materials)

CLAUDE.md                  — AI guide with pillar-specific role and guardrails
AGENTS.md                  — Hackbot agent spec (copy from P4, swap pillar name)
README.md                  — Decision funnel + repo map + rubric scores
QUICKSTART.md              — 6-step fast path for teams
HACKBOT_BOOT_PROMPT.md     — Hackbot conversational boot sequence
research_notes.md          — Unverified findings hub
evidence_log.md            — Verified sources tracker
VERIFICATION_TODO.md       — Verification checklist
.env.example               — Template for API keys
.gitignore
```

---

## Process (per pillar)

### Step 0 — Extract from rubric doc
Read `Pillar[N]_[Name]_RubricEvaluation.docx` and pull:
- Pillar name and 1-sentence theme
- All problem statements with scores (D1–D8 and total)
- Band ratings (Strong / Moderate / Needs work)
- Committee notes on gaps, constraints, quick-kill flags
- Names of problem statement authors

### Step 1 — Create repo
```bash
SLUG="pillar-[name]"
cd /Users/williamprior/Development/GitHub/hackathon/pillar-repos/$SLUG
```
(Repo already exists with just a LICENSE file)

### Step 2 — Copy reusable scaffolding from Pillar 4
```bash
P4=/Users/williamprior/Development/GitHub/hackathon/pillar-repos/pillar-thriving-economy

# Copy verbatim, then swap pillar name
cp $P4/AGENTS.md .
cp $P4/HACKBOT_BOOT_PROMPT.md .
cp -r $P4/99_templates/ ./99_templates/
cp -r $P4/skills/ ./skills/
cp -r $P4/05_prompts/perplexity_runner/ ./05_prompts/perplexity_runner/
cp -r $P4/scripts/ ./scripts/
cp $P4/.gitignore .
cp $P4/.env.example . 2>/dev/null || true
```

### Step 3 — Write pillar-specific files

**CLAUDE.md** — Role definition specific to this pillar's themes, guardrails, strong/weak solution patterns

**README.md** — Full decision funnel (phases 0–9), repo map, rubric scores table, quick-kill flags, appendix

**QUICKSTART.md** — 6-step fast path, 5 questions to answer, high-probability project types for this pillar

**00_core/00_pillar_overview.md** — Pillar purpose, why it matters, useful/less-useful prototype directions

**00_core/01_map_alignment.md** — MAP framework connection

**01_problem_space/01_bluesky_problem_statements.md** — Blue sky statements with scores and notes

**01_problem_space/02_targeted_problem_statements.md** — Top 2 targeted statements with full HMW framing, context, constraints, success criteria, gaps

**02_data/00_index.md** — Annotated list of relevant public datasets and APIs

**02_data/source_inventory.csv** — CSV registry: name, url, format, access_method, notes, verified

**03_artifacts/user_journeys.md** — 2–3 user journey maps for primary personas

**03_artifacts/prototype_recommendations.md** — 3–6 seeded concepts with feasibility, risks, demo pitch

**03_artifacts/benchmark_scan.md** — 3–5 comparable tools nationally, what worked/failed

**03_artifacts/continuation_plan.md** — Post-hackathon partners, artifacts worth continuing, next steps

**04_build_guides/01_mvp_shapes.md** — 4–5 MVP shapes: best-for, inputs, demo flow

**04_build_guides/02_recommended_architectures.md** — Tech stacks per MVP shape

**04_build_guides/05_demo_advice.md** — Demo clarity archetypes, credibility proof, useful framing

**research_notes.md** — Seed with 500–1000 words of unverified domain knowledge; mark [Unverified]

**evidence_log.md** — Empty tracker: columns: id, claim, source_url, verified_date, notes

**VERIFICATION_TODO.md** — Checklist of top 10 claims needing verification

### Step 4 — Write research prompt corpus

Create ~55 `.txt` files in `05_prompts/research/`. Each is a focused deep-research question (2–4 paragraphs). Format:

```
[Section Label] — [Descriptive Title]

[2-3 paragraphs: what to investigate, Richmond/Virginia context, what to look for]

Output
- Facts (with URLs)
- Inferences (clearly labeled)
- Unknowns (what cannot be verified publicly)
- [1-2 specific output requirements]
```

Files to create:
| Filename | Section | Focus |
|----------|---------|-------|
| 00_pillar_summary_context.txt | Context | Pillar overview and problem framing |
| 01_master_research_prompt.txt | Master | Comprehensive research framework |
| 90_top_10_research_questions.txt | Cross-cutting | 10 key questions to answer |
| 91_top_10_hypotheses_to_test.txt | Cross-cutting | 10 testable hypotheses |
| 92_red_flags.txt | Cross-cutting | Risk signals and warning signs |
| 93_missing_information_gaps.txt | Cross-cutting | Critical unknowns |
| A1_problem_landscape_[topic1].txt | A | Primary problem area, root causes |
| A2_problem_landscape_[topic2].txt | A | Secondary problem area |
| A3_problem_landscape_compare.txt | A | Compare both targeted statements |
| A4_problem_landscape_types.txt | A | Problem typology and categories |
| A5_problem_landscape_systemic.txt | A | Systemic/structural factors |
| B1_users_primary_persona.txt | B | Primary user persona |
| B2_users_secondary_persona.txt | B | Secondary user persona |
| B3_users_stakeholders_map.txt | B | Full stakeholder map |
| B4_users_stakeholder_priorities.txt | B | What each stakeholder needs |
| B5_users_staff_knowledge.txt | B | Staff/expert knowledge gaps |
| C1_services_landscape.txt | C | Existing programs and services |
| C2_services_front_doors.txt | C | Current front doors and pathways |
| C3_services_gaps.txt | C | Service gaps and blind spots |
| C4_services_fragmentation.txt | C | Fragmentation and duplication |
| C5_services_digital.txt | C | Digital service landscape |
| D1_data_primary_source.txt | D | Primary public data source |
| D2_data_secondary_sources.txt | D | Supporting data sources |
| D3_data_access_methods.txt | D | APIs, downloads, formats |
| D4_data_structured_vs_manual.txt | D | Structured vs. unstructured data |
| D5_data_quality.txt | D | Data quality and completeness |
| E1_prior_art_national.txt | E | Comparable tools nationally |
| E2_prior_art_patterns.txt | E | Solution pattern library |
| E3_prior_art_archetypes.txt | E | Tool archetypes relevant here |
| E4_prior_art_failures.txt | E | What has failed and why |
| E5_prior_art_weekend.txt | E | Weekend-viable prior art |
| F1_opportunities_ranked.txt | F | Ranked solution spaces |
| F2_opportunities_primary.txt | F | Primary problem's opportunity |
| F3_opportunities_secondary.txt | F | Secondary problem's opportunity |
| F4_opportunities_where_software.txt | F | Where software specifically helps |
| F5_opportunities_do_not_build.txt | F | Do-not-build list |
| G1_risks_ai_hallucination.txt | G | AI hallucination risks |
| G2_risks_harm_cases.txt | G | Harm cases and misuse scenarios |
| G3_risks_inclusion.txt | G | Inclusion and accessibility risks |
| G4_risks_bias.txt | G | Algorithmic and data bias |
| G5_risks_guardrails.txt | G | Practical guardrails and mitigations |
| H1_mvp_48hr_framework.txt | H | 48-hour viability framework |
| H2_mvp_primary_shape.txt | H | MVP shape for primary problem |
| H3_mvp_secondary_shape.txt | H | MVP shape for secondary problem |
| H4_mvp_minimums.txt | H | Minimum viable demo requirements |
| H5_mvp_scope_boundaries.txt | H | Scope limits and out-of-bounds |
| I1_demo_archetypes.txt | I | Demo clarity archetypes |
| I2_demo_primary_pitch.txt | I | Primary problem demo pitch |
| I3_demo_secondary_pitch.txt | I | Secondary problem demo pitch |
| I4_demo_credibility.txt | I | Credibility evidence for judges |
| I5_demo_framing.txt | I | Framing language and talking points |

### Step 5 — Initialize empty research/ directory

Create `research/README.md` and `research/index.json` (empty array) as placeholders. These will be populated when `scripts/run_all_deep_research.py` runs.

### Step 6 — Git commit
```bash
git add .
git commit -m "feat: initialize [pillar name] pillar repo from rubric evaluation"
```

---

## Pillar registry

| Slug | Pillar Number | Name | Rubric Doc |
|------|---------------|------|------------|
| pillar-thriving-economy | 4 | A Thriving Economy | Pillar4_ThrivingEconomy_RubricEvaluation.docx ✅ |
| pillar-thriving-city-hall | 1 | A Thriving City Hall | Pillar1_ThrivingCityHall_RubricEvaluation.docx |
| pillar-thriving-neighborhoods | 2 | Thriving Neighborhoods | Pillar2_ThrivingNeighborhoods_RubricEvaluation_1.docx |
| pillar-thriving-families | 3 | Thriving Families | Pillar3_ThrivingFamilies_RubricEvaluation.docx |
| pillar-thriving-inclusive-communities | 5 | Thriving and Inclusive Communities | Pillar5_InclusiveCommunities_RubricEvaluation.docx |
| pillar-thriving-built-environment | 6 | A Thriving and Sustainable Built Environment | Pillar6_BuiltEnvironment_RubricEvaluation.docx |
| pillar-city-storytelling | 7 | A City That Tells Its Stories | Pillar7_Stories_RubricEvaluation.docx |

---

## Not done by this playbook (future step)

Running the deep research:
```bash
cd 05_prompts/perplexity_runner
# Set PERPLEXITY_API_KEY in .env
cd ../..
python scripts/run_all_deep_research.py --delay 3
```

This generates `research/` outputs. Run after the repo is fully scaffolded.
