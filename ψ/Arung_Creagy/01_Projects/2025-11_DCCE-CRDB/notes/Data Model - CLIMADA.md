---
status: current
tags:
  - data_model
created: 2026-01-14
last_updated: 2026-01-14
AI_prompt: false
project:
  - DCCE_CRDB
type:
  - Artifact
---
>[!summary] structured arundprobabilistic risk assessment framework

In the CLIMADA (CLIMate ADAptation) architecture, the data model is fundamentally structured around a probabilistic risk assessment framework that implements the "risk triangle": the intersection of hazard, exposure, and vulnerability,. 

As a data architect would observe, the system is built on a modular logical model where risk is quantified as the product of probability and severity,.

The key data domains and their constituent entities are detailed below:
# Data domain
### 1. The Hazard Domain

This domain encompasses the spatiotemporal definition of dangerous phenomena.

- **Key Entity: `Hazard`**: Represents probabilistic event sets (both historical and synthetic),. It is characterized by **centroids** (geographical points where the hazard has defined values), **intensity** (e.g., wind speed, flood depth), and **frequency** (the probability of occurrence, often expressed as return periods),,.
- **Key Attributes**: `event_id`, `intensity` (often stored as a sparse matrix), `frequency`, and `centroids`,.

### 2. The Exposure Domain

This domain defines the "assets at risk" within the research area.

- **Key Entity: `Exposures`**: A georeferenced dataset, typically implemented as a `GeoPandas.GeoDataFrame`, representing the goods, people, or infrastructure susceptible to hazard impacts,,.
- **Sub-Entities/Modules**: Includes specialized types such as **LitPop** (disaggregating value based on nightlight intensity and population count), **BlackMarble**, or custom user-defined points and rasters,,.
- **Key Attributes**: `latitude`, `longitude`, `value` (monetary or population count), and `geometry`,.

### 3. The Vulnerability Domain

This domain mediates the relationship between hazard intensity and exposure damage.

- **Key Entity: `ImpactFunc` (formerly Vulnerability Function)**: A mathematical cumulative distribution function that relates a specific hazard's intensity to a percentage of damage or "mean damage degree" (MDD) for an asset category,,.
- **Entity: `ImpactFuncSet`**: A container object that maps specific exposure categories to their corresponding impact functions for a given hazard type,.

### 4. The Risk & Impact Domain

This domain captures the results of the probabilistic convolution of the previous three domains.

- **Key Entity: `Impact`**: The primary output object representing the combined effect of hazards on exposures mediated by impact functions.
- **Key Attributes**:
    - **`imp_mat`**: A `sparse.csr_matrix` (num_events x num_exposures) providing a high-resolution, geographically resolved record of damages,.
    - **Metric Attributes**: Includes **AAI** (Average Annual Impact), **EAI** (Expected Annual Impact per exposure location), and **at_event** (summed impact per hazard event),,.

### 5. The Adaptation & Appraisal Domain

Aligned with Phase 7 of the ECA methodology, this domain focuses on mitigating identified risks,.

- **Key Entity: `Measure`**: Defines a specific climate change adaptation (CCA) intervention (e.g., seawalls, green infrastructure, or building codes),.
- **Key Entity: `MeasureSet`**: A collection of adaptation options used to perform Cost-Benefit Analysis (CBA),.
- **Key Attributes**: Implementation **cost**, **risk-reduction potential** (modeled as a shift in the hazard intensity or the impact function), and **saved persons** or **averted damage**,,.

### 6. The Container/Management Domain

- **Key Entity: `Entity`**: A master container class used in complex projects to aggregate `Exposures`, `ImpactFuncSet`, `MeasureSet`, and `DiscRates` (discount rates for net present value calculations) into a single object for analysis,,.