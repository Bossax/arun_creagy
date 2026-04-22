# CRI Phase 1 Stage 3 — Subtask 8 Level 2 Tambon Outputs Report

Generated (UTC): 2026-04-21T02:36:53.663329+00:00

## Inputs
- Impact tambon numerator: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_impact_tambon_numerator.csv`
- Relief tambon redistributed: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv`
- Tambon geometry enriched: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg`
- Tambon boundary crosswalk: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv`
- Bangkok policy note: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md`

## Output artifacts
- Level 2 impact CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level2_impact_tambon_year_disaster.csv`
- Level 2 relief CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level2_relief_tambon_year_sector.csv`
- Impact geometry join-failure CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask8_level2_impact_geometry_join_failure.csv`
- Relief geometry join-failure CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask8_level2_relief_geometry_join_failure.csv`
- Validation JSON: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask8_level2_tambon_validation.json`

## Implemented Level 2 logic
- Impact Level 2 persists tambon-year-disaster facts from Subtask 5 with explicit geometry eligibility status against crosswalk `match_status=matched` keys.
- Relief Level 2 aggregates Subtask 6 redistributed tambon rows to tambon-year-sector totals with explicit geometry eligibility status.
- Shared Bangkok exclusion (`province_code=10`) is enforced for both outputs.

## Validation highlights
- Impact rows with matched geometry: 39100
- Impact rows missing matched geometry: 2033
- Relief rows with matched geometry: 105862
- Relief rows missing matched geometry: 5627
- Bangkok rows in Level 2 impact output: 0
- Bangkok rows in Level 2 relief output: 0
- Relief total reconciliation to Subtask 6 redistributed source: True

## Unresolved blockers preserved
- level2_geometry_join_incomplete: Some published Level 2 tambon keys are not present in matched tambon geometry crosswalk and remain in explicit join-failure artifacts.
- bangkok_tambon_crosswalk_mismatch_persist: Bangkok tambon mismatch rows from Subtask 2 remain unresolved and are preserved as policy evidence for lower-level exclusion.
