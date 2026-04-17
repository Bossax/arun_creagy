# Pilot execution packet — CRI capacity tagging dictionary v2 refresh

This packet defines the **next execution cycle** for the CRI capacity tagging dictionary v2 NotebookLM workflow.

It:

- records the **pilot verdict** based on [`03_pilot_flattening_qc_note.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/03_pilot_flattening_qc_note.md) and the pilot-only synthesis in [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md);
- encodes the **post-pilot operating model** from [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md);
- provides an **execution scaffold for full, staged runs** using the prompts in [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md).

It does **not** run NotebookLM itself; it describes the manual steps and gates.

## 1. Boundary status (unchanged)

- NotebookLM work remains **extraction-only**.  
- Local repo work remains responsible for **flattening, harmonisation, de-duplication, QC, canonical register maintenance, and downstream artifact generation**.  
- No NotebookLM outputs are fabricated here; all real runs must be saved verbatim under `responses/`.

## 2. Pilot verdict

### 2.1 What the pilot did

Completed pilot artifacts:

- Local-only Pass 1:
  - pasted subset source: [`pilot/01_pass1_local_paste_source.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/pilot/01_pass1_local_paste_source.md)
  - flattened JSON: [`responses/2026-04-08_pilot_pass1_local_raw_rows.json`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass1_local_raw_rows.json)
- NotebookLM Pass 2 (methodological literature, with source-fidelity caveat):
  - prompt: [`pilot/02_pass2_methodological_prompt.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/pilot/02_pass2_methodological_prompt.md)
  - raw output: [`responses/2026-04-08_pilot_pass2_methodological_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass2_methodological_notebooklm_raw.md)
- NotebookLM Pass 3 (framework literature, with source-fidelity caveat):
  - prompt: [`pilot/03_pass3_framework_prompt.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/pilot/03_pass3_framework_prompt.md)
  - raw output: [`responses/2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md)
- Local flattening + QC and pilot synthesis:
  - QC / flattening note: [`03_pilot_flattening_qc_note.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/03_pilot_flattening_qc_note.md)
  - pilot-only indicator concept register: [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md)

### 2.2 QC outcome

From the QC note, the pilot:

1. **Validated the extraction-only shape and schema.**  
   - NotebookLM returned flat JSON arrays matching the target row schema.  
   - Local flattening effort was modest.

2. **Validated the local harmonisation pattern.**  
   - Raw rows were flattened, row IDs assigned, and a pilot-only synthesis register constructed for review.

3. **Failed strict source-packet fidelity.**  
   - NotebookLM reported that requested pilot source titles were not literal matches in the notebook and substituted nearby uploaded literature instead.  
   - The pilot therefore validated the **workflow shape**, not the **exact planned source packets**.

4. **Did not, on its own, authorise unconstrained full-scale extraction.**  
   - The pilot is usable as a methodological proof-of-concept and harmonisation test.  
   - Scale-up must happen under tighter **source-fidelity** and **batching** controls.

These conclusions are now encoded into the operating model in [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md) and the prompt pack in [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md).

## 3. Operating model for next execution cycle

The next cycle is **staged full execution** across the NotebookLM corpus, under the following constraints (mirroring Section 5 of [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md)):

1. **Smaller, exact-title source packets per run**  
   - Each run is anchored to a **small, explicitly named source packet** (typically 1–3 exact titles).  
   - NotebookLM is instructed to treat these titles as a hard filter and to fail fast if they are not present.

2. **Narrower batched extraction runs**  
   - Each run addresses **one analytical purpose only** (e.g. methodological capacity categories, framework indicator concepts, a specific gap-fill, or an ambiguity check).  
   - Do not ask for all capacity areas or all dimensions in a single broad run.

3. **Fail-fast source-fidelity behaviour**  
   - When named titles are missing or cannot be clearly restricted, NotebookLM must **report the mismatch and stop**, not substitute nearby literature.  
   - Any batch that substitutes sources without failing fast is **invalid as evidence** and must be discarded and rerun with corrected prompts or source packets.

4. **Open candidate extraction + fixed schema**  
   - Extraction remains **open** to whatever capacity categories and aspects the sources support.  
   - The **row schema is fixed** (Section 4.1 of [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md)); categories/aspects are candidate-only at extraction time.

5. **Exemplar capacity lists as coverage lenses only**  
   - Any list of exemplar capacity areas (governance, technical, financial, social, etc.) appears in prompts **only as a coverage lens**, not as a mandatory vocabulary.  
   - It is acceptable if some exemplar areas do not appear when the named sources do not support them.

6. **Dimension tagging discipline**  
   - `candidate_dimension_if_explicit` may take `asset`, `process`, or `output` **only when the source uses clear dimension language**.  
   - Otherwise it remains `not explicit`. No global dimension inference by NotebookLM.

7. **Targeted follow-up passes only after local review**  
   - Gap-fill or ambiguity passes (Pass 4+) are allowed **only after** local review of saved raw rows reveals specific gaps or ambiguities.  
   - Each such pass is narrow in scope and uses the same small-packet, fail-fast pattern.

8. **Taxonomy and synthesis remain local**  
   - NotebookLM never assigns final taxonomy labels or globally harmonises concepts.  
   - All harmonisation, de-duplication, dimension assignment, and dictionary structuring remain in local markdown and scripts, centred on [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md).

## 4. Execution packets and batching strategy

### 4.1 Source-packet concepts

For full execution, group NotebookLM sources into **small packets** by function:

- **Methodological packets (M"):** sources about adaptive capacity concepts, dimensions, and indicators for climate resilience and related measurement approaches.
- **Framework packets (F"):** sources describing urban resilience frameworks and indicator sets.
- **Adjacency packets (A"):** relevant adjacent literature that extends coverage for specific capacity areas (e.g. finance, data/knowledge, community participation).

Each packet should contain 1–3 exact titles, with names copied directly from the NotebookLM source list.

Example high-level batching table (to be concretised in project planning, not here):

| Batch ID | Packet type | Approx. size | Intended focus |
| --- | --- | --- | --- |
| M1 | Methodological | 2–3 sources | Core capacity category framings |
| M2 | Methodological | 2–3 sources | Additional capacity/aspect framings |
| F1 | Framework | 2–3 sources | Indicator concepts for governance/institutional readiness |
| F2 | Framework | 2–3 sources | Indicator concepts for infrastructure and services |
| A1 | Adjacency | 1–2 sources | Finance, business environment, and PPPs |
| A2 | Adjacency | 1–2 sources | Information/data/knowledge systems |

The exact packet definitions live in operational notes or task lists, not in this packet.

### 4.2 Mapping to prompt types

For each packet, choose the prompt pattern from [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md):

- **Methodological packets → Pass 2 prompt template** (capacity categories and aspects in methodological literature).  
- **Framework packets → Pass 3 prompt template** (framework indicator concepts).  
- **Adjacency or follow-up packets → Pass 4+ templates** (gap-fill or ambiguity/evidence-completion prompts).

All runs must prepend the **global extraction-only instruction block** from Section 2 of [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md), so fail-fast source fidelity and dimension discipline are active for every batch.

## 5. Manual NotebookLM actions per batch

For each defined source packet (M1, M2, F1, etc.):

1. **Prepare the prompt text**  
   - Start from the relevant template in [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md).  
   - Paste the global extraction-only instruction block at the top.  
   - Under the "Using only the uploaded literature…" paragraph, list the **exact NotebookLM source titles** for this packet.  
   - Ensure the prompt explicitly instructs NotebookLM to **fail fast** when any named title is missing (no substitution).

2. **Run the batch in NotebookLM**  
   - Open the CRI NotebookLM notebook.  
   - Confirm that all named sources for the packet are present with matching titles.  
   - Paste the prepared prompt.  
   - Inspect the response for any indication that sources were substituted or broadened beyond the named packet.

3. **Save the raw response verbatim**  
   - Save the full response exactly as returned into `responses/`, using a date- and packet-based naming convention, for example:  
     - `responses/2026-04-YY_batch_M1_methodological_notebooklm_raw.md`  
     - `responses/2026-04-YY_batch_F1_framework_notebooklm_raw.md`  
   - Do not edit or reformat before saving.

4. **Apply the source-fidelity gate**  
   - If NotebookLM reports missing titles and responds with substitute sources instead of failing fast, mark the batch as **invalid** for evidence use.  
   - In that case, adjust the prompt or packet definition and rerun the batch.  
   - Only batches that both respect the row schema and pass the source-fidelity check move forward.

## 6. Local handling and QC for full execution

For each **valid** batch (i.e. passes both shape and source-fidelity checks):

1. **Flatten and clean locally**  
   - Convert the NotebookLM output into one row per evidence statement or candidate concept.  
   - Standardise formatting only (field order, table alignment, JSON clean-up, line breaks).  
   - Preserve duplicates, competing labels, and source-near wording.  
   - Enforce `candidate_dimension_if_explicit` discipline: keep `not explicit` unless the source states asset/process/output.

2. **Integrate into the synthesis register**  
   - Extend [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md) with new rows and clusters.  
   - Maintain traceability via row IDs and references back to the batch and row indices (similar to the P1/P2/P3 convention used in the pilot).

3. **Apply QC gates from [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md)**  
   - Citation coverage: every row must have usable citations.  
   - Row structure consistency: flat, row-oriented, required fields populated or marked `not explicit`.  
   - Low drift into synthesis: NotebookLM did not attempt to harmonise or canonise.  
   - Manageable local harmonisation effort: integration workload remains proportionate.  
   - Boundary compliance: no reliance on repo-local files inside NotebookLM.

4. **Decide on follow-up passes (optional)**  
   - Only after reviewing the integrated rows in the register, decide whether targeted Pass 4+ runs are needed for:  
     - gap fill in specific capacity areas;  
     - ambiguity resolution;  
     - dimension evidence checks.  
   - Any such follow-up runs should reference the relevant batches and row IDs in their prompts and use the targeted templates from [`01_query_pack.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/01_query_pack.md).

## 7. Execution status and next steps

### 7.1 Batch integration status

| Batch ID | Status | Outcome | Reference |
| --- | --- | --- | --- |
| **M1** | ✅ Complete | Passed source-fidelity gate; 100% integrated into register. | `responses/2026-04-08_batch_M1_methodological_notebooklm_raw.md` |
| **F1** | ✅ Complete | Passed source-fidelity gate; 100% integrated into register. | `responses/2026-04-08_batch_F1_framework_notebooklm_raw.md` |
| **A1** | ✅ Complete | Passed source-fidelity gate; 100% integrated into register. | `responses/2026-04-08_batch_A1_adjacency_notebooklm_raw.md` |

### 7.2 Immediate next steps

The April 2026 M1, F1, and A1 batches have successfully validated the staged full-execution model. Methodological, framework, and adjacency core concepts are now integrated into [`synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md).

For the **current CRI Phase 2 capacity-tagging deliverables**, treat the integrated M1/F1/A1 batches as a **sufficient extraction set**. Additional batches (M2, F2, A2) remain **optional future gap-filling runs** that can be scheduled later if specific coverage gaps are identified during dictionary v2 drafting.

Immediate practical steps are:

1. **Review register for M2/F2/A2 requirements**
   - Assess whether the current coverage of methodological categories (M), frameworks (F), and adjacencies (A) is sufficient or requires the next planned batches.

2. **Refine Adjacency Packets (A")**
   - Identify specific data/knowledge system sources for Batch A2 if coverage gaps are found in the digital/innovation cluster.

This packet is the **source-of-truth operational guide** for running the next NotebookLM cycle under the post-pilot, extraction-only, staged full-execution model.
