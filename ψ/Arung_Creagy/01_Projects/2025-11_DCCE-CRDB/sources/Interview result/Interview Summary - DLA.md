
**Date:** 20/2/2569 (February 20, 2026) 
**Interviewee Name/Title:** Representatives including Head of Section and Director 
**Department:** Environmental Division and the newly established Disaster Prevention and Mitigation Division 
**Agency:** Department of Local Administration (DLA / สถ.)

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** DLA acts as a promoter, advisor, and supporter for Local Administrative Organizations (LAOs / อปท.) nationwide, rather than a direct command authority. Their main climate-related missions historically focus on solid waste management and public health, but they are currently working to integrate climate change, greenhouse gas reduction, and circular economy principles into local operational plans.
    
- **Associated legal frameworks:** DLA sets standard guidelines and criteria for LAOs to follow. They recently established a new Disaster Prevention and Mitigation Division specifically to handle disaster relief, security, and to streamline the regulations that dictate how local funds can be deployed during emergencies.
    

### 2. Highlighted Key Projects

- **DLA Waste Platform:**
    
    - _Status & Scope:_ Active. A central system where LAOs input basic waste data (generation volume, collection rates, waste composition like organics vs. recyclables) to track local waste trends.
        
    - _Exclusions/Constraints:_ The data is not perfectly real-time and heavily depends on how fast and accurately individual LAOs input their numbers.
        
    - _Data Integration:_ Individual LAOs can only see their own data, while DLA sees the consolidated national overview.
        
- **Local Performance Assessment (LPA):**
    
    - _Status & Scope:_ Active. DLA evaluates LAOs across five main dimensions (including public service, environmental management, and disaster readiness) to ensure they meet basic legal standards.
        
    - _Future Lifecycle:_ High scores on the LPA act as a direct incentive, as they are used to justify annual bonus budget allocations for the LAOs.
        
- **Climate Standard Guidelines:**
    
    - _Status & Scope:_ Drafting/Publishing. DLA is issuing two new guideline books—one for climate change adaptation and one for GHG reduction—to introduce baseline concepts to local governments.
        

### 3. Current Workflow & Data Usage

- **Context and Hazard Scope:** The focus is largely on waste management, PM 2.5, droughts, and floods.
    

- **Data Sources:** For demographic data, DLA pulls open data from the Department of Provincial Administration (DOPA) to calculate waste metrics, but this is done manually rather than via an automated API. For hazard data, LAOs must hunt for information themselves from specialized agencies like the DDPM or TMD.
    

- **Modeling Techniques and Granularity:** DLA evaluates data at the national and provincial levels, while LAOs need data granular enough to see their own exact municipal or sub-district boundaries to plan local projects.
    
- **Inter-agency Collaborations:** DLA operates through its provincial offices, which act as the frontline to answer questions from local LAOs regarding legal or budget constraints.
    

### 4. Climate Data Needs & Gaps
- **Projections and Baselines:** Most local governments lack any systematic collection of climate or environmental data, unless they are participating in specific initiatives like the "Clean City" competition. They desperately need localized hazard projections to know exactly what risks to plan for in their annual budgets.
    
    
- **Standardizations & Roadblocks:**
    - _Severe Budgeting Constraints:_ The central government does not typically provide direct disaster relief budgets to LAOs. When a disaster strikes, LAOs are forced to drain their own "accumulated funds" (เงินสะสม) to buy supplies like sandbags or relief kits, which leaves them financially depleted for future years.
        
    - _Data Fragmentation:_ Hazard data is scattered, forcing LAOs to guess which agency's data to use for their local planning.
        
- **Specific Requests for DCCE:** * Provide a centralized, easy-to-digest data repository that LAOs can directly reference to quickly justify budget approvals for resilience projects.
    
    - Provide tools or indicators that can prove the cost-effectiveness and ROI of climate interventions (e.g., how a specific project lowers risk or GHG emissions).
        
    - Link climate risk data directly to the national e-MENSCR system so that local, provincial, and national plans align seamlessly.
        

### 5. Next Steps & CRDB Integration

- **Map to CRDB Implementation Plan:** DLA's request for an easy-to-digest, centralized data hub strongly validates the core purpose of the WP4 Spreadsheet Data Catalog. Providing a single source of truth will eliminate the friction LAOs face when searching for data to justify local budgets.
    
- **Seed Use Cases for WP3 Conceptual Data Model (CDM):** * _Scenario:_ "Linking mapped local climate risks directly to a municipality's Annual Budget Ordinance (เทศบัญญัติรายจ่าย) to justify the deployment of Accumulated Funds (เงินสะสม) for proactive disaster mitigation." This will inform the relationship between `Hazard_Exposure`, `LAO_Entity`, and `Budget_Allocation` in the CDM.
    
- **Planned Participation:** DLA specifically requested that DCCE expand the invitation list for the April Public Hearing to include four key municipal associations: The National Municipal League of Thailand, Subdistrict Administrative Organization Association, Provincial Administrative Organization Association, and City Municipality Association.
    
