# CRI Phase 1 Stage 3 — Subtask 9 Level 3 Spatial Outputs Report

Generated (UTC): 2026-04-21T02:54:26.141374+00:00

## Inputs
- WorldPop raster: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif`
- Tambon geometry enriched: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg`
- Tambon crosswalk: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv`
- Level 2 impact: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level2_impact_tambon_year_disaster.csv`
- Level 2 relief: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_fact_level2_relief_tambon_year_sector.csv`
- Bangkok policy: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md`

## Level 3 outputs
- Population raster (non-Bangkok, matched tambon mask): `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_level3_worldpop_2020_non_bangkok_matched_tambon.tif`
- Eligibility mask raster (1=eligible, 0=outside): `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_level3_tambon_eligibility_mask_non_bangkok.tif`
- Tambon key coverage CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask9_level3_tambon_key_coverage.csv`
- Validation JSON: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask9_level3_spatial_validation.json`

## Validation highlights
- Raster CRS: EPSG:4326
- Raster dimensions: 9953 x 17824
- Eligible tambon geometry rows: 7539
- Eligible mask pixels: 59117643
- Bangkok exclusion compliant: True
- Inherited Subtask 8 impact rows missing matched geometry: 2033
- Inherited Subtask 8 relief rows missing matched geometry: 5627
- Inherited Subtask 6 unallocated province-year-sector rows: 4973

## Scope guardrail
- This subtask publishes only shared Level 3 spatial outputs and module-level validation.
- Final end-to-end integrity checks are intentionally out of scope and preserved for later stage work.
