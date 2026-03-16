# Evidence Log

Purpose: Track claims and their citations. Status must be one of: verified | corrected | inferred | unknown.

Columns: id | claim | source_name | source_url | date_accessed | status | notes

| id | claim | source_name | source_url | date_accessed | status | notes |
|----|-------|-------------|------------|---------------|--------|-------|
| E-001 | City procurement contracts available via Socrata API (SODA/OData) | City of Richmond Open Data Portal | https://data.richmondgov.com/Well-Managed-Government/City-Contracts/xqn7-jvv2 | 2026-03-15 | verified | Updated monthly per Socrata foundry page. CSV endpoint: https://data.richmondgov.com/resource/xqn7-jvv2.csv |
| E-002 | Active solicitations managed via OpenGov procurement portal | City of Richmond Procurement | https://www.rva.gov/procurement-services/solicitations | 2026-03-15 | verified | Portal: https://procurement.opengov.com/portal/rva — electronic submission required. City "continually updates" forecast list; no fixed cadence stated. |
| E-003 | eVA used by Richmond regional entities (e.g., RAA) | Richmond International Airport / eVA | https://flyrichmond.com/business/contracting-procurement/ | 2026-03-15 | verified | Airport directs vendors to eVA for solicitation notifications. eVA homepage: https://eva.virginia.gov/ |
| E-004 | iSupplier required for vendor registration; 2-minute session timeout | City of Richmond Supplier Portal | https://rva.gov/procurement-services/supplier-portal | 2026-03-15 | verified | Session timeout confirmed. 3–5 business-day approval after registration. Registration entry: https://corerpext.richmondgov.com/OA_HTML/OA.jsp?OAHP=POS_GUEST_REG_HP&OAPB=POS_ISP_BRAND&OASF=POS_SUPPREG_REGISTER |
| E-005 | OMBD maintains MBE/ESB directory | City of Richmond OMBD | https://www.rva.gov/minority-business | 2026-03-15 | verified | Supplier & Diversity Portal replaced prior directory. Portal: https://richmondombd.diversitycompliance.com/ — handles MBE/ESB registration and compliance tracking. |
| E-006 | SBSD SWaM certification processing time | Virginia SBSD | https://sbsd.virginia.gov/certification/how-to-get-swam-certified/ | 2026-03-15 | corrected | CORRECTION: Official guidance says ~60 business days (not "30–60 days" as previously stated). Update any team-facing materials. |
| E-007 | RVA Business Portal launched for BPP/BPOL (2025) | City of Richmond Finance | https://www.rva.gov/finance/bpol-tax | 2026-03-15 | verified | Portal: https://rvapay.rva.gov/bpp — launched January 2025. For 2026: threshold doubled to $500k; businesses under threshold pay $30 flat fee. Filing deadline March 1, 2026. |
| E-008 | BPOL new-business incentive: $30 flat for first 2 years | City of Richmond Finance | https://www.rva.gov/finance/bpol-exemption-program | 2026-03-15 | verified | Qualifying new businesses pay $30 license fee for first two years in place of BPOL tax. |
| E-009 | Food establishment plan review timing and requirements | VDH / Richmond City Health District | https://www.vdh.virginia.gov/environmental-health/food-safety-in-virginia/foodapplication/ | 2026-03-15 | verified | Submit permit application at least 30 days before opening (after plan review approval). CO required before final inspection. Allow 7–10 working days for opening inspection. RCHD checklist PDF: https://www.vdh.virginia.gov/content/uploads/sites/119/2023/12/Opening-a-Food-Establishment-Procedures-Checklist-Final-Inspection-Checklist-RCHD.pdf |
| E-010 | ABC licensing timelines and public notice requirements | Virginia ABC Authority | https://www.abc.virginia.gov/licenses/apply/retail | 2026-03-15 | verified | Up to 60-day processing. 10 consecutive days posted public notice required. 30-day objection window after publication (VA Code § 4.1-230: https://law.lis.virginia.gov/vacode/title4.1/chapter2/section4.1-230/). Application PDF: https://www.abc.virginia.gov/library/licenses/pdfs/retail-license-application.pdf |

Instructions:
- Add additional rows as claims are extracted during research or editing.
- Source: `deep-research-report.md` (March 2026)
