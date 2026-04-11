---
title: # Treat NotebookLM as a data extraction engine, not an extension of the Oracle’s
tags: [notebooklm, extraction, prompt-design, source-fidelity, guardrail, workflow-integrity, deep-research]
created: 2026-04-09
source: ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md
---

# # Treat NotebookLM as a data extraction engine, not an extension of the Oracle’s

# Treat NotebookLM as a data extraction engine, not an extension of the Oracle’s brain

## Extraction vs harmonisation

- Use NotebookLM primarily for **literature-grounded extraction and citation-bearing concept harvesting**: indicator concepts, candidate capacity categories, aspect labels, evidence snippets, and source-backed language from the notebook corpus.
- Keep **heavy synthesis and harmonisation work** in the repo: flattening nested outputs into row-level records, de-duplication across passes, and QC over living registers (e.g., indicator concept registers) should be done locally where structure and history are explicit.
- Treat later-pass NotebookLM outputs as supporting evidence unless they strictly match the expected transform shape.

This mirrors the discipline in [`2026-04-08_notebooklm-extraction-vs-local-harmonisation.md`](ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md).

## Prompt design

Treat NotebookLM as a **data extraction engine**, not an extension of the Oracle’s brain:

- Design prompts around **what information to extract**, not around controlling high-level reasoning.
- Keep prompts short enough to type in about a minute.
- Summarize prohibitions instead of listing every rule.
- Break oversized tasks into atomic extraction passes, or move general instructions into a separate system prompt.

This preserves context for sources and keeps NotebookLM runs focused on high‑value extraction instead of brittle, rule‑heavy control scripts. See [`2026-04-08_notebooklm-prompt-design-principles-of-extraction.md`](ψ/memory/learnings/2026-04-08_notebooklm-prompt-design-principles-of-extraction.md) for the original formulation.

## Source fidelity & parameters

When using NotebookLM inside a structured evidence workflow, treat **execution parameters and source binding as hard gates**:

- Make every execution parameter explicit in the orchestration layer: `notebook_id`, concrete `session_id`, relevant browser settings, and the exact source-binding assumption for the batch.
- Do not rely on repo-side filenames or inbox handles as proxies for NotebookLM source titles. Instead, first run a **title-resolution** step that asks NotebookLM to list its source titles and use those strings as canonical identifiers.
- If required sources cannot be resolved or are not present in the notebook, the batch should stop; superficially useful output is not acceptable if the source-binding rule was violated.

These principles come from [`2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md`](ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md).

## Title probes & guardrails

The `notebooklm-rules` guardrail skill relies on a **title probe** against NotebookLM to discover the exact strings it treats as source titles (often still filename-like, e.g., `Global City Resilience Index.pdf`). Guardrails must:

- Treat these raw NotebookLM titles as canonical identifiers for source packets.
- Compare source-packet definitions against these canonical strings, not cleaned human labels, to avoid drift.
- Ensure project plans either quote NotebookLM titles verbatim or clearly map local labels to NotebookLM titles so the guardrail remains auditable.

See [`2026-04-08_notebooklm-title-probe-and-guardrail-implementation.md`](ψ/memory/learnings/2026-04-08_notebooklm-title-probe-and-guardrail-implementation.md) for implementation detail.


---
*Added via Oracle Learn*
