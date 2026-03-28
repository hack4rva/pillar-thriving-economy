> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../docs/methodology.md) for details.

# Master Research Prompt – Comprehensive Template
*Version 1.0 | 2026-03-24 (Updated)* 

## Executive Summary
This document serves as a standardized, production-ready template for executing AI-powered deep research. It replaces previous placeholder-heavy drafts with a concrete, source-backed workflow designed to yield actionable strategic insights. By leveraging structured prompting techniques [1] and adhering to strict data validation protocols, this template ensures that AI-generated outputs are reliable, properly cited, and directly aligned with business objectives. It incorporates best practices for large language model interactions [2], ensuring consistent formatting and rigorous quality assurance.

--- 

## 🎯 Goal
Create a reproducible, source-backed research workflow that reliably delivers **action-oriented insights** for strategic decision-making, utilizing structured prompts and iterative workflows to improve quality [1]. 

--- 

## 📋 Table of Contents
1. [Context & Scope](#context--scope) 
2. [Research Questions & Objectives](#research-questions--objectives) 
3. [Methodology & Data Sources](#methodology--data-sources) 
4. [Prompt Structure (System → User → Assistant)](#prompt-structure-system--user--assistant) 
5. [Output Format & Deliverables](#output-format--deliverables) 
6. [Quality Assurance & Review Checklist](#quality-assurance--review-checklist) 
7. [References & Citations](#references--citations) 

--- 

## Context & Scope
- **Industry focus:** *Technology & Innovation* (can be swapped for any sector). 
- **Time horizon:** Short-term (3-6 months) market trends plus medium-term (12-24 months) strategic outlook. 
- **Geography:** Global, with explicit notes for NA, EU, APAC when data diverge. 

> **Note:** All dates are expressed as **YYYY-MM** when the exact day is not required (e.g., "2025-02" for a February 2025 report). 

--- 

## Research Questions & Objectives

| # | Question | Business Impact |
|---|----------|-----------------|
| 1 | Which emerging AI-driven product categories will generate > $5B annual revenue by 2027? | Guides investment pipeline and partnership scouting. |
| 2 | What regulatory shifts are expected in the EU AI Act after 2025-07? | Enables compliance-by-design and risk mitigation. |
| 3 | How are top-5 competitors reallocating R&D spend post-2024 Q4? | Informs budgeting and talent acquisition strategy. |
| 4 | What talent-skill gaps are most acute in ML Ops across APAC? | Supports talent-pipeline planning and up-skilling programs. |

--- 

## Methodology & Data Sources

1. **Primary data** – Structured surveys (N = 500 executives) and semi-structured interviews (30 subject-matter experts). 
2. **Secondary data** – 
 * Market-size reports from **Gartner** (2025-03) and **IDC** (2025-01). 
 * Regulatory trackers from **EU Commission** (2025-06) and **FTC** (2025-04). 
 * Financial statements (SEC 10-K, FY 2024-2025) for top-5 firms. 
3. **AI-assisted extraction** – Use advanced language models to generate text and extract insights from a prompt [2], utilizing a deterministic temperature (0.0) to parse PDFs and web-tables accurately. 

> **Why this mix?** Combining human-centric insights with vetted secondary sources reduces bias while keeping the research cost-effective. 

--- 

## Prompt Structure (System → User → Assistant)

### 1️⃣ System Prompt (sets the role)
```markdown
You are a senior research analyst specializing in technology market intelligence. 
Your output must be **evidence-backed**, cite sources in Harvard style, and include a concise "So What?" section for each insight. 
If a data point is unavailable, state "Data not publicly disclosed" rather than "Unknown". 
All dates must follow ISO-8601 (YYYY-MM or YYYY). 
```

### 2️⃣ User Prompt (what we ask the model)
```markdown
Using the methodology outlined above, answer the research questions listed in Section 2. 
Provide: 
- A bullet-point insight for each question (max 2 sentences). 
- The source (link or citation key) for every factual claim. 
- An actionable recommendation (≤ 1 sentence). 

Format the response as a Markdown table with columns: **Question**, **Insight**, **Source**, **Recommendation**. 
```

### 3️⃣ Assistant Prompt (example of a correct response)
```markdown
| Question | Insight | Source | Recommendation |
|----------|---------|--------|----------------|
| 1 | Generative-AI content creation tools are projected to exceed $6B in 2027 revenue, driven by enterprise adoption of large-language-model APIs. | Gartner, "AI Market Forecast 2025-2027", 2025-03. | Prioritize API-integration partnerships with at least two leading LLM providers by Q4 2026. |
|... |... |... |... |
``` 

--- 

## Output Format & Deliverables

- **Executive Summary** – ≤ 300 words, high-level takeaways + "Next Steps" bullet list. 
- **Full Research Report** – 6-8 pages, includes tables, charts, and an appendix of raw data. 
- **Data Repository** – CSV files stored in a shared drive, versioned with ISO timestamps (e.g., `2026-03-24_v1.csv`). 

All deliverables must be reviewed against the **Quality Assurance Checklist** below before client hand-off. 

--- 

## Quality Assurance & Review Checklist

| Item | Description | Done (✔/✘) |
|------|-------------|------------|
| 1 | All factual statements have a citation (URL or report reference). | ✘ |
| 2 | Dates conform to YYYY-MM or YYYY format. | ✘ |
| 3 | No placeholder text ("REPLACEME", "INSERT", "TBD", "LOREM"). | ✘ |
| 4 | AI disclaimer removed; responsibility rests with analyst. | ✘ |
| 5 | "Data not publicly disclosed" used where gaps exist. | ✘ |
| 6 | Tables are rendered correctly in Markdown preview. | ✘ |
| 7 | Final document proof-read for grammar & consistency. | ✘ |

*Action:* Assign the checklist to the lead analyst; complete before the final sign-off deadline (2026-04-15). 

--- 

## References

1. *My Guide to Deep Research, Prompt Engineering, and Multi-Step ...*. https://www.reddit.com/r/ChatGPTPro/comments/1in87ic/mastering_aipowered_research_my_guide_to_deep/
2. *Prompt engineering | OpenAI API*. https://developers.openai.com/api/docs/guides/prompt-engineering/