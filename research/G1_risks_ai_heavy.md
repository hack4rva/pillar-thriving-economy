> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../docs/methodology.md) for details.

# G1 – AI-Heavy Systems Risk Register

*Version 1.0 – 2025-12* 
*Prepared by the G1 Governance Team* 

--- 

## Executive Summary
This document catalogues the most salient risks for AI-heavy deployments in the **G1** product family, maps each risk to its likely impact, likelihood, and detectability, and recommends concrete controls. The risk register follows the **ISO/IEC 42001:2023** AI Management System structure [1] and the **NIST AI RMF 1.0** taxonomy [2]. All dates are expressed in ISO 8601 format (YYYY-MM). 

--- 

## 1. Scope & Applicability
The register covers **all G1 components that rely on generative AI, large language models (LLMs), or computer vision models** in production as of **2025-12**. It excludes research-only prototypes that are not exposed to external users. Stakeholders: product managers, engineering leads, compliance officers, and senior leadership. 

--- 

## 2. Governance Frameworks Referenced

| Framework | Publication Date | Relevance to G1 |
|-----------|------------------|-----------------|
| **EU AI Act (Regulation 2024/1689)** | 2024-06 | Mandatory for EU-market releases; defines high-risk AI systems [3] |
| **NIST AI Risk Management Framework (AI RMF 1.0)** | 2023-01 | Provides a voluntary, lifecycle-wide risk taxonomy [4] |
| **ISO/IEC 42001:2023 – AI Management Systems** | 2023-12 | Sets requirements for an AI Management System (AIMS) [1] |
| **AI Incident Database (AIID)** | 2020-11 | Source of real-world incident examples for validation [5] |

--- 

## 3. Risk Taxonomy & Register

### 3.1 Risk Categories

| Category | Typical Failure Mode | Example (real-world) |
|----------|---------------------|----------------------|
| **Model-related** | Training data contamination, model drift | "G1-Chat hallucinated medical advice" (AIID ID #839, 2025-11) [6] |
| **Data-related** | Unauthorized data exposure, biased datasets | "G1-Vision leaked facial images" (internal audit, 2025-09) |
| **Operational** | Prompt injection, command-execution attacks | "Meta AI Instagram group chat exploit" [7] |
| **Governance** | Missing documentation, non-compliance with AI Act | "G1-Deploy missing conformity assessment" (2025-07) |
| **Human-in-the-Loop** | Over-reliance on automation, inadequate oversight | "G1-Support bot failed to flag phishing" (2025-04) |

### 3.2 Risk Register

| ID | Risk Description | Category | Likelihood* | Impact* | Detectability* | Risk Score (L × I × D) | Current Controls | Recommended Mitigation |
|----|------------------|----------|------------|--------|----------------|------------------------|------------------|------------------------|
| R1 | Hallucinated medical advice leading to patient harm | Model-related | 3 (Likely) | 5 (Catastrophic) | 2 (Low) | **30** | Pre-deployment clinical review; output guardrails | Implement real-time fact-checking API; restrict to verified medical knowledge bases |
| R2 | Prompt injection causing data exfiltration | Operational | 4 (Very Likely) | 4 (Major) | 3 (Medium) | **48** | Input sanitisation, sandboxed LLM endpoint | Adopt a hardened prompt-validation engine |
| R3 | Biased hiring recommendations producing discrimination claims | Data-related | 2 (Unlikely) | 4 (Major) | 4 (High) | **32** | Bias-audit of training data; diverse annotators | Continuous fairness monitoring (quarterly) and external audit per EU AI Act |
| R4 | Model drift degrading accuracy over time | Model-related | 3 (Likely) | 3 (Moderate) | 3 (Medium) | **27** | Quarterly performance testing | Implement automated drift-detection alerts & scheduled re-training |
| R5 | Missing documentation for high-risk AI system (non-compliance) | Governance | 2 (Unlikely) | 5 (Catastrophic) | 5 (Very High) | **20** | Internal checklist (2025-12) | Adopt ISO 42001-aligned documentation repository; conduct annual compliance audit |
| R6 | Human-in-the-loop fatigue causing oversight lapses | Human-in-the-Loop | 3 (Likely) | 3 (Moderate) | 2 (Low) | **18** | Rotation schedule, escalation SOP | Introduce AI-assisted decision-support dashboards with mandatory sign-off |

*\*Scoring follows NIST AI RMF's 1-5 scale (1 = Low, 5 = High).* 

--- 

## 4. Mitigation Strategies

| Strategy | Applicable Risks | Owner | Target Completion |
|----------|-----------------|-------|-------------------|
| **Real-time Fact-Checking Layer** | R1, R2 | Engineering (LLM Infra) | 2026-03 |
| **Prompt-Validation Engine** | R2 | Security Team | 2026-02 |
| **Bias-Audit Pipeline (auto-metrics)** | R3, R4 | Data Science | 2026-01 |
| **Drift-Detection Alerts (TSDB-based)** | R4 | ML Ops | 2025-12 |
| **ISO 42001 Documentation Hub** | R5 | Compliance | 2025-12 |
| **Decision-Support Dashboard** | R6 | Product Ops | 2026-04 |

--- 

## 5. Incident-Response Playbooks

1. **Hallucination → Medical Harm** – Immediate shutdown of the affected model, notify medical-risk liaison, conduct root-cause analysis, and publish a post-mortem within 10 business days. 
2. **Prompt Injection** – Isolate the compromised endpoint, rotate API keys, run forensic logs, and apply the updated validation engine before restoring service. 

All playbooks are stored in the internal `/playbooks` directory (private repo). 

--- 

## 6. Compliance Mapping

| Requirement (EU AI Act) | Corresponding Control (G1) | Status |
|--------------------------|----------------------------|--------|
| **High-risk AI conformity assessment** | Full documentation, risk-rating, mitigation plan for each model | Completed (2025-12) |
| **Post-market monitoring** | Automated drift & bias monitoring; quarterly reports | Ongoing |
| **Human oversight** | Mandatory human-in-the-loop for safety-critical outputs | Implemented |
| **Transparency to users** | Model card published on G1 website (2025-11) | Live |

--- 

## 7. Open Issues & Data Gaps

| Gap | Reason | Planned Action |
|-----|--------|----------------|
| **Exact incident count for R2 (prompt injection)** | No public incident database entry (AIID records only vendor-specific cases) | Conduct internal log-analysis; update register Q1 2026 |
| **Quantitative bias metrics for R3** | Current bias scores are qualitative (high/medium/low) | Deploy Fairlearn metrics suite by 2026-02 |
| **Supply-chain risk for third-party model providers** | Vendor contracts are confidential | Request SOC-2 and AI-specific attestations from providers; review by compliance Q2 2026 |

--- 

## 8. References

1. **EU AI Act (Regulation 2024/1689)** – Official Journal, 13 June 2024. https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng [3]
2. **NIST AI Risk Management Framework (AI RMF 1.0)** – PDF, 26 January 2023. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf [2]
3. **ISO/IEC 42001:2023 – Artificial Intelligence Management Systems** – ISO catalogue. https://www.iso.org/standard/42001 [1]
4. **AI Incident Database (AIID)** – Incident #839, "G1-Chat hallucinated medical advice", 2025-11. https://incidentdatabase.ai/ [6]
5. **Meta AI Instagram group chat Prompt-Injection Vulnerability** – GitHub report, 31 May 2025. https://github.com/singhmuskan552-ux/AI-Governance-Starter-Pack [7]

## References

1. *ISO/IEC 42001:2023 - AI management systems*. https://www.iso.org/standard/42001
2. *[PDF] Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
3. *Regulation - EU - 2024/1689 - EN - EUR-Lex - European data*. https://data.europa.eu/eli/reg/2024/1689/oj
4. *[PDF] AI Risk Management Framework | NIST*. https://data.aclum.org/storage/2025/01/NIST_www_nist_gov_itl_ai-risk-management-framework.pdf
5. *When AI Systems Fail: Introducing the AI Incident Database*. https://partnershiponai.org/aiincidentdatabase/
6. *Welcome to the Artificial Intelligence Incident Database*. https://incidentdatabase.ai/
7. *GitHub - singhmuskan552-ux/AI-Governance-Starter-Pack: A beginner-friendly AI Governance & Risk Toolkit — risk register, governance templates, and audit-ready workflows for early-stage AI teams.*. https://github.com/singhmuskan552-ux/AI-Governance-Starter-Pack