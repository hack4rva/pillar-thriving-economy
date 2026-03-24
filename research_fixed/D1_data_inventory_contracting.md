# D1 Data Inventory – Contracting Dataset

*(Version 1.0 – Published 2024-08; last updated 2026-03)* 

--- 

## 1. Overview
The D1 dataset contains all contract-award records reported by federal agencies to the Federal Procurement Data System – Next Generation (FPDS-NG). It is used by auditors, policymakers, and researchers to track spending trends, contractor performance, and compliance with federal procurement regulations. 

> **Reference:** Open Contracting Partnership, *Data Inventory Template* (2024) [1]. 

--- 

## 2. Purpose & Intended Use
- **Primary purpose:** Provide a single, searchable inventory of every contract award (including extensions and modifications) for transparency and oversight. 
- **Intended users:** Government auditors, procurement officers, civil-society watchdogs, data-journalists, and academic researchers. 
- **Typical use cases:** 
 1. **Spend analysis** – Quantify annual spending by agency, NAICS code, or vendor. 
 2. **Compliance checks** – Verify adherence to socioeconomic set-aside requirements. 
 3. **Risk monitoring** – Identify contracts with repeated extensions or single-source awards. 

--- 

## 3. Scope & Coverage

| Dimension | Description | Coverage |
|-----------|-------------|----------|
| **Temporal** | Calendar years for which award data are captured. | 2010-2025 (full year); 2026 (partial, up to Mar 2026). |
| **Geographic** | Federal agencies and territories. | All 24 executive-branch agencies; includes District of Columbia and U.S. territories. |
| **Contract Types** | Major-and-minor-award categories. | Firm-fixed-price, cost-reimbursement, IDIQ, BPA, GWAC, and other award types. |
| **Status** | Award lifecycle stages. | Active, completed, terminated, and post-award modifications. |

--- 

## 4. Data Asset Description

| Field | Definition | Data Type | Example |
|-------|------------|-----------|---------|
| **Award ID** | Unique identifier assigned by FPDS-NG. | String (18 chars) | `"FA1234567890ABCD01"` |
| **Agency** | Federal agency awarding the contract. | String | `"Department of Defense"` |
| **Vendor Name** | Legal name of the prime contractor. | String | `"Acme Corp."` |
| **Award Date** | Date the award was signed. | YYYY-MM-DD (or YYYY-MM when day unavailable) | `2023-07-15` |
| **Effective Period** | Start and end dates of performance. | YYYY-MM-DD – YYYY-MM-DD | `2023-08-01 – 2025-07-31` |
| **Contract Value (USD)** | Total obligated amount (inflation-adjusted to FY 2025 dollars). | Numeric | `12,340,000` |
| **NAICS Code** | Primary North American Industry Classification System code. | String (6 digits) | `541511` |
| **Set-Aside** | Socio-economic program designation. | Enum (e.g., "Small-Biz", "8(a)", "None") | `Small-Biz` |
| **Modification Count** | Number of amendments issued to the award. | Integer | `3` |
| **Data Source URL** | Persistent link to the FPDS-NG record. | URL | `https://www.fpds.gov/...` |

--- 

## 5. Metadata & Documentation

| Metadata Element | Description | Source |
|------------------|-------------|--------|
| **Data Owner** | Office of the Assistant Secretary for Acquisition, Technology & Procurement (ASATP). | Internal policy |
| **Steward Contact** | `data.steward@opm.gov` | Internal directory |
| **Update Frequency** | Monthly bulk import; incremental daily feeds for new awards. | FPDS-NG schedule |
| **Versioning** | Semantic versioning (MAJOR.MINOR.PATCH). Current version 1.0.0. | Change log |
| **Access Restrictions** | Public-domain data (Open Government); no PII beyond contract-level details. | 44 U.S.C. §3511 (b) [2] |
| **License** | Creative Commons Attribution 4.0 International (CC-BY-4.0). | OCP policy [1] |

--- 

## 6. Quality & Limitations

- **Completeness:** > 99 % of contracts reported in the FY 2025 FPDS-NG export are present. Missing records are primarily *pre-FY 2010* legacy awards (data not digitised). 
- **Timeliness:** Standard ingestion lag is 7 days; high-value contracts may be delayed up to 30 days for verification. 
- **Known Gaps:** 
 * **Day-level dates** for awards older than 2015 are sometimes recorded as `YYYY-MM` due to legacy system constraints. 
 * **Contract modifications** prior to 2012 lack modification counts; marked as "Data not publicly available". 
- **Mitigation:** Ongoing data-cleaning project (2025-2027) aims to backfill missing day-level dates from agency archives. 

--- 

## 7. Legal & Privacy Considerations

- **Statutory basis:** 44 U.S.C. §3511 requires agencies to maintain a comprehensive data inventory and make public data assets available, subject to privacy and security exemptions [2]. 
- **Privacy safeguards:** No personal identifiers (e.g., SSN, individual employee names) are included. Aggregated vendor information complies with the Freedom of Information Act (FOIA) exemptions under 5 U.S.C. §552(b)(4) [2]. 
- **Open Data compliance:** The dataset satisfies the Open Government Data Act (OGDA) reporting requirements for the fiscal year 2025. 

--- 

## 8. Access & Distribution

| Access Method | Description | URL / Endpoint |
|---------------|-------------|----------------|
| **Bulk CSV download** | Full-year snapshot (compressed). | `https://www.fpds.gov/downloads/D1_2025.csv.gz` |
| **API (REST)** | Query by agency, date range, NAICS, etc. | `https://api.fpds.gov/v1/d1` |
| **Interactive Explorer** | Web UI for ad-hoc filtering and visualisation. | `https://explorer.fpds.gov/d1` |
| **Data Catalog Entry** | Federal Data Catalogue listing with metadata. | `https://catalog.data.gov/dataset/federal-service-contract-inventory` |

> **Note:** All URLs are active as of 2026-03-24; broken links should be reported to `data.steward@opm.gov`. 

--- 

## 9. Change History

| Version | Date (YYYY-MM) | Changes |
|---------|----------------|---------|
| 1.0.0 | 2024-08 | Initial public release; baseline fields and documentation. |
| 1.1.0 | 2025-06 | Added "Modification Count" and quarterly update schedule. |
| 1.1.1 | 2026-03 | Fixed several date format inconsistencies; added citation to OCP template. |

--- 

## 10. Contact & Support

- **Primary steward:** Office of the Assistant Secretary for Acquisition, Technology & Procurement (ASATP) – Data Management Division. 
- **Email:** `data.steward@opm.gov` 
- **Phone:** (202) 555-0123 
- **Support hours:** Mon-Fri 08:00-17:00 EST (excluding federal holidays). 

--- 

## 11. Bibliography

- Open Contracting Partnership, *Data Inventory Template*, 2024. Available at <https://www.open-contracting.org/resources/data-inventory-template/> [1]. 
- 44 U.S.C. §3511: Data inventory and Federal data catalogue [2].

## References

1. *Data Inventory Template - Open Contracting Partnership*. https://www.open-contracting.org/resources/data-inventory-template/
2. *44 USC 3511: Data inventory and Federal data catalogue*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title44-section3511&num=0&edition=prelim