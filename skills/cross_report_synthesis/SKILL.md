> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# cross_report_synthesis

Purpose: Synthesize findings from multiple research reports into a coherent answer while preserving source traceability and acknowledging uncertainty.

## When To Use
- A user asks a question that spans multiple reports or sections
- A team needs a summary of findings across a problem domain
- An agent needs to answer: "What does the research say about X across all relevant reports?"
- A user asks for a synthesis of risks, opportunities, or data sources

## Inputs
- User question or synthesis goal
- List of relevant report files (from `research_corpus_navigation` skill)
- Access to the source `.md` files

## Outputs
- Synthesized answer with per-claim source citations
- Tensions or contradictions noted explicitly
- Confidence level per claim (confirmed, likely, uncertain)
- List of reports read vs. reports not read
- Identified gaps where synthesis is incomplete

## Process

### Step 1 — Load Navigation Context

Before synthesizing, confirm you have run `research_corpus_navigation` or equivalent to identify which files are relevant. Do not synthesize from random file selections.

### Step 2 — Read Source Files Fully

For each file in the reading list:
1. Read the full `.md` file (not just summaries or frontmatter)
2. Note specific claims, data points, named entities, and source citations
3. Note the confidence level of each claim: does the report cite a primary source, or is it a secondary synthesis?

Do NOT synthesize from index summaries alone. Summaries are navigation aids, not authoritative content.

### Step 3 — Build a Claim Map

For each substantive claim you plan to include:

```
Claim: [statement]
Source: [filename, section heading if helpful]
Confidence: confirmed | likely | uncertain
Primary source: [URL or citation if available in the report]
Conflicts with: [other report + how it conflicts, if applicable]
```

### Step 4 — Identify Tensions and Gaps

Before writing the synthesis, explicitly check:
- Do any reports contradict each other? (If so, note both positions and their sources)
- Are there claims that appear in one report but are absent from others where you would expect them?
- Are there questions that the reports together still do not answer?

Flag gaps with: `[Gap: no report in this corpus addresses X]`

### Step 5 — Write the Synthesis

Structure:
1. **Scope**: which files were read, which were not
2. **Main findings**: 3–7 bullet points with inline citations
3. **Tensions**: any conflicting information and its sources
4. **Gaps**: what the corpus does not cover
5. **Confidence summary**: overall confidence in the synthesis

### Citation Format

Use inline citations:
- `(per research/A1_problem_landscape_mbe_contracting.md)`
- `(per _admin/evidence_log.md, E-001)`
- `[Unverified: not found in files read]`
- `[Uncertain: mentioned in summary but not verified in source]`

Never blend claims from different sources into a single uncited sentence.

### Step 6 — State What Was NOT Read

Always end the synthesis with:

```
Files read for this synthesis:
  - research/[FILE].md
  - research/[FILE].md

Files not read (possibly relevant):
  - research/[FILE].md — reason it may contain relevant information
```

This allows the user or a future agent to know the synthesis is incomplete if additional files exist.

## Anti-Patterns to Avoid

- **Never** synthesize from index.json summaries alone
- **Never** blend claims from different reports without attribution
- **Never** omit tensions or contradictions to make the answer cleaner
- **Never** claim the synthesis is complete if relevant unread files exist
- **Never** invent figures or statistics not present in the source files

## Example Output Structure

```
**Synthesis: MBE Data Availability for a Procurement Tool**

Files read: A1, D1, D2, D4, 02_data/source_inventory.csv
Files not read (possibly relevant): D3 (business setup data), D5 (data quality)

**Main Findings**
1. Richmond publishes contract award data via Socrata API at data.rva.gov with monthly update cadence (per D1, D2; confirmed in evidence_log E-001).
2. MBE utilization is documented at 3.43% vs. 17.93% availability across FY2017–2021 (per A1; primary source: MGT Consulting disparity study 2025).
3. OpenGov platform (procurement.opengov.com/portal/rva) provides current solicitations but no public API for bulk download (per D1; confirmed in evidence_log E-002).
4. iSupplier portal has a documented 2-minute session timeout and 3–5 business-day approval delay (per D1; confirmed in evidence_log E-004).

**Tensions**
- D1 states OpenGov publishes "all solicitations" but D4 notes data freshness varies and some historical contracts may be missing [Uncertain — D5 data quality report not yet read].

**Gaps**
- [Gap: no report read addresses whether the Socrata contract dataset includes MBE/ESB classification flags, which would be needed for a filtering tool]

**Confidence: Moderate** — main findings confirmed; D5 not read, so data quality claims are incomplete.
```
