# NotebookLM query pack — CRI capacity tagging dictionary v2 refresh

This query pack is rewritten for an **extraction-only** NotebookLM workflow.

Its purpose is to help the team harvest citation-bearing raw rows from notebook literature. It must **not** be used to ask NotebookLM to harmonise, consolidate, de-duplicate, QC, or maintain the living v2 register.

## 1. Boundary reminder

NotebookLM prompts in this file may refer only to:

- literature uploaded into the notebook; and
- text pasted directly into NotebookLM by the human.

NotebookLM prompts in this file must **not** claim access to repo-local markdown files or local synthesis artifacts.

## 2. Global extraction-only instruction block

Use or adapt the following instruction block for every NotebookLM extraction run. It encodes the extraction-only boundary, fail-fast source-fidelity behaviour, and dimension-tagging discipline learned from the pilot.

```text
You are assisting with extraction only for the CRI capacity tagging dictionary v2 workflow.

Your job is to harvest source-backed candidate rows from the uploaded literature or from text pasted directly by the human.

Return flat, row-oriented raw outputs only.

Required behaviour:
1) Stay close to the source language.
2) Keep one row per source-backed statement or candidate concept.
3) Preserve duplicates or near-duplicates across sources.
4) Use citations for every row.
5) If a field is not directly supported by the source, write "not explicit" rather than inferring a final answer.
6) Only assign "asset", "process", or "output" in the `candidate_dimension_if_explicit` field when the source uses clear dimension language; otherwise keep it as "not explicit".
7) When the prompt names specific sources or a specific small source packet, restrict your evidence strictly to those sources.
8) Before answering, check whether all explicitly named sources in the prompt are present in the notebook. If any are missing or unclear, stop and report which ones are unavailable instead of substituting other literature.
9) At the end, include a reference list for all cited sources used in the response.

Explicit prohibitions:
- Do not harmonise labels across sources.
- Do not remove duplicates.
- Do not merge rows.
- Do not rewrite the output into a canonical taxonomy.
- Do not infer missing fields beyond what the source supports.
- Do not infer dimensions globally when they are not explicit in the evidence.
- Do not compare or consolidate with prior pass outputs unless that text is pasted directly into the prompt.
- Do not QC or repair a living local register.
- Do not generate downstream dictionary, crosswalk, or synthesis artifacts.
- Do not silently substitute nearby literature when requested sources are unavailable; instead, clearly report the mismatch and stop.
```

## 3. Raw row schema for NotebookLM outputs

All NotebookLM extraction responses should use the following flat JSON array shape:

```json
[
  {
    "row_kind": "capacity_category_statement | aspect_statement | indicator_concept_candidate",
    "source_id_reference": "short source handle or source title",
    "quoted_or_close_paraphrase": "short quote or close paraphrase grounded in the source",
    "candidate_indicator_label": "source-backed candidate label or 'not explicit'",
    "candidate_capacity_category": "source-backed category wording or 'not explicit'",
    "candidate_aspect": "source-backed aspect wording or 'not explicit'",
    "candidate_dimension_if_explicit": "asset | process | output | not explicit",
    "extraction_notes": "brief note on ambiguity, scope, or why a field is not explicit",
    "citation": "(Author, Year, page/section if available)"
  }
]
```

### Raw row rules

- Return a **flat array** only.
- Do **not** nest rows under categories or frameworks.
- Use `not explicit` when a source does not support a field, including for `candidate_dimension_if_explicit` unless the dimension is explicit in the source.
- Keep rows separate even when they look similar.
- Prefer close paraphrase or direct wording over rewritten synthesis language.
- Treat any lists of capacity areas or dimensions mentioned in the prompt as coverage lenses only, not as mandatory output vocabularies. It is acceptable if some listed areas are not represented when the sources do not support them.

## 4. Local-only pattern — Pass 1

Pass 1 is **not** a NotebookLM notebook pass. It is a local transformation pattern for cases where the human pastes text from the existing dictionary or related local notes such as Tik's CBI notes.

### Pass 1 local instruction block

```text
Work only on the text pasted by the human.

Convert the pasted material into the same flat raw-row schema used by the NotebookLM extraction passes.

Preserve the source wording as much as possible.
Do not invent new concepts.
Do not harmonise labels.
Do not remove duplicates.
If a field is not explicit in the pasted text, write "not explicit".
```

### Pass 1 local prompt template

```text
From the pasted local text, extract source-near candidate rows in the required JSON array format.

Focus on:
- any candidate capacity-category wording;
- any candidate aspect wording;
- any candidate indicator concepts;
- any broader areas beyond governance if they appear in the pasted text.

Do not consolidate. Do not normalise labels. Do not infer a final taxonomy.
```

## 5. NotebookLM Pass 2 — methodological literature extraction

### Pass 2 purpose

Extract source-backed candidate statements about capacity categories and aspects from methodological literature relevant to climate resilience / CRI-type measurement.

### Pass 2 prompt template

```text
Using only the uploaded methodological literature relevant to climate resilience capacity and related measurement approaches, extract flat raw rows in the required JSON array format.

This run must be scoped to a small, explicit source packet named in the prompt (for example, one or a few exact source titles). Restrict your evidence strictly to those named sources.

Focus on source-backed candidate statements about:
- capacity categories;
- aspects or sub-dimensions of capacity;
- wording that suggests broader capacity areas beyond governance, such as technical, financial, social, informational, planning, coordination, implementation, or service-related capacity, when and only when those are supported by the named sources;
- any explicit asset / process / output framing if the source states it.

Rules:
- Keep one row per source-backed statement.
- Preserve duplicates or competing labels across sources.
- Do not group rows into a final category catalogue.
- Do not choose the best labels.
- Do not harmonise or de-duplicate.
- Use "not explicit" where the source does not support a field.
- If any of the explicitly named sources for this run are not present in the notebook, stop and return a short explanation listing which titles are missing instead of answering from substitute sources.

Return the JSON array first, then a reference list.
```

## 6. NotebookLM Pass 3 — urban resilience framework extraction

### Pass 3 purpose

Extract indicator-concept candidate rows from urban resilience framework literature.

### Pass 3 prompt template

```text
Using only the uploaded literature on urban resilience frameworks and closely related resilience measurement approaches, extract flat raw rows in the required JSON array format.

This run must be scoped to a small, explicit source packet named in the prompt (for example, one or a few exact framework titles). Restrict your evidence strictly to those named sources.

Focus on:
- candidate indicator concepts used in the named frameworks;
- associated source-backed category or aspect language when available;
- short quoted or close-paraphrase evidence;
- explicit asset / process / output wording only when the source clearly supports it.

Rules:
- Keep one row per source-backed statement or candidate concept.
- Preserve framework-specific wording.
- Preserve duplicates across frameworks.
- Do not merge conceptually similar rows.
- Do not rewrite rows into a CRI-ready taxonomy.
- Do not compare or consolidate with previous pass outputs unless those rows are pasted directly into the prompt.
- Use "not explicit" where needed.
- If any of the explicitly named framework sources for this run are not present in the notebook, stop and return a short explanation listing which titles are missing instead of answering from substitute sources.

Return the JSON array first, then a reference list.
```

## 7. NotebookLM Pass 4+ — targeted extraction only

Later NotebookLM passes are allowed only when they remain extraction-scoped and are triggered by local review of previously saved raw rows (for example, gaps or ambiguities discovered in the pilot or later batches).

### 7.1 Targeted gap-fill prompt template

Use this when local review finds under-covered areas and the team wants more source-backed rows.

```text
Using only the uploaded literature, extract additional raw rows in the required JSON array format for the following under-covered area or question:

[insert specific local need, e.g. "financial capacity", "data and information management", "community participation", or another bounded gap]

Rules:
- Extract only rows relevant to that bounded gap.
- Keep one row per source-backed statement.
- Preserve duplicates and competing labels.
- Do not harmonise or summarise the wider corpus.
- Do not merge with prior outputs.
- Use "not explicit" where needed.
- If the prompt names a small source packet, restrict evidence to those sources and fail fast if they are not available instead of substituting other literature.

Return the JSON array first, then a reference list.
```

### 7.2 Ambiguity / evidence-completion prompt template

Use this when local review identifies a narrow unresolved issue and the team wants more evidence, not synthesis.

```text
Using only the uploaded literature, extract raw rows in the required JSON array format that help clarify the following bounded ambiguity or evidence gap:

[insert specific question, e.g. "how sources distinguish coordination from participation", "whether this concept is framed as process or output", or "what wording is used for technical capacity in city resilience frameworks"]

Rules:
- Return only source-backed rows relevant to the stated ambiguity.
- Do not decide a final canonical label.
- Do not merge rows.
- Do not reconcile sources into one answer.
- Use "not explicit" where the source does not settle the issue.
- If the prompt names a small source packet, restrict evidence to those sources and fail fast if they are not available instead of substituting other literature.

Return the JSON array first, then a reference list.
```

## 8. Explicit do / don't summary

### Do

- extract source-backed rows;
- keep outputs flat and row-oriented;
- preserve source-near wording;
- retain duplicates and disagreements;
- mark unsupported fields as `not explicit` and avoid inferring dimensions when not explicit;
- include citations and a reference list;
- restrict evidence to the small, explicitly named source packet for each run;
- fail fast and report when requested sources are not available instead of substituting.

### Don't

- harmonise labels across sources;
- de-duplicate or merge rows;
- produce a nested synthesis catalogue;
- infer a canonical capacity taxonomy;
- globally assign missing dimensions when not explicit in the source;
- QC the living local register;
- generate `CRI_Capacity_Tagging_Dictionary_v2.md` or `CRI_CBI_indicator_crosswalk.md`;
- broaden a run to the entire notebook corpus when the prompt is meant for a small, explicit source packet.

## 9. Local follow-on reminder

After NotebookLM returns raw outputs:

1. save them verbatim under `responses/`;
2. flatten and clean locally;
3. harmonise and maintain the canonical register locally in `synthesis/indicator_concept_register.md`;
4. generate downstream artifacts only after local review.

That local work happens outside NotebookLM.
