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
        *   **Forensic Alignment**: Applies 11 targeted nomenclature patches to resolve legacy attribute errors in the Bronze GIS file (e.g., renames, district shifts).
        *   **Enrichment**: Attaches canonical 6-digit `subdistrict_code` and 2-digit `province_code` from the **Gold** `dim_location_master`.
    *   **Outputs**: 
        *   `1_silver/dopa/tambon_boundaries_enriched.shp`
        *   `1_silver/dopa/province_boundaries_enriched.shp`

---

## 4. Location Master (Gold Spine)
- **URL**: https://stat.bora.dopa.go.th/stat/statnew/statMenu/newStat/ccaa.php
*   **Raw Source**: `0_bronze/dopa/ccaatt.xlsx` (Master Hierarchy) + `0_bronze/dopa/code_village_dopa_2019.xls` (Village Names).
*   **Processing Script**: `etl_dopa_master.py`
    *   **Logic**:
        *   **Hierarchical Schema Validation**: Uses `ccaatt.xlsx` as the absolute sovereign schema for codes and names. Records with invalid parent codes are discarded.
        *   **Nomenclature Inheritance**: Parent names (Province/District/Subdistrict) are inherited strictly from the CCAATT master, overwriting all variants in the `code_village_dopa_2019.xls` list.
        *   **Hardening Tweaks**: 
            *   **Restoration of Official Names**: Corrects shortened names like "เมือง" back to the canonical "เมืองนครราชสีมา".
            *   **Spelling Consistency**: Enforces the official spelling from the CCAATT master (e.g., "เทพารักษ์" with 'ก').
            *   **Noise Reduction**: Purges 176 invalid village records caused by sliding rows or typos in the source list.
    *   **Output**: `2_gold/dopa/dim_location_master.csv` (The National Administrative Spine).

---

## 5. WorldPop Zonal Statistics
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

## 8. Integrity Standards (Metadata Layer)

*   **Location Spine Integrity**: All enriched Silver and Gold spatial tables are joined against the **Gold** `dim_location_master.csv`. This spine achieved 100% referential integrity with the CCAATT master hierarchy. Systematic nomenclature errors in the `code_village_dopa_2019.xls` source (e.g., Korat's capital being shortened to "Mueang") were resolved via hierarchical inheritance.
*   **Hazard Canonicalization**: Mappings between raw disaster strings and canonical IDs are documented in `data/2_gold/dim_hazard_canonical.csv`.

---

## 9. Forensic Patch Registry (GIS Alignment)

The following 11 targeted patches were applied in `prep_dopa_boundaries.py` to bridge the gap between legacy GIS attributes (Bronze) and the modern Gold Spine:

| Province | GIS District | GIS Subdistrict | Resolution (Target DOPA Name/District) | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **อุตรดิตถ์** | ท่าปลา | ท่าแฝก | **น้ำปาด**, ท่าแฝก (530407) | Subdistrict moved district in 2015. |
| **อุบลราชธานี** | สิรินธร | นิคมลำโดมน้อย | **นิคมสร้างตนเองลำโดมน้อย** (342905) | Full name required for Gold match. |
| **เชียงใหม่** | แม่วาง | ทุ่งปี้ | **ทุ่งปี๊** (502202) | Tone mark mismatch (๊ vs ี้). |
| **ชัยภูมิ** | เกษตรสมบูรณ์ | ซับสีทอง | **เมืองชัยภูมิ**, ซับสีทอง (360119) | District shift since GIS capture. |
| **หนองคาย** | เมืองหนองคาย | สองห้อง | **โพนสว่าง** (430111) | Renamed to avoid local duplication. |
| **เชียงใหม่** | อมก๋อย | สบโขง | **แม่หลอง** (501805) | Renamed to align with local geography. |
| **บึงกาฬ** | เมืองบึงกาฬ | หนองเข็ง | **โนนสว่าง** (380103) | Renamed to avoid local duplication. |
| **นครสวรรค์** | เมืองนครสวรรค์ | วัดไทร | **วัดไทรย์** (600113) | Gold Spine uses official spelling. |
| **แพร่** | เมืองแพร่ | วังหงษ์ | **วังหงส์** (540113) | Gold Spine uses official spelling. |
| **มหาสารคาม** | ยางสีสุราช | ขามเรียน | **สร้างแซ่ง** (441106) | Renamed in modern DOPA hierarchy. |
| **อุบลราชธานี** | วารินชำราบ | ห้วยขะยูง | **ห้วยขะยุง** (341524) | Corrected official spelling (ย vs ยู). |

---

## 10. Standardization & Exclusion Rules

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
 from the CRI pipeline.
*   **Reason**: These represent line-agency expenditures that cannot be spatially attributed to a specific province or village, and would introduce noise into the spatial risk index.
*   **Reference**: These rules are maintained in `metadata/standardization_mapping.csv`.
