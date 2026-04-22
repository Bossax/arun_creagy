# CRI Phase 1 Stage 3 — Subtask 5 Tambon Numerator Report

Generated (UTC): 2026-04-21T02:01:28.375105+00:00

## Inputs
- DDPM village impact: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv`
- Canonical spine: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv`
- Bangkok policy note: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md`
- Subtask 2 tambon mismatch log: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv`

## Canonical key strategy
- Observed join key for tambon assignment: DDPM `Village Code` (normalized to 8 digits) -> canonical `village_code` in dim_location_master.
- Canonical tambon output keys: `province_code` (2), `district_code` (4), `subdistrict_code` (6).

## Coverage summary
- Total DDPM rows: 209935
- Matched rows (all provinces): 168685
- Matched rows used in shared output (non-Bangkok): 168685
- Unmatched village-code rows: 41250
- Null village-code rows: 0
- Match rate: 0.803511

## Bangkok policy checks
- Matched Bangkok rows excluded from shared tambon output: 0
- Bangkok rows present in tambon output: 0
- Bangkok policy compliance (shared Level 2 exclusion): True
- Bangkok mismatch rows noted from Subtask 2 log: 2

## Reconciliation checks (non-Bangkok matched source vs tambon output)
- affected_people: source=1312523.000000, output=1312523.000000, diff=0.000000, reconciled=True
- affected_households: source=2366545.000000, output=2366545.000000, diff=0.000000, reconciled=True
- deaths: source=925.000000, output=925.000000, diff=0.000000, reconciled=True
- housing_damage: source=830145.000000, output=830145.000000, diff=0.000000, reconciled=True
- business_damage: source=35856.000000, output=35856.000000, diff=0.000000, reconciled=True
- agriculture_damage: source=3510297.050000, output=3510297.050000, diff=0.000000, reconciled=True
- livestock_damage: source=256238.000000, output=256238.000000, diff=0.000000, reconciled=True
- fishing_damage: source=21619.700000, output=21619.700000, diff=0.000000, reconciled=True
- transport_damage: source=17394.000000, output=17394.000000, diff=0.000000, reconciled=True
- health_damage: source=47.000000, output=47.000000, diff=0.000000, reconciled=True
- utilities_damage: source=3178.000000, output=3178.000000, diff=0.000000, reconciled=True

## Outputs
- Tambon numerator CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_impact_tambon_numerator.csv`
- Unmatched village-code CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask5_tambon_numerator_unmatched_village_code.csv`
- Null village-code CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask5_tambon_numerator_null_village_code.csv`
- Validation JSON: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask5_tambon_numerator_validation.json`

## Scope guardrail
- This module implements only Subtask 5 tambon numerator aggregation and validation artifacts.
- Redistribution, provincial risk computation, tambon rendering, and spatial outputs remain out of scope.
