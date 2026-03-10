
- **Date:** February 23, 2026
- **Interviewee Name/Title:** Three representatives assigned as the environmental coordination sub-team
- **Department:** Economic Statistics Division
- **Agency:** National Statistical Office (NSO)
- **Interviewer:** Sittichat (Crygy Consulting Team for DCCE)
    

# **1. Role and Responsibility of the Agency**

- **Key duty and roles:**
    - Acts as the country's primary source for baseline data production (e.g., Population and Housing Census, Agricultural Census, Industrial Census, Labor Force Survey, and Socio-Economic Survey) .
        
    - Serves as the central agency managing the national statistical data system under a decentralized framework .
        
    - Reviews and catalogs statistical lists to determine which agency produces specific datasets, tracks the frequency of publication, and verifies if data is hosted on agency websites or the Government Data Catalog (GD Catalog) .
        
    - **International Data Focal Point:** Acts as the primary gateway for international data requests. When international organizations require national datasets, NSO coordinates with relevant domestic agencies, consolidates the information into a single official national dataset, and submits it to fulfill these international obligations .
        
    - Currently, NSO lacks a dedicated environmental division; therefore, environmental coordination is managed by a three-person sub-team within the Economic Statistics Division.
        
- **Associated legal frameworks:**
    
    - Operates under the Statistics Act B.E. 2550 (2007).

    - The Act mandates strict privacy protections, prohibiting the disclosure of individual-level data that can be traced back to the informant .
        
    - The Act provides NSO the statutory right to request data from any government agency for statistical compilation.
        

# **2. Highlighted Key Projects**

- **Framework for the Development of Environment Statistics (FDES):**
    
    - _Status:_ The statistical list is nearly complete but is currently pending Cabinet approval, which has been delayed due to the government formation period .
        
    - _Scope:_ Adapted from UN guidelines to fit the Thai context. It contains 6 main components (e.g., Environmental conditions, Extreme events and disasters, Human settlements) and 21 sub-components .
        
    - _Committee Approval Process:_ The approval of required statistics goes through Sectoral Statistical Committees (divided into Economic, Social, and Environmental branches). The environmental sub-committee invites relevant agencies to evaluate existing data, categorizes them into tiers (Tier 1: published regularly, Tier 2: internal use, Tier 3: not yet produced), and officially assigns the responsible production agency .
        
- **Natural Resources and Environment Statistical Data Center:**
    - _Status:_ Currently under development by the Economic Statistics Division .
    - _Scope & Exclusions:_ Aims to be a central hub. If data is on the GD Catalog, it is pulled directly. If data is only hosted on an agency's website, NSO strictly links to the source URL rather than copying the raw data .
    - _Data Tagging System:_ Utilizes a centralized tagging system for data management. Datasets pulled from various agencies are tagged according to standardized frameworks (like FDES). This allows users to discover the same dataset (e.g., solid fuel usage) through multiple thematic search angles .
        
- **SDG Monitoring Support:**
    - _Status/Scope:_ NSO provides methodological support for calculating indicators . The NESDC currently leads tracking via the eMENSCR system, requiring departments to report budget usage against SDG progress .
        
- **Common Frame Database:**
    - _Scope & Integration:_ Integrates nationwide establishment/enterprise data down to the sub-district level . Merges data from over 10 agencies (e.g., Dept. of Business Development, Dept. of Industrial Works) to capture the number of accommodations, restaurants, and manufacturing plants per area .
        

**3. Current Workflow & Data Usage**

- **Context, Hazard Scope, and Data Sources:**
    
    - NSO relies heavily on primary surveys. For example, the Labor Force Survey collects data from approximately 20,000 households (~100,000 people) per month .
        
    - _Cascading Impacts & Disaster Workflow:_ During hazard events (e.g., floods in Hat Yai), NSO overlays basic census data (population, agriculture, establishments) onto DDPM’s declared disaster areas at the sub-district level to calculate the volume of affected people and properties .
        
- **Modeling techniques and data granularity:**
    
    - _Enumeration Area (EA):_ The smallest spatial unit utilized by NSO. An EA consists of a single village or a maximum of approximately 250 buildings . High-density areas (like 30-story condos) are split into multiple EAs to ensure a surveyor can complete data collection within 1-2 days .
        
    - _Population Metric Nuance:_ Unlike the Ministry of Interior's civil registration (based on birth registry), NSO measures "actual residence" (e.g., counting individuals working in Bangkok rather than their registered home province) for accurate infrastructure planning .
        
    - _Spatial Degradation:_ Deep financial attributes in business censuses are only statistically viable and published at the provincial level due to sampling constraints, while basic attributes go down to the sub-district level .
               
- **Data Sharing, QA, and Quality Evaluation:**
    
    - _Capacity Building for Quality Assurance:_ To ensure data quality on the GD Catalog, NSO actively performs capacity building for responsible agencies. They educate them on the required data structures, standard formats for data exchange, and the necessity of attaching comprehensive metadata (revision frequency, definitions, project tags) before data can be uploaded .
        
    - _Statistics Quality Evaluation (GSBPM):_ NSO conducts continuous statistics quality evaluation using the Generic Statistical Business Process Model (GSBPM) . Before initiating or renewing any routine survey (even those done every 3-5 years), NSO thoroughly reviews the actual demand and utility of the data with relevant user agencies to ensure the collected statistics still provide public value and justify the budget .
        

**4. Climate Data Needs & Gaps**

- **Gaps in projections, baseline indicators, and standardizations:**
    - NSO currently has no direct environmental surveys; they rely on proxy questions embedded in existing surveys (e.g., solid fuel usage in the SES) .
        
    - International standard gaps (e.g., SDGs) often require proxy indicators because global metrics (like those for landlocked or snow-dependent nations) do not align with Thailand's physical context .
        
- **Severe budgeting or policy roadblocks:**
    - _Capacity Constraints:_ NSO provincial offices operate with only ~20 staff handling 20-30 projects monthly . To increase survey granularity to the district/sub-district level, the sample size would need to scale exponentially, drastically exceeding current manpower and budget limits .
        
    - _Budget Justification:_ Conducting a national census requires massive budgets. NSO struggles to justify budgets for single-agency use cases unless there is demonstrable "value added" and severe negative impacts of not collecting the data .
        
    - _IT Infrastructure:_ Utilizing hundreds of thousands of volunteers for concurrent digital data collection frequently overloads and crashes central servers . Rural internet blackspots also necessitate paper-based surveys .
        
    - _Legal Roadblocks:_ NSO's statutory right to request inter-agency data often collides with the privacy laws of data-holding agencies (e.g., Revenue Dept., Dept. of Provincial Administration) . This hierarchy-of-law conflict requires lengthy MOUs to resolve .
        
- **Specific requests for DCCE intervention / policy recommendations:**
    - NSO recommends that DCCE models incorporate granular agricultural vulnerability indicators from the Agricultural Census . These include household debt levels, debt repayment status, ownership of agricultural assets (e.g., tractors), and land tenure status (owned vs. rented) to improve model accuracy .
        

**5. Next Steps & CRDB Integration**

- **Map findings directly to CRDB Implementation Plan:**
    
    - The NSO's Natural Resources and Environment Statistical Data Center can serve as a prime node to catalog CRDB's future climate risk and adaptation datasets .
        
    - CRDB will share the resulting conceptual data structure and baseline mappings with NSO, linking them to FDES and the broader official statistics ecosystem.
        
- **Seed use cases for WP3 Conceptual Data Model / WP4 Data Catalog:**
    
    - _Exposure Mapping:_ DCCE can leverage the "Enumeration Area" (EA) logic (blocks of ~250 buildings) to vastly improve the spatial resolution of the risk map's exposure layer .
        
    - _Vulnerability Indices:_ Utilize the Common Frame database to assess Human Settlement vulnerability , and integrate the recommended Agricultural Census indicators (debt, asset ownership) into agricultural risk modeling .
        
    - _Economic Loss Modeling:_ Tap into the Ministry of Tourism and Sports' tourism accounts for deep-dive economic vulnerability, as suggested by NSO .
        
- **Planned participation in workshops:**
    
    - NSO is invited and confirmed their willingness to participate in the upcoming Public Hearing event in April to provide feedback on the draft CRDB platform, NCAIF structures, and user data needs .