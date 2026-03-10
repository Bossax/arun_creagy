---
status: evergreen
tags: []
created: 2026-01-14
last_updated: 2026-01-14
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type:
  - Artifact
sticker: emoji//1f5d2-fe0f
---
>[!note] 
>Analysis of the interview notes from UNDP project. These interviews were conducted with line agency representatives to understand their climate services, data products, and the use cases of their products and their needs.
# Use cases
from key stakeholders—including technical agencies (GISTDA, TMD), research bodies (PIER, RU CORE), and disaster management authorities (DDPM, ADPC).

The following are the shared use case themes that emerge as critical requirements for the proposed data architecture:

### 1. Smart Agricultural Planning and Food Security

This is the most dominant use case across multiple informants, requiring high-resolution temporal data.

- **Crop Simulation & Monitoring:** Agencies utilize satellite and in-situ data to track growth cycles and health for economic crops like rice, maize, and sugarcane. TMD specifically operates "Climate Field Schools" that integrate weather data (rain, humidity, sunlight) with crop and soil models to simulate optimal planting solutions.
- **Yield & Damage Assessment:** Informants use simulation models to estimate potential damage to agricultural yields under different climate scenarios, comparing outcomes with and without adaptation measures.
- **Risk Mitigation:** The goal is to help farmers plan cultivation in alignment with changing climate patterns to reduce risk while maintaining or increasing productivity.

### 2. Integrated Water Resource Management (IWRM)

The system must support complex hydrological modeling to manage both scarcity and surplus.

- **Hydrological Modeling:** Use cases involve dividing areas into river basins to study the water cycle—analyzing how rainfall translates into surplus or deficit. This includes monitoring reservoir levels and planning water allocation during dry seasons.
- **Flood and Drought Mapping:** Informants like RU CORE and GISTDA focus on developing risk maps for flood and drought, often using downscaled climate projections (e.g., CORDEX SEA) to understand future impacts.
- **Transboundary Analysis:** Some projects, such as those by ADPC and RU CORE, focus specifically on the Mekong River basin, requiring cross-border data integration.

### 3. Urban Resilience and Infrastructure Planning

Architecture must accommodate "micro-scale" data to serve urban decision-makers.

- **Urban Heat and Air Quality:** There is a shared focus on "Integrated Urban Services" (IUS) that monitor heat islands and air quality (specifically PM2.5) to improve urban health.
- **Sub-City Modeling:** TMD and ADPC emphasize the need for high-resolution data at the sub-city level to model urban floods and the impact of the built environment on climate risks.
- **Mainstreaming into Land Use:** A critical use case is integrating climate risk data into provincial land-use planning to prevent the construction of housing in flood-prone areas.

### 4. Disaster Risk Reduction (DRR) and Early Warning

This theme bridges the gap between historical response and future-oriented preparedness.

- **Near Real-Time Monitoring:** Systems like GISTDA’s disaster portal provide near real-time tracking of active hazards such as forest fires and floods to support immediate evacuation and rescue operations.
- **Multi-Hazard Early Warning Systems (MHEWS):** Informants are moving toward integrated systems that provide not just weather alerts, but actionable risk communication for various disasters.
- **Bridging CCA and DRR:** A key objective is integrating future climate scenarios into current hazard assessments to move from short-term response to long-term "anticipatory" planning.

### 5. Economic Impact and Loss Assessment

From an architecture perspective, this requires linking physical hazard data to socio-economic financial layers.

- **Monetizing Risk:** PIER and ADPC focus on translating physical climate impacts into monetary terms (Loss and Damage) to make climate adaptation more attractive to policy-makers.
- **Budget Tagging:** Use cases involve tracking government spending on climate and disaster activities (budget tagging) to evaluate the cost-effectiveness of investments.
- **Insurance and Finance:** There is an emerging need for data that supports disaster insurance products, particularly for the agricultural sector.

### 6. Environmental and Ecosystem Monitoring

Monitoring the "Biosphere" is essential for nature-based solutions.

- **Coastal and Marine Management:** GIZ and GISTDA monitor coastal erosion, sea surface temperature, and mangrove health to support coastal adaptation planning.
- **Greenhouse Gas (GHG) Tracking:** Use cases include monitoring "green spaces" and forest cover to calculate carbon sequestration and methane emissions from agricultural fields.

### Summary for System Design

To serve these use cases, the data system must transition from providing "raw data" to "analytic data". It must move beyond a "siloed" approach by creating a centralized hub or standardized data catalog that allows for interoperability between climate variables (TMD, GISTDA) and socio-economic indicators (NSO, DDPM).

---

# Data domains

As a data engineer and architect designing a high-performance system for climate risk assessment, I have synthesized the information from the sources to identify the core data domains and their respective entities. To serve real-world use cases—such as national adaptation planning (NAP) and disaster risk reduction (DRR)—the architecture must move beyond storing raw data and instead facilitate the integration of physical climate hazards with socio-economic vulnerability layers.

Based on the UNFCCC framework and the specific use cases shared by informants like GISTDA, TMD, and ADPC, the following data domains and entities are inferred:

### 1. Observational Data Domain (The Ground Truth)

This domain captures the current state of both the physical environment and the human systems occupying it. It serves as the "baseline" for all risk calculations.

- **Climate & Physical Entities:**
    - **Essential Climate Variables (ECVs):** Atmospheric, terrestrial, and oceanic variables collected via in-situ or remote sensing.
    - **Satellite/Earth Observation (EO) Data:** High-resolution imagery used for tracking green spaces, forest cover (GFMS), and marine ecosystems (sea surface temperature, chlorophyll-a).
    - **Hydrological Observations:** Rainfall, water cycle parameters (surplus/deficit), and reservoir levels monitored by agencies like HII.
    - **Near Real-Time Disaster Layers:** Active monitoring of forest fires, floods, and air quality indices (PM2.5).
- **Socio-economic & Exposure Entities:**
    - **Land Use and Land Cover:** Detailed mapping of economic crops (rice, maize, sugarcane, etc.) and urban built environments.
    - **Demographics:** Population data disaggregated by sex, age, and income, primarily sourced from national census data.
    - **Public Health Data:** Specifically, patient records linked to environmental hazards like PM2.5 to understand impact-based health risks.

### 2. Projected Data Domain (The Future Outlook)

This domain is characterized by simulation and uncertainty. It is essential for "anticipatory" planning rather than just reactive response.

- **Climate Model Entities:**
    - **Global & Regional Climate Models (GCMs/RCMs):** Large-scale projections (e.g., CMIP6, CORDEX SEA) that provide downscaled temperature and precipitation data at resolutions as fine as 5 km for specific regions like the Mekong.
    - **Climate Predictions:** Seasonal to decadal forecasts used specifically for agricultural planning and water management.
- **Hazard Projection Entities:**
    - **Future Hazard Maps:** Simulated 100-year flood maps or drought indices derived from climate scenarios like RCP8.5.
    - **Scenario Assumptions:** Radiative forcing pathways (RCPs) and Shared Socio-economic Pathways (SSPs) that define the "what-if" parameters of the models.
- **Socio-economic Projection Entities:**
    - **Macroeconomic Trends:** Future GDP and sector-specific economic developments (though these are often fragmented and not yet fully aligned with climate SSPs).

### 3. Historical Data Domain (The Contextual Baseline)

This domain provides the evidence required to validate models and understand the sensitivity of systems to past extreme events.

- **Historical Climate Entities:**
    - **Climatological Normals:** Long-term averages (e.g., 30-year records) used to identify patterns, frequency, and intensity of past hazards.
    - **Archival Records:** Digitized or paper-based records of sub-daily extreme weather events.
- **Impact and Loss Entities:**
    - **Disaster Statistics:** Historical records of event frequency and spatial extent.
    - **Damage and Loss (D&L) Records:** Data on affected assets and government compensation figures. _Note: Architecturally, this is a known gap; current databases often reflect compensation caps rather than actual economic loss._

### 4. Risk and Vulnerability Domain (The Analytic Layer)

From an architectural perspective, this is a "computed" domain where the system integrates data from the other three domains to produce actionable insights.

- **Risk Entities:**
    - **Risk Maps:** Multi-hazard maps that combine hazard, vulnerability, and exposure (Risk = Hazard x Vulnerability x Exposure).
    - **Vulnerability Indices:** Composite indicators representing social, physical, environmental, and economic susceptibility.
- **Economic Impact Entities:**
    - **Monetized Loss Estimates:** Models that translate physical damage (e.g., crop yield loss) into monetary value to inform policy-makers and budget tagging.
    - **Adaptive Capacity:** Indicators reflecting the ability of a community or sector to adjust to climate change.

### Engineering Implications for the Data Model

To serve the shared use cases effectively, the system must support **spatial-temporal indexing** across all domains. For instance, an "Urban Resilience" use case requires overlaying **High-resolution Sub-city Climate Projections** (Domain 2) with **Urban Land Use and Population Density** (Domain 1) to generate a **Future Heat Risk Map** (Domain 4).

Furthermore, the architecture must transition from a "Project-based/Siloed" model to a "Centralized Data Catalog" (as suggested by BDI and GIZ) to ensure data continuity and interoperability between technical agencies (TMD, GISTDA) and implementing agencies (DDPM, Ministry of Agriculture).