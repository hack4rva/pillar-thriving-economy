# Pillar 4 (Thriving Economy) — Structured Research Plan

Purpose
- Convert available options into a clear, Richmond-specific research plan that guides evidence gathering, analysis, comparison, and selection of a weekend-buildable prototype.
- Anchor to two targeted statements: (1) minority-owned business access to City contracting opportunities; (2) small-business setup/navigation.

Scope and constraints
- Official procurement portal remains the source of truth.
- No policy changes, eligibility determinations, or system integrations.
- Prefer public data, public documents, and clearly cited sources.
- No overclaiming impact; identify continuation owners where possible.

Primary tracks
- Track A: Procurement access (MBE contracting)
- Track B: Small-business setup/navigation
- Cross-cutting: Prior art, risks/ethics, MVP feasibility, and demo alignment

Timeline (suggested)
- Block 1 (2–3 hours): Source inventory + quick landscape
- Block 2 (2–3 hours): Journey maps + pain points
- Block 3 (2–3 hours): Option research + scoring
- Block 4 (2–3 hours): Recommendations + next steps

Tools and methods
- Perplexity API with strict citation enforcement and query chains focused on Richmond sources.
- Manual source inventory (URLs, formats, owners) using public portals and open data.
- Lightweight data inspection (CSV/JSON/OData) and page sampling for structure/recency.
- Document summarization with source-linked snippets; no authoritative legal or procurement advice.
- Simple scoring rubric (feasibility, data reliance, user value, demo clarity, risks, continuation potential).

Evaluation rubric (use for all options)
- Data availability/structure: Is there public, machine-readable or reliably scrapeable data?
- Richmond specificity: Can we ground all claims in local sources?
- User value: Does it reduce time-to-understanding/confusion for target users?
- Weekend feasibility: Can a mixed team demo a working flow by Sunday?
- Risk/ethics: Can we avoid legal, eligibility, or authoritative claims?
- Demo clarity: Is the value obvious in 60–90 seconds?
- Continuation: Is there a plausible owner or artifact value post-event?

Expected outputs (research packet)
- Problem landscape summary (A1–A5 prompts)
- User/stakeholder map and journeys (B1–B5 + A2)
- Source inventory with formats (D1–D5)
- Prior art catalog with patterns (E1–E5)
- Ranked options with scores and tradeoffs (F1–F5)
- Risk/guardrail checklist (G1–G5)
- Two MVP shapes with must-have vs. mockable components (H1–H5)
- Demo plan beats and framing (I1–I5)

Track A — Procurement Access (MBE Contracting)

Option A1 — Procurement Opportunity Translator (search/match/explain)
- Key objectives
  - Determine if public procurement listings + City Contracts Registry support relevance filtering aligned to business capabilities.
  - Identify minimal fields (title, category, NAICS/commodity, due date, description) and map to user-entered capability tags.
  - Validate plain-language explanations that improve time-to-understanding without implying eligibility.
- Data/info needed
  - Procurement portal listings (URL, structure, frequency); City Contracts Registry (CSV/JSON/OData); any public vendor registration guidance.
  - Glossary of procurement terms; examples of real solicitations (n≈10–20 sample).
- Research methods
  - Run D1–D2 prompts to inventory sources and confirm formats; sample n=20 listings; extract fields into a lightweight schema.
  - A/B prompt Perplexity to generate plain-language summaries with citations back to the official listing.
  - Build a minimal taxonomy for business capabilities (free-text tags mapped to solicitation text).
- Evaluation criteria
  - Data structure score (OData/CSV=high; scrape-only=medium; PDF-only=low).
  - Relevance quality (top 5 surfaced opportunities match stated capability in ≥60% of tests).
  - Demo clarity (search -> relevant cards -> explainers -> official link).
  - Risk controls (disclaimer, no eligibility claims, source links on every card).
- Expected outcomes
  - Finding: viable as search+explain overlay with public data.
  - Next: prepare 5–10 curated listings, capability-tag mapping, and explanation templates with citations.

Option A2 — Plain-Language Bid Explainer
- Key objectives
  - Test whether summarizing opportunity language + key dates materially reduces confusion for first-time vendors.
  - Identify the minimum set of fields to explain without legal advice.
- Data/info needed
  - Live or archived solicitations; glossary; City guidance pages.
- Research methods
  - Prompt Perplexity for section-by-section summaries with inline source references; human review for correctness.
  - Usability test script: 3 tasks comparing raw portal vs. explainer card.
- Evaluation criteria
  - Time-to-understanding reduction (target ≥30% faster on 3 scripted tasks).
  - Correctness (no invented steps; all claims source-linked).
- Expected outcomes
  - Finding: high demo clarity with low data coupling.
  - Next: build 6–8 explainer cards and a glossary component.

Option A3 — Contracting Readiness Checklist
- Key objectives
  - Identify common pre-requisites vendors should review before contacting staff; frame as guidance, not determination.
- Data/info needed
  - Public vendor registration info, training pages, frequently asked procurement questions.
- Research methods
  - Content audit of public pages; extract checklist items and map to sources.
- Evaluation criteria
  - Clarity and usefulness (do users report better confidence to take first step?).
  - Risk posture (no definitive “you are eligible” statements).
- Expected outcomes
  - Finding: feasible as a preparatory guide with links.
  - Next: checklist component with source badges.

Option A4 — Process Transparency Dashboard (narrow)
- Key objectives
  - Explore whether historic contract data can reveal simple, useful patterns (timing, categories) for context.
- Data/info needed
  - City Contracts Registry fields and update cadence.
- Research methods
  - Load CSV/JSON; build one timeline or category chart; annotate limitations.
- Evaluation criteria
  - Relevance to end users (context only, not decision-making).
- Expected outcomes
  - Finding: supportive but secondary to A1/A2 in user value.

Track B — Small-Business Setup / Navigation

Option B1 — Business Setup Decision Tree
- Key objectives
  - Reconstruct a minimal, source-cited sequence for 2–3 personas (e.g., home-based service, food/regulated, brick-and-mortar retail).
  - Identify branches that are public vs. staff-knowledge dependent.
- Data/info needed
  - Department pages, permits/licenses, process PDFs, contact pages; ordinances where applicable.
- Research methods
  - D3–D4 prompts to catalog sources and flag unstructured areas; create draft flowcharts with citations.
- Evaluation criteria
  - Coverage (start-to-first-contact path for 2–3 personas).
  - Source-backed steps (each step has a URL; unknowns labeled).
- Expected outcomes
  - Finding: feasible if narrow; gaps remain for staff-only logic.
  - Next: publish 2 persona flows and highlight unknowns.

Option B2 — “Smarter Front Door” Navigator
- Key objectives
  - Provide a start-here intake that routes users to the right pages and contacts in 3–5 questions.
- Data/info needed
  - Curated index of pages/resources; contact points; office hours where public.
- Research methods
  - Content inventory; decision-tree routing to pages; microcopy testing for clarity.
- Evaluation criteria
  - Routing success (≥80% of test scenarios land on plausible next step in ≤3 clicks).
- Expected outcomes
  - Finding: feasible with curated links and limited logic.
  - Next: build a small Q&A flow with source links.

Option B3 — Resource Sequencing Assistant
- Key objectives
  - Clarify “what comes first” for common cases; distinguish informative routing from official determinations.
- Data/info needed
  - Ordered steps from public pages + explicit caveats where ambiguous.
- Research methods
  - Extract step order; annotate with “why first” rationale and sources.
- Evaluation criteria
  - Sequence clarity and user confidence uplift (qualitative test notes).
- Expected outcomes
  - Finding: feasible for limited personas; label assumptions.

Option B4 — Public Information Explainer Hub
- Key objectives
  - Reduce jargon and consolidate scattered guidance into source-cited explainers.
- Data/info needed
  - Key pages + PDFs; glossary terms; common FAQs.
- Research methods
  - Summarize with citations; build topic pages aligned to personas.
- Evaluation criteria
  - Comprehension gain and bounce reduction (qualitative proxy during tests).
- Expected outcomes
  - Finding: very feasible; lower engineering, strong clarity value.

Option B5 — Staff Knowledge Capture (internal artifact)
- Key objectives
  - Document tacit decision logic that is not publicly written down.
- Data/info needed
  - Interview notes (if accessible), mentor inputs, publicly inferred decision points.
- Research methods
  - Create a 1–2 page process map per persona; mark unknowns.
- Evaluation criteria
  - Utility to staff/partners post-event; clarity of unknowns list.
- Expected outcomes
  - Finding: feasible as a companion artifact; strengthens navigator/decision-tree tools.

Cross-cutting research steps
- Prior art scan (E1–E5): Identify navigator, explainer, matching, and dashboard patterns that don’t require integration or policy change.
- Risk/ethics (G1–G5): Draft guardrails (source links, disclaimers, no eligibility/legal advice, human escalation, confidence labels).
- MVP feasibility (H1–H5): Define must-have vs. mockable elements; set scope boundaries.
- Demo alignment (I1–I5): Script a 90-second flow with source citations and clear handoff to official pages.

Decision and next steps
- Scoring and selection
  - Score A1–A4 and B1–B5 with the evaluation rubric; pick one primary and one backup.
- Expected outcomes
  - A concise research brief with: (1) chosen direction; (2) why it wins; (3) data inventory; (4) risks/guardrails; (5) MVP outline; (6) demo beats.
- Post-selection actions
  - Create a source-backed glossary; assemble 5–10 canonical examples (solicitations or journeys);
  - Prepare content stubs and UI copy; define a minimal data model.

