---
status: raw
tags:
  - data_model
created: 2026-02-05
last_updated: 2026-02-05
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type:
  - Artifact
---
#. The Semantic Schism: IPCC AR6 Risk Framework vs. Sendai Framework Data Requirements

The integration of climate science and disaster management data is currently hindered by a "semantic schism"—a divergence in how fundamental entities are defined, modeled, and stored. The IPCC AR6 and the Sendai Framework utilize overlapping terminology but employ distinct ontological definitions that fundamentally alter data modeling requirements.

## 1.1 The Epistemological Divergence of "Hazard"

The core friction between the IPCC and Sendai frameworks lies in the temporal orientation and granularity of their entity definitions. This is not merely a linguistic difference but a structural one that dictates database schema design.

**IPCC AR6 Risk Framework: Probabilistic and Systemic** The IPCC AR6 adopts a systemic view where **Risk** is the product of the interaction between **Hazard**, **Exposure**, and **Vulnerability**. In this context, the definition of "Hazard" has evolved significantly.

- **Climatic Impact-Drivers (CIDs):** A critical shift in AR6 Working Group I (WGI) is the move away from a simple "hazard" definition toward **Climatic Impact-Drivers (CIDs)**. CIDs are defined as physical climate system conditions (e.g., means, events, extremes) that affect an element of society or ecosystems.
    
- **Data Implication:** In a data model, an IPCC "Hazard" is rarely a single database row representing a localized event. Instead, it is a **probabilistic distribution** or a **multidimensional raster coverage**. It represents a continuous field of potentiality (e.g., a wind speed exceedance probability curve or a heat stress index raster). It encompasses both "slow-onset" phenomena (e.g., sea-level rise, ocean acidification) and "extreme events". The "Hazard" entity in an IPCC-aligned database is effectively a pointer to a NetCDF file or a stochastic event set, not a static record of a past occurrence.
    

**Sendai Framework for Disaster Risk Reduction: Deterministic and Retrospective**

In contrast, the Sendai Framework focuses on **Disaster Impact**, which is the realized, historical outcome of a hazard interacting with a vulnerable system.

- **Hazard Event as a Discrete Entity:** In the context of Sendai monitoring, a "Hazard Event" is treated as a discrete, bounded temporal occurrence (e.g., "Typhoon Yagi, Sept 2024"). It is an object with a specific start time, end time, and geographic scope. In relational database terms, the "Hazard Event" acts as a **Foreign Key** that links to loss data tables.
    
- **Disaster Impact as Accounting:** Impact is defined strictly through the lens of **Targets A, B, C, and D**—specifically mortality, affected populations, economic loss, and infrastructure damage.
    
- **Data Implication:** The Sendai data model requires deterministic, historical records. It does not store the "potential" for damage (risk) but the "actual" damage (loss). The database schema is transactional, recording specific instances of loss associated with specific instances of hazards.
    

## 1.2 Semantic Mapping and Ontological Gaps

The transition from AR6 to Sendai requires mapping **Climatic Impact-Drivers (CIDs)** to **Hazard Events**. This is a non-trivial many-to-many relationship.

**Table 1: Semantic and Ontological Comparison**

|**Concept**|**IPCC AR6 Definition (Probabilistic)**|**Sendai Framework / DesInventar Definition (Deterministic)**|**Semantic & Data Modeling Gap**|
|---|---|---|---|
|**Event Ontology**|**Climatic Impact-Driver (CID):** Physical condition (heat, cold, wet, dry, wind, snow, ice, coastal, open ocean). Defines the _state_ of the climate system.|**Hazardous Event:** A discrete occurrence identified by a start date, end date, and geographic scope. Defines a _transaction_ of energy release.|AR6 CIDs include continuous trends (e.g., sea-level rise) which defy the "start/end date" constraints of the Sendai schema. A "trend" cannot easily be a foreign key for a "daily loss" record without arbitrary temporal segmentation.|
|**Impact Logic**|**Risk Equation:** $Risk = f(Hazard, Exposure, Vulnerability)$. Risk is latent and potential.|**Loss Accounting:** $Loss = \sum (Direct Impacts + Indirect Impacts)$. Loss is realized and actual.|Sendai databases (DesInventar) generally lack the "Exposure" denominator (total exposed population) required to calculate the AR6 risk equation. They quantify the numerator (affected population) only.|
|**Temporal Scope**|Multi-decadal projections (SSP scenarios) and historical baselines (1850-1900).|Historical observation (2005–2015 baseline vs. 2020–2030 implementation).|Connecting a 2050 IPCC projection to a 2023 Sendai loss record requires complex "Time of Emergence" modeling to attribute the loss to climate change vs. natural variability.|
|**Entity Nature**|**Continuous Field:** Represented as Coverages (ISO 19123).|**Discrete Object:** Represented as Features (ISO 19109).|Requires a "Zonal Statistics" or "Spatial Join" operation to map the field values (Hazard) to the object location (Disaster).|

The IPCC AR6 emphasizes that risk stems from the _interaction_ of CIDs with vulnerability and exposure, whereas Sendai reporting often flattens this into a direct causal link between a named event and a loss figure. This necessitates a data architecture where "Hazard" is not merely an attribute of the loss record (e.g., `Column: HazardType = "Flood"`), but a separate, sophisticated entity linked via spatiotemporal intersection.

---

# 2. UNDRR DesInventar Sendai: Data Dictionary and Schema Specifications

The **DesInventar Sendai** system is the operational data store for monitoring the seven global targets of the Sendai Framework. It represents a shift from the older DesInventar methodology to a schema strictly aligned with the Sustainable Development Goals (SDG) indicators. While the older system allowed for flexible, bottom-up definition of effects, DesInventar Sendai enforces a rigid schema to ensure global comparability.

### 2.1 Core Schema Architecture

The DesInventar Sendai database is conceptually a **Star Schema** data warehouse, centered on a Fact Table of **"Disaster Cards"** (Loss Records) linked to Dimension Tables for **Geography**, **Time**, **Hazard Type**, and **Demographics**.

**Key Architectural Constraints:**

- **Granularity:** Data is collected at the lowest administrative unit (Level 2 or 3, e.g., District or Municipality) per event. This "atomized" storage allows for aggregation up to national and global levels.
    
- **Disaggregation:** The schema mandates disaggregation by sex, age, and disability for human impact indicators. This typically requires "child tables" or JSONB structures within the main Fact table to handle the one-to-many relationship of demographic breakdowns.
    

## 2.2 Required Attributes for Targets A, B, C, and D

The following specifications define the mandatory attributes for the Sendai Framework Monitor (SFM) as implemented in DesInventar Sendai. These attributes constitute the core columns of the "Disaster Impact" entity.

### **Target A: Substantially Reduce Global Disaster Mortality**

_Goal:_ Reduce mortality rate per 100,000 population.

_SDG Linkage:_ Indicator 11.5.1, 13.1.1.

|**Indicator ID**|**Attribute Name**|**Data Type**|**Description**|**Validation Rule**|
|---|---|---|---|---|
|**A-1**|`Deaths`|Integer|Total number of deaths attributed to the disaster event.|$\ge 0$; Cannot exceed total population of unit.|
|**A-2**|`Missing`|Integer|Number of persons whose whereabouts are unknown since the hazardous event.|$\ge 0$; Presumed dead for statistical purposes.|
|**A-3**|`Mortality_Rate`|Float|(Calculated) $(A1 + A2) / Total Population \times 100,000$.|Derived field.|
|**Disaggregation**|`Sex`|Enum|Male, Female, Other/Unknown.|Sum of Sex breakdown must equal Total A-1/A-2.|
|**Disaggregation**|`Age_Group`|Enum|0-14, 15-24, 25-64, 65+.|Standard demographic buckets.|
|**Disaggregation**|`Disability`|Boolean|Persons with disabilities.|Subset of Total.|

### **Target B: Substantially Reduce the Number of Affected People**

_Goal:_ Reduce affected persons per 100,000 population.

_SDG Linkage:_ Indicator 11.5.1, 13.1.1.

|**Indicator ID**|**Attribute Name**|**Data Type**|**Description**|**Validation Rule**|
|---|---|---|---|---|
|**B-1**|`Directly_Affected`|Integer|(Compound) Sum of B-2 to B-5.|Derived automatically.|
|**B-2**|`Injured_Ill`|Integer|People suffering physical injury or illness requiring immediate medical attention.|$\ge 0$.|
|**B-3**|`Damaged_Dwellings_Pop`|Integer|People living in dwellings with minor damage (habitable).|Estimated via avg household size if direct count unavailable.|
|**B-4**|`Destroyed_Dwellings_Pop`|Integer|People living in dwellings that are collapsed or uninhabitable.|Estimated via avg household size.|
|**B-5**|`Livelihood_Disrupted`|Integer|People whose livelihoods were disrupted or destroyed (e.g., crop failure, business closure).|Most complex indicator; prone to double-counting.|

### **Target C: Reduce Direct Disaster Economic Loss**

_Goal:_ Reduce loss in relation to Global GDP.

_SDG Linkage:_ Indicator 11.5.2.

|**Indicator ID**|**Attribute Name**|**Data Type**|**Description**|**Validation Rule**|
|---|---|---|---|---|
|**C-1**|`Direct_Ag_Loss`|Currency|Economic loss in the agriculture sector (crops, livestock, forestry, fisheries).|Must ideally separate Crops vs Livestock.|
|**C-2**|`Direct_Industrial_Loss`|Currency|Economic loss to productive assets in the industrial sector.|Excludes business interruption (indirect).|
|**C-3**|`Direct_Commercial_Loss`|Currency|Economic loss in the commercial/service sector (tourism, trade).|Direct asset damage only.|
|**C-4**|`Housing_Sector_Loss`|Currency|Economic value of damage to the housing sector (derived from B-3/B-4).|Often calculated: $Count \times ReplacementCost$.|
|**C-5**|`Infra_Loss`|Currency|Economic loss to critical infrastructure (transport, energy, water).|Sum of D-series monetary conversion.|
|**C-6**|`Cultural_Heritage_Loss`|Currency|Economic loss to cultural heritage assets.|Specific valuation challenges.|

_Note on Currency:_ All economic values must be stored in Local Currency Units (LCU) at the time of the event, but the system must maintain a **Conversion Table** to convert to US Dollars (USD) adjusted for Purchasing Power Parity (PPP) and inflation to the base year (2015) for global aggregation. This implies a temporal database of exchange rates and deflators.

### **Target D: Reduce Disaster Damage to Critical Infrastructure**

_Goal:_ Reduce damage to health/education facilities and service disruptions.

_SDG Linkage:_ Indicator 11.5.2.

|**Indicator ID**|**Attribute Name**|**Data Type**|**Description**|**Validation Rule**|
|---|---|---|---|---|
|**D-1**|`Critical_Infra_Damage`|Integer|(Compound) Number of destroyed/damaged facilities (Health + Education + Other).|Derived sum.|
|**D-2**|`Health_Facilities_Destroyed`|Integer|Number of health facilities destroyed or damaged.|Count of facilities (not monetary).|
|**D-3**|`Edu_Facilities_Destroyed`|Integer|Number of educational facilities destroyed or damaged.|Count of facilities.|
|**D-4**|`Other_Infra_Destroyed`|Integer|Transport, ICT, Energy, Water facilities damaged.|Count of facilities.|
|**D-5**|`Service_Disruption`|Integer|Number of disruptions to basic services (Compound).|Derived sum.|
|**D-6**|`Edu_Service_Interruption`|Integer|Number of times/days educational services were interrupted.|Metric: Facility-Days or just Count (methodology varies).|
|**D-7**|`Health_Service_Interruption`|Integer|Number of times/days health services were interrupted.|Metric: Facility-Days.|

## 2.3 Data Dictionary Constraints

The DesInventar Sendai schema enforces strict validation to ensure data integrity:

- **Geocoding:** Every event must be linked to a standard administrative unit code (e.g., GAUL or ISO 3166-2). This establishes the spatial join key.
    
- **Hazard Classification:** Events must use the standard Sendai Hazard Cluster definitions (Geophysical, Meteorological, Hydrological, Climatological) to align with IPCC CIDs.
    
- **Status Flags:** Records track the status of data collection (`Preliminary`, `Validated`, `Official`). This is critical for progressive refinement of loss estimates.
    

---

# 3. WMO Methodology: Linking Extreme Events to Economic Losses

The World Meteorological Organization (WMO) has established a rigorous methodology to solve the "attribution problem"—the challenge of inextricably linking a specific physical atmospheric phenomenon to a specific economic ledger entry. This is operationalized through the **WMO Cataloguing of Hazardous Events (WMO-CHE)**.

## 3.1 Standard Unique Identifiers (UUIDs) for Hazard Events

To avoid duplication and ensure international interoperability, the WMO mandates the use of a **Universally Unique Identifier (UUID)** for every hazardous event. This addresses the common problem where the same cyclone is named differently by different agencies, or where a "flood" is recorded as ten separate municipal events rather than one synoptic event.

**UUID Structure and Schema:** The WMO-CHE standard proposes a random or semi-structured UUID to uniquely identify an event record. This record acts as the "Parent" object to which "Child" impact records (DesInventar entries) are attached.

- **Format:** The standard recommends a 128-bit UUID (e.g., `f3ja-9ub3-ks92-mvyp-791a`) generated at the source of the meteorological observation. Alternatively, a structured format like `YYYY-ISO3-EVENTTYPE-SEQ` (e.g., `2023-VNM-TY-001`) is often used in practice for human readability, though the random UUID is preferred for machine-to-machine (M2M) interoperability.
    
- **Scope:** The UUID is assigned by the National Meteorological and Hydrological Service (NMHS) at the _start_ of the event (Record Creation). It is immutable.
    

**The WMO-CHE Data Record Schema:**

The "Event" entity in this schema is distinct from the "Impact" entity.

|**Field**|**Requirement**|**Description**|
|---|---|---|
|`Event_UUID`|**Mandatory**|The global unique key.|
|`Event_Type`|**Mandatory**|Based on the WMO Standard Typology (e.g., Tropical Cyclone, Heatwave).|
|`Start_DateTime`|**Mandatory**|ISO 8601 Timestamp of event initiation (UTC).|
|`End_DateTime`|**Mandatory**|ISO 8601 Timestamp of event cessation (UTC).|
|`Spatial_Footprint`|**Mandatory**|Polygon or Bounding Box (WKT/GeoJSON) defining the physical extent.|
|`Linkage_ID`|Optional|UUID of a "Parent" synoptic event (e.g., linking a "Flash Flood" UUID to the causing "Cyclone" UUID). This enables the modeling of **Cascading Hazards**.|

## 3.2 Methodology for Attribution of Economic Losses

The WMO methodology for linking events to losses (Target C) relies on **Impact-Based Forecasting (IBF)** principles utilized retrospectively. It moves beyond simple correlation to causal attribution.

**The Attribution Logic:**

1. **Event Definition:** The NMHS defines the physical event boundaries (time and space) and assigns the UUID.
    
2. **Asset Intersection:** The spatial footprint is overlaid with the exposure database (infrastructure, agriculture).
    
3. **Damage Assessment:** Direct Economic Loss ($L_D$) is calculated using replacement costs.
    
4. **Attribution Factor:** For complex disasters (e.g., a flood following a landslide), the loss is attributed to the "Primary Hazard" unless a "Cascading Event" model is used.
    

**Standard Formula for Direct Economic Loss:**

While specific valuation methods vary (e.g., market value vs. replacement cost), the WMO and UNISDR align on the **replacement cost method** for physical assets to ensure consistency in reconstruction planning:

$$L_D = \sum_{i=1}^{n} (Q_i \times P_i)$$

Where:

- $L_D$ is the Total Direct Economic Loss.
    
- $Q_i$ is the quantity of the asset $i$ damaged or destroyed (e.g., square meters of housing, kilometers of road).
    
- $P_i$ is the replacement price or repair cost of asset $i$ per unit.
    

**Indirect Loss Integration:** The WMO acknowledges **Indirect Economic Losses** (e.g., business interruption, supply chain disruption), often calculated using Input-Output (I-O) models or Computable General Equilibrium (CGE) models. However, these are reported separately from Direct Losses under Sendai Target C to prevent double counting of stock (asset) and flow (income) losses.

---

# 4. EU Climate-ADAPT: Data Ontology and Entity Analysis

The **EU Climate-ADAPT** platform manages unstructured and semi-structured knowledge regarding climate adaptation. Its ontology is designed to facilitate the retrieval of adaptation options based on hazard exposure, acting as a semantic bridge between scientific data and policy action.

## 4.1 Top-Level Entities and Semantic Structure

The Climate-ADAPT data model (and the associated **EIFFEL Ontology** ) is built on a Semantic Web architecture (RDF/SKOS/OWL). The ontology classifies knowledge into distinct, interconnected domains.

**Core Entities:**

1. **Case Studies:** Real-world implementations of adaptation (e.g., "Flood defense in Rotterdam"). These are the "Instance" data.
    
2. **Adaptation Options:** Generic solutions (e.g., "Green Roofs," "Managed Retreat," "Early Warning Systems"). These are the "Class" definitions of potential actions.
    
3. **Climate Impacts / Hazards:** The stressors (e.g., "Heatwave," "Sea Level Rise," "Drought").
    
4. **Sectors:** The economic or social domain affected (e.g., "Agriculture," "Health," "Transport").
    
5. **Organisations:** Entities responsible for implementation or funding.
    

### 4.2 Classification of 'Adaptation Options' vs. 'Climate Hazards'

The ontology classifies Adaptation Options in relation to Hazards using a **Many-to-Many** relationship, typically mediated by the concept of **Vulnerability** or **Risk Reduction**.

- **Relationship Logic:** `Adaptation_Option` -- _mitigates_impact_of_ --> `Climate_Hazard`.
    
- **Taxonomy Alignment:**
    
    - **Hazards** are classified using the **CIDs** (Climatic Impact-Drivers) framework from IPCC AR6 (e.g., Heat, Cold, Wet, Dry). This ensures that the "Problem" space is defined by physical science.
        
    - **Adaptation Options** are classified by **Category** (Grey/Structural, Green/Ecosystem-based, Soft/Policy) and **Sector**. This ensures that the "Solution" space is defined by policy and engineering domains.
        

**The EIFFEL Ontology (EIFF-O) Extension:** The **EIFFEL Ontology** extends the Climate-ADAPT model by integrating **Essential Climate Variables (ECVs)** and **SDGs**. It uses a "Wrapper Ontology" to link the **EO Taxonomy** (Earth Observation data) with the **Climate Change Domain**.

- **Triple Structure:** `Dataset (EO)` -- _measures_ --> `ECV` -- _indicates_ --> `Climate_Hazard` -- _addressed_by_ --> `Adaptation_Option`.
    
- **Significance:** This semantic chain allows a user to start with a satellite image (EO Dataset) and traverse the graph to find relevant policy solutions (Adaptation Options) without manual keyword searching. It automates the link between "Observation" and "Action."
    

---

## 5. ISO 14091:2021 Data Model: Vulnerability, Impacts, and Risk

**ISO 14091:2021** (Adaptation to climate change — Guidelines on vulnerability, impacts and risk assessment) standardizes the data model for risk assessments, codifying the shift from the older IPCC AR4 definition (where Vulnerability included Exposure) to the AR5/AR6 definition where they are distinct components of risk.

### 5.1 Core Data Model Entities

The ISO 14091 conceptual model relies on the **Impact Chain** methodology. This is a directed acyclic graph (DAG) representing cause-and-effect relationships. The core entities are:

1. **Climate Stimuli (Hazard):** The physical driver (e.g., Temperature increase, Precipitation decrease).
    
2. **Exposure:** The inventory of assets (people, buildings, ecosystems) present in the place where hazard events occur.
    
3. **Sensitivity:** The degree to which a system is affected, either adversely or beneficially, by climate variability or change (e.g., crop heat tolerance, building thermal efficiency).
    
4. **Adaptive Capacity:** The ability of systems, institutions, humans, and other organisms to adjust to potential damage, to take advantage of opportunities, or to respond to consequences.
    
5. **Vulnerability:** The propensity or predisposition to be adversely affected.
    
6. **Risk:** The potential for adverse consequences where something of value is at stake and where the occurrence and degree of an outcome is uncertain.
    

### 5.2 Relationship: Adaptive Capacity, Sensitivity, and Vulnerability

ISO 14091 defines the relationship functionally, which informs the computational logic of the risk assessment model:

$$Vulnerability \approx f(Sensitivity, Adaptive Capacity)$$

- **Sensitivity** is a _positive_ function of potential damage (Higher Sensitivity = Higher Vulnerability).
    
- **Adaptive Capacity** is a _negative_ function of potential damage (Higher Adaptive Capacity = Lower Vulnerability).
    

**Conceptual ERD Relationships:**

- `System` -- _has_attribute_ --> `Sensitivity`.
    
- `System` -- _has_attribute_ --> `Adaptive_Capacity`.
    
- `Hazard` -- _impacts_ --> `System` (_mediated by Sensitivity_).
    
- `Vulnerability` is a **derived entity** or computed attribute resulting from the interaction of `Sensitivity` and `Adaptive_Capacity` relative to a specific `Hazard`. It is not a static attribute of the asset itself but a dynamic state relative to a hazard.
    

**Crucial Distinction in Data Modeling:** ISO 14091 explicitly separates **Exposure** from **Vulnerability**. In the data model, **Exposure** is a **Spatial Intersection** (Is the asset in the flood zone?), whereas **Vulnerability** is an **Intrinsic Property** (Is the asset made of mud or concrete?). This separation allows for more accurate queries: one can query for "Highly Vulnerable assets" (mud houses) regardless of their location, or "Highly Exposed assets" (houses in the floodplain) regardless of their material.

---

## 6. Spatial Risk Assessment: ISO 19123 and DGGS

A critical bottleneck in large-scale risk modeling is the computational mismatch between **Continuous Fields** (Climate Rasters, e.g., NetCDF temperature arrays) and **Discrete Features** (Administrative Boundaries, Buildings, Roads). Traditional GIS operations (e.g., "Zonal Statistics") are computationally expensive and prone to errors at global scales.

### 6.1 Modeling the Intersection: Fields vs. Features

**ISO 19123 (Schema for Coverage Geometry):**

ISO 19123 defines the **Coverage**, a function that returns values from a spatiotemporal domain for any direct position within its domain. Climate models are typically **Grid Coverages**.

- _Challenge:_ Aggregating a raster coverage into a vector polygon (e.g., "Average temperature in District X") requires complex geometric intersection calculations. This is an $O(n \log m)$ operation that scales poorly with high-resolution data.
    

**OGC Discrete Global Grid Systems (DGGS):**

OGC DGGS standards propose a radical solution by tessellating the Earth into hierarchical, equal-area cells (e.g., hexagons, triangles).

- _Methodology:_ Both the Climate Raster (Field) and the Asset Vector (Feature) are **quantized** into the _same_ DGGS Cell ID structure (e.g., H3 or rHEALPix indices).
    
- _Data Model:_ Instead of spatial joins ($Polygon \cap Raster$), the operation becomes a **Set Intersection** of Cell IDs (`WHERE Cell_ID_A = Cell_ID_B`).
    
- _Performance:_ This allows for $O(1)$ or $O(\log n)$ retrieval speed, transforming a complex geometric problem into a fast database indexing lookup.
    

### 6.2 The 'Common Spatial Unit' (CSU) or 'Proxy Asset'

To avoid real-time spatial joins in operational risk dashboards, systems utilize a **Common Spatial Unit (CSU)** as a proxy asset.

- **Pattern:** All exposure data (population, GDP, buildings) is pre-aggregated to a standardized grid (e.g., 1km x 1km or a specific Level-14 DGGS cell).
    
- **Proxy Asset:** The Grid Cell itself becomes the "Asset" in the risk database.
    
- **Benefit:** This creates a **Data Cube** structure where Time, Hazard, and Exposure are dimensions of the same spatial unit. This enables **OLAP (Online Analytical Processing)** capabilities, allowing users to slice and dice risk data (e.g., "Show me total risk for all cells where Temperature > 35°C AND Population_Density > 1000") in sub-seconds.
    

---

## 7. Multidimensional Climate Data: W3C SSN and NetCDF CF

Integrating sensor observations (IoT, Weather Stations) with global climate models (GCMs) requires rigorous temporal semantics to distinguish between "when it happened" and "when it was predicted."

### 7.1 Observation Time vs. Model Reference Time

**W3C SSN (Semantic Sensor Network) Ontology:**

Designed for sensor data, SSN (and its lightweight core SOSA - Sensor, Observation, Sample, and Actuator) is precise about observation events.

- **`sosa:resultTime`:** The instant of time when the observation result was generated (e.g., when the thermometer reading was digitized).
    
- **`sosa:phenomenonTime`:** The time interval or instant during which the feature of interest was observed (e.g., the 10-minute period over which wind speed was averaged).
    

**NetCDF CF (Climate and Forecast) Metadata Conventions:**

Designed for model outputs, CF focuses on the simulation timeline.

- **Reference Time (`reftime`):** The initialization time of the model run (e.g., "Days since 2023-01-01 00:00:00"). This is the anchor point for the forecast.
    
- **Valid Time (`time`):** The coordinate variable representing the time for which the forecast is valid.
    
- **Distinction:** In a relational ERD or Data Warehouse, a forecast is identified by a **Composite Key** of `(Model_Run_ID, Valid_Time)`. The `Model_Run_ID` links to the _Reference Time_. A common error in simple databases is storing only the Valid Time, which leads to overwriting old forecasts and losing the ability to analyze forecast accuracy (hindcasting).
    

### 7.2 Modeling 'Climate Scenario' in an ERD

How should a **Climate Scenario** (e.g., RCP 8.5, SSP3-7.0) be represented in a relational schema?

- **Analysis:** A Climate Scenario is **not** merely an attribute of a model run, nor is it a subtype of Time. In Data Warehousing terms, it is a fundamental **Dimension** of the data hypercube.
    
- **ERD Recommendation:**
    
    - **Entity:** `Scenario` Dimension (Attributes: `Scenario_ID`, `Description`, `Radiative_Forcing_Target`, `Socio_Economic_pathway`).
        
    - **Relationship:** `Model_Run` -- _simulates_ --> `Scenario`.
        
    - **Fact Table:** `Climate_Projection_Fact` has a foreign key to `Scenario_ID`.
        
- **Why?** Scenarios represent **Alternative Futures**—parallel timelines that cannot be merged. Treating them as a dimension allows for "Scenario Analysis" (comparing outcomes across scenarios), which is the core requirement of reporting frameworks like the **Task Force on Climate-related Financial Disclosures (TCFD)** and the **Network for Greening the Financial System (NGFS)**.
    

---

## 8. Hazard Taxonomy and Database Design: GED4ALL

The **GED4ALL (Global Exposure Database for All)** initiative provides the blueprint for multi-hazard exposure schemas, addressing the complexity of characterizing assets for different types of threats.

### 8.1 Hazard Taxonomy Modeling

GED4ALL employs a comprehensive **Taxonomy** that characterizes assets based on attributes relevant to specific hazards.

- _Example:_ A building in the database has attributes for "Roof Type" (relevant for Wind hazard/Typhoon), "Wall Material" (relevant for Earthquake), and "Ground Floor Elevation" (relevant for Flood).
    

### 8.2 Polymorphic Association vs. Flat Denormalized Structure

**The Challenge:** Different hazards require different event details. A flood needs "Inundation Depth" and "Duration"; an earthquake needs "Magnitude," "Hypocenter," and "Peak Ground Acceleration."

**Pattern Analysis:**

1. **Polymorphic Association:** A central `Event` table links to specific sub-tables like `Flood_Detail`, `Quake_Detail`, `Drought_Detail`.
    
    - _Pros:_ Clean, normalized, strictly typed, infinitely extensible.
        
    - _Cons:_ Complex SQL joins are required for aggregation. Querying "all events with severity > X" is difficult because "severity" is defined differently in each sub-table.
        
2. **Flat Denormalized:** A single `Event` table with columns for all possible attributes (`Flood_Depth`, `Quake_Mag`, `Wind_Speed`), mostly NULL for any given record.
    
    - _Pros:_ Fast analytic queries (OLAP). Easy to aggregate.
        
    - _Cons:_ Sparse matrix (mostly empty space), hard to maintain schema changes.
        

**GED4ALL & DesInventar Approach:**

GED4ALL and modern risk libraries generally favor a **Hybrid** or **Extensible** approach.

- **Recommended Pattern:** A **Star Schema** with a unified `Event_Fact` table containing common measures (UUID, StartDate, EndDate, TotalLossUSD, TotalDeaths). Specific hazard parameters should remain in Dimension tables or, increasingly, in **JSONB / NoSQL** columns within the relational table.
    
- **Why?** This allows for high-speed aggregation of the "Common Denominators" (Loss, Death) for Sendai reporting, while preserving the rich, variable-structure technical data required for scientific analysis.
    

---

## 9. Conceptual GIS: Events as Objects

Moving beyond the traditional "Map Layer" paradigm, **Camara & Montzka (2016)** and related work by Gilberto Camara propose an **Object-Oriented GIS** approach where events are treated as first-class citizens.

### 9.1 Distinguishing 'Hazard Event' and 'Hazard Driver'

In a unified **Risk Registry**, we must distinguish between the _discrete_ and the _continuous_ to avoid category errors.

1. **Hazard Event (Spatiotemporal Object):**
    
    - **Concept:** A discrete object with a lifecycle (Birth, Evolution, Death) and a changing spatial footprint.
        
    - _Example:_ Typhoon Yagi.
        
    - _Data Structure:_ `Object_ID`, `Trajectory` (LineString), `Lifecycle_State`, `Moving_Polygon_Footprint`.
        
2. **Hazard Driver (Continuous Field):**
    
    - **Concept:** A continuous field varying in space and time, influencing the _probability_ of events but not constituting an event itself in the same way.
        
    - _Example:_ Sea Surface Temperature (SST) anomaly, Soil Moisture.
        
    - _Data Structure:_ 4D Raster/Coverage ($x, y, z, t$).
        

### 9.2 Compatibility in a Risk Registry (Minimal Attributes)

To make these compatible in a single registry, the **Driver** must often be reduced to an attribute of the **Event** or the **Spatial Unit** via spatiotemporal intersection.

**Minimal Attributes for Compatibility:**

To query both "Typhoons" and "Sea Level Rise" in the same risk dashboard, they must share:

1. **UUID:** The WMO-CHE identifier for the Event.
    
2. **Spatiotemporal Bounding Box (ST-BBOX):** The unified 4D extent $(x_{min}, y_{min}, t_{start})$ to $(x_{max}, y_{max}, t_{end})$.
    
3. **Intensity Measure (IM):** A normalized scalar value representing severity (e.g., "Return Period" or "Exceedance Probability") allows comparison between a Typhoon (Event) and Drought (Driver/Slow-onset).
    
4. **Impact Metric:** The common denominator (e.g., USD Loss, Mortality).
    

---

## 10. Conclusion

The integration of IPCC AR6 risk dynamics with Sendai Framework monitoring requires a sophisticated data architecture that transcends traditional GIS layers and flat spreadsheets. The semantic gap between "Risk" (probabilistic) and "Impact" (deterministic) can be bridged using **WMO-CHE UUIDs** as the primary key for event cataloging, enabling a clear lineage from physical cause to economic effect. To handle the computational load of associating continuous climate drivers (NetCDF) with discrete exposure assets (GED4ALL), the adoption of **DGGS (common spatial units)** and **Data Cube** architectures is essential to avoid the $O(n^2)$ complexity of spatial joins. Finally, the ISO 14091 impact chain provides the necessary logical schema to model the complex dependencies between Sensitivity, Adaptive Capacity, and Vulnerability, ensuring that adaptation data is not just archived, but actionable. By adopting these standards, we move from disjointed datasets to a cohesive Global Risk Data Infrastructure capable of supporting the complex decision-making required in a changing climate.

### References

- **IPCC/Sendai Frameworks:**
    
- **DesInventar/Targets:**
    
- **WMO/UUID/Loss:**
    
- **Ontologies/Climate-ADAPT:**
    
- **ISO Standards:**
    
- **Spatial/GIS Theory:**
    
- **Data Modeling:**