> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../docs/methodology.md) for details.

# MBE Contracting — Data Feasibility (Draft — needs verification)

Questions to answer
- Can we build a useful matching/interpretation layer from public data alone?
- What enrichment is needed? What’s feasible in a weekend?
- What remains brittle, manual, or risky?
- Can historical contract data improve ranking or explain likely fit?

Preliminary assessment (user-provided; verify before relying)
- Sources: City Open Data (Socrata/SODA) [E-001], OpenGov (active solicitations) [E-002], Virginia eVA [E-003], OMBD/ESB + SBSD/SWaM directories [E-005][E-006].
- Access modes: API for Socrata; OpenGov has no public API — headless browser scraping required (direct fetch returns 403) (corrected 2026-03-18); likely HTML/search for eVA; OMBD bulk export confirmed via Excel download (corrected 2026-03-18). Socrata/eVA access modes confirmed.
- Fields sufficiency: Titles, categories (NAICS/NIGP), deadlines, attachments (PDFs) may support matching, reminders, and explainers; needs schema confirmation.
- Enrichment needed: Plain-English ↔ NAICS/NIGP mapping; supplier capability profiles; vocabulary normalization; deduping across portals.
- Weekend-feasible:
  - Pull historical contracts via SODA; normalize fields
  - Scrape or export current solicitations to prototype a unified feed
  - Lightweight code-mapping helper (seed dictionary + heuristic/LLM mapping)
  - Email/SMS deadline reminders sourced from scraped/exported due dates
- Brittle/risky areas:
  - Scrape-only sources (rate limits/HTML changes)
  - Attachment parsing (PDF requirements) at scale
  - Eligibility guidance beyond descriptive summaries (guardrail: no legal determinations)
- Historical value:
  - Use past awards and vendors to suggest relevance (“similar to…”) with clear disclaimers

Next steps
- Confirm each source URL, access mode, update cadence; fill `02_data/source_inventory.csv`
- Extract field lists from each source; attach to inventory
- Decide on code mapping approach (dictionary vs. LLM) with transparent fallbacks

