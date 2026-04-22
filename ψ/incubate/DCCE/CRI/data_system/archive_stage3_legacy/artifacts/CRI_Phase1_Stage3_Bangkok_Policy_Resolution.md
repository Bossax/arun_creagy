# CRI Phase 1 Stage 3 Bangkok Policy Resolution

**Status**: Resolved policy note for shared Stage 3 implementation  
**Scope**: Subtask 3 only. This note resolves Bangkok handling for downstream Stage 3 code-mode work without implementing denominator, numerator, redistribution, or visualization modules.

---

## 1. Audited evidence base

This resolution is grounded in direct inspection of the following artifacts:

- [`CRI_Phase1_Stage3_Detailed_Implementation_Plan.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Detailed_Implementation_Plan.md)
- [`CRI_Phase1_Stage3_Subtask2_Crosswalk_Report.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Subtask2_Crosswalk_Report.md)
- [`stage3_subtask2_blockers.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_blockers.md)
- [`CRI_Phase1_Stage3_Input_Baseline_Audit.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Input_Baseline_Audit.md)
- [`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md)
- [`data-sources.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-sources.md)
- [`build_fact_impact.py`](ψ/incubate/DCCE/CRI/data_system/script/build_fact_impact.py)
- [`build_fact_relief.py`](ψ/incubate/DCCE/CRI/data_system/script/build_fact_relief.py)
- [`bkk_hazard_impact_yearly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/bma/bkk_hazard_impact_yearly.csv)
- [`dim_location.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location.csv)
- [`dim_location_master.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv)
- [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv)
- [`master_financial_relief_by_sector.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv)
- [`stage3_dopa_province_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_province_boundary_code_crosswalk.csv)
- [`stage3_dopa_tambon_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv)
- [`stage3_subtask2_tambon_boundary_mismatch.csv`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv)

---

## 2. Verified Bangkok-relevant observations

### 2.1 BMA impact stream is Bangkok-only, but location anchoring is legacy and non-canonical

- [`data-sources.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-sources.md) describes the BMA source as multi-hazard disaster statistics for Bangkok districts.
- [`bkk_hazard_impact_yearly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/bma/bkk_hazard_impact_yearly.csv:1) contains only these fields for location handling: `location_id`, `report_year_be`, `hazard_type_id`, `deaths_count`, `affected_people_count`, and `relief_amount_baht`.
- The observed BMA `location_id` values are hashed legacy identifiers such as `LOC_2705485c21` and `LOC_fd19886c47` in [`bkk_hazard_impact_yearly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/bma/bkk_hazard_impact_yearly.csv:2).

### 2.2 The current legacy remapping path is not verified against the observed BMA IDs

- [`build_fact_impact.py`](ψ/incubate/DCCE/CRI/data_system/script/build_fact_impact.py:23) still attempts a two-step BMA remap through legacy [`dim_location.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location.csv) and then the canonical spine.
- The directly observed legacy location IDs in [`dim_location.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location.csv:2) are `LOC0001`, `LOC0002`, `LOC0003`, and similar sequential identifiers rather than the hashed `LOC_*` values observed in [`bkk_hazard_impact_yearly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/bma/bkk_hazard_impact_yearly.csv:2).
- Because the observed BMA silver IDs and the observed legacy lookup IDs are not the same format, the current BMA remapping path in [`build_fact_impact.py`](ψ/incubate/DCCE/CRI/data_system/script/build_fact_impact.py:25) is not a verified basis for shared Stage 3 joins.

### 2.3 Canonical DOPA assets support Bangkok at province level and mostly at tambon level

- [`stage3_dopa_province_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_province_boundary_code_crosswalk.csv:3) shows Bangkok province matched deterministically to `province_code=10`.
- [`dim_location_master.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv:62599) directly shows Bangkok canonical rows at `admin_level=subdistrict` with DOPA-style codes such as `100101`, `100102`, and `100103`.
- [`stage3_dopa_tambon_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv:34) shows many Bangkok tambon matches, confirming that most Bangkok polygons can already be anchored to canonical subdistrict codes.

### 2.4 A row-level Bangkok tambon inconsistency remains in Subtask 2 artifacts

- [`CRI_Phase1_Stage3_Subtask2_Crosswalk_Report.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Subtask2_Crosswalk_Report.md:56) and [`stage3_subtask2_blockers.md`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_blockers.md:6) state that no Bangkok-specific unresolved joins were detected.
- However, the row-level mismatch log shows at least two Bangkok unmatched tambon rows:
  - `กรุงเทพมหานคร, บางนา, บางนา` in [`stage3_subtask2_tambon_boundary_mismatch.csv`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv:301)
  - `กรุงเทพมหานคร, บางบอน, บางบอน` in [`stage3_subtask2_tambon_boundary_mismatch.csv`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv:322)
- For downstream coding, the row-level crosswalk and mismatch artifacts must take precedence over the narrative sentence in the report.

### 2.5 DDPM representation of Bangkok is provincial for relief, but not verified in village-impact silver

- Bangkok name normalization rules already exist in [`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:64), where `กรุงเทพ`, `กทม.`, and `กรุงเทพฯ` are normalized to `กรุงเทพมหานคร`.
- Bangkok provincial relief rows are directly visible in [`master_financial_relief_by_sector.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv) as `กรุงเทพฯ` and in [`master_financial_relief_by_sector.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv) as `กรุงเทพฯ`.
- [`build_fact_relief.py`](ψ/incubate/DCCE/CRI/data_system/script/build_fact_relief.py:38) generates province-anchor IDs by appending `000000` to a 2-digit province code, which would yield `10000000` for Bangkok after normalization.
- No Bangkok rows were found during audit search of [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv), so Bangkok village-level DDPM impact coverage is not verified for the shared Stage 3 pipeline. %% this is untrue. You can find `กรุงเทพมหานคร` in many rows, for example rows 67840-67845 %%

---

## 3. Policy decision

Bangkok shall be handled as a **province-only inclusion with lower-level exclusion in the first shared Stage 3 implementation**.

This means:

1. **Level 1 is in scope for Bangkok** through a controlled province-level branch.
2. **Level 2 is out of scope for Bangkok in the shared pipeline** until a separate, approved Bangkok lower-level allocation method exists.
3. **Level 3 is out of scope for Bangkok in the shared pipeline** until a separate, approved Bangkok spatial allocation method exists.

This is a recommended policy and does **not** require immediate human approval for the first modular Stage 3 pass. Human approval becomes necessary only if the project decides to include Bangkok at Level 2 or Level 3 before a new audited allocation method is created.

---

## 4. Level-specific rules for code-mode subagents

### 4.1 Level 1: Provincial handling

**Policy**: Include Bangkok in Level 1 outputs.

**Allowed joins and transforms**

- Bangkok relief may enter Level 1 after province-name normalization under the rules already documented in [`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:64).
- Bangkok province geometry may use [`stage3_dopa_province_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_province_boundary_code_crosswalk.csv:3) as the canonical spatial anchor for `province_code=10`.
- Bangkok BMA impacts may be aggregated to Bangkok province total **only because the BMA source is explicitly Bangkok-only** in [`data-sources.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-sources.md:10).

**Prohibited assumptions**

- Do **not** join BMA hashed `location_id` values directly to [`dim_location_master.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv).
- Do **not** treat the current BMA `location_id` values as canonical district, tambon, or village identifiers.
- Do **not** infer a lower-level Bangkok code from the BMA silver file unless a new audited lookup table is created first.

**Fallback behavior**

- If BMA lower-level mapping is still unresolved, collapse BMA records to a single Bangkok province contribution before union with other Level 1 sources.
- If a downstream Level 1 module does not consume BMA impacts, Bangkok may still remain in Level 1 for provincial relief and province geometry outputs.

**Validation requirements**

- Assert that every Bangkok Level 1 output row uses only the province anchor for Bangkok and never a hashed `LOC_*` key.
- Emit a validation note stating whether Bangkok Level 1 used relief only, BMA impact only, or both.

### 4.2 Level 2: Tambon handling

**Policy**: Exclude Bangkok from the shared Level 2 pipeline in the first modular implementation.

**Allowed joins and transforms**

- Shared Level 2 code may use only canonical DOPA-anchored village-to-tambon inputs and the verified tambon geometry crosswalk in [`stage3_dopa_tambon_boundary_code_crosswalk.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv:34).
- Bangkok rows may be included in a future dedicated Bangkok branch only after a new audited lookup connects BMA observations to lower-level DOPA anchors.

**Prohibited assumptions**

- Do **not** disaggregate Bangkok BMA district observations to tambon by equal split, area share, population share, or nearest-name guess.
- Do **not** redistribute Bangkok provincial relief inside the shared tambon engine.
- Do **not** force unmatched Bangkok tambon rows into the canonical spine. The observed unmatched rows for `บางนา` and `บางบอน` must remain unresolved until the spine or crosswalk is corrected.

**Fallback behavior**

- Shared Level 2 modules must drop Bangkok from published tambon outputs and record the exclusion explicitly in their validation artifact.
- If Bangkok-specific Level 2 output is requested before a new branch exists, the module must fail closed with a documented dependency error rather than fabricate a join.

**Validation requirements**

- Fail validation if any Bangkok record enters shared Level 2 output through a hashed `LOC_*` key.
- Fail validation if any Bangkok tambon output is published without `match_status=matched` in the crosswalk layer.
- Report the unresolved Bangkok mismatch rows from [`stage3_subtask2_tambon_boundary_mismatch.csv`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv:301) and [`stage3_subtask2_tambon_boundary_mismatch.csv`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv:322) whenever Bangkok lower-level eligibility is evaluated.

### 4.3 Level 3: Spatially explicit handling

**Policy**: Exclude Bangkok from the shared Level 3 pipeline in the first modular implementation.

**Allowed joins and transforms**

- Shared Level 3 code may use only sources that already have audited spatial anchors suitable for raster allocation.
- Bangkok may enter a future dedicated branch only after the project approves an audited district-to-subdistrict or district-to-raster allocation design.

**Prohibited assumptions**

- Do **not** rasterize Bangkok BMA records by spreading district totals across province area, tambon area, or population surface without an approved model.
- Do **not** redistribute Bangkok provincial relief to raster cells inside the shared engine.
- Do **not** backfill Bangkok raster exposure from unmatched tambon polygons.

**Fallback behavior**

- Shared Level 3 outputs must exclude Bangkok and document that exclusion as policy-driven rather than as missing data noise.
- If a national raster is produced, Bangkok cells must either be omitted from the modeled layer or explicitly marked as not computed under the first-pass contract.

**Validation requirements**

- Fail validation if Bangkok values appear in Level 3 outputs without a documented audited allocation method.
- Require a published exclusion note whenever Bangkok is absent from national raster outputs.

---

## 5. Downstream implementation contract

Code-mode subagents shall follow these exact implementation rules:

1. **No legacy hashed keys in shared Stage 3 modules**
   - Any shared module that receives Bangkok rows with `LOC_*` identifiers must stop before join or redistribution logic.

2. **Province branch only for first-pass Bangkok inclusion**
   - Bangkok may be present only in the Level 1 provincial branch of the shared implementation.

3. **No Bangkok redistribution in shared engines**
   - Provincial-to-lower-level redistribution logic must treat Bangkok as out of scope until a dedicated Bangkok branch is approved.

4. **Row-level crosswalk evidence overrides narrative summaries**
   - When report prose conflicts with row-level crosswalk outputs, subagents must trust the row-level artifacts with explicit `match_status`.

5. **Fail closed, not open**
   - If a future module cannot prove a canonical Bangkok lower-level anchor, it must exclude Bangkok from that level and emit a validation message rather than guess.

---

## 6. Human approval boundary

No additional human approval is required to proceed with the recommended first-pass shared policy above.

Human approval is required only if the project decides to do any of the following before a new audit is completed:

- include Bangkok in shared Level 2 outputs
- include Bangkok in shared Level 3 outputs
- introduce a district-to-tambon redistribution method for BMA observations
- introduce a tambon-to-raster or district-to-raster redistribution method for Bangkok
- override the observed unmatched Bangkok tambon rows without a corrected canonical source

---

## 7. Ready-state conclusion

Subtask 3 is considered resolved when downstream code-mode work treats Bangkok as:

- **included at Level 1 only**
- **excluded from shared Level 2 and Level 3 modules**
- **blocked from any lower-level redistribution until a separate audited Bangkok branch is created**

