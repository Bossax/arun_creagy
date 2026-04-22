# CRI Phase 1 Stage 3 — Subtask 6 Redistribution Report

Generated (UTC): 2026-04-21T02:16:44.502943+00:00

## Inputs
- Provincial relief (sector): `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv`
- Tambon numerator basis: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_impact_tambon_numerator.csv`
- Provincial denominator reference: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv`
- Canonical spine: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv`
- Bangkok policy: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md`

## Redistribution basis and method
- Basis candidates from observed Stage 3 tambon numerator fields: `affected_households`, `affected_people`, `village_event_row_count`.
- Province-year basis selection priority: `affected_households` -> `affected_people` -> `village_event_row_count` -> unresolved (`none`).
- Relief sectors are redistributed from provincial totals to tambon rows by province-year allocation shares from the selected basis metric.
- Shared lower-level Bangkok exclusion is enforced (`province_code=10` removed before redistribution).

## Coverage and policy checks
- Matched relief rows: 1848
- Unmatched province rows: 24
- Positive relief province-year-sector rows: 7222
- Allocated province-year-sector rows: 2249
- Unallocated province-year-sector rows: 4973
- Bangkok relief rows excluded from shared redistribution: 24
- Bangkok rows in redistributed output: 0

## Reconciliation and quality
- Reconciliation groups: 2249
- Non-reconciled groups: 0
- Max absolute source-vs-redistributed difference: 2.9802322387695312e-08
- Negative redistributed amount rows: 0

## Outputs
- Redistributed relief CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv`
- Reconciliation CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask6_relief_redistribution_reconciliation.csv`
- Unmatched province CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask6_relief_redistribution_unmatched_province.csv`
- Unallocated province-year-sector CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask6_relief_redistribution_unallocated_province_year.csv`
- Validation JSON: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask6_relief_redistribution_validation.json`

## Scope guardrail
- This module implements only Stage 3 Subtask 6 redistribution outputs and validation evidence.
- Final Level 1/Level 2 products, visualization, and end-to-end integrity checks remain out of scope.
