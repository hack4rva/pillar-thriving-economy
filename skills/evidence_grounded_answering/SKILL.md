# evidence_grounded_answering

Purpose: Answer user questions using only content actually present in this repository corpus, with explicit grounding and uncertainty marking.

## When To Use
- Any time a factual claim about Richmond programs, data, or services is being made
- When a user asks: "Does X exist?" "Is Y available?" "What does the City do about Z?"
- When an agent is about to state something it cannot directly verify from files it has read
- Before asserting that a dataset, program, service, or policy exists

## Inputs
- User question
- Files read in current context
- Optional: `_admin/evidence_log.md` for verified claims

## Outputs
- Answer grounded in specific file content
- Inline citations for each substantive claim
- Explicit uncertainty markers for unverified statements
- "Not found" statements when information is absent

## Process

### Step 1 — Establish What Has Been Read

Before answering, state (internally or explicitly) which files have been read. Only make claims from those files. Do not interpolate from general knowledge.

### Step 2 — Classify Each Claim

For every substantive claim in your answer, classify it:

| Status | Meaning | Marker |
|--------|---------|--------|
| `Confirmed` | Present in a source file AND verified in `_admin/evidence_log.md` | No marker needed; cite source |
| `Stated in corpus` | Present in a research file but not independently verified | `(per [filename])` |
| `Uncertain` | Implied or summarized but not directly stated in a file read | `[Uncertain: implied by X but not stated directly]` |
| `Not found` | Not present in any file read | `[Not found in files read]` |
| `Requires reading` | Likely in a specific file that has not been read | `[Requires reading: filename]` |

### Step 3 — Check the Evidence Log

For claims about:
- Specific portal URLs and their capabilities
- Processing timelines (e.g., SWaM certification takes ~60 business days)
- Data update cadences (e.g., Socrata monthly updates)
- Program availability (e.g., RVA Business Portal launched January 2025)
- Fee structures (e.g., BPOL $30 flat for 2 years)

Cross-check `_admin/evidence_log.md`. If the claim has an `E-` entry with `Confirmed` status, you can cite it with high confidence. If the claim is not in the log, mark it `[Stated in corpus: not independently verified]`.

### Step 4 — Formulate the Answer

Structure:
1. Direct answer to the question
2. Supporting evidence with citations
3. Explicit uncertainty statements
4. What is NOT covered (to set expectations)

### Step 5 — Apply the Anti-Fabrication Check

Before finalizing the answer, run this check:

- Does every named government program actually appear in a file I have read?
- Does every dataset I mentioned actually appear in D section files or `02_data/`?
- Does every URL I mentioned appear in `_admin/evidence_log.md` or a research file?
- Am I inventing specificity (exact percentages, exact dates) not present in the source?

If any check fails → remove or mark the claim as `[Unverified]`.

### Step 6 — State Scope Limits

At the end of the answer, state:
- What files were used to answer this question
- What topics the answer does NOT cover because relevant files were not read

## Required Language

When information is absent, use:
- "This repository does not contain that information."
- "I cannot verify that from the files I have read in this session."
- "That would require reading [specific file] which I have not yet loaded."
- "[Unverified]: this appears in a summary but I have not read the source file."

Do NOT use:
- "Likely..."  (without a citation)
- "Generally..." (as a hedge for an ungrounded claim)
- "It is common for cities to..." (implies external knowledge not in corpus)
- "I believe..." (implies opinion substituting for evidence)

## Example

**Question:** "Is there an API to get Richmond's contract award data?"

**Grounded answer:**

Yes. Richmond publishes contract award data through its Socrata open data platform at `data.rva.gov` (per `research/D1_data_inventory_contracting.md`; confirmed in `_admin/evidence_log.md` entry E-001). The platform supports SODA v2.1 and v3.0 API endpoints with CSV export capability (per `research/D2_data_formats_procurement.md`). The data is updated on a monthly cadence (confirmed: E-001).

The OpenGov platform at `procurement.opengov.com/portal/rva` provides current solicitations but `research/D1` does not describe a public bulk API for that portal (E-002 confirms the portal exists but notes it has no fixed update cadence). [Requires reading: `research/D4_data_structured_vs_manual.md` for a fuller assessment of structured vs. manual data access.]

*Files read for this answer: D1, D2, _admin/evidence_log.md*
*Not covered: D3 (business setup data), D5 (data quality), D4 (structured vs. manual)*

## Anti-Patterns

- Never state a City program exists without a source file citation
- Never quote a statistic (percentage, dollar amount, processing time) without a source
- Never say "Richmond has X program" based only on index.json summaries
- Never blend confirmed and uncertain claims in the same sentence without differentiation
