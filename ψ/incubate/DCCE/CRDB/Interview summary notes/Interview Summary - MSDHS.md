**Date:** 17/2/2569 (February 17, 2026) 
**Interviewee Name/Title:** Representatives from the Policy Development Division, Data Analysis Group (Technology Center), Statistician, Social Standard Expert, and Social Developer 
**Department:** Office of the Permanent Secretary **Agency:** Ministry of Social Development and Human Security (MSDHS / พม.)

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** The core mission is to develop society, build human capacity, and create opportunities to improve the overall quality of life. The ministry acts as both a policy regulator and a direct practitioner. While some policies target the general public, their primary focus is providing special care and welfare for specific vulnerable populations.
- **Associated legal frameworks:** The agency's institutional duties include drafting the annual social situation report, setting social standards, managing social welfare distribution, and drafting provincial social development plans.
### 2. Highlighted Key Projects

- **Vulnerable Group Management Center (สปก.):** * _Status & Scope:_ Active, established in FY 2025. It manages disaster care for vulnerable groups and coordinates funding distribution to 76 provincial offices (พมจ.) and 11 academic promotion centers.
    
- **"Teacher Kor" (ครู ก.) Disaster Readiness Training:**
    - _Status & Scope:_ Active. In FY 2025, they trained over 43,000 personnel (MSDHS staff and local partners) on disaster readiness and evacuation protocols. In FY 2026, the scope expands to train vulnerable individuals directly, targeting at least 200 people per province (approx. 15,000-20,000 total).
        
        
- **World Bank Collaboration:** * _Status & Scope:_ Active (FY 2024-2025). The World Bank, alongside Ajarn Pongsak from Chulalongkorn University, helped MSDHS map risk areas against vulnerable populations in pilot areas like Chiang Mai, Korat, and Pattani.
    
    - _Integration & Future Lifecycle:_ A second component with Chula Demography analyzes specific climate impacts on vulnerable groups, with results presenting in Feb 2026. This includes a joint disaster integration plan with the Ministry of Interior, Ministry of Natural Resources and Environment, and Ministry of Transport.
### 3. Current Workflow & Data Usage

- **Context and Hazard Scope:** Climate change is a very new topic for the ministry, having only gained traction over the last two years. Their focus is heavily weighted toward disaster response (floods, droughts, heatwaves, landslides, and PM2.5) rather than long-term adaptation.
- **Data Sources:** They rely entirely on secondary open data for hazards: GISTDA (heat spots via API), TMD (temperature), LDD (drought), ONWR (water), and DDPM (historical disasters). Vulnerable group data comes from their own welfare registries, field surveys, and external data like the Ministry of Interior's civil registry (linked via 13-digit ID).
    
- **Modeling Techniques and Granularity:** Their main technique is spatial overlay, combining hazard maps with vulnerable population locations. Their internal data is kept at the individual/household level but is published on dashboards at the sub-district (ตำบล) level.
    
- **Inter-agency Collaborations & Cascading Impacts:** The Technology Center acts as the data hub, converting raw data into dashboards for executives (who use them on iPads during field visits) and provincial offices. During crises, they share detailed personal data with local authorities and health departments to execute physical evacuations.
    

### 4. Climate Data Needs & Gaps

- **Projections and Baselines:** The agency only has historical, annual statistical data; they completely lack predictive forecasts. They critically need data broken down to the sub-district (ตำบล) and municipality (เทศบาล/อปท.) levels, because municipalities are the actual entities holding the budgets for local relief.
    
- **Standardizations & Roadblocks:** * _Data Governance:_ There is no central data catalog, causing staff to waste time hunting across multiple websites. Datasets lack technical metadata or data dictionaries, forcing staff to call source agencies (like DDPM) just to understand how to read the data.
    
    - _Resources:_ They have zero data scientists and no dedicated IT infrastructure for climate data; they run heavy spatial queries on servers meant for basic welfare administration. Furthermore, they have no dedicated budget for disaster relief supplies, relying entirely on donations or ad-hoc provincial funds.
        
    - _Policy Disconnect:_ Local field staff and trainers often cannot differentiate between "Disaster" and "Climate Change". Additionally, DCCE initially excluded MSDHS from the National Adaptation Plan (NAP) drafting process, focusing the Human Settlement sector primarily on the Ministry of Interior instead.
        
- **Specific Requests for DCCE:** * DCCE must establish clear, standardized social indicators for the NAP's Human Settlement sector.
    
    - Highly granular impact data: They need to know exactly how specific hazards impact specific subgroups (e.g., children vs. elderly vs. the 7 types of disabled persons).
    - Gender and Equality: The Department of Women's Affairs needs data to plan gender-inclusive shelters, safe bathrooms, and specific protocols for pregnant women and LGBTQ+ individuals during disasters.
    - Relocation Timelines: They need 2-5 year habitability forecasts (e.g., "This area will be permanently flooded") to proactively plan community relocations and occupational retraining.
        

### 5. Next Steps & CRDB Integration

- **Map to CRDB Implementation Plan:** The overwhelming pain point regarding scattered data and absent metadata validates the core need for the Spreadsheet Data Catalog and Technical Data Dictionaries (WP4). The local confusion between weather events and climate change proves the necessity of the NCAIF Business Glossary (WP3).
    
- **Seed Use Cases for WP3 Conceptual Data Model (CDM):** * _Scenario 1:_ Assessing habitability timelines (2-5 year projections) for vulnerable agricultural communities to trigger early occupational retraining and relocation planning.
    
    - _Scenario 2:_ Mapping flood risk down to the municipality (เทศบาล) level to match specific exposed subgroups (e.g., pregnant women, bedridden patients) directly to the local government units that control the relief budgets.
        
- **Inputs for WP4 Data Catalog:** The MSDHS vulnerable group dashboard (MSO-Logbook) and the World Bank risk maps should be logged in the External System Assets and Information Product Inventory.
    

- **Planned Participation:** MSDHS is an ideal candidate for the April Public Hearing & Brainstorming workshop. We will test the "municipality-level" seed use case with them to see how the CRDB conceptual model can better connect climate hazards to actual local budget allocation.
    
