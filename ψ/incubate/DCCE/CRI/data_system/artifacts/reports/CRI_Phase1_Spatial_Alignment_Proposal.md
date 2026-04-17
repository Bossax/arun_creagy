# Proposal: CRI Phase 1 Spatial Alignment & Pipeline
**Date**: 2026-04-17
**Status**: Updated - Ready for Execution
**Objective**: Establish a canonical spatial spine using DOPA master codes (`CCAATT`) and the 2019 Village Code dataset to ensure auditability, village-level precision, and multi-source harmonization.

---

## 1. The Canonical Anchors: DOPA Master Datasets

We utilize two primary DOPA sources to build the spatial spine:

### **A. DOPA CCAATT Master (`ccaatt.xlsx`)**
Used for historical reference and top-level administrative consistency (Province to Subdistrict).
*   **Hierarchy**: Changwat (2), Amphoe (2), Tambon (2), Moo Baan (2).
*   **Role**: Provides the "Rulebook" for active vs. cancelled (*) administrative codes.

### **B. DOPA Village Code 2019 (`code_village_dopa_2019.xls`)**
Used as the high-resolution bridge for village-level data.
*   **Fields**: `VILL_CODE` (8-digit), `VILL_T` (Village Name), `TAM_CODE`, `AMP_CODE`, `PROV_CODE`.
*   **Role**: Maps the 8-digit village codes found in DDPM village statistics to official Thai names, enabling precise sub-district and district aggregation.

---

## 2. Analysis Pipeline: "Spine-to-Surface"

### **Stage 1: Dimension Table Construction (Standardization)**
We will parse both DOPA files into a unified **Canonical Location Master**.
*   **Transformation**: Normalize sequential codes into full 8-digit keys.
*   **Gap Resolution**: Use the 2019 Village dataset to fill "Missing district/subdistrict" attributes in the current `dim_location.csv` based on the DDPM village codes.

### **Stage 2: Data Binding & Cross-Verification**
*   **DDPM Village Stats**: Direct relational join on the 8-digit `VILL_CODE`.
*   **BMA (Bangkok)**: Name-to-Code mapping (e.g., "เขตคลองเตย" -> `1033`) using the `CCAATT` reference.
*   **Relief Verification**: Aggregate village-level counts to district/provincial totals to verify official fiscal relief extracts.

### **Stage 3: Constrained Redistribution (Spatial Disaggregation)**
1.  **Global Weights**: Use **WorldPop (100m)** and **ESA WorldCover** (Urban/Agri classes) as spatial masks.
2.  **Local Constraints**: The sum of all pixels within a DOPA administrative boundary (from Stage 1) must **exactly equal** the official administrative total for that specific boundary (Province or District).
3.  **Output**: A high-resolution raster (100m) where every pixel's value is traceable to a specific DOPA code and village context.

### **Stage 4: Gap Flag Protocol (Governance)**
By aligning to DOPA codes, we can cross-reference with hazard data:
*   **Rule**: If `Hazard (GISTDA) = TRUE` AND `Relief (DDPM) = 0` within a specific DOPA code boundary.
*   **Flag**: Mark as **"Administrative Data Gap"** (Pink Code). This ensures "Zero" values are not misinterpreted as "Low Risk" when hazard exposure is present.

---

## 3. Implementation Plan

| Task                 | Description                                                                    | Output                    |
| :------------------- | :----------------------------------------------------------------------------- | :------------------------ |
| **ETL: DOPA Master** | Parse `ccaatt.xlsx` and `code_village_dopa_2019.xls` into a unified hierarchy. | `dim_location_master.csv` |
| **ETL: Crosswalk**   | Map BMA and DDPM source names to the canonical master.                         | Unified Mapping Layer     |
| **ETL: Binding**     | Join raw impact/relief data to the canonical master IDs.                       | Analysis-ready tables     |
| **Verification**     | Cross-check village counts vs. official DOPA totals to ensure 100% coverage.   | Coverage Report           |

---

## 4. Expected Benefits
*   **Institutional Trust**: DCCE and Ministry of Interior can audit CRI numbers back to official village-level house registration.
*   **Precision**: Enables moving from "Coarse Province" views to "Precise Village" views, resolving the pilot phase resolution issues.
*   **Sustainability**: The relational structure allows future datasets (CRI Phase 2) to be easily integrated into the same spatial spine.

---
**Next Action**: I am ready to begin **Task 1: ETL DOPA Master** as soon as confirmed.
