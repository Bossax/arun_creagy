---
title: NotebookLM source fidelity and parameter discipline
created: 2026-04-08
related:
  - 2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md
---

# NotebookLM source fidelity and parameter discipline

When using NotebookLM as part of a structured evidence workflow, the orchestration layer must make every execution parameter explicit. That includes the exact `notebook_id`, a concrete `session_id`, visible browser settings when required, and the exact source-binding assumption for the batch. These details cannot be left implicit or delegated to a subtask's judgment, because the quality of the evidence output depends on them.

Source fidelity must also be treated as a hard gate, not a cleanup preference. Repo-side filenames or inbox handles are not trustworthy substitutes for actual NotebookLM source titles. If a batch depends on named sources, the workflow should first run a title-resolution step that asks NotebookLM to identify the real titles from notebook-readable content. Only after those titles are confirmed should the extraction prompt be written and executed.

If the sources cannot be resolved or are not present in the notebook, the batch should stop. A superficially useful raw output is not enough if the source-binding rule was violated. Clean evidence workflows require explicit parameters, title resolution from content, and fail-fast handling of missing sources.

Logged from `/rrr` on 2026-04-08.
