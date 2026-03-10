---
status: current
tags:
  - Data_model
  - Climate_risk
created: 2026-01-14
last_updated:
AI_prompt: false
project:
  - DCCE_CRDB
type:
aliases:
  - Idea / note
---
 To build a scalable data system, we must structure our architecture around the three fundamental data domains identified by the UNFCCC: **Observational**, **Projected**, and **Historical**.

Within these domains, data must be cross-indexed by its nature: **Climate** (physical atmosphere/land/ocean processes) and **Socio-economic** (human and economic drivers/vulnerabilities).

### 1. Key Data Domains and Core Entities

#### Domain A: Observational Data (Current & Recent State)

This domain provides the "ground truth" for assessing current vulnerabilities and establishing baselines.

- **Climate Entities:** The system must ingest **Essential Climate Variables (ECVs)**. These are categorized into:
    - **Atmospheric:** Surface (precipitation, temperature), Upper-air, and Atmospheric Composition.
    - **Terrestrial:** Hydrosphere (groundwater), Cryosphere (glaciers, snow), and Biosphere (land cover, soil moisture).
    - **Oceanic:** Physical (sea level, temperature), Biogeochemical, and Biological/Ecosystems.
- **Socio-economic Entities:** These define the exposure and vulnerability of the system.
    - **Population:** Density, age/gender structure, and distribution (e.g., coastal vs. urban).
    - **Economic:** GDP per capita, wealth distribution, and sector-specific data (agriculture, industry).
    - **Land/Resource Use:** Arable land, permanent pasture, and water withdrawal rates.

#### Domain B: Projected Data (Future Outlooks)

This domain is critical for strategic planning and is characterized by different temporal horizons and levels of uncertainty.

- **Model Entities:**
    - **Weather Forecasts:** Short-term (hours/days) for emergency alerts.
    - **Climate Predictions:** Medium-term (seasonal/decadal) for strategic infrastructure planning.
    - **Climate Projections:** Long-term (decades/centuries) for policy-level negotiations.
- **Scenario Entities:**
    - **Radiative Forcing (RCPs):** Pathways like RCP4.5 or RCP8.5 that describe future atmospheric conditions.
    - **Socio-economic Pathways (SSPs):** Assumptions on global population growth and economic development.
- **Downscaling Entities:** **Global Climate Models (GCMs)** and **Regional Climate Models (RCMs)** which translate global trends to local resolutions.

#### Domain C: Historical Data (Contextual Baselines)

Historical data is essential for validating models and understanding the sensitivity of human systems to past extremes.

- **Archival Entities:** Climatological normals, scanned paper records, farmer diaries, and proxy records (e.g., tree rings).
- **Analogue Entities:** Temporal analogues that characterize how past societies managed climate risks.

---

### 2. Conceptual Data Model for Climate Risk Assessment

To support high-resolution risk assessment, our conceptual model must ensure interoperability between climate hazards and socio-economic exposure.

#### Entity-Relationship Framework:

**1. Data Source Metadata (Parent Entity)**

- _Attributes:_ Provider (NMHS, Satellite, NGO), Collection Method (In-situ, Remote Sensing, Citizen Science), Quality Standard (WMO, ISO), Policy (Open Access vs. Restrictive).

**2. Spatial-Temporal Dimension (Indexing Entity)**

- _Spatial Scale:_ Global, Regional, National, Local/Urban.
- _Temporal Scale:_ Real-time, Monthly, Decadal, Century.
- _Note:_ The local level requires the highest resolution and disaggregation.

**3. Climate Hazard (Fact Entity)**

- _Attributes:_ Variable Type (ECV), Value, Unit, Uncertainty Range.
- _Relationship:_ Linked to **Historical Data** for baseline comparison and **Projected Data** for future risk.

**4. Socio-Economic Vulnerability (Fact Entity)**

- _Attributes:_ Indicator (e.g., Poverty Index, Population Density), Sector (Agriculture, Health, Energy), Disaggregation (Sex, Age, Ethnicity).
- _Relationship:_ Overlays with **Climate Hazard** to calculate **Potential Loss Estimates**.

**5. Adaptation Measure (Output Entity)**

- _Attributes:_ Measure Type (Infrastructure, Policy, Early Warning), Cost-Benefit Analysis, Multi-Criteria Analysis (MCA) score.
- _Relationship:_ Monitored via **Observational Data** to evaluate effectiveness.

### 3. Architectural Considerations for Real Use Cases

- **Handling Uncertainty:** The model must support "Deep Uncertainty" attributes. Instead of a single value, the system should store **Ensembles**—sets of forecasts starting with slightly different conditions to account for chaotic atmospheric behavior.
- **Quantitative vs. Qualitative:** Our architecture must ingest both structured numeric data (e.g., temperature) and unstructured narrative data (e.g., expert judgements, stakeholder interviews) to provide a "bottom-up" assessment of risk.
- **Big Data Integration:** To scale, we should implement **Data Cubes** and **Cloud/Edge Computing**. This allows for the processing of petabytes of satellite imagery and reanalysis data without local infrastructure bottlenecks.
- **Bridging the Gap:** The system acts as a **Climate Service**, transforming raw observational and projected data into customized products like **Climate Atlases**, **Gridded Data**, and **Risk Maps** for non-specialist decision-makers.