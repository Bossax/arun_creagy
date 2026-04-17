# Packet M1 prompt — methodological literature extraction (production batch)

Use this prompt in NotebookLM for the first production **methodological** batch.

- **Packet ID:** `M1_methodological_core_capacity`
- **Source Titles:** 
  - `Climate adaptation indicators and metrics - State of local policy practice.pdf`
  - `sustainability-14-02481.pdf`
  - `Urban Resilience - Methodologies, Tools and Evaluation.pdf`

## Copy-paste prompt (NotebookLM)

```text
Check if these exact source titles are present in the notebook:
- Climate adaptation indicators and metrics - State of local policy practice.pdf
- sustainability-14-02481.pdf
- Urban Resilience - Methodologies, Tools and Evaluation.pdf

If any are missing, stop and return only: {"error": "missing_sources", "missing": [list missing titles]}

Otherwise, extract up to 20 raw rows from ONLY these sources. Focus on:
- Capacity categories and sub-dimensions.
- Language suggesting technical, financial, social, informational, or coordination capacity.
- Explicit "asset", "process", or "output" framing (if stated; otherwise "not explicit").

Requirements:
1. Flat JSON array output.
2. One row per source statement.
3. Keep duplicates/competing labels across sources; do NOT harmonize.
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
- `ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_batch_M1_methodological_notebooklm_raw.md`
