# Packet F1 prompt — urban resilience framework extraction (production batch)

Use this prompt in NotebookLM for the first production **framework** batch.

- **Packet ID:** `F1_framework_core_urban`
- **Source Titles:**
  - `Global City Resilience Index.pdf`
  - `WGS-A Blueprint for Holistic Urban Resilience.pdf`
  - `Climate Resilience Assessment in Regions, Cities, Strategic Services, and Critical Infrastructure_Implementation and Outcomes.pdf`

## Copy-paste prompt (NotebookLM)

```text
Check if these exact source titles are present in the notebook:
- Global City Resilience Index.pdf
- WGS-A Blueprint for Holistic Urban Resilience.pdf
- Climate Resilience Assessment in Regions, Cities, Strategic Services, and Critical Infrastructure_Implementation and Outcomes.pdf

If any are missing, stop and return only: {"error": "missing_sources", "missing": [list missing titles]}

Otherwise, extract up to 20 raw rows from ONLY these sources. Focus on:
- Indicator concepts used in these frameworks.
- Associated category or aspect language.
- Explicit "asset", "process", or "output" wording (if stated; otherwise "not explicit").

Requirements:
1. Flat JSON array output.
2. One row per source statement/concept.
3. Keep framework-specific wording; do NOT harmonize or merge rows.
4. Fields must be source-near; use "not explicit" if the source doesn't support a field.
5. Provide a reference list at the end.

JSON Schema:
[
  {
    "row_kind": "capacity_category_statement | aspect_statement | indicator_concept_candidate",
    "source_id_reference": "source title",
    "quoted_or_close_paraphrase": "quote or close paraphrase",
    "candidate_indicator_label": "label or 'not explicit'",
    "candidate_capacity_category": "category or 'not explicit'",
    "candidate_aspect": "aspect or 'not explicit'",
    "candidate_dimension_if_explicit": "asset | process | output | not explicit",
    "extraction_notes": "brief notes",
    "citation": "(Author, Year, page)"
  }
]
```

## Save target after NotebookLM responds

Save the raw NotebookLM response verbatim under:
- `ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_batch_F1_framework_notebooklm_raw.md`
