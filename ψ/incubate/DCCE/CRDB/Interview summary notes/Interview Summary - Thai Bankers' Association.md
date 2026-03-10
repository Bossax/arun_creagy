

**Date:** 26 Feb 2026

**Interviewee Name/Title:** Representatives from KBank, Krungsri Bank, and SCB **Department:** Various Risk and Data Analytics Departments 
**Agency:** Thai Bankers' Association (TBA) / Commercial Banks

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** Commercial banks are responsible for managing financial portfolios, assessing financial exposure to physical and transition climate risks, and proposing disaster risk reduction (DRR) measures to their clients.
    
- **Associated legal frameworks:** The banks operate under the Bank of Thailand (BoT) regulatory framework, which will soon include climate stress testing within their Internal Capital Adequacy Assessment Process (ICAAP) standard.
    

### 2. Highlighted Key Projects

- **BoT Physical Risk Analysis & Stress Testing:** * _Status & Scope:_ Active/Development. Banks are analyzing their portfolio exposure to satisfy BoT's physical risk analysis framework.
    
    - _Data Integration & Lifecycle:_ While the framework and stress testing methodologies are common across the banking sector, the actual data sources used to satisfy them vary significantly depending on each bank's internal capacity. The BoT currently relies on the 2011 Thailand flood event as a baseline scenario guideline.
        

### 3. Current Workflow & Data Usage

- **Context, Hazard Scope, and Data Sources:** The primary physical hazard focus is flooding. Banks currently procure disaster data from the DDPM, and hydrological hazard/risk data from the Hydro Informatics Institute (HII). For example, KBank is registered as a data provider with HII and utilizes their repeated flooded zone maps, current/near-future runoff forecasts, and CMIP5 future flood scenarios. They also noted that the BMA relies on GISTDA spatial data for their own independent pipelines.
    
- **Modeling Techniques and Granularity:** Banks require highly specific asset-level data; provincial-level data is entirely insufficient for their financial modeling. They strongly prefer probabilistic maps over basic index maps. Their specific hydrological modeling needs include the probability of flooding at specific locations, multi-modal flood tracking (pluvial, riverine, and coastal), and precise metrics on flood depth and duration.
    
- **Inter-agency Collaborations & Cascading Impacts:** Banks are highly concerned with how direct physical risks trigger secondary cascading impacts, specifically supply chain disruptions, in order to advise corporate clients on holistic risk reduction.
    

### 4. Climate Data Needs & Gaps

- **Projections, Baselines, and Standardizations:** * _Damage Functions:_ There is a severe gap in risk quantification regarding damage functions. Banks currently rely on macro/generic regional studies, which are not precise enough for asset-level financial modeling.
    
    - _Transition Risk:_ There is a lack of clear guidance and numeric Long-Term Low Emission Development Strategy (LT-LEDS) pathways down to the sub-sector level. Banks also struggle to map the International Standard Industrial Classification (ISIC) codes to actual domestic industrial operations.
        
    - _Stress Testing:_ The scenarios provided for stress testing lack clear definitions.
        
- **Roadblocks & Uncertainty Handling:** There is a major roadblock regarding how analysts handle data uncertainty. When using a 100-year probabilistic flood map for the entire country, analysts often overestimate the financial impact by treating the probabilistic map as a deterministic one (i.e., assuming the 100-year flood happens everywhere simultaneously in a single year). There is an urgent need to educate analysts and standardize uncertainty handling for climate risk assessments.
    
- **Specific Requests for DCCE:** Informants explicitly stated that foundational datasets are severely needed and _must_ be provided by the DCCE as a central, accessible data repository. This would eliminate the need for banks to procure refined data from third-party providers. They requested that risk maps ideally be categorized or presented as asset type-aggregates.
    

### 5. Next Steps & CRDB Integration

- **Map to Implementation Plan:** The banks' struggle to map ISIC codes to real-world operations and their need for standardized damage functions perfectly validate the requirement for the NCAIF Business Taxonomy (WP3). Furthermore, their urgent request for a central repository directly supports the development of the Spreadsheet Data Catalog (WP4).
    
- **Seed Use Cases for WP3 Conceptual Data Model (CDM):** _Scenario:_ "Conducting an ICAAP stress test on a commercial loan portfolio using asset-level probabilistic flood maps (depth/duration) and standardized damage functions to quantify financial exposure and secondary supply chain disruptions.". This will heavily inform the attributes required for the `Impact_Assessment` and `Loss_Damage_Record` entities.
    
- **Inputs for WP4 Data Catalog:** HII's repeated flooded zone maps and CMIP5 future flood scenarios (as used by KBank) should be immediately logged in the Baseline Data Inventory.