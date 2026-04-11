---
title: NotebookLM title probe and guardrail implementation
created: 2026-04-08
related:
  - 2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md
---

# NotebookLM title probe and guardrail implementation

On 2026-04-08 I implemented the `notebooklm-rules` guardrail skill and ran a minimal NotebookLM MCP probe against the CRI Urban Climate Resilience Frameworks & Indicators notebook.

Key learning:

- For the purposes of source-fidelity gates, the authoritative “titles” that NotebookLM recognises are exactly the strings shown in its source list, many of which are still filename-like (e.g. `Global City Resilience Index.pdf`, `Climate-Resilience-Index-2024-ESI-Center-for-the-Future-of-Cities.pdf`). Even when prompted to avoid filenames, NotebookLM surfaces these raw strings. The guardrail must therefore treat these as canonical identifiers for source packets, and any cleaning or human-friendly renaming must be done carefully without breaking exact matches.

Implications for the guardrail skill:

1. Title resolution steps should ask NotebookLM to list its current source titles and use those strings directly when defining small, exact source packets. Repo-side labels or inbox filenames are not reliable substitutes.
2. The source-fidelity gate should compare packet definitions against these canonical strings, not against cleaned human labels, to avoid silent drift.
3. When project plans refer to sources, they should either quote the NotebookLM strings verbatim or clearly map local labels to NotebookLM titles so the gate remains transparent and auditable.

This learning underpins the title-resolution and source-packet sections in [`notebooklm-mcp-ruleset.md`](.roo/skills/notebooklm-rules/references/notebooklm-mcp-ruleset.md) and should be considered a non-negotiable constraint when designing future NotebookLM extraction batches.

