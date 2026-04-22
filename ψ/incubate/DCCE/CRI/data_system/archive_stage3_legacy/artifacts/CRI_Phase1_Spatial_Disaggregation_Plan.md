# CRI Phase 1 (Stage 3): Spatial Disaggregation & Asset-Based Mapping Plan

**Objective:** To define the datasets, decision points, and analytical pipelines required to downscale provincial and district-level disaster data (from the DDPM Silver layer) to high-resolution village boundaries (8-digit DOPA codes) using WorldPop and ESA spatial proxies.  

---

## 1. Strategic Decision Points

Based on the Phase 1 audit of the TEI Pilot and the DDPM Silver datasets, the following critical decisions frame the spatial disaggregation approach:

1. **Discard Legacy Gold Layer:** The previous `fact_impact` and `fact_relief` tables (and their generation scripts) are deprecated. They relied on ad-hoc chatbot-generated IDs for BMA and did not solve the core spatial scale mismatch. We will build directly from the "Analytical Ready" **DDPM Silver Transactional** tables.
2. **Prioritize Dense Administrative Indicators:** Based on the DDPM village-level statistics, `Affected Households` (141k+ records) and `Housing Damage` (123k+ records) are the only indicators with sufficient data density. Other indicators (like `Affected People`, `Deaths`, and minor sectors) are dominated by zeros.
3. **Drop Sparse Sectoral Quantities:** We will firmly **drop** specific but severely under-reported physical indicators (e.g., exact counts of damaged livestock, specific business damages) because using them would create false precision.
4. **The "Meta-Sector" Relief Grouping:** DDPM financial relief sectors (e.g., `ด้านการดำรงชีพ`, `ด้านเกษตร_ประมง`) are based on Ministry of Finance emergency eligibility categories, not strict economic sectors. We will group them into **Meta-Sectors** to reliably disaggregate the funds based on physical proxies.
5. **Denominator Correction:** We will correct the TEI Pilot's flaw of dividing Agricultural Relief by Total Provincial GPP. We will use spatial masking (isolating rural/agricultural zones) to create accurate exposure denominators.

---

## 2. Approved Datasets for the Pipeline

### A. Administrative Baseline (The "Numerators")
*   **DDPM Village Impact** (`1_silver/ddpm/master_village_disaster_stat_2557_2567.csv`): Contains `Affected Households` and `Housing Damage`. Already mapped to 8-digit village codes.
*   **DDPM Sectoral Relief** (`1_silver/ddpm/master_financial_relief_by_sector.csv`): Contains provincial lump-sum payouts. Needs downscaling.
*   **DOPA Gold Spine** (`2_gold/dim_location_master.csv`): The canonical geographic boundaries for aggregation.

### B. Spatial Proxies & Weights (The "Disaggregators")
*   **WorldPop Constrained Population (100m, R2025A v1)**: Top-down demographic counts constrained to built settlements.
*   **WorldPop Harmonized Building Metrics (100m, 2023)**: Building counts, total area, and perimeters (Proxy for structural assets/capital).
*   **WorldPop Covariates (Infrastructure)**: Distance to Roads, Distance to Major Intersections (Proxy for economic hubs and relief accessibility).
*   **ESA WorldCover (10m)**: Land cover classification, specifically Cropland, Grassland, and Water bodies.

---

## 3. Analytical Pipelines (The 5-Pillar Strategy)

Based on the confidence levels of the available data, we have designed 5 possible data analysis pipelines. We will actively execute Pillars 1-4 and explicitly drop Pillar 5.

### Pillar 1: High Confidence - Human Impact Pipeline
*   **Target Data:** `Affected Households` (Primary) + `Deaths` / `Affected People` (Secondary where available).
*   **Spatial Proxy:** WorldPop Constrained Population (100m).
*   **Methodology:** Since DDPM impact data is largely at the village level, we use the 100m WorldPop data to define the **Exposure Denominator**. We overlay the village boundaries onto the WorldPop grid to calculate the true population density of the affected area, allowing us to calculate "Impact per 100k exposed residents/households."

### Pillar 2: High Confidence - Residential/Structural Pipeline
*   **Target Data:** `Housing Damage` (DDPM Village Stats) + `Village-Level Relief` (if granularly available).
*   **Spatial Proxy:** WorldPop Building Count + Building Area.
*   **Methodology:** Physical relief money and "housing damage" quantities have a direct physical relationship with Building Footprint covariates. We use WorldPop's building metrics to create a "Total Structural Asset" baseline. This allows us to calculate a **Damage Ratio** (Damaged Houses / Total Buildings).

### Pillar 3: Medium-High Confidence - Consolidated Fiscal Relief (Cross-Sectoral)
*   **Target Data:** Provincial Social/Infrastructure categories (`ด้านการดำรงชีพ`, `ด้านสังคมสงเคราะห์`, `ด้านบรรเทาสาธารณภัย`, `เชิงป้องกันหรือยับยั้ง`).
*   **Spatial Proxy:** WorldPop Building Area + Infrastructure Connectivity (Distance to Intersections / Roads).
*   **Methodology:** Fiscal relief for infrastructure or business recovery correlates strongly with economic connectivity. We distribute the provincial sectoral money to areas with high connectivity, creating an "Economic Exposure Map." We weight grid cells by combining building area and road density, then distribute the provincial lump sum to these 100m cells before re-aggregating to the village level.

### Pillar 4: Medium Confidence - Rural / Agricultural Relief Pipeline
*   **Target Data:** `Agriculture Damage` (DDPM Qty) + Agri-Relief categories (`ด้านเกษตร_พืช`, `ด้านเกษตร_ประมง`, `ด้านเกษตร_ปศุสัตว์`).
*   **Spatial Proxy:** ESA WorldCover (Cropland + Grassland + Water masks).
*   **Methodology:** Mask out all urban and forested areas in the province using ESA WorldCover. Distribute the provincial agricultural relief lump sum *only* to the remaining 10m/100m agricultural pixels. Re-aggregate the financial values from these pixels up to the 8-digit DOPA village boundaries.

### Pillar 5: Low Confidence - Specific Sectoral Assets [DROPPED]
*   **Target Data:** `Livestock Damage`, `Business Damage`, `Utilities Damage`.
*   **Spatial Proxy:** Ancillary Covariates (Grassland / Industrial masks).
*   **Status:** **FIRMLY DROPPED.**
*   **Rationale:** These indicators are mostly zero due to the absence of comprehensive surveys. Attempting to process these sparse datasets individually would introduce "false precision" and noise into the final index.

---

## 4. Next Steps (Implementation Preparation)
1. Ingest the identified WorldPop and ESA WorldCover GeoTIFFs for Thailand.
2. Develop a pilot script to run the active pipelines (Pillars 1-4) on a single highly-affected province (e.g., Ubon Ratchathani or Nakhon Si Thammarat) to validate the dasymetric distribution against known historical damage reports.