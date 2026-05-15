# Data Lineage: CRI Phase 1 Impact System

This document provides a human-readable map of the transformation logic used to build the CRI Phase 1 analytical tables, bridging the gap between raw Bronze files and the Gold analytical layer.

---

## 1. DDPM Village Stream
*   **Raw Source**: `0_bronze/ddpm/*.csv` (11 yearly files: 2557–2567).
*   **Processing Script**: `consolidate_village_stats_ddpm.ipynb`
    *   **Logic**:
        *   **Dynamic Parsing**: Years 2565–2567 use dual headers (EN/TH); script skips the Thai header row.
        *   **Standardization**: Village codes are zero-padded to 8 digits.
        *   **Consolidation**: Merges ~210,000 village-level observations into a single master silver file.

## 2. DDPM Financial Stream
*   **Raw Source**: `0_bronze/ddpm/สถิติข้อมูลการใช้จ่ายเงินทดรองราชการ ปี 2546 - ปัจจุบัน.xlsx`
*   **Processing Script**: `clean_financial_relief_data_ddpm.ipynb`
    *   **Logic**:
        *   **Multi-Sheet Extraction**: Iteratively slices sheets (Indices 4–18 for Hazards, 28–42 for Sectors).
        *   **Layout Adaptation**: Handles structural changes between older and newer sheet formats.
        *   **Aggregation**: Consolidates 1,872 provincial records for both Hazard and Sector-based relief.

## 3. DOPA Spatial Spine
- **URL**: https://drive.google.com/drive/folders/1zi3Z0l7wvsGN1p5YIWVVL3LFs3WnS7VQ
*   **Raw Source**: `0_bronze/dopa/thailanda-administrative-boundary/*.shp`
*   **Processing Script**: `prep_dopa_boundaries.py`
    *   **Logic**:
        *   **Geometry Normalization**: Ensures CRS is set to WGS84 (EPSG:4326).
        *   **Enrichment**: Attaches canonical 6-digit `subdistrict_code` and 2-digit `province_code` from the dim_location_master.
    *   **Outputs**: 
        *   `1_silver/dopa/tambon_boundaries_enriched.shp`
        *   `1_silver/dopa/province_boundaries_enriched.shp`

## 4. WorldPop Zonal Statistics
*   **Raw Source**: `0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif`
*   **Processing Script**: `prep_worldpop_exposure.py`
    *   **Logic**:
        *   **Zonal Aggregation**: Overlays enriched Tambon geometries on the 100m population raster.
        *   **Calculation**: Sums pixel values to derive total registration-independent population count per Tambon.
    *   **Outputs**: 
        *   `1_silver/worldpop/tambon_population_count_worldpop.csv`
        *   `1_silver/worldpop/tambon_population_count_worldpop.tif` (rasterized version)

## 5. TEI Pilot Baseline
*   **Raw Source**: `0_bronze/tei_pilot/casualties_by_hazard_2559_2566.csv`
*   **Processing Script**: `prep_tei_casualties.py`
    *   **Logic**:
        *   **Code Mapping**: Resolves legacy provincial names to canonical DOPA 2-digit codes.
        *   **Cleaning**: Handles encoding issues and whitespace normalization in casualty figures.
    *   **Output**: `1_silver/tei_pilot/provincial_casualties_clean.csv`

## 6. DDPM Intermediate Aggregation
*   **Raw Source**: `1_silver/ddpm/master_village_disaster_stat_2557_2567.csv`
*   **Processing Script**: `prep_ddpm_climate_history.py`
    *   **Logic**:
        *   **Hazard Filtering**: Uses `dim_hazard_canonical.csv` to filter strictly for climate-related events.
        *   **Spatial Roll-up**: Aggregates village-level `Affected Households` to the 6-digit Tambon level.
    *   **Output**: `1_silver/ddpm/tambon_climate_affected_household_aggregate_ddpm_village_stat.csv`

---

## 7. Integrity Standards (Metadata Layer)

*   **Gold Spine Integrity**: All Gold tables must pass a Foreign Key (FK) check against `dim_location_master.csv`. Unmatched records are discarded to prevent spatial noise.
*   **Hazard Canonicalization**: Mappings between raw disaster strings and canonical IDs are documented in `data_dictionary.xlsx` (Sheet: `bridge_hazard_canonical`) when available; the current in-repo canonical lookup table is `data/2_gold/dim_hazard_canonical.csv`.

## 8. Standardization & Exclusion Rules

To ensure spatial consistency across the CRI, the following rules are applied during the transformation from Silver to Gold:

### 8.1 Name Normalization
The following variants are normalized to "กรุงเทพมหานคร" (Province Code 10):
*   `กรุงเทพ` (From TEI Pilot)
*   `กทม.` (From DDPM Silver)
*   `กรุงเทพฯ` (From DDPM Silver)

### 8.2 Administrative Exclusions
*   **Non-Spatial Agencies**: Records associated with `หน่วยงานในสังกัด` (Affiliated Agencies) are **excluded** from the CRI pipeline.
*   **Reason**: These represent line-agency expenditures that cannot be spatially attributed to a specific province or village, and would introduce noise into the spatial risk index.
*   **Reference**: These rules are maintained in `metadata/standardization_mapping.csv`.
