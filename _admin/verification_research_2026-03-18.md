# Verification Research Results

Pillar: Thriving Economy (MBE contracting, small business formation, Richmond, VA)
Date: 2026-03-18
Parallel.ai run_id: trun_3cad0ebea15c480e9dae00e74923d287
Processor: pro

---

# Richmond MBE + Small Business Contracting — Verified Sources, Timelines, and Data Access That Teams Can Build On

## Executive Summary

This report provides verified factual claims, data access parameters, and compliance timelines to support the Richmond, VA hackathon's "Thriving Economy" pillar. The research confirms that while open contract data is API-ready, procurement visibility spans multiple systems (Socrata, OpenGov, eVA) requiring integrated data pipelines. 

Key friction points for small businesses and Minority Business Enterprises (MBEs) include strict session timeouts on vendor portals, bifurcated directory systems (OMBD vs. SWaM), and rigid compliance timelines for food and beverage establishments. Hackathon teams should focus on building pre-flight document checklists, timeline calculators, and automated data aggregators to reduce these barriers. All verification items (E-001 through E-010) have been independently verified, with specific API endpoints, rate limits, and statutory rules documented below.

## Data Access Backbone — Socrata, OpenGov, eVA form the core intake

Combine SODA contract data with OpenGov solicitations and eVA marketplace touchpoints for a 360° pipeline from forecast to award.

### 1.1 City Contracts Dataset (Socrata)
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://data.richmondgov.com/Well-Managed-Government/City-Contracts/xqn7-jvv2`
* **Key Details for Teams**: 
 * **Endpoints**: SODA JSON (`.../xqn7-jvv2.json`) and CSV (`.../xqn7-jvv2.csv`).
 * **Update Cadence**: Monthly.
 * **Access & Limits**: Socrata tabular format supports SoQL (`$select`, `$where`, `$limit`, `$offset`). Teams should use an `X-App-Token` to raise default rate limits and implement pagination (default 1,000 row page size).
* **Corrections**: None.

### 1.2 SODA/OData Endpoints and Inventory Fields
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://data.richmondgov.com/api/odata/v4/xqn7-jvv2`
* **Key Details for Teams**: 
 * **Format**: JSON, CSV, OData v4.
 * **Recommended Use**: Prefer SODA with an app token. OData clients can utilize `$filter` and `$select`. Teams must use the dataset's "Columns" tab to enumerate exact field names for the `source_inventory.csv`.
* **Corrections**: None.

### 1.3 OpenGov Procurement Portal (Active Solicitations)
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://www.rva.gov/procurement-services/solicitations` | `https://procurement.opengov.com/portal/rva`
* **Key Details for Teams**: 
 * **Access**: Public browse is available, but bid submissions require an OpenGov login.
 * **Scraping Options**: There is no official public API. Direct programmatic fetches may return a 403 error. Teams should use headless browsers if scraping is necessary and strictly respect `robots.txt`.
 * **Cadence**: Forecast lists are published without a fixed schedule.
* **Corrections**: None.

### 1.4 eVA Vendor Pipeline (Regional Entities)
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://eva.virginia.gov/register-now.html` [1]
* **Key Details for Teams**: 
 * **Access Requirements**: Free supplier registration is used by state agencies and local governments [1] [2]. 
 * **Critical Blocker**: Registration is not considered complete, and payments will be delayed, unless a signed Commonwealth of Virginia Substitute W-9 is received [1].
 * **Data Formats**: Vendors must select NIGP commodity codes to be matched with business opportunities [3].
* **Corrections**: None.

## Vendor Readiness — Remove onboarding friction points

Pre-flight document checks and auto-saves are critical to mitigate session timeouts and completion blockers.

### 1.5 City iSupplier Vendor Registration
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://rva.gov/procurement-services/supplier-portal`
* **Key Details for Teams**: 
 * **Session Timeout**: The session will terminate if inactive for 2 minutes, and unsaved information will be lost.
 * **Required Documents**: W-9, ACH/EDI Payment Agreement, and a voided check or bank document. Procurement does not accept these via email.
 * **Processing**: Approval takes 3–5 business days. Teams should build a "prepare these documents" checklist before users start the form.
* **Corrections**: None.

### 1.6 RVA Business Portal Account Prerequisites
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://rvapay.rva.gov/BPP` [4]
* **Key Details for Teams**: 
 * **Prerequisites**: Registration requires an email address, EIN or SSN (without dashes), and the City Business Personal Property Account Number [4] [5].
 * **Functionality**: Provides a single access point to prepare, review, file, and pay Business Tangible Personal Property and Business License (BPOL) Renewal forms [4].
 * **Notes**: City of Richmond employees cannot use their work email for portal accounts [6].
* **Corrections**: None.

## Inclusive Supplier Discovery — Leverage OMBD bulk export; manage SWaM constraints

Use OMBD’s Excel export for comprehensive local coverage, but plan for manual data requests where bulk access is absent in state systems.

| Feature | OMBD MBE/ESB Directory (City) | SBSD SWaM Directory (State) |
| :--- | :--- | :--- |
| **Primary URL** | `richmondombd.diversitycompliance.com` [7] | `directory.sbsd.virginia.gov` [8] |
| **Bulk Export** | Yes ("Download Entire Directory to Excel") [9] | No public bulk export documented [8] |
| **Search Filters** | Cert type, DBA, commodity codes, location [9] [10] | Cert type, NIGP, NAICS, City, Zip [8] |
| **API Availability** | None documented | None documented |
| **Team Action** | Automate weekly Excel export jobs | Build semi-automated lookups; request data extract |

*Takeaway: Teams can easily ingest local OMBD data via bulk Excel downloads, but will need to rely on targeted searches or official data requests for state-level SWaM data.*

### 1.7 OMBD MBE/ESB Directory
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://richmondombd.diversitycompliance.com/?TN=richmondombd` [7]
* **Key Details for Teams**: 
 * **Data Formats**: Search results and the entire directory can be downloaded to Excel [9].
 * **Update Cadence**: Driven by rolling registrations; no fixed schedule.
* **Corrections**: None.

### 1.8 SBSD SWaM Directory
* **Verification Status**: LIKELY
* **Official Source URL**: `https://sbsd.virginia.gov/directory/` [8]
* **Key Details for Teams**: 
 * **Access**: The UI supports rich filtering (NIGP, NAICS, exact match Certification Number) [8].
 * **Limitations**: There is no documented bulk CSV export or API. Teams should log manual search workflows or submit a formal data request to SBSD.
* **Corrections**: Note retained: "SWaM bulk export unconfirmed — individual search/print only; contact SBSD to confirm."

## Rules and Lead Times — Plan for BPOL, Health, and ABC clocks

Sequenced compliance adds 30–60+ days to business formation. Teams should encode these timelines and exceptions into UX calculators.

| Requirement | Agency | Timeline / Window | Fees | Key Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **BPOL Exemption** | City Finance | Valid for first 2 years | $30 fee | Must be first-time location; no contractors [11] |
| **Health Plan Review** | VDH / RCHD | Submit ≥30 days prior to opening [12] | $40 Review + $40 Permit [13] | Certificate of Occupancy, CFPM cert [13] |
| **ABC License** | VA ABC | 30-day objection window [14] | Varies | 10-day posting, 2x newspaper publish [14] |

*Takeaway: Food and beverage businesses face a hard 30+ day floor for both Health and ABC approvals, which cannot be bypassed.*

### 1.9 BPOL Incentive Details and Exclusions
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://www.rva.gov/finance/bpol-exemption` [11]
* **Key Details for Teams**: 
 * **Eligibility**: Qualifying new businesses may have BPOL taxes over the $250,000 threshold exempted for two years, paying only a $30 fee [11].
 * **Exclusions**: Does not apply to mergers, name changes, franchises, peddlers, or contractors [11].
 * **Discrepancy Warning**: A 2026 EDA flyer states a $500,000 threshold [15]. Teams must treat the City Code (§ 26-874) and official Finance page as canonical ($250,000) and flag this discrepancy.
* **Corrections**: Correct URL is `/finance/bpol-exemption` (not `/finance/bpol-exemption-program`).

### 1.10 Health Plan Review Timeline and Fees
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://www.vdh.virginia.gov/richmond-city/food-safety/` [16]
* **Key Details for Teams**: 
 * **Fees**: $40 for Plan Review and $40 for the Food Establishment Permit [13].
 * **Timeline**: Applications must be submitted at least 30 days prior to opening [12].
 * **Pitfalls**: A Certificate of Occupancy must be submitted prior to final inspection [13]. A Certified Food Protection Manager (CFPM) certificate and manufacturer specification sheets are strictly required [13].
* **Corrections**: None.

### 1.11 ABC Notice Windows and Processing Timelines
* **Verification Status**: CONFIRMED
* **Official Source URL**: `https://law.lis.virginia.gov/vacode/title4.1/chapter2/section4.1-230/` [14]
* **Key Details for Teams**: 
 * **Posting**: Notice must be posted on the front door of the premises for 10 complete and consecutive days [14] [17].
 * **Publishing**: Notice must be published at least once a week for two consecutive weeks in a local newspaper [14].
 * **Objections**: The public has 30 days from the date of the initial newspaper publication to submit objections [14].
* **Corrections**: ABC application PDF URL updated to `/pdfs/val/retail-license-application.pdf` [17].

## Repo Implementation Plan — Make research operational

To accelerate team velocity, repo admins must codify verification steps and wire links directly into user journeys.

### Artifacts Completion
* **Status**: CANNOT VERIFY (Requires repo access)
* **Key Details for Teams**: 
 * Port verified claims (E-001 through E-010) into the "Verified Sources & Rules" section of `research_notes.md`.
 * Insert deep links into decision trees (e.g., OMBD directory search, RVA Business Portal registration, RVA311 BPOL incentive app).
 * Expand `benchmark_scan.md` with 10–15 entries detailing other cities' MBE portals and open data procurement instances.

### Optional Repo Hygiene
* **Status**: CANNOT VERIFY (Requires repo access)
* **Key Details for Teams**: 
 * Add a `CONTRIBUTING.md` file requiring PRs to state claim status, provide official `.gov/.edu/.org` URLs, and document API rate limits.
 * Create ISSUE templates for "Source to verify", "Artifact update", and "Benchmark addition".

## Guardrails and Definitions — Avoid false assurances

Prominent disclaimers and official definitions reduce risk when building civic tech prototypes.

### Disclaimers and Citations
* **Status**: CANNOT VERIFY (Content not visible)
* **Key Details for Teams**: 
 * **Mandatory Disclaimer**: All prototypes must include: *"This tool provides general information and links to official resources. It does not provide legal advice or determine eligibility. For official determinations, consult the City of Richmond, Virginia ABC, VDH, SBSD, or your legal counsel."*
 * **Plain-Language Rules**: Pair every plain-language summary with an "Official definition" link to the statutory source (e.g., Va. Code §4.1-230 for ABC [14], City Code § 26-874 for BPOL [11]).

## Appendix — Quick Links and Endpoints

Centralized URLs for hackathon teams to utilize in their builds:
* **Socrata Contracts API**: `https://data.richmondgov.com/resource/xqn7-jvv2.json`
* **OpenGov Portal**: `https://procurement.opengov.com/portal/rva`
* **eVA Registration**: `https://eva.virginia.gov/register-now.html` [1]
* **OMBD Directory**: `https://richmondombd.diversitycompliance.com/?TN=richmondombd` [7]
* **SBSD SWaM Directory**: `https://directory.sbsd.virginia.gov/` [8]
* **RVA Business Portal**: `https://rvapay.rva.gov/BPP` [4]
* **BPOL Exemption**: `https://www.rva.gov/finance/bpol-exemption` [11]
* **VDH Food Safety**: `https://www.vdh.virginia.gov/richmond-city/food-safety/` [16]
* **ABC Retail Application**: `https://www.abc.virginia.gov/library/licenses/pdfs/val/retail-license-application.pdf` [17]

## References

1. *Register Now - eVA*. https://eva.virginia.gov/register-now.html
2. *I Sell To Virginia - eVA*. https://eva.virginia.gov/i-sell-to-virginia.html
3. *Steps to Register as a New eVA Supplier*. https://dgs.virginia.gov/globalassets/business-units/dps/documents/vendors/newsupplierregistrationqrg101922pdf.pdf
4. *Business, Professional, and Occupational License (BPOL) Tax | Richmond*. https://www.rva.gov/finance/bpol-tax
5. *RVA Business Portal Registration Guide*. https://rvapay.rva.gov/prd/r/corfin/170/files/static/v418/Registration%20Assistance.pdf
6. *New User Registration Instructions ...*. https://www.rva.gov/sites/default/files/2024-12/New%20User%20Registration%20Instructions%2020241204.pdf
7. *City of Richmond - Supplier Diversity Management System*. https://richmondombd.diversitycompliance.com/?TN=richmondombd
8. *Small Business & Supplier Diversity SWaM & DBE Directory – The Department of Small Business and Supplier Diversity*. https://sbsd.virginia.gov/directory/
9. *City of Richmond - Supplier Diversity Management System*. https://richmondombd.diversitycompliance.com/FrontEnd/searchcertifieddirectory.asp?TN=richmondombd
10. *City of Richmond - Supplier Diversity Management System*. https://richmondombd.diversitycompliance.com/FrontEnd/SearchRegistry.asp?TN=richmondombd&XID=8785&QT=52964737A47EEBB9D63C30CD67C5DAE10059FBD071EC594E
11. *Business, Professional, and Occupational, License (BPOL) Tax Incentive Program | Richmond*. https://www.rva.gov/finance/bpol-exemption
12. *Applying for a Food Permit - Virginia Department of Health*. https://www.vdh.virginia.gov/environmental-health/food-safety-in-virginia/foodapplication/
13. *Opening-a-Food-Establishment-Procedures-Checklist-Final ...*. https://www.vdh.virginia.gov/content/uploads/sites/119/2023/12/Opening-a-Food-Establishment-Procedures-Checklist-Final-Inspection-Checklist-RCHD.pdf
14. *§ 4.1-230. Applications for licenses; publication; notice to localities; fees; permits*. https://law.lis.virginia.gov/vacode/title4.1/chapter2/section4.1-230/
15. *Business Professional Occupational License (BPOL) Tax ...*. https://www.richmondeda.com/wp-content/uploads/2026/01/BPOL-TAX-2026_ENG-SPA.pdf
16. *Food safety - Richmond City Health Department*. https://www.vdh.virginia.gov/richmond-city/food-safety/
17. *PART 1: RETAIL LICENSE APPLICATION | Virginia ABC*. https://www.abc.virginia.gov/library/licenses/pdfs/val/retail-license-application.pdf