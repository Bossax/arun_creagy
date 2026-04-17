# Raw responses directory note

This directory stores raw pilot and later-pass outputs for the refreshed v2 workflow.

## Rules

1. Save every NotebookLM response verbatim.
2. Keep one file per run.
3. Do not clean, harmonise, de-duplicate, or rewrite the raw response before saving it here.
4. Perform flattening, formatting cleanup, harmonisation, and QC only after the raw response is safely stored.

## Pilot file targets

- Local Pass 1 raw rows already created: [`2026-04-08_pilot_pass1_local_raw_rows.json`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass1_local_raw_rows.json)
- NotebookLM Pass 2 save target: `2026-04-08_pilot_pass2_methodological_notebooklm_raw.md`
- NotebookLM Pass 3 save target: `2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md`

These NotebookLM files should be created only after the human runs the prompts manually and pastes the response verbatim.
