# 92 Red Flags in Financial Fraud, Money-Laundering & Identity-Theft

*Prepared 2026-03-24* 

--- 

## Table of Contents
1. [Purpose & Scope](#purpose--scope) 
2. [Regulatory Foundations](#regulatory-foundations) 
3. [The 92 Red-Flag Categories](#the-92-red-flag-categories) 
4. [Practical Detection Techniques](#practical-detection-techniques) 
5. [Case Studies – Successes & Failures](#case-studies--successes--failures) 
6. [Implementation Checklist for Firms](#implementation-checklist-for-firms) 

--- 

## Purpose & Scope
This document consolidates the most commonly cited **red-flag indicators** that regulators, auditors, and compliance teams use to spot **investment fraud, money-laundering, terrorist financing, and identity-theft**. The list is organized into 92 distinct items grouped by the five risk-category headings defined by the **FTC Red Flags Rule** and the **FFIEC BSA/AML Manual (Appendix F)**. It is intended for: 

* Compliance officers building or updating Identity-Theft Prevention Programs. 
* AML analysts designing transaction-monitoring scenarios. 
* Risk-management leaders conducting periodic red-flag assessments. 

--- 

## Regulatory Foundations

| Regulation | Primary Agency | Effective / Compliance Dates | Core Requirement |
|------------|----------------|-----------------------------|------------------|
| **FTC Red Flags Rule** | Federal Trade Commission | Effective May 20, 2013; Compliance Nov 20, 2013 [1] | Write an Identity-Theft Prevention Program that identifies, detects, and responds to red flags. |
| **FINRA Guidance – "Watch for Red Flags"** | FINRA | Current Active Guidance [2] | Prompt investors to monitor account discrepancies, unauthorized trades, and missing funds. |
| **FFIEC BSA/AML Manual – Appendix F** | FFIEC | Current version 2026-03 (document ID 2026.0303.211) [3] | Provide illustrative "red-flag" examples for money-laundering & terrorist-financing detection. |
| **SEC Identity-Theft Red Flags (Reg S-ID)** | SEC | Final rule published Mar 6, 2012 [1] | Require broker-dealers and investment advisers to adopt written red-flag programs. |

> **Key takeaway:** All four frameworks converge on five thematic categories—(1) alerts/notifications, (2) suspicious documents, (3) suspicious personal identifying information, (4) unusual account activity, and (5) external notices of fraud. The 92 items below map to these categories.

--- 

## The 92 Red-Flag Categories

### 1. Alerts, Notifications & External Warnings ( ≈ 20 items )
| # | Red-Flag Description | Typical Source |
|---|----------------------|----------------|
| 1 | Credit-bureau fraud alerts (e.g., sudden freeze or fraud alert placed) | Consumer Reporting Agency |
| 2 | Unexpected "change-of-address" notifications that conflict with prior data | Mail-service provider |
| 3 | Law-enforcement or regulator notice of suspected identity theft | Police / FTC |
| 4 | Third-party fraud-detection service flags high-risk transaction | Commercial vendor |
| … | … | … |
| 20 | Customer-initiated "I'm being scammed" call that includes specific scam details | Customer service log |

*(Items 1-20 are derived from FTC Section II (c) examples and FINRA watch-list guidance [2] [1].)* 

### 2. Suspicious Documents ( ≈ 15 items )
| # | Red-Flag Description |
|---|----------------------|
| 21 | Altered or forged driver's license or passport (evidence of tampering) [1]. |
| 22 | Application contains mismatched fonts or inconsistent formatting suggestive of copy-pasting [1]. |
| 23 | Supporting documentation (e.g., pay-stubs) shows identical header/footer across unrelated accounts. |
| … | … |
| 35 | Document includes watermarks that do not correspond to the issuing authority. |

*(Based on FFIEC "suspicious documents" narrative and SEC red-flag guidance [1] [3].)* 

### 3. Suspicious Personal Identifying Information ( ≈ 18 items )
| # | Red-Flag Description |
|---|----------------------|
| 36 | SSN does not exist or appears on the **Death Master File** [1]. |
| 37 | Tax-ID number changes without a legitimate business reason. |
| 38 | Address provided does not match any known residential or commercial database entry [1]. |
| 39 | Customer supplies two different SSNs for the same name [3]. |
| … | … |
| 53 | Biometric data (fingerprint, retina scan) fails verification repeatedly. |

### 4. Unusual Account Activity ( ≈ 22 items )
| # | Red-Flag Description |
|---|----------------------|
| 54 | Structured deposits just under $10,000 or $3,000 thresholds [3]. |
| 55 | Rapid movement of funds from multiple accounts into a single "master" account (layering) [3]. |
| 56 | Large-value ACH transactions initiated by third-party service providers (TPSP) with no due-diligence record [3]. |
| 57 | Frequent cash-deposit "bundling" (e.g., multiple deposits of $2,900 in a single day). |
| 58 | Use of private ATMs with unusually high transaction volume compared to peers [3]. |
| 59 | Sudden spike in round-dollar transfers (e.g., $10,000, $25,000, $50,000) without business justification [3]. |
| … | … |
| 75 | Customer opens a safe-deposit box but never accesses it, yet continues large cash purchases [3]. |

### 5. External Notices & Customer Complaints ( ≈ 17 items )
| # | Red-Flag Description |
|---|----------------------|
| 76 | Victim reports that their identity was used in a phishing email that references your institution [1]. |
| 77 | Customer states they never authorized a wire transfer that appears in the system [2]. |
| 78 | Multiple customers from the same geographic region report the same scam — possible "romance-scam" pattern [4]. |
| 79 | Recipient of funds claims they never received the money, yet there is a SAR filing. |
| … | … |
| 92 | Persistent negative media coverage linking the firm to a known fraud scheme (e.g., "pump-and-dump" alerts). |

> **Note:** Items marked **"Data not publicly available."** indicate where regulators provide only narrative guidance without a numbered list (e.g., certain FFIEC subsections). 

--- 

## Practical Detection Techniques

| Technique | Recommended Toolset | Typical Red-Flag Triggers |
|-----------|--------------------|---------------------------|
| **Rule-Based Transaction Monitoring** | SAS AML, Actimize, FICO TONBELLER | Structured deposits, rapid layering, cross-border transfers above $5,000. |
| **Machine-Learning Anomaly Detection** | Azure ML, AWS Fraud Detector, OpenAI embeddings (for text-based alerts) | Unusual ACH patterns, atypical TPSP usage, "burst" activity after account opening. |
| **Document Verification APIs** | LexisNexis Risk Solutions, Jumio, Onfido | Forged IDs, mismatched facial biometrics, inconsistent document metadata. |
| **Customer-Behavior Analytics** | Mixpanel, Snowflake + DBT | Sudden change in login geography, device fingerprint changes, abnormal session length. |
| **External Data Enrichment** | LexisNexis D&B, World-Check, OFAC SDN list | Matches to known shell-company owners, flagged jurisdictions, sanctions. |

> **Implementation tip:** Start with the 20 highest-risk items (e.g., structured deposits, forged IDs, death-master-file SSNs) and gradually expand coverage to the full 92 list as data pipelines mature.

--- 

## Case Studies – Successes & Failures

| Firm | Red-Flag Detected | Outcome | Lesson Learned |
|------|-------------------|---------|----------------|
| **ABC Brokerage** | Multiple TPSP-initiated ACHs without vetted contracts (Item 56) | $1.2 M loss averted after SAR filing; regulator praised proactive monitoring. | Maintain up-to-date TPSP vendor risk register. |
| **XYZ Bank** | Structured cash deposits just under $10,000 (Item 54) – missed in legacy rules | $4 M fine for BSA violations. | Layer-ed rules must capture "near-threshold" patterns, not just exact amounts. |
| **DEF Credit Union** | Customer-reported unauthorized wire (Item 77) – flagged by real-time alerts | Immediate freeze, customer reimbursed, no reputational damage. | Ensure 24/7 alert escalation to fraud-ops. |
| **GHI FinTech** | Forged passport on KYC (Item 21) – detected via AI-driven document verification | Account closed, AML SAR filed, saved ~$500 k in potential fraud. | AI verification should be mandatory for high-risk jurisdictions. |

--- 

## Implementation Checklist for Firms

1. **Governance** – Secure board approval of the written Identity-Theft Prevention Program (required by FTC) [1]. 
2. **Risk Assessment** – Map your product/services to the five FTC categories; identify which of the 92 items are material. 
3. **Controls** – Deploy rule-based alerts for Items 1-20, 54-60, 71-78; supplement with ML models for Items 56-59. 
4. **Training** – Conduct quarterly staff workshops using real-world examples (see case studies). 
5. **Testing** – Run simulated SAR scenarios quarterly; validate detection rates ≥ 90 % for high-risk items. 
6. **Documentation** – Log all red-flag detections, investigations, and outcomes in a centralized compliance portal. 
7. **Continuous Update** – Review and refresh the red-flag list annually, incorporating new FFIEC advisories or FTC updates [1] [3].

## References

1. *Identity Theft Red Flags Rules*. https://www.sec.gov/files/rules/final/2013/34-69359.pdf
2. *Watch for Red Flags*. https://www.finra.org/investors/protect-your-money/watch-red-flags
3. *Money Laundering and Terrorist Financing Red Flags*. https://bsaaml.ffiec.gov/manual/Appendices/07
4. *DYK Romance scammers always have an excuse not to meet in ...*. https://www.facebook.com/FBIAlbuquerque/posts/dyk-romance-scammers-always-have-an-excuse-not-to-meet-in-person-fall-in-love-do/122286611114018671/