# CRI Phase 1 Stage 3 — Subtask 4 Provincial Denominator Report

Generated (UTC): 2026-04-21T01:47:58.289432+00:00

## Inputs
- Raster: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif`
- Province enriched geometry: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_province_geometry_enriched.gpkg`
- Province crosswalk: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/stage3_dopa_province_boundary_code_crosswalk.csv`
- Canonical spine: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/dim_location_master.csv`

## Output
- Denominator CSV: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv`

## Coverage & quality checks
- Total province features in geometry: 77
- Matched province features used for denominator: 77
- Denominator rows written: 77
- Bangkok rows in denominator (province_code=10): 1
- Null population rows: 0
- Zero population rows: 0
- Negative population rows: 0
- Zero valid-pixel rows: 0
- Raster read error rows: 0
- All province codes exist in dim_location_master: True

## Notes
- This module only produces Level 1 provincial denominator required for later Stage 3 risk computation.
- Shared Level 2 and Level 3 outputs are intentionally out of scope in Subtask 4.
- If raster_read_error_rows > 0, this run is policy-blocked and requires raster integrity remediation before downstream use.
- Detailed machine-readable validation is stored in `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/reports/stage3_subtask4_provincial_denominator_validation.json`.
