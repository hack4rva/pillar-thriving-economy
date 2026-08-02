> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../docs/methodology.md) for details.

# Prototype Recommendations (Seeded from intake — verify constraints)

## Problem 1 — Minority-owned businesses & City contracting

### Concept A: Procurement Matchmaker
- What it is: Unified opportunity feed that maps plain-English capabilities to NAICS/NIGP and surfaces relevant solicitations across OpenGov/eVA (+ historical context via Socrata).
- User served: First-time and small MBE/ESB vendors and partners.
- 48-hour feasibility: Fetch historical via SODA; scrape/export current opportunities; build code-mapping helper; simple alerting.
- Data/content: SODA API; OpenGov/eVA listings; seed code dictionary; OMBD/SWaM directory links (not stored).
- Team roles: Data wrangler, full-stack dev, UX writer/translator, product lead.
- Key risk/limitation: Scrape fragility; incomplete fields; avoid eligibility claims.
- Compelling demo: Enter “asphalt paving” → see mapped code → 3 relevant open bids → deadlines + plain-language summaries with source links.

### Concept B: Plain-Language Solicitation Explainer
- What it is: Attachment-aware explainer that highlights requirements (bonding/insurance/pre-bid) and unfamiliar terms.
- User served: Vendors new to procurement jargon.
- 48-hour feasibility: Manually parse a few sample PDFs; template-driven glossary; link to official attachments.
- Data/content: Sample solicitations; glossary; official definitions.
- Team roles: PM, content designer, dev.
- Key risk/limitation: PDF variability; scope limited to exemplars.
- Compelling demo: “Before/after” view of one RFP with highlighted terms and checklists.

### Concept C: Pre‑iSupplier Registration Coach
- What it is: Guided checklist and upload prep to minimize timeouts; email deliverability tip sheet for workflow mailer.
- User served: Vendors registering for the first time.
- 48-hour feasibility: Static checklist + simple form; timed autosave.
- Data/content: Official required docs list; contact/escalation info.
- Team roles: UX, frontend dev, researcher.
- Key risk/limitation: Must not handle sensitive documents; link out to official portal only.
- Compelling demo: Walkthrough that prepares all docs and shows successful, fast submission.

## Problem 2 — Small business navigation & setup friction

### Concept D: Richmond Business Setup Wizard
- What it is: Decision-tree wizard producing a tailored checklist (SCC → EIN → Zoning → BPOL → sector add-ons).
- User served: Home-based and emerging entrepreneurs.
- 48-hour feasibility: Encode initial decision tree; generate step-by-step plan with links; mobile-friendly.
- Data/content: Official pages for SCC, IRS EIN, OPP/Zoning, RVA Business Portal, sector guides.
- Team roles: PM, UX, full-stack dev.
- Key risk/limitation: Sequencing edge cases; must clearly label unknowns and “confirm with staff”.
- Compelling demo: Three personas produce three distinct, credible pathways.

### Concept E: Zoning Pre‑Check (Address + Use)
- What it is: Lightweight address/use checker that returns a “confidence hint” with links to official lookup and contact.
- User served: Home-based and retail/contractor entrepreneurs.
- 48-hour feasibility: Static permitted-use table + address input; show disclaimers and escalation path.
- Data/content: Public zoning/use tables or excerpts; contact info for staff.
- Team roles: Frontend dev, UX writer.
- Key risk/limitation: Must not claim eligibility; advisory only.
- Compelling demo: Type address + “cottage food” → shows likely path and questions to ask staff.

### Concept F: BPOL Deadline & Incentive Guide
- What it is: Plain-language explainer with calculator stubs and alerts for renewals and incentives.
- User served: New businesses navigating first two years.
- 48-hour feasibility: Static content + basic calculator; opt-in reminders.
- Data/content: Official BPOL rules; incentive criteria.
- Team roles: Content designer, frontend dev.
- Key risk/limitation: Must avoid tax advice; cite sources and link forms.
- Compelling demo: Walkthrough for a new retail shop showing fees and exemption eligibility steps.

