---
title: NotebookLM extraction vs local harmonisation
created: 2026-04-08
related:
  - 2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md
---

# NotebookLM extraction vs local harmonisation

NotebookLM should be used mainly for literature-grounded extraction and citation-bearing concept harvesting. It is useful for surfacing indicator concepts, candidate capacity categories, aspect labels, evidence snippets, and source-backed language from the notebook corpus.

Heavy synthesis work over evolving local artifacts should stay in the repo, not be offloaded back into NotebookLM. In particular, harmonisation, flattening nested outputs into row-level records, de-duplication across passes, and QC over a living indicator concept register should be performed locally where structure is controlled and previous outputs are explicit.

When NotebookLM is asked to do transformation-heavy work, it tends to drift back into open-ended literature synthesis. The result can still be citation-rich and useful, but it will often be structurally misaligned with the intended workflow step. That creates downstream cleanup work and blurs the boundary between extraction and synthesis.

Recommended discipline:
- Use NotebookLM for extraction.
- Save raw outputs verbatim.
- Do row-level harmonisation and QC locally.
- Treat NotebookLM later-pass outputs as supporting evidence unless they strictly match the expected transform shape.

Logged from retrospective workflow on 2026-04-08.
