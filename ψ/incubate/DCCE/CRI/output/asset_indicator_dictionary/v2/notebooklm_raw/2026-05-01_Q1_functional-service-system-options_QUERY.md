# NotebookLM Query (Q1) — Functional Service-System Options (Extraction-Only)

This file contains the **copy/paste prompt** for the next step in the v2 workflow.

Working area orientation: [`ORIENTATION.md`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/v2/ORIENTATION.md:1)

## Fixed parameters (for manual use)

- Notebook: **Urban Resilience - Infrastructure and Assets**
- `notebook_id = urban-resilience-infrastructur`
- `session_id = 6085058f`

## Guardrails (must follow)

- **Extraction-only**: do not ask NotebookLM to harmonize/merge/deduplicate.
- **Cite sources by exact title** as shown in the notebook.
- **Keep output bounded** (ask for concise output) to avoid long responses.

## Prompt to paste into NotebookLM

Extraction-only task.

Across all sources in this notebook, extract **2–3 distinct perspectives/frameworks** for grouping *urban infrastructure/assets* into *functional service systems* (e.g., urban services / lifelines / critical infrastructure).

For EACH perspective, return:
1) Perspective name (short label)
2) Candidate service-system categories under that perspective (bullet list)
3) Evidence: list the **exact notebook source title(s)** that support that perspective (use titles exactly as they appear in the notebook)

Keep the answer concise (max ~300–400 words). **Do not merge/deduplicate across perspectives**; just extract what the sources present.

## Paste-back instruction (after you run it)

After you run the prompt, paste the verbatim output into:

- [`2026-05-01_Q1_functional-service-system-options_raw.md`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/v2/notebooklm_raw/2026-05-01_Q1_functional-service-system-options_raw.md:1)

