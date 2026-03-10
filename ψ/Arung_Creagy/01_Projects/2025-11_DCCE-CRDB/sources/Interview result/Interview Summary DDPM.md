- **Date:** February 23, 2026
- **Interviewee Name/Title:** Representatives from the Policy Division, Disaster Relief Division, Research and International Cooperation Bureau (สว.), and Data Center
- **Department:** Various
- **Agency:** Department of Disaster Prevention and Mitigation (DDPM)
- **Interviewer:** Sittichat (Crygy Consulting Team for DCCE)
    

# **1. Role and Responsibility of the Agency**

- **Key duty and roles:**
    - The Data Center is the central hub for collecting occurrence data on all disasters affecting people, property, and the environment.
        
    - **Disaster Declaration Criterion:** DDPM staff clarified that an event is officially announced as a "disaster zone" not merely because a hazard occurred, but specifically when the Local Administration Organization (LAO/อปท.) cannot manage the situation with their own capacity and requires outside agency intervention and relief funds.
        
    - The Disaster Relief Division coordinates emergency relief across 6 defined categories based on Ministry of Finance regulations: living/subsistence, medical, social welfare, agriculture, disaster relief, and relief operations.
        
- **Associated legal frameworks:**
    
    - Operates under Ministry of Finance regulations and guidelines (recently updated in 2025 and effective March 2026) which dictate the criteria for distributing emergency disaster relief funds.

# **2. Highlighted Key Projects**

- **Northern Region Climate Risk Assessment:**
    - _Status:_ Currently in the procurement stage, with expected completion around September 2026.
        
    - _Ownership & Scope:_ Owned by the Policy Division / Research Center of DDPM. Phase 1 targets 17 districts across 17 northern provinces, focusing specifically on floods, landslides, and earthquakes.
        
    - _Methodology & Objective:_ The project utilizes an index-based methodology. It aims to develop a standardized set of 10-20 vulnerability indices. The primary objective is to support provinces and LAOs by allowing them to "shop" for relevant indices to assess their own localized risks systematically.
        
- **Hazard Mapping Initiatives:**
    - _Current State:_ DDPM historically relies on plotting past occurrence data (e.g., 3-5 years of historical events) to create quasi-hazard maps. For actual scientific hazard projections, they do not produce their own; instead, they are heavily supported by other line agencies such as the Royal Irrigation Department (RID), Office of the National Water Resources (ONWR), and the Department of Water Resources.
        
- **DDPM Alert Platform / Data Portal:**
    - _Integration & Sharing:_ Aggregates warning data via MOUs with 7 technical agencies (e.g., TMD, RID). DDPM maintains a Data Catalog with approximately 40 datasets available for inter-agency exchange via API.
        

# **3. Current Workflow & Data Usage**

- **Data Collection Flow and QA/QC:**
    - LAOs act as the primary data collectors on the ground, reporting damage counts to the District, which then forwards them to the Province.
        
    - _Quality Assurance:_ Provincial DDPM staff perform the initial Quality Control (QC) before inputting data into the central system. However, the data flow is strictly "one-way." Central DDPM cannot feasibly ground-truth or verify the accuracy of the local reports and must rely entirely on the province's confirmation.
        
    - _Data Granularity:_ Currently tracks events down to the village level over a 10-year historical baseline, though exact spatial coordinates within the villages are missing. A new GIS reporting tool is being rolled out to address this.
        
- **LAO Incentives and Capacity Building:**
    - Data collection at the local level is heavily incentivized by the disbursement of relief and compensation funds (เงินเยียวยา). Tying financial assistance to the reporting system is the primary motivator that forces LAOs to build their data entry capacity and adopt new digital/online systems, despite initial learning curves and struggles.
        

# **4. Climate Data Needs & Gaps**

- **Lack of Rigid Data Frameworks (UNDRR Standards):**
    - DDPM collects raw counts of damaged items (e.g., number of flooded roads, dead livestock, damaged temples) but lacks a rigid taxonomy or framework for categorizing these into standard "Exposure" and "Vulnerability" metrics. They do not rigorously map their statistics to international standards (like UNDRR's sector groupings) for macro-level economic loss.
        
- **Economic Loss Valuation Gap:**
    - While past pilot projects (like the Post Disaster Needs Assessment - PDNA) attempted to apply proxy values (e.g., cost per kilometer of road) to estimate physical damages, these methods failed to capture indirect economic losses and stalled due to difficulties in obtaining multi-agency data.
        
- **Data Screening and AI Requests:**
    - Because LAO staff frequently input data late, incorrectly, or into the wrong categories, DDPM specifically expressed a need for automated screening tools or AI to clean and standardize raw data before it hits the central database.
        
- **Adaptive Capacity Gap:**
    
    - DDPM noted that objectively measuring "management capacity" or adaptive capacity is currently impossible. They rely solely on After Action Reviews (AAR) to identify operational bottlenecks rather than quantifying resilience.

# **5. Next Steps & CRDB Integration**

- **Map findings directly to CRDB Implementation Plan:**
    
    - _Loss & Damage Logical Data Model (WP3/WP4):_ DDPM's historical disaster occurrence data will be vital for the CRDB baseline. However, due to the lack of a rigid UNDRR-aligned framework at DDPM, the CRDB's Conceptual Data Model must be designed to ingest raw physical impact counts and apply its own logical groupings to estimate economic vulnerability.
        
    - _Data Cataloging (WP4):_ The 40 items currently sitting in DDPM's portal must be mapped and registered into the CRDB external system assets inventory.
        
- **Seed use cases for WP3 Conceptual Data Model:**
    
    - The new 10-20 index-based methodology being developed for the Northern Region Climate Risk Assessment should be closely tracked. These indices can serve as a direct "seed use case" for populating the Vulnerability Factors entity in the CRDB's Enterprise Data Model.
        
- **Planned participation in workshops:**
    
    - DDPM representatives have been formally invited to the CRDB Public Hearing and Brainstorming workshop in April to share their use cases and validate the proposed data architecture.