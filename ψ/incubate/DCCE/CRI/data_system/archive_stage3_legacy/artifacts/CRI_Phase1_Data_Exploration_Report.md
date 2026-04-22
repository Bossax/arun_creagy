# CRI Phase 1 Data Exploration Report

**Date**: 2026-04-17
**Context**: Stage 1 & 2 of CRI Phase 1 (Inventory and Cleaning)
**Source Data**: `ψ/incubate/DCCE/CRI/inbox_source/phase1-data/`

---

## 1. Summary of Available Datasets

### **BMA (Bangkok Metropolitan Administration)**
- **`bkk_hazard_impact_yearly.csv`**: A cleaned, district-level table for Bangkok (2560–2563). Includes deaths, affected people, and relief amounts.
- **`สถิติข้อมูล..._BMA.xlsx`**: The raw source containing multi-hazard statistics for the capital.

### **DDPM (Dept of Disaster Prevention & Mitigation)**
- **`master_financial_relief_by_hazard.csv`**: Provincial-level financial data (2546–Present). Tracks proposed, approved, and rejected relief funds categorized by hazard type.
- **`master_financial_relief_by_sector.csv`**: Similar to above, but categorized by impact sector (Agriculture, Housing, Infrastructure, etc.).
- **`master_village_disaster_stat_2557_2567.csv`**: **High-Signal Asset.** Granular village-level (`Moo`) impact data including physical damage counts (houses, businesses, livestock) and human impact.

### **TEI Pilot Processed Data**
- **`CRI_pilot_processed_data/`**: Benchmarking data (2559–2566 averages) for relief, casualties, and denominators (Population/GPP). This serves as the baseline for the new Phase 1 calculations.

### **Dimension & Reference Tables**
- **`dim_hazard_canonical.csv`** & **`dim_hazard_type.csv`**: Map source-specific terminology (e.g., `BKK_FLOOD`, `DDPM_DRY_SPELL`) to central hazard groups (Flood, Drought, etc.).
- **`dim_location.csv`**: Unified location keys across provinces, districts, and sub-districts.
- **`dim_sector.csv`**: Standardizes impact sectors (Agriculture, Fishery, Health, etc.).

---

## 2. Strategic Use Cases (What we can do)

### **A. Granular Dasymetric Mapping**
Using the `master_village_disaster_stat` (Village level) alongside the `dim_location` table, we can disaggregate provincial totals to specific sub-districts or grid cells. This directly solves the "Coarse Resolution" pain point of the pilot phase.

### **B. Fiscal Relief Gap Analysis**
By joining `master_financial_relief_by_sector` with the `master_village_disaster_stat`, we can quantify the delta between **Physical Damage** (e.g., number of houses destroyed) and **Approved Relief Funds**. This provides a more accurate "Fiscal Relief Intensity" metric.

### **C. Multi-Hazard Correlation**
The data structure allows us to see if specific provinces (e.g., industrial BKK vs. agricultural Central Plains) face recurring "Hazard Cascades" (e.g., Flood followed by Drought) and how fiscal relief responds to these shifts.

### **D. Robust Relational Model**
Primary keys (`location_id`, `hazard_type_id`) have been established. This enables a "Single Source of Truth" where BMA and DDPM data can be queried together for national-level analysis without duplicating records.

---

## 3. Gaps to Close

### **1. Temporal Normalization**
The datasets cover different time ranges (DDPM: 10 years, BKK: 4 years, Pilot: 8-year average). We need to decide on a **Target Window** (e.g., 2560–2566) to ensure the index is comparable across all regions.

### **2. Spatial "Blind Spot" Resolution**
`dim_location.csv` contains entries with "Missing district/subdistrict in source." These must be cross-referenced with official DOPA code lists to ensure the "Constrained Redistribution" logic doesn't drop impact data.

### **3. Monetary Consistency**
We must confirm if the `relief_amount` in the BKK data and the `วงเงินอนุมัติ` (Approved Amount) in the DDPM data follow the same accounting rules. Inflation adjustment for older relief amounts should also be considered.

### **4. Gap Flag Execution**
We have the raw data to implement the **Administrative Gap Flag**. We need to define the threshold: *At what level of physical damage (DDPM Stat) should we expect to see relief (DDPM Relief)?* If Damage > 0 but Relief = 0, the record must be flagged as "Insufficient Data" rather than "Low Risk."

---

## 4. Next Steps
1. **Clean Spatial Joins**: Standardize `dim_location` using DOPA canonical codes.
2. **Build Relational Views**: Join DDPM relief with village-level statistics to prepare the first "Fiscal Relief Intensity" prototypes.
3. **Register Artifacts**: Update the `CRI-Evidence-Registry.md` with the new BMA and DDPM source IDs.
