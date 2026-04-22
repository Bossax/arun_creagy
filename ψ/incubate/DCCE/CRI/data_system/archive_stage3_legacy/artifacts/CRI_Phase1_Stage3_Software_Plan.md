# Analysis Software Plan: CRI Phase 1 (Stage 3)
**Status**: Strategic Pivot - Modular Design
**Objective**: To implement a robust, decoupled pipeline for spatial disaggregation, ensuring that data acquisition, processing, and visualization can fail or be updated independently.

---

## 1. Pipeline Architecture (Medallion Pattern)

We are moving away from a monolithic script to a modular sequence:

### **Module 1: Ingestion (`0_bronze`)**
*   **Purpose**: Programmatic acquisition of external APIs and files.
*   **Key Inputs**: WorldPop REST API, GitHub GeoJSON.
*   **Fail Conditions**:
    *   API 404/500 errors (Endpoint drift).
    *   Large file timeout (100MB+ rasters).
    *   SSL/Certificate errors in restricted environments.
*   **Safeguard**: Implement local file-caching (check for existence before download).

>[!status]
>Done. The file is available at `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/worldpop/tha_ppp_2020.tif`.
>
### **Module 2: Spatial Pre-processing (`1_silver`)**
*   **Purpose**: Build a reliable administrative-code join layer on top of DOPA province and tambon boundaries.
*   **Key Tasks**:
    *   Use boundary sources: `THA_Province.shp` and `THA_Tambon.shp` from DOPA.
    *   Join DOPA administrative codes into shapefile attributes (province, amphoe, tambon) using Thai/English name matching and controlled standardization.
    *   Validate one-to-one/one-to-many joins and produce a mismatch log for unresolved names.
*   **Fail Conditions**:
    *   Name ambiguity across Thai/English variants leading to duplicate or null code assignment.
    *   Missing expected columns in shapefile attributes (province/amphoe/tambon names).
    *   Encoding inconsistencies in Thai script causing failed joins.
*   **Safeguard**: Enforce pre-join schema checks, maintain a transparent standardization dictionary, and block downstream execution until unmatched records are resolved or explicitly waived.

### **Module 3: Risk Calculation (`2_gold`)**
*   **Purpose**: Pure mathematical computation of risk ratios.
*   **Key Tasks**: Zonal statistics (Raster + Vector overlay), aggregation of DDPM numerators.
*   **Fail Conditions**:
    *   Memory exhaustion (Processing 77 provinces x millions of pixels).
    *   Division by zero (Valid boundaries with 0 population).
    *   Logical disconnect between DDPM years and WorldPop vintage.
*   **Safeguard**: Output pure CSV as the primary audit trail.

### **Module 4: Multi-Level Visualization**
*   **Purpose**: Synthesis of results into the three requested granularity levels. using percentile instead of absolute data to map to the colorbar
*   **Fail Conditions**:
    *   Missing plotting libraries (`matplotlib`, `geopandas` dependencies).
    *   Scaling artifacts (Level 3 heatmaps appearing uniform).
    *   Lack of Thai fonts for labels.
*   **Safeguard**: Use robust HTML-based charts for wide baseline; static PNGs for high-res rasters.


---

## 2. Granularity Definitions

Every module must support these three levels:

1.  **Level 1 (Provincial)**: 
    *   *Metric*: Risk per 10k Residents.
    *   *Output*: CSV Report + Choropleth Map.
2.  **Level 2 (Sub-district, Tambon)**:
    *   *Metric*: Village-aggregated household impact per Tambon.
    *   *Output*: Map Only (High-precision administrative view).
3.  **Level 3 (Spatially Explicit)**:
    *   *Metric*: 100m Raster Risk Surface.
    *   *Output*: Raster Map (Physical exposure view).

---

## 3. Data Integrity Rules

*   **Principle of Persistence**: Bronze files must never be modified once downloaded.
*   **The Gold Spine Rule**: All joins must be anchored to the DOPA `dim_location_master.csv`. Any record not in the spine is flagged and logged.
*   **No Monoliths**: Each module must be an independent script that can be run in isolation if its preceding input folder is populated.
