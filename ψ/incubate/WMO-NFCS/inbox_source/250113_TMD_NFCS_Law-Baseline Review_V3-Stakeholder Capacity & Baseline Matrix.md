This module is synthesized primarily from the `2.1-2.2_List-Baseline capac` and `Stakeholder map (Human)` datasets. It establishes the technical "as-is" state of the climate service value chain in Thailand, specifically focused on the **Human Settlement and Security (HS&S)** sector.

---

# **Module 2: Stakeholder Capacity & Baseline Matrix**

**Source Data:** `250113_TMD_NFCS_Law-Baseline Review_V3.xlsx - 2.1-2.2_List-Baseline capac.csv`

**Focus:** Institutional capacity across the five pillars of the **Global Framework for Climate Services (GFCS)**.

## **2.1 Stakeholder Taxonomy & Value Chain Positioning**

The ecosystem is categorized by functional roles within the data lifecycle:

|**Category**|**Primary Entities**|**Key Functions**|
|---|---|---|
|**Data Providers**|TMD, GISTDA, RID, DWR, HII|Surface observations, satellite remote sensing, hydrological monitoring.|
|**Co-Producers**|DCCE, DDPM, DPT, DOH|Translation of raw climate data into sector-specific risk indices and urban planning guidelines.|
|**Boundary Orgs**|DGA, Media, Thai Red Cross|Data dissemination, tailoring for non-technical audiences, and "last-mile" communication.|
|**End Users**|BMA (Bangkok), Local Gov (DLA), Private Sector|Application of services for urban drainage, infrastructure resilience, and insurance.|

## **2.2 Baseline Capacity by GFCS Pillar**

|**Pillar**|**Current Capacity (Highlights)**|**Lead Agencies**|
|---|---|---|
|**Observations & Monitoring (O&M)**|120+ Synoptic stations; Real-time telemetry; Satellite-based flood monitoring (GISTDA).|TMD, GISTDA, RID|
|**Research, Modelling & Prediction (RMP)**|Seasonal outlooks; Initial forays into **Urban Heat Island (UHI)** modeling and street-level downscaling.|TMD, DCCE, Academia|
|**Climate Services Info. System (CSIS)**|TMD Data Portal; DCCE Risk Area Database; GISTDA Disaster Platform.|TMD, DCCE, GISTDA|
|**User Interface Platform (UIP)**|Line Alert (TMD); DPM Reporter (DDPM); Thai Water app (HII).|DDPM, TMD, HII|
|**Capacity Development (CD)**|Climate Field Schools (TMD); International training (CITC by TGO/DCCE).|DCCE, TMD|

## **2.3 Existing Products & Services (Selected)**

- **Integrated Urban Climatic Map:** Spatial data showing climate-sensitive urban zones (TMD).
    
- **Climate Models at Street/Urban Level:** High-resolution simulations for urban morphology (TMD/DCCE).
    
- **Impact-based Forecast (IbF):** Moving from "what the weather will be" to "what the weather will _do_" (TMD/DDPM).
    
- **Urban Risk Maps:** GIS layers for flood and drought vulnerability in city centers (DPT/BMA).
    

---

## **2.4 Identified Gaps & Barriers (Architectural Challenges)**

Based on the baseline assessment, the following "Data Silos" and technical hurdles must be addressed in the DCCE Strategic Plan:

1. **Semantic Non-Standardization:** Different agencies use varying metadata standards for "Risk" and "Vulnerability," making cross-sectoral data fusion difficult.
    
2. **Granularity Gap:** While national-level data is robust, there is a lack of **Hyper-local (1km x 1km)** data required for urban adaptation planning in rapidly expanding cities.
    
3. **Governance Overlap:** As noted in Module 1, both TMD and DCCE are developing "Downscaling" capabilities. This requires a **Data Sovereignty Agreement** to prevent redundant computational spending.
    
4. **Feedback Loop Deficit:** The User Interface Platforms (UIP) are currently "Push-only." There is a missing architectural component for users to report "Ground Truth" back to providers to calibrate models.
    

---

### **Architectural Recommendation**

To resolve the **Granularity Gap (Barrier #2)**, the DCCE should architect a **Common Operating Picture (COP)**. This would involve a federated database where TMD provides the atmospheric "forcing" data, and DPT/BMA provides the high-resolution "urban fabric" data (building height, land use), enabling automated UHI and flood risk calculations.

