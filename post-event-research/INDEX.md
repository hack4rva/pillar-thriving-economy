# Post-Event Research Index — A Thriving Economy

**Pillar:** A Thriving Economy
**GitHub:** [hack4rva/pillar-thriving-economy](https://github.com/hack4rva/pillar-thriving-economy)
**Problem Statements:**
- PS1: MBE Contracting Discovery — Help minority-owned businesses identify and understand City contracting opportunities
- PS2: Small Business Navigation — Help first-time entrepreneurs understand what steps to take to start a business in Richmond

**For AI agents:** Read this file to locate any post-event research artifact. Do not list the directory.

---

## Shared Research (Cross-Demo, Per Problem Statement)

| Dir | JTBD | Pain Points | Prior Art |
|-----|:----:|:-----------:|:---------:|
| [`_shared-mbe-contracting/`](_shared-mbe-contracting/) | ✅ | ✅ | ✅ |
| [`_shared-small-business/`](_shared-small-business/) | ✅ | ✅ | ✅ |

These files synthesize the problem statement across all demos in that PS. Read them before reading any per-project file.

---

## Per-Project Research Inventory

| Project | Problem Statement | JTBD | Pain | Prior Art | Solution Ideas |
|---------|------------------|:----:|:----:|:---------:|:--------------:|
| [`career-bridge/`](career-bridge/) | Misaligned (Families) | ✅ | ✅ | — | — |
| [`ibuild/`](ibuild/) | PS2: Small Business | ✅ | ✅ | — | — |
| [`ombd-proactive-match-dashboard/`](ombd-proactive-match-dashboard/) | PS1: MBE Contracting | ✅ | ✅ | — | — |
| [`richmond-business-launch-wizard/`](richmond-business-launch-wizard/) | PS2: Small Business | ✅ | ✅ | — | — |
| [`richmond-contract-navigator/`](richmond-contract-navigator/) | PS1: MBE Contracting | ✅ | ✅ | — | — |
| [`tradepath-rva/`](tradepath-rva/) | PS1: MBE Contracting | ✅ | ✅ | — | — |
| [`vendor-onboarding-wizard/`](vendor-onboarding-wizard/) | PS1: MBE Contracting | ✅ | ✅ | — | — |
| [`you-get-what-you-give/`](you-get-what-you-give/) | PS2: Small Business | ✅ | ✅ | — | — |

**Note:** `career-bridge` is misaligned — it addresses workforce pathways, which belongs in Thriving Families.

---

## Research Answers (`_research-answers/`)

Parallel AI queries that answered the JTBD open questions. Read `QUERY_MAP.md` to see which file answers which question.

| File | Problem Statement | Questions Answered |
|------|------------------|-------------------|
| [`QUERY_MAP.md`](_research-answers/QUERY_MAP.md) | Both | Full map of JTBD questions → query files |
| [`mbe_q1_system_data.md`](_research-answers/mbe_q1_system_data.md) | PS1 | Socrata contracts, BidNet API, OMBD, SWaM database |
| [`mbe_q2_usage_equity.md`](_research-answers/mbe_q2_usage_equity.md) | PS1 | User needs, equity gaps, outreach channels |
| [`mbe_q3_prior_art.md`](_research-answers/mbe_q3_prior_art.md) | PS1 | Comparable MBE tools, integration approaches |
| [`sb_q1_system_data.md`](_research-answers/sb_q1_system_data.md) | PS2 | SCC filings, BPOL, CZC, RVA business portal |
| [`sb_q2_usage_equity.md`](_research-answers/sb_q2_usage_equity.md) | PS2 | User needs, equity gaps, language access |
| [`sb_q3_prior_art.md`](_research-answers/sb_q3_prior_art.md) | PS2 | Small business navigator tools, comparable cities |

---

## Agent Reading Sequence

```
1. Read this file (INDEX.md) — orient
2. For PS1 context: _shared-mbe-contracting/jtbd_analysis.md
3. For PS2 context: _shared-small-business/jtbd_analysis.md
4. For a specific project: <project>/jtbd_analysis.md → <project>/pain_points.md
5. For answered research questions: _research-answers/QUERY_MAP.md → relevant query file
```
