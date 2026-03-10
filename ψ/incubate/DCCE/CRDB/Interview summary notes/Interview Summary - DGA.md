**Date:** 4/3/2569 (March 4, 2026)

**Interviewee Name/Title:** Dr. Montha Chaiyakornwikrom (Director), Saran Jainom (Head of Open Data Team), and Kunat (GDX Team)

**Department:** Government Data Management and Integration Department

**Agency:** Digital Government Development Agency (DGA / สพร.)

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** DGA provides the central digital infrastructure and data governance standards for the entire Thai government. Their three main missions are driving Open Data (via data.go.th), facilitating the exchange of Non-Open data among government agencies via the GDX platform, and enforcing the Data Governance Framework (DGF) across the public sector.
    
- **Associated legal frameworks:** They operate strictly under the Digital Government Administration and Provision Act B.E. 2562 (2019). Specifically, Article 15 mandates agencies to digitize and exchange data via the central exchange center. Articles 17 and 18 govern Open Data publishing, while Article 8 dictates the establishment of internal Data Governance Frameworks within government agencies.
    

### 2. Highlighted Key Projects & Open Data Strategy

- **Open Data Strategy & Center (data.go.th):**
    
    - _Status & Scope:_ Active. This is a central hub that automatically harvests "Open Data" from individual agency catalogs (Agency Catalogs) using CKAN-based technology.
        
    - _Standardization & Sharing:_ Agencies are required to publish data in machine-readable, non-proprietary formats (e.g., at least a 3-star level like CSV) as structured data. Agencies tag their datasets at the source with relevant keywords, which DGA then harvests to allow public searching, access, and analytics without restriction.
        

### 3. Dedicated Focus: Government Data Exchange (GDX) & Non-Open Data Strategy

- **GDX Platform Status & Scope:** Active for over 10 years, currently connecting 222 consumer agencies and facilitating over 400 million transactions.
    
- **The Non-Open Data Strategy:**
    
    - _Strict G2G Limitation:_ GDX is strictly limited to government-to-government (G2G/B2B) data exchange for e-services and internal analytics. The public and private sectors cannot access this platform.
        
    - _Data Integration Workflow:_ Data sharing on GDX is not automatic; it requires a strict 1-on-1 agreement between agencies. The "Consumer" agency must formally request permission from the "Provider" agency, citing their legal mandate and using standard templates (e.g., the Department of Business Development's template).
        
    - _Granular Access Control:_ The Provider agency retains full control over the data and dictates exact access levels. For instance, a provider might have 22 fields available but only grant the consumer access to 5 specific fields based on their mandate.
        
    - _DGA's Role as the Highway:_ Once the provider approves the request, DGA opens the API gateway to connect the two agencies. If an API is already available, integration via the GDX "highway" takes less than one month per dataset, saving agencies the time and budget of building redundant 1-on-1 connections.
        

### 4. Data Catalog Creation & Implementation Strategy

- **Agency Catalogs vs. GD Catalog:** * Every government agency is expected to have an "Agency Catalog," typically built on the open-source CKAN framework provided by DGA.
    
    - Agencies must then register their datasets with the "GD Catalog" (currently hosted by the National Statistical Office) to establish them as official government data records.
        
- **Technical Implementation & Harvesting:**
    
    - When an agency uploads a dataset to their local Agency Catalog, the data owner must attach metadata and specific keyword tags.
        
    - If the catalog is CKAN-based, the central data.go.th portal automatically "harvests" this metadata and displays it centrally. The actual data file remains hosted on the agency's local server; data.go.th simply provides the search portal and a direct download link back to the source.
        
    - If an agency chooses not to use CKAN and builds a custom system, DGA can still harvest the data, but it requires the agency to develop a custom API or a web scraping link.
        
- **Strategic Advice for DCCE's Climate Data Hub:**
    
    - DCCE has the legal authority to create its own domain-specific "Climate Data Hub".
        
    - They must choose an architecture: integrate these new climate datasets into the existing DCCE Agency Catalog, or spin up a completely separate platform (similar to how the National Housing Authority built a separate National Housing Information Center alongside their standard agency catalog).
        
    - DGA explicitly warned that this architectural choice directly impacts DCCE's "Digital Government Readiness" KPI. DCCE must consult with DGA when designing this catalog to ensure they select a primary host that maximizes their evaluation scores.
        

### 5. Current Workflow & Data Governance Framework (DGF) Support

- **Context and Hazard Scope:** DGA does not produce climate or hazard data. Instead, they provide the technical infrastructure and governance rules for DCCE and other agencies to share it securely.
    
- **Data Governance Framework (DGF) Support Services:**
    
    - DGA actively assists agencies in complying with Article 8 of the DG Act by helping them set up internal Data Governance Committees, define data management policies, and establish data quality controls aligned with national standards.
        
    - **Data Classification Service:** A major DGF service DGA provides is assisting agencies with Data Classification. They help agencies categorize their raw data into three buckets: what must remain strictly internal, what can be shared securely via GDX, and what must be routed to the Open Data portal (data.go.th).
        
    - DGA also provides direct training to government staff regarding these data governance missions.
        

### 6. Climate Data Needs, Gaps & Incentives

- **Standardizations & The "PDPA" Roadblock:** A major roadblock in government data sharing is agencies refusing to share data by claiming it contains "Personal Data". DGA solves this through their DGF consulting services, teaching agencies proper data masking and anonymization techniques. This allows agencies to strip personal identifiers and publish the core analytical data as Open Data without violating privacy laws.
    
- **Incentives for Data Sharing (Digital Readiness KPIs):** DGA highlighted that the primary incentive for agencies to standardize and share data is the **Digital Government Readiness Survey**. An agency's performance on this survey directly impacts its organizational KPIs.
    
- **Specific Requests/Recommendations for DCCE:** * _Do Not Build Redundant Infrastructure:_ DGA strongly recommended that DCCE leverage existing DGA infrastructure (like GDX and CKAN) instead of spending the budget to build a completely new data exchange pipeline from scratch.
    

### 7. Next Steps & CRDB Integration

- **Map to Implementation Plan:** DGA's advice directly impacts the architectural recommendations for the CRDB project. The final report must include a recommendation to utilize DGA's existing GDX platform for confidential data and data.go.th for open data, preventing redundant budget requests. The Data Governance Framework (WP3) must also directly reference DGA's Data Classification guidelines.
    
- **Seed Use Cases for WP3/WP4:** _Scenario:_ Utilizing GDX as the central highway to pull mandatory Greenhouse Gas (GHG) emissions data from the Department of Industrial Works (DIW) and the Ministry of Energy directly into DCCE's upcoming GHG reporting platform, bypassing the need to build individual 1-on-1 APIs.
    
- **Planned Participation:** DCCE and DGA agreed to set up a specific technical meeting to map out the exact datasets (e.g., from 3-4 target agencies) required for the GHG tracking platform, so DGA can verify if those APIs already exist on the GDX highway.