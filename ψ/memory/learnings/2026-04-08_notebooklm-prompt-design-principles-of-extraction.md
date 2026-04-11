date: 2026-04-08
type: learning
status: distilled
concepts:
  - notebooklm
  - prompt-design
  - extraction
  - guardrail
  - workflow-integrity
  - deep-research
source: ψ/memory/logs/info/2026-04-08_05-28_notebooklm-prompt-design.md
related:
  - 2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md
---

Treat NotebookLM as a **data extraction engine**, not an extension of the Oracle’s brain: design prompts around what information to extract, keep them short enough to type in about a minute, summarize prohibitions instead of listing every rule, and break oversized tasks into atomic extraction passes (or move general instructions into a separate system prompt). This preserves context for sources and keeps NotebookLM runs focused on high‑value extraction instead of brittle, rule‑heavy control scripts.

