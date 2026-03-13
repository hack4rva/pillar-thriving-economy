# Recommended Architectures (Sketches)

## Search + Explain (Contracting)
- Static index of sampled solicitations -> lightweight search -> result cards with plain-language explainers + source badges -> official portal links.
- Tech: simple web app, small JSON index, no DB required.

## Intake -> Sequenced Steps (Business Setup)
- Few-question intake -> branch to source-cited step list -> official page handoff.
- Tech: static site + JSON/YAML rules; keep branches narrow and labeled.

## Content-First Explainer Hub
- Source-backed FAQs/glossary + curated links; emphasize citations and last-checked dates.
- Tech: static site generator; markdown-driven.
