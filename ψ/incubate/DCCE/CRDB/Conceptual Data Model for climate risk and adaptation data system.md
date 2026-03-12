---
type: task
status: In Progress
project:
  - DCCE_CRDB
start date: 2026-01-09T00:00:00.000Z
due date: 2026-02-06T00:00:00.000Z
color: var(--mk-color-green)
---
# Where CDM Fits: Mapping to TOR Clauses

 **Implicit Requirements That Demand a CDM:**

| TOR Clause                                                      | What It Asks For                                                                  | Why It Needs a CDM                                                                          |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **5.2.3** "Data Management Structure"                           | Data sources, responsible agencies, mechanisms                                    | **Can't define "structure" without modeling entities and their relationships**              |
| **5.3.5** Baseline Data Inventory categorized by risk framework | Hazard, Exposure, Sensitivity, Adaptive Capacity, Impact, Response, Loss & Damage | **These categories ARE entities that need relationship definitions**                        |
| **5.3.6** Minimum Viable Dataset (MVD) for Loss & Damage        | Design a dataset structure                                                        | **This explicitly requires a logical data model, which builds on a conceptual model**       |
| **5.3.8** Gap Analysis (Supply vs. Demand)                      | Identify missing data quantitatively and qualitatively                            | **Gap analysis requires knowing WHAT entities/relationships are needed (conceptual model)** |


**Purpose:** Define the core entities, relationships, and business rules for the IVRA data system

---

>[!document]
>- [[Data Model - CLIMADA]]
>- [[Data Model - UNFCCC Data for Adaptation]]
>- [[01_Projects/2025-11_DCCE-CRDB/output/Use cases and Data domain- UNDP project interview result]]
>- [[Projects/2025-11_DCCE-CRDB/What is Conceptual Data Modeling Purpose & Examples]]

Draft data model
https://drive.google.com/file/d/1l48sVaKuFjx-iAfoAxgkyR9qincLlOHM/view?usp=sharing


**Business Rules Examples:**
- An Impact Assessment MUST reference at least one Hazard Event
- An Exposed Asset CAN have multiple Vulnerability Factors
- A Hazard Event CAN affect multiple Exposed Assets (many-to-many through Impact Assessment)

---
# Archived
## A) First Draft of the Conceptual Data Model for IVRA Domain (#archived)
The draft is based on deep research results and project documents
>[!Document]
> Deep research note
> 1. [[Technical Interoperability and Data Modeling in Disaster Risk Reduction - A Comparative Analysis of IPCC, Sendai, and Global Standards]]
> 
> Project Documents
> 2. [[CRDB - Implementation Plan]]
> 3. [[What is Conceptual Data Modeling Purpose & Examples]]
> 4. [[Data System Artifact Guide]]



**Subject Area 1: Physical Climate & Hazards**
- **`CLIMATE_SCENARIO`**
    - **Definition:** The hypothetical future pathway (e.g., SSP3-7.0, RCP 8.5) or historical baseline used for simulation.
    - **Business Rule:** Essential for distinguishing "Reference Time" (Model initialization) from "Valid Time" (Forecast target).
        
- **`CLIMATE_DRIVER` (The Continuous Field)**
    - **Definition:** A specific Climatic Impact-Driver (CID) as defined by IPCC AR6 (e.g., Mean Surface Temperature, Sea Level Rise).
    - **Data Nature:** Typically 4D Spatiotemporal Cubes (NetCDF).
    - **Key Distinction:** Represents the _state_ of the system, not a specific disaster instance.
        
- **`HAZARDOUS_EVENT` (The Discrete Object)**
    - **Definition:** A specific, named occurrence (e.g., "Typhoon Yagi", "2024 Phrae Flood") bounded by time and space.
    - **Business Rule:** Must possess a **WMO-CHE UUID** to allow aggregation of disparate local reports into a single synoptic event. This entity is the "Parent" for Loss & Damage records.
        

**Subject Area 2: Exposure & Vulnerability (The System)**
- **`SPATIAL_UNIT`**
    - **Definition:** The common geographic denominator used to link Hazards to Assets.
    - **Strategic Choice:** To solve the $O(n^2)$ computational cost of spatial joins, this should ideally represent a **DGGS Cell** or a standardized Administrative Unit (Level 3).
        
- **`EXPOSED_ASSET`**
    - **Definition:** Elements of society (Population, Infrastructure, Ecosystems) present in hazard zones.
    - **Taxonomy:** Aligned with **GED4ALL** (e.g., Building structural types, Crop varieties).
    - **GHG Synergy (TGEIS Alignment):** This entity doubles as "Activity Data" for GHG inventory (Division 2.1). Attributes must include TGEIS requirements (e.g., Manure management type for livestock, Rice variety for methane calcs) to prevent double-reporting.
        
- **`VULNERABILITY_PROFILE`**
    - **Definition:** The intrinsic predisposition of an asset to be adversely affected.
    - **Logic (ISO 14091):** Derived from the interaction of _Sensitivity_ (e.g., crop heat intolerance) and _Adaptive Capacity_ (e.g., irrigation access).
    - **Constraint:** Separated from Exposure. A house is vulnerable due to its material (wood), regardless of whether it is currently flooded.
        

**Subject Area 3: Outcomes (Risk & Loss)**
- **`RISK_ASSESSMENT` (Probabilistic)**
    - **Definition:** The calculated potential for adverse consequences.
    - **Formula:** $Risk = f(Hazard, Exposure, Vulnerability)$.
    - **Output:** Return periods, Exceedance probabilities, Risk Indices.
        
- **`LOSS_DAMAGE_RECORD` (Deterministic)**
    - **Definition:** Historical, realized impact data linked to Sendai Framework Targets A-D.
    - **Attributes:** Mortality counts, Economic loss (LCU/USD), Infrastructure damage counts.
    - **Linkage:** Must be a child of `HAZARDOUS_EVENT` to enable attribution analysis.

```mermaid
erDiagram
    %% CLIMATE SCIENCE DOMAIN
    CLIMATE_SCENARIO ||--|{ CLIMATE_DRIVER : simulates
    CLIMATE_DRIVER ||--o{ HAZARD_EVENT : manifests_as
    
    %% SPATIAL FOUNDATION (DGGS / ADMIN)
    SPATIAL_UNIT ||--|{ EXPOSED_ASSET : contains
    SPATIAL_UNIT ||--|{ CLIMATE_DRIVER : intersects
    
    %% SOCIO-ECONOMIC DOMAIN
    EXPOSED_ASSET ||--|| VULNERABILITY_PROFILE : has_intrinsic
    VULNERABILITY_PROFILE ||--|{ SENSITIVITY_FACTOR : composed_of
    VULNERABILITY_PROFILE ||--|{ ADAPTIVE_CAPACITY : composed_of
    
    %% RISK & IMPACT DOMAIN
    HAZARD_EVENT ||--o{ LOSS_DAMAGE_RECORD : causes
    EXPOSED_ASSET ||--o{ LOSS_DAMAGE_RECORD : sustains
    EXPOSED_ASSET ||--o{ RISK_ASSESSMENT : subject_of
    
    %% M&E / ADAPTATION (External/Shallow)
    RISK_ASSESSMENT }|--|| ADAPTATION_INTERVENTION : informs
```



## B) CDM of the IVRA domain as of Feb 5

Additional context was given, including

>[!Document]
>1. [[Development of National Climate Risk Index - Thailand]]
>2. [[Process-Based and Governance-Oriented Frameworks for Measuring Climate Resilience - Consensus.AI]]
>3. [[Data Model - CLIMADA]]
>4. [[Spatial climate risk map DCCE v1]]
>5. [[Sources/Spatial climate risk map DCCE v2|Spatial climate risk map DCCE v2]]

This context informs the existing use cases of climate risk data products to align the CDM to best practices.

The following summary traces the evolution of the CDM, highlighting the specific architectural decisions made to bridge the gap between "Hard Science" rigor and "Soft Science" policy requirements.

| **Phase**                                          | **Use Case Challenge**                                                                                                                                                                                                                    | **Strategic Modification**                                                                                                                                                                                                                                                                                  | **Outcome**                                                                                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Initial Foundation** (IVRA-First)             | **Scope Definition:** How to ground the data system in rigorous climate science (IPCC AR6) while acknowledging disaster management needs?                                                                                                 | **Subject Area Definition:** Established the core separation between **Physical Climate** (Probabilistic Potential) and **Discrete Events** (Deterministic Accounting).                                                                                                                                     | A baseline structure rooted in the **IPCC Risk Equation** ($Risk = Hazard \times Exposure \times Vulnerability$) but separated from the **Loss Accounting** domain.         |
| **2. The "Slow-Onset" Fix** (Trends vs. Events)    | **Integration Conflict:** Sendai Reporting requires discrete "Events" (Typhoons), but Climate Science tracks continuous "Drivers" (Sea Level Rise). How to attribute loss to a slow trend without "faking" an event?                      | **Added `ATTRIBUTION_LINK`:** An associative entity that acts as a "Universal Adapter." It allows a `LOSS_DAMAGE_RECORD` to link _either_ to a `HAZARDOUS_EVENT` (Shock) _or_ a `CLIMATE_DRIVER` + `TIME_PERIOD` (Stress).                                                                                  | Solves the **"Semantic Schism."** Prevents the database from being polluted with arbitrary "Fake Events" (e.g., "Drought of 2024") just to satisfy foreign key constraints. |
| **3. The "Soft Science" Fix** (Curves vs. Indices) | **Methodology Conflict:** **CLIMADA** calculates risk using mathematical **Damage Functions** (Curves), whereas the **National CRI** uses **Composite Indices** based on social indicators. The initial model was too rigid to hold both. | **Vulnerability "Strategy Pattern":** Split the Vulnerability entity into two subtypes:<br><br>  <br><br>1. **`IMPACT_FUNCTION`:** Stores math curves (for CLIMADA).<br><br>  <br><br>2. **`VULNERBILITY_COMPONENT`:** Store qualities, variables, statistics that could be used to represent vulnerability | A **Polymorphic Model** that allows the database to store "Hard" actuarial risk models and "Soft" policy scores side-by-side without schema changes.                        |
| **4. The "Fluid Indicator" Fix** (Dynamic Roles)   | **Flexibility Conflict:** In policy maps (DCCE Risk Map), a variable like "Poverty" changes roles—it is **Sensitivity** in one project but **Adaptive Capacity** in another. Hard-coding it breaks flexibility.                           | **Added `VULNERABILITY_DETERMINANT`:** Moved all social variables (Governance, Social, Economic) into a neutral library.<br><br>  <br><br>**Added `FRAMEWORK_MAPPING`:** An entity that assigns roles _dynamically_ to `VULNERABILITY_DETERMINANT` according to `VULNERABILITY_FRAMEWORK`                   | Supports the **Stakeholder-Driven** nature of DCCE work, where indicator lists and groupings are frequently revised.                                                        |
|                                                    |                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                             |

## Current State: A "Hybrid" Enterprise Architecture
The CDM has evolved from a purely scientific model into a **Pragmatic Enterprise Solution**. It is now capable of supporting four distinct but interconnected analytical workflows:
1. **Probabilistic Modeling:** via `IMPACT_FUNCTION` $\rightarrow$ `RISK_METRIC`.
2. **Composite Indexing:** via `CAPACITY_FRAMEWORK` $\rightarrow$ `COMPOSITE_INDEX`.
3. **Disaster Accounting:** via `HAZARDOUS_EVENT` $\rightarrow$ `LOSS_DAMAGE_RECORD`.
4. **Trend Attribution:** via `ATTRIBUTION_LINK` $\rightarrow$ `CLIMATE_DRIVER`.


## IVRA Domain ERD

- **Top Left (The Cause):** We have Climate Drivers (Trends) and Hazardous Events (Shocks).
- **Center (The Bridge):** The `ATTRIBUTION_LINK` solves the "Slow Onset" problem. It lets us link a Loss Record to _either_ a specific Typhoon UUID _or_ a general Sea Level Rise trend.
- **Right (The Flexible Vulnerability):** The `VULNERABILITY_DEFINITION` acts as a switch. It allows the system to use "Engineering Curves" (`IMPACT_FUNCTION`) for CLIMADA, or "Social Indicators" (`VULNERABILITY_DETERMINANT`) for the National Climate Risk Index, without breaking the database.


[View online](https://mermaid.ai/app/projects/db6be078-a24c-4259-b99d-edbb06a16c4b/diagrams/da770855-008c-4804-9860-49f9411421f0/share/invite/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2N1bWVudElEIjoiZGE3NzA4NTUtMDA4Yy00ODA0LTk4NjAtNDlmOTQxMTQyMWYwIiwiYWNjZXNzIjoiVmlldyIsImlhdCI6MTc3MDI4NjA0Mn0.txK531D045v45plJ_BXsf3b7n9ferjESJNEkGULqbrA)

```mermaid
erDiagram
    %% --- SUBJECT AREA 1: PHYSICAL CLIMATE (The Cause) ---
    CLIMATE_SCENARIO ||--|{ CLIMATE_DRIVER : simulates
    CLIMATE_DRIVER ||--o{ HAZARDOUS_EVENT : manifests_as
    
    %% --- SUBJECT AREA 2: ATTRIBUTION (The Bridge) ---
    %% The Link explains the Loss by pointing to a Cause
    LOSS_DAMAGE_RECORD ||--|{ ATTRIBUTION_LINK : explained_by
    
    %% The Cause can be a distinct Event (Shock) OR a Driver (Stress)
    ATTRIBUTION_LINK }|..o| HAZARDOUS_EVENT : attributed_to_event
    ATTRIBUTION_LINK }|..o| CLIMATE_DRIVER : attributed_to_driver

    %% --- SUBJECT AREA 3: ASSETS & SPACE (The Receptor) ---
    SPATIAL_UNIT ||--|{ CLIMATE_DRIVER : spatial_reference_for
    SPATIAL_UNIT ||--|{ EXPOSED_ASSET : contains
    
    %% --- SUBJECT AREA 4: VULNERABILITY (The Strategy) ---
    %% Asset is assigned a vulnerability definition
    EXPOSED_ASSET }|--|| VULNERABILITY_DEFINITION : has_assigned
    
    %% The Strategy Pattern: Two ways to define vulnerability
    VULNERABILITY_DEFINITION ||--|{ IMPACT_FUNCTION : implements_math_curve
    VULNERABILITY_DEFINITION ||--|{ VULNERABILITY_FRAMEWORK : implements_index_logic
    
    %% The Indicator Library Pattern (Soft Data)
    VULNERABILITY_FRAMEWORK ||--|{ FRAMEWORK_MAPPING : defines_structure
    FRAMEWORK_MAPPING }|--|| VULNERABILITY_DETERMINANT : maps_variable_to_vulnerability_component

    %% --- SUBJECT AREA 5: OUTCOMES (The Products) ---
    %% Risk Assessment uses the Science (Driver) + The Asset + The Vuln Def
    RISK_ASSESSMENT }|--|| CLIMATE_DRIVER : analyzes
    RISK_ASSESSMENT }|--|| EXPOSED_ASSET : analyzes
    RISK_ASSESSMENT }|--|| VULNERABILITY_DEFINITION : utilizes

    %% The Outputs
    RISK_ASSESSMENT ||--|{ RISK_METRIC : produces_probabilistic
    RISK_ASSESSMENT ||--|{ COMPOSITE_INDEX : produces_composite_score

    %% Retrospective Link (Loss happens to Asset)
    LOSS_DAMAGE_RECORD }|--|| EXPOSED_ASSET : sustained_by
```

---
## Associative Entities
### 1)`ATTRIBUTION_LINK`
`{C}ATTRIBUTION_LINK`solves the hardest problem identified in the technical analysis: 
>[!warning] How to store "Slow-Onset" losses (like Sea Level Rise) in a database designed for "Disaster Events" (like Floods).

1. **Why "Attribution"? The Semantic Reason**
	I chose the term **"Attribution"** because it reflects the scientific and policy necessity of **"Event Attribution"** in climate science.
	In the provided documents, there is a fundamental conflict called the "Semantic Schism":

	- **Sendai Framework (The Accountant):** Requires a discrete **"Hazard Event"** with a start/end date (e.g., "Typhoon Yagi") to attach a loss to.
	- **IPCC AR6 (The Scientist):** Recognizes **"Climatic Impact-Drivers" (CIDs)** like Sea Level Rise or Temperature Increase, which are **Continuous Trends**, not discrete events with a simple start date.
    
	**The Problem:** If a farmer loses rice yield due to a 10-year warming trend, there is no "Event UUID" to type into the database. If you force it into a "Event" table, you have to invent arbitrary start/end dates (e.g., "Heatwave of 2024"), which scientifically misrepresents the long-term trend.

	**The Solution:** The **`ATTRIBUTION_LINK`** entity allows the database to formally record the _assertion of cause_. It answers the question: _"To what physical phenomenon do we attribute this specific economic loss?"_

2. **How it reflects in the CDM (The Structure)**
	In data modeling terms, `ATTRIBUTION_LINK` is an **Associative Entity** (sometimes called a Junction Table or Bridge Table). It acts as a "Universal Adapter" that sits between the **Outcome** (Loss) and the **Cause** (Hazard/Driver).
	This structure allows the `LOSS_DAMAGE_RECORD` table to remain clean and standardized (Target A, B, C, D), regardless of whether the cause was a sudden shock or a slow stress.

>[!Comment]
>
>**It supports Polymorphic Causes:**
>- It allows the database to say: "This loss was caused by **Event X**" (Typhoon).
>- _OR_ "This loss was caused by **Driver Y**" (Sea Level Rise) intersecting with this location.
>  
>**It captures "Scientific Confidence":**
>- Attributing a flood to a specific storm is easy (Confidence = 100%).
>- Attributing a crop failure to "Climate Change induced Drought" is a probabilistic assertion
> - The `ATTRIBUTION_LINK` entity can hold an attribute like `Confidence_Level` (e.g., "High Confidence" vs. "Medium Confidence"). A simple foreign key cannot capture this nuance.


### 2) `FRAMEWORK_MAPPING` and `VULNERABILITY_DETERMINANT`

`VULNERABILITY_FRAMEWORK` contains the theory  used to conceptualize vulnerability.
`FRAMEWORK_MAPPING` then contains the implementation of the theory to what group (sensitivity, coping capacity, lack of adaptive capacity, adaptive capacity, transformative capacity, readiness) how the `VULNERABILITY_DETERMINANT` is assigned. 

## Stress test the model 📉
#### Use Case 1: CLIMADA Flood Risk 
- **Input:** `HAZARDOUS_EVENT` (Flood depth raster).
- **Vulnerability:** The system selects a **`VULNERABILITY_DEFINITION`** of type **`IMPACT_FUNCTION`** (e.g., "Depth-Damage Curve ID #55").
- **Process:** It applies the curve coefficients to the raster.
- **Output:** It generates a **`RISK_METRIC`** (e.g., "Expected Annual Damage: $5M").
- _Result:_ Fully compatible with the probabilistic risk logic.
    
#### Use Case 2: National Resilience Index 
- **Input:** `VULNERABILITY_DETERMINANT` (Poverty stats, Governance survey).
- **Vulnerability:** The system selects a **`VULNERABILITY_DEFINITION`** of type **`VULNERABILITY_FRAMEWORK`** (e.g., "National CRI 2026").
- **Process:** It looks up **`FRAMEWORK_MAPPING`** to see that "Governance Survey" is assigned to the "Transformative Capacity" role.
- **Output:** It generates a **`COMPOSITE_INDEX`** (e.g., "Resilience Score: 0.75").
- _Result:_ Fully compatible with the governance/process-oriented frameworks.


---

## C) CDM of the Resilience Domain

The design of this domain is based on [[CRI Phase 2 Methodology]] and [[Approaches of index development - concensus]]. These files give the context of how "indicators" are conceptualized. 

```mermaid
erDiagram

    %% --- INTEGRATION POINTS (Shared with IVRA) ---

    %% These entities are the "Bridge" to the Risk Domain

    SPATIAL_UNIT {

    }

    VULNERABILITY_DETERMINANT {

    }

  

    %% --- DEFINITION LAYER (The Methodology) ---

    %% Defines "National CRI Phase 2"

    RESILIENCE_FRAMEWORK {

    }

  

    %% Defines the axes: "Coping", "Adaptive", "Transformative"

    RESILIENCE_DIMENSION {

    }

  

    %% The semantic map: "Indicator X acts as Capacity Y in this framework"

    FRAMEWORK_STRUCTURE {

    }

  

    %% --- ASSESSMENT LAYER (The Execution) ---

    %% The event of measuring resilience for a place at a time

    RESILIENCE_ASSESSMENT {

    }

  

    %% --- SCORING LAYER (The Recursive Product) ---

    %% The unified entity for all scores (Final Index AND Sub-Dimensions)

    COMPOSITE_INDEX {

    }

  

    %% --- RELATIONSHIPS ---

  

    %% 1. Methodology Definition

    RESILIENCE_FRAMEWORK ||--|{ RESILIENCE_DIMENSION : defines_dimensions

    RESILIENCE_DIMENSION ||--|{ FRAMEWORK_STRUCTURE : defines_logic_for

    VULNERABILITY_DETERMINANT ||--|{ FRAMEWORK_STRUCTURE : provides_variable_for

  

    %% 2. Assessment Context

    RESILIENCE_FRAMEWORK ||--|{ RESILIENCE_ASSESSMENT : governs_logic_of

    SPATIAL_UNIT ||--|{ RESILIENCE_ASSESSMENT : subject_of

  

    %% 3. The Recursive Score Structure

    %% An Assessment generates a set of index scores

    RESILIENCE_ASSESSMENT ||--|{ COMPOSITE_INDEX : generates

  

    %% A Score can be composed of other Scores (Parent -> Child)

    COMPOSITE_INDEX ||--o{ COMPOSITE_INDEX : composed_of

  

    %% 4. Traceability

    %% Linking the generic score back to its specific meaning (e.g., "This is a Coping Score")

    RESILIENCE_DIMENSION ||--o{ COMPOSITE_INDEX : defines_meaning_of

    %% Linking the lowest level score back to the raw data used

    VULNERABILITY_DETERMINANT }|--o{ COMPOSITE_INDEX : feeds_into
```


## D) Expanded Subject Areas (Feb 10 Update)

Based on benchmarking with **A-PLAT (Japan)**, **KLiVO (Germany)**, and **Climate-ADAPT (EU)**, and analysis of DCCE "Orphaned" products (SAR, Eco-School, T-PLAT), the CDM is expanded into three new domains to bridge the "Science-to-Action" gap.

### 1. Adaptation & Response Domain
*Focus: Transforming risk information into fundable projects and tracking implementation.*

- **`ADAPTATION_OPTION`**
    - **Definition:** A library of standardized solutions (e.g., NbS Mangrove Restoration, Early Warning Systems).
    - **Attributes:** Technology Readiness Level (TRL), Sector (NAP-aligned), estimated CBA ratio.
- **`ADAPTATION_PROJECT`**
    - **Definition:** A specific instance of an option applied to a `SPATIAL_UNIT`.
    - **Relationship:** Linked to `RISK_ASSESSMENT` to justify the business case.
- **`FUNDING_SOURCE`**
    - **Definition:** Tracking the origin of capital (Budget, GCF, GEF, Private).

### 2. Activity & Audit Domain (Management Tracking) (not implemented in this phase)
*Focus: Accommodating DCCE management platforms like Eco-School and Green City (SAR).*

- **`MANAGEMENT_PROGRAM`**
    - **Definition:** The high-level initiative (e.g., "National Eco-School Network").
- **`PARTICIPANT_ENTITY`**
    - **Definition:** The school, municipality, or community group enrolled in the program.
- **`AUDIT_RECORD`**
    - **Definition:** The result of a self-assessment or external audit (e.g., SAR scores).
    - **Business Rule:** Allows querying "Risk vs. Preparedness" (e.g., "Show me Eco-School scores in High-Flood-Risk basins").

### 3. Knowledge & Content Domain (not implemented in this phase)
*Focus: Bridging the "Awareness" gap via T-PLAT qualitative content.*

- **`KNOWLEDGE_ASSET`**
    - **Definition:** Qualitative resources (Infographics, Case Studies, Best Practice PDFs).
- **`CONTENT_TAG`**
    - **Definition:** Dynamic semantic links that bind a document to a physical `HAZARDOUS_EVENT` or a `SPATIAL_UNIT`.

```mermaid
erDiagram
    %% --- ADAPTATION & RESPONSE ---
    ADAPTATION_OPTION ||--o{ ADAPTATION_PROJECT : "instantiates"
    ADAPTATION_PROJECT }|--|| SPATIAL_UNIT : "located_at"
    ADAPTATION_PROJECT }|--o| RISK_ASSESSMENT : "addresses"
    ADAPTATION_PROJECT }|--o{ FUNDING_SOURCE : "funded_by"
    
    %% --- ACTIVITY & AUDIT (Management) ---
    MANAGEMENT_PROGRAM ||--|{ PARTICIPANT_ENTITY : "enrolls"
    PARTICIPANT_ENTITY ||--o{ AUDIT_RECORD : "undergoes"
    PARTICIPANT_ENTITY ||--|| SPATIAL_UNIT : "situated_in"
    
    %% --- KNOWLEDGE MANAGEMENT ---
    KNOWLEDGE_ASSET }|--|{ CONTENT_TAG : "classified_by"
    CONTENT_TAG }|..o| HAZARDOUS_EVENT : "references"
    CONTENT_TAG }|..o| ADAPTATION_OPTION : "illustrates"
```



Refinement on 16 Feb
1. Refine Adaptation Planning subject. The current structure is based on ISO 14090
	1. research on ISO 14090, focusing on Adaptation Plan section [[ISO 14090 2019   “Adaptation to climate change — Principles, requirements and guidelines]]
	2. extract "decision-making" space processes and entities from [[Comprehensive Risk Management (CRM) - Full structure]]
	3. analyze common structures 
	4. design a new Adaptation Planning subject
		1. [[Adaptation Planning refinement]] this note contains a summary of what I am thinking

---

# E) Refined IVRA Domain (Feb 25)
### Subject Area 1: Physical Climate (The Cause)
_Focus: From raw observations to drivers._
- **`CLIMATE_DRIVER` (Stressors):** Based on IPCC CID and GCOS ECVs. Attributes include domain (Atmosphere/Land/Ocean), spatial/temporal resolution, and uncertainty estimates.
- **`CLIMATE_SCENARIO`:** Projections (SSP/RCP) from CMIP6 models that simulate drivers.
- **`HAZARDOUS_EVENT` (Shocks):** Discrete occurrences (e.g., a specific cyclone) with WMO-CHE UUIDs.
- **`SATELLITE_OBSERVATION`:** Remote sensing observation capturing hazard extent and supporting observed hazard maps.
### Subject Area 2: Risk & Impact Assessment (The Calculation)
_Focus: The core engine combining Hazard, Exposure, and Vulnerability._
#### 2.1 Hazard Modeling
- **`HAZARD_MODELS`:** The computational engines.
    - _Inputs:_ `CLIMATE_DRIVER`, `METEOROLOGICAL_OBSERVATION`, and static environmental data (`TOPOGRAPHY`, `ENVIRONMENT`).
- **`HAZARD_MAP`:** A spatial representation of hazard intensity that can be **modeled** (from `HAZARD_MODELS`) or **observed** (from satellite-derived historical extent maps).
#### 2.2 Vulnerability & Exposure
- **`SPATIAL_UNIT`:** The geometric foundation (DGGS, HydroBASINS, Admin).
- **`EXPOSED_ASSET`:** Societal elements (Population, Infrastructure) mapped to GED4ALL taxonomies.
- **`VULNERABILITY_DEFINITION`:** The abstract definition of a vulnerability curve or index.
    - **`IMPACT_FUNCTION`:** Math-based (e.g., Depth-Damage curves) for actuarial calculations.
    - **`VULNERABILITY_FRAMEWORK`:** Indicator-based (e.g., Social Vulnerability Index) for policy scoring.
        
- **`FRAMEWORK_STRUCTURE`:** The logic layer mapping a generic variable to a specific framework dimension (e.g., mapping "Poverty Rate" to "Sensitivity").
    
- **`VULNERABILITY_DETERMINANT`:** A neutral library of social/economic indicators used as variables.
#### 2.4 Risk Assessment Outputs
- **`RISK_ASSESSMENT`:** The event of running a calculation that can be **physical** (via `HAZARD_MAP`) or **index-based** (via `CLIMATE_DRIVER`).
- **`RISK_METRIC`:** Probabilistic, quantitative outputs (e.g., Average Annual Loss) derived from `IMPACT_FUNCTION`.
- **`COMPOSITE_INDEX`:** Qualitative or normalized scores (1-10) derived from `VULNERABILITY_FRAMEWORK`.
#### 2.5 Impact (Loss & Damage)
- **`DISASTER_RECORD`:** A single observed occurrence of a disaster event with summary statistics (affected population/assets, duration, total losses).
- **`LOSS_DAMAGE_RECORD`:** Historical data on actual impacts sustained by assets.
- **`ATTRIBUTION_LINK`:** An aggregated attribution summary linked to a `LOSS_DAMAGE_RECORD` and `CLIMATE_DRIVER`. This entity might be ahead of time but included for the sake of logical consistency. 
    
### Key Decisions (2026-02-25)
1. **Dual-path Risk Assessment (Physical + Index-Based)**
   - **Decision:** `RISK_ASSESSMENT` can reference `HAZARD_MAP` (physical modeling) and/or `CLIMATE_DRIVER` (index-based assessment).
   - **Reason:** Keeps a single assessment structure while supporting both hazard-extent modeling and climate-index workflows without duplicating schema.

2. **Observed vs Modeled Hazard Maps**
   - **Decision:** `HAZARD_MAP` can be produced by `HAZARD_MODELS` or derived from `SATELLITE_OBSERVATION` (subtypes can remain implicit).
   - **Reason:** Reflects real practice where historical hazard extents are compiled from satellite imagery while future scenarios are modeled outputs.

3. **Loss-Driven Attribution**
   - **Decision:** `ATTRIBUTION_LINK` attaches only to `LOSS_DAMAGE_RECORD` as an aggregated attribution summary; no direct event/driver attribution.
   - **Reason:** Attribution is only defensible when loss evidence exists; avoids speculative causal links without impact data.

4. **Disaster Record Definition**
   - **Decision:** `DISASTER_RECORD` represents a single observed occurrence with summary statistics (1:1 with `HAZARDOUS_EVENT`).
   - **Reason:** Maintains a clean event registry while allowing separate, granular loss entries via `LOSS_DAMAGE_RECORD`.