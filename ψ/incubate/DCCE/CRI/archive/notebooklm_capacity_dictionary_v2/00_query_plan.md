# NotebookLM query plan — CRI capacity tagging dictionary v2 refresh

## 1. Purpose of this refresh

This plan resets the CRI NotebookLM capacity dictionary v2 workflow to a **clean fresh-start pipeline**.

The governing problem in the earlier workflow was boundary drift: NotebookLM was asked to do transformation-heavy work that should be controlled locally in the repo. This refresh restores the intended split:

- **NotebookLM = literature-grounded extraction only**
- **Local repo workflow = harmonisation, flattening, de-duplication, QC, canonical register maintenance, and downstream artifact generation**

This file prepares the pipeline for later orchestration. It does **not** execute NotebookLM and does **not** recreate deleted outputs.

## 2. Governing boundary

This plan follows the discipline recorded in the local notes:

- `ψ/memory/logs/info/2026-04-07_22-59_notebooklm-usage-discipline.md`
- `ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md`

### 2.1 Boundary statement

NotebookLM may be used only for:

- extracting source-backed candidate concepts from uploaded literature;
- harvesting candidate capacity-category and aspect language from sources;
- harvesting indicator-concept candidates from comparative framework literature;
- returning citation-bearing raw rows that can later be processed locally.

NotebookLM must **not** be used for:

- harmonising labels across sources;
- flattening nested outputs into the living register;
- de-duplicating or merging candidate rows across passes;
- maintaining the canonical v2 taxonomy;
- globally dimension-tagging the evolving register when the source is not explicit;
- QC over the living local register;
- generating downstream dictionary or crosswalk artifacts.

### 2.2 Repo/notebook separation

NotebookLM prompts may refer only to:

- literature uploaded into the NotebookLM notebook; and
- text pasted directly into NotebookLM by the human.

Repo-local markdown files are **not** notebook-accessible. They are local working context for humans and local scripts only.

That means prompts must **not** tell NotebookLM to open or rely on repo paths such as:

- `ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`
- `ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md`
- `ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md`

Those files remain local reference points for the team when reviewing and harmonising outputs outside NotebookLM.

## 3. Working objective

The objective is to build a stronger evidence base for the future v2 capacity tagging dictionary by collecting **raw, citation-bearing candidate rows** covering broader capacity areas than the governance-heavy v1 baseline.

The extraction workflow should therefore surface candidate language across whatever capacity areas are evidenced in the literature, for example:

- institutional / governance;
- technical;
- financial;
- social / community;
- informational / data / knowledge;
- planning / coordination / implementation;
- service / delivery / performance-related capacity.

These areas are **not** treated as a final canonical list at extraction time. NotebookLM should harvest source-backed candidate labels; the local workflow decides later how they are harmonised into the living register.

## 4. Target raw extraction shape

All NotebookLM extraction passes should return **flat, row-oriented raw outputs**. One row should represent one source-backed candidate statement or indicator concept. Duplicates are allowed and often desirable at this stage.

### 4.1 Preferred raw row fields

Use the following fields in raw extraction outputs:

| Field | Purpose |
| --- | --- |
| `row_kind` | One of `capacity_category_statement`, `aspect_statement`, or `indicator_concept_candidate` |
| `source_id_reference` | Short source handle or source title |
| `quoted_or_close_paraphrase` | Short quote or close paraphrase anchored in the source |
| `candidate_indicator_label` | Candidate concept label if the source supports one; otherwise `not explicit` |
| `candidate_capacity_category` | Capacity-category wording from or closely grounded in the source |
| `candidate_aspect` | Aspect wording from or closely grounded in the source |
| `candidate_dimension_if_explicit` | `asset`, `process`, `output`, or `not explicit` |
| `extraction_notes` | Short note on ambiguity, scope, or why a field is `not explicit` |
| `citation` | In-text citation tied to the source evidence |

### 4.2 Raw extraction rules

- Keep rows **flat**; do not return nested catalogues.
- Keep rows **source-near**; do not rewrite into a canonical taxonomy.
- Preserve duplicates or near-duplicates across sources.
- If a field is not supported by the source, use `not explicit` rather than inferring a final value.
- If a source offers broader capacity areas than governance, keep that breadth in the raw rows.

## 5. Operating model and pass structure after pilot

The April 2026 pilot (documented in [`03_pilot_flattening_qc_note.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/03_pilot_flattening_qc_note.md) and the pilot-only synthesis in [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md)) confirmed that the **extraction-only shape** and row schema are workable with modest local effort.

It also exposed a critical limitation: NotebookLM silently substituted nearby uploaded literature when exact requested source titles were missing or not literal matches. As a result, the pilot validated the **workflow shape and schema**, but **did not authorise full-scale extraction** from the intended source packet.

The next-iteration operating model therefore tightens as follows:

1. **Smaller, exact-title source packets per run**  
   - Each NotebookLM run must be anchored to a **small, explicitly named source packet** (one source or a very small cluster).  
   - The human names the exact titles; NotebookLM is instructed to treat them as a hard filter.

2. **Narrower batched extraction runs**  
   - Each run serves **one analytical purpose only** (e.g. methodological categories, framework indicators, or a single bounded gap-fill question).  
   - Do **not** ask for all capacity areas or dimensions in a single broad sweep.

3. **Fail-fast source-fidelity gate before accepting a run**  
   - If the named sources are not present in the notebook, or if NotebookLM cannot clearly restrict itself to them, the run must **fail fast**: report the mismatch explicitly and **do not** substitute other literature.  
   - Any run that silently substitutes sources fails the source-fidelity gate and must be discarded.

4. **Open candidate extraction + fixed schema**  
   - Keep first-pass extraction **open to whatever capacity categories and aspects the sources actually support**, without forcing them into a fixed final taxonomy.  
   - The **row schema is fixed** (Section 4.1), but category/aspect vocabularies remain candidate-only at extraction time.

5. **Targeted follow-up passes only after local review**  
   - Use Pass 4+ only when local review of saved raw rows reveals gaps or ambiguities.  
   - Each follow-up run is narrowly targeted (one gap or ambiguity, one small source packet) and remains extraction-only.

6. **Dimension tagging discipline**  
   - `candidate_dimension_if_explicit` may take `asset`, `process`, or `output` **only when explicit in the source evidence**.  
   - When the source does not clearly support a dimension, keep `candidate_dimension_if_explicit` as `not explicit`.  
   - Do **not** use NotebookLM to globally infer dimensions across the register.

Within this operating model, the refresh still uses a small number of tightly bounded passes. Only **extraction passes** go through NotebookLM.

### Pass 1 — Local-only transformation over pasted existing material

**Type:** local only, not a NotebookLM notebook pass.

**Purpose:** if needed, convert pasted text from the existing dictionary and/or other local notes such as Tik's CBI notes into the same flat raw-row shape used by later extraction outputs.

**Rules:**

- Treat this as a local transformation pattern over human-pasted text.
- Do not assume NotebookLM can access repo files.
- Do not harmonise, merge, or canonise anything here.
- Preserve original wording as candidate labels where possible.
- If the pasted local material already points to broader areas beyond governance, preserve them as candidate rows rather than collapsing them.

**Output:** a local raw file under `responses/` in the same row-oriented shape used by the NotebookLM passes.

### Pass 2 — NotebookLM extraction from methodological literature

**Type:** NotebookLM extraction only.

**Purpose:** harvest source-backed candidate statements about capacity categories and aspects from methodological literature relevant to climate resilience / CRI-type measurement.

**What to extract:**

- explicit category labels;
- explicit aspect labels;
- close-paraphrase evidence rows where the source implies a category or aspect without naming it in exactly the same way;
- any explicit asset / process / output framing if present in the source.

**What not to ask NotebookLM to do:**

- build a final category catalogue;
- pick the best global labels;
- reconcile terms across sources;
- remove duplicates.

**Output:** raw evidence rows saved verbatim under `responses/`.

### Pass 3 — NotebookLM extraction from urban resilience framework literature

**Type:** NotebookLM extraction only.

**Purpose:** harvest indicator-concept candidate rows from urban resilience frameworks and adjacent literature.

**What to extract:**

- candidate indicator concepts used in frameworks;
- the source-near category / aspect language associated with those concepts;
- evidence snippets and citations;
- explicit dimension wording only when the source clearly supports it.

**What not to ask NotebookLM to do:**

- merge framework concepts into a single CRI taxonomy;
- compare against previous pass outputs unless the human pastes text directly into the prompt;
- decide the canonical register structure.

**Output:** raw evidence rows saved verbatim under `responses/`.

### Pass 4+ — Targeted extraction only

**Type:** optional NotebookLM extraction only.

These later passes are allowed only when they stay extraction-scoped.

Valid uses include:

- **gap fill:** extract more evidence for under-covered capacity areas;
- **ambiguity check:** extract rows for competing labels or unclear aspect wording;
- **evidence completion:** extract additional source-backed rows for concepts that appear thinly supported after local review;
- **dimension evidence check:** look specifically for explicit source language that supports `asset`, `process`, or `output` where this is unclear.

Invalid uses include:

- asking NotebookLM to merge previous outputs;
- asking NotebookLM to de-duplicate rows;
- asking NotebookLM to QC the evolving local register;
- asking NotebookLM to rewrite the canonical dictionary.

## 6. Local harmonisation and post-processing flow

Everything below happens **locally in the repo**, not inside NotebookLM.

### 6.1 Save raw NotebookLM outputs verbatim

For every NotebookLM run:

1. save the returned output **verbatim** under `ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/`;
2. keep each response as its own run artifact;
3. do not rewrite the raw response before saving it.

This preserves traceability and makes later harmonisation decisions auditable.

### 6.2 Flatten and clean locally

After raw responses are saved:

1. convert response content into one row per evidence statement or candidate concept;
2. standardise formatting only (field order, markdown table alignment, JSON cleanup, line breaks);
3. keep source-near labels intact at this stage;
4. preserve duplicates and competing formulations.

### 6.3 Harmonise locally

Only after raw rows exist locally should the team:

1. compare overlapping rows across passes;
2. cluster near-duplicates;
3. choose local canonical labels for the living register;
4. decide how broader capacity areas should be represented in the v2 structure;
5. assign or confirm dimensions where local review supports it;
6. maintain traceability back to the source rows.

This is the step where the repo workflow, not NotebookLM, performs harmonisation, de-duplication, and canonical register maintenance.

### 6.4 Update the synthesis register locally

The working synthesis target remains:

- `ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md`

Update that file only after local flattening and harmonisation review. It should contain the curated synthesis register, not raw NotebookLM dumps.

### 6.5 Generate downstream artifacts only after local review

Only after the synthesis register has been locally reviewed should the team generate downstream artifacts such as:

- `CRI_Capacity_Tagging_Dictionary_v2.md`
- `CRI_CBI_indicator_crosswalk.md`

Those outputs are intentionally downstream of local harmonisation and are **not** part of the NotebookLM extraction step.

## 7. Pilot run status and gates

### 7.1 Pilot sequence (completed)

The initial pilot sequence has been executed and reviewed:

1. **Pilot Pass 1 (local-only):** transformed a small pasted subset of the existing dictionary and Tik's CBI-related notes into the raw-row shape.  
   - Raw JSON: `responses/2026-04-08_pilot_pass1_local_raw_rows.json`.
2. **Pilot Pass 2 (NotebookLM):** ran one tightly bounded extraction over a small subset of methodological literature.  
   - Raw NotebookLM response: `responses/2026-04-08_pilot_pass2_methodological_notebooklm_raw.md`.
3. **Pilot Pass 3 (NotebookLM):** ran one tightly bounded extraction over a small subset of urban resilience framework literature.  
   - Raw NotebookLM response: `responses/2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md`.
4. Saved all three pilot outputs verbatim under `responses/`.  
5. Performed local flattening and a first harmonisation test on the pilot rows only, documented in [`03_pilot_flattening_qc_note.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/03_pilot_flattening_qc_note.md) and reflected in the pilot-only register in [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md).

### 7.2 Pilot success criteria / QC gates

The pilot QC still uses the original gates, now applied to the completed runs. A pilot iteration must pass all of the following **and** the source-fidelity gate (Section 7.3) before scaling up:

1. **Citation coverage**
   - every extracted row has a usable citation;
   - source references are traceable enough for local review.

2. **Row structure consistency**
   - outputs are flat and row-oriented;
   - required fields are present consistently;
   - nested catalogue structures are absent or rare enough to fix easily.

3. **Low drift into synthesis**
   - NotebookLM stayed close to extraction;
   - it did not attempt to harmonise, de-duplicate, or rewrite a canonical taxonomy;
   - it preserved source-near differences.

4. **Manageable local harmonisation effort**
   - the local team can flatten and review the pilot without disproportionate cleanup work;
   - if cleanup burden is too high, revise the query pack before scaling.

5. **Boundary compliance**
   - prompts did not treat repo files as notebook-accessible;
   - local-only work remained local.

### 7.3 Source-fidelity gate (added after pilot)

The April 2026 pilot introduced an additional mandatory gate:

- **Source-packet fidelity**  
  - When a run is instructed to use an exact named source packet, the effective evidence in the response must come from those sources.  
  - If NotebookLM reports that the named titles are not present and instead uses substitute thematic literature, the run **fails** this gate even if the row shape is correct.  
  - Runs that fail this gate may still be used as methodological examples, but they **cannot** be used as proof that the planned source packet is working.

Future runs must implement the **fail-fast source-fidelity behaviour** encoded in [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md): when the exact named sources are not available, NotebookLM should report the mismatch and stop rather than substituting.

### 7.4 Scale-up gate (revised)

Only after a pilot iteration passes:

1. all QC gates in Section 7.2; **and**
2. the source-fidelity gate in Section 7.3;

should orchestrator run any wider extraction sequence across the notebook corpus.

If the pilot fails any gate:

- revise the prompts in `01_query_pack.md` and/or the NotebookLM source inventory to tighten source-fidelity; and
- rerun the pilot over **small, exact-title source packets** before continuing.

## 8. Immediate next-step status (post-pilot)

As of the April 2026 pilot review:

- The extraction-only boundary and row schema are validated in shape.  
- The pilot harmonised register remains **pilot-only** and is not, on its own, a green light for unconstrained extraction.  
- The next execution cycle is a **staged full execution** across the notebook corpus, under strict source-fidelity and batching constraints.

Immediate next orchestration steps are:

1. Update `01_query_pack.md` to encode fail-fast source-fidelity behaviour, smaller exact-title source packets, and narrower per-run analytical scope.  
2. Align the CRI NotebookLM notebook source list so that the intended source titles are present with known, stable titles.  
3. Initiate full execution by running the first wave of small, exact-title extraction batches using the updated prompts.  
4. Monitor these batches against the QC and source-fidelity gates; pause and adjust prompts or the source inventory if any batch fails a gate.  

This file does not execute any NotebookLM runs; it defines the operating model and gates for the next iteration.
