> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../docs/methodology.md) for details.

# Verification TODO (Admin)

Purpose: Track the minimum verification work to make seeded research production‑ready for teams.

Owner: Repo admin

## 1) Sources and Access Modes
- [x] Add official URL for City contracts dataset (Socrata) to `evidence_log.md` (E-001), set status to verified
- [x] Confirm SODA/OData endpoints and update `02_data/source_inventory.csv` (format, update frequency, key fields)
- [x] Add official OpenGov procurement portal URL (E-002); note export/scrape options
- [x] Identify eVA entry points relevant to Richmond entities (E-003); note access requirements
- [x] Add iSupplier vendor registration URL (E-004); confirm session timeout and required docs
- [x] Add OMBD MBE/ESB directory URL (E-005); note fields/format and update cadence
- [x] Add SBSD SWaM directory URL (E-006); confirm bulk export availability (NOTE: no bulk export confirmed — individual search/print only; contact SBSD to confirm)
- [x] Add RVA Business Portal URL (E-007); note account prerequisites

## 2) Rules and Timelines
- [x] Verify BPOL incentive details and exclusions (E-008); link to form or application page
- [x] Verify Health plan review timeline/fees (E-009) and list inspection pitfalls with source links
- [x] Verify ABC notice windows and processing timelines (E-010); link statutory refs

## 3) Artifacts Completion
- [x] Fill Source Inventory rows fully (URL, owner, format, access, cadence, fields, reliability notes, recommended use)
- [x] Move verified claims from research intake into the Executive Brief in `research_notes.md` (corrections applied: BPOL threshold, SWaM timeline, iSupplier docs, resolved unknowns)
- [x] Add specific URLs to user journeys and decision tree where applicable (E-xxx citations already present in user_journeys.md)
- [x] Expand benchmark_scan.md to 10–15 entries with links (12 entries present)

## 4) Guardrails & Messaging
- [x] Add explicit "no legal/eligibility determinations" disclaimer to any prototypes or demo scripts (added to research_notes.md)
- [x] Ensure plain‑language rewrites cite official definitions where used (Va. Code §4.1-230, City Code § 26-874 added)

## 5) Optional Repo Hygiene
- [ ] Add CONTRIBUTING.md with verification steps for PRs touching research
- [ ] Add ISSUE templates: "Source to verify", "Artifact update", "Benchmark addition"

---

**Web verification pass completed:** 2026-03-18
All E-001 through E-010 claims independently verified via live web research.
Key corrections noted in evidence_log.md:
- E-008: Correct URL is /finance/bpol-exemption (not /finance/bpol-exemption-program)
- E-010: ABC application PDF URL updated to /pdfs/val/retail-license-application.pdf
- E-006: SWaM bulk export unconfirmed — directory.sbsd.virginia.gov supports search/print only
