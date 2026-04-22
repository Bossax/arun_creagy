# CRI Phase 1 Stage 3 — Subtask 7 Level 1 Provincial Outputs Report

Generated (UTC): 2026-04-21T02:27:36.041836+00:00

## Inputs
- Denominator: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv`
- Tambon numerator (Subtask 5): `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_impact_tambon_numerator.csv`
- Redistributed relief (Subtask 6): `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv`
- Provincial relief source: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv`
- Canonical spine: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv`
- Bangkok policy note: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md`

## Output artifacts
- Level 1 impact CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level1_impact_province_year_disaster.csv`
- Level 1 relief CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level1_relief_province_year_sector.csv`
- Validation JSON: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask7_level1_provincial_validation.json`

## Implemented Level 1 logic
- Impact Level 1 is aggregated from `stage3_fact_impact_tambon_numerator` by (`year_be`, `province_code`, `province_name_th`, `disaster_type`).
- Relief Level 1 uses province-year-sector values from `master_financial_relief_by_sector` mapped to canonical province codes via observed `dim_location_master` province names.
- Subtask 6 redistributed relief is aggregated to province-year-sector and joined for explicit allocation-gap accounting.
- Bangkok is included at Level 1 through denominator and provincial relief source; lower-level redistributed Bangkok remains zero by policy.

## Validation highlights
- Denominator province coverage: 77 provinces.
- Impact Level 1 province coverage: 76 provinces.
- Relief Level 1 province coverage: 77 provinces.
- Bangkok rows in impact Level 1: 0.
- Bangkok rows in relief Level 1: 27.
- Relief source total equals Level 1 source total: True.
- Relief source total equals redistributed total: False.

## Unresolved blockers preserved
- Bangkok impact is absent from shared Level 2-derived impact input and is not fabricated.
- Subtask 6 unallocated redistribution gaps are retained as explicit residuals.
- Unmatched non-spatial relief rows remain excluded from province outputs.
