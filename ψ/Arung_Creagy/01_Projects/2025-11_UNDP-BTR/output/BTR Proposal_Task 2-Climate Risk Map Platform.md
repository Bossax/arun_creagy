---
type:
  - strategy
status:
  - archived
tags:
version: 1
parent_hypothesis: "[[ ]]"
created: 2025-10-29
project:
  - UNDP_BTR
color: ""
---

The application is designed using a **3-tier architecture**, which is a well-established pattern for building scalable and maintainable web applications.

This architecture separates the system into three distinct logical and physical computing tiers:
1. Presentation Tier
2. Application Tier
3. Database Tier

This separation of concerns is crucial for managing complexity, improving security, and allowing different parts of the system to be updated and scaled independently.

Here's a breakdown of each tier as described in the document.

# 1. Presentation Tier (Frontend)

This is the user-facing layer that *runs in the client's web browser*. Its primary responsibility is to deliver an intuitive and interactive user experience for visualizing complex geospatial data.

- **Purpose:** To render the user interface (UI), including interactive maps, dashboards, data filters, and reporting tools. It's designed to be responsive, working across desktops, tablets, and mobile devices.
    
- **Key Technologies:** The proposal suggests a modern JavaScript framework like **React** or **Next.js** for building the UI. For mapping, it specifies libraries like **MapLibre GL** or **Leaflet**. The overall styling would be managed with **TailwindCSS**.
    

# 2. Application Tier (Backend)

This is the server-side layer that contains the core application logic. It acts as the intermediary between the presentation and data tiers, processing requests from the user, executing analyses, and managing data flow8

- **Purpose:** To expose a secure **REST API** that the frontend consumes. This tier handles tasks like geospatial analysis, compound risk calculations, data ingestion pipelines, and user authentication.
    
- **Key Technologies:** The backend is built on **Python** with the **FastAPI** framework, which is excellent for creating high-performance APIs. The entire application is containerized using **Docker**, which simplifies deployment and ensures consistency across different environments.

## Key program logic
### 1. API Gateway & Service Orchestration

The application layer's entry point is an **API Gateway**, which manages all incoming requests from the user interface2. It handles routing, security, and versioning, ensuring that client requests are directed to the correct internal service. This logic acts as the central coordinator for all the application's functions3.

### 2. Core Analytical & Data Services

#### 2.1 Hazard & Exposure Service
1.  **Spatial Risk Quantification Module**
	This module's core logic is to calculate and map risk intensity across the country at a very granular level.
	- **Purpose**: To generate nationwide risk assessments at the district and, where possible, subdistrict level.
	    
	- **Inputs**: It takes **hazard layers** (like maps of floods, droughts, and heatwaves) and intersects them with **local exposure datasets** (like population centers and infrastructure locations).
	    
	- **Process**: The module essentially overlays these different map layers to **calculate** the potential impact of a specific hazard on a specific area.
	    
	- **Outputs**: The results are district-to-subdistrict **risk maps**, **vulnerability indices**, and **tabular reports** that can be used for national monitoring and UNFCCC reporting.

2. **Socio-Economic Disaggregation Module**
	This module adds a critical social dimension to the risk analysis, ensuring that the human impact of climate events is understood.
	- **Purpose**: To analyze and break down climate risk impacts across key social and economic dimensions, with a focus on vulnerable groups.
	- **Inputs**: It uses demographic and socio-economic indicators.
	- **Process**: The logic disaggregates risk impacts on specific categories like **urban areas**, **agricultural land**, and **vulnerable populations** such as women, the elderly, and low-income communities. This ensures assessments are gender-responsive and socially inclusive.
	- **Outputs**: disaggregated climate impact scores

 3. **Compound Risk Modeling Module**
	- **Purpose**: To assess **compound and cascading risks**, which occur when multiple hazards happen simultaneously or sequentially, amplifying the total impact.
	    
	- **Inputs**: It uses multi-hazard overlays and scenario-based simulations.
	    
	- **Process**: The logic implements a formal framework for identifying several types of compound events:
	    - **Preconditioned events**: A drought making a subsequent heatwave more damaging.
	    - **Multivariate events**: A storm bringing both heavy rain and a storm surge at the same time.
	    - **Temporally compounding events**: Back-to-back typhoons in a single season.
	    - **Spatially compounding events**: Widespread drought affecting multiple river basins simultaneously.
	        
	- **Outputs**:  spatial composite risk scores 
    
4. **Real-time Service:** This component manages live data updates. It uses technologies like WebSockets or webhooks to push real-time information (e.g., new landslide sensor data, weather alerts) to the user dashboard without requiring the user to refresh the page.
    
#### 2.2 Data Management & Integration

A significant part of the logic is dedicated to getting data into the system and connecting with external sources.

- **Data Pipeline:** The application uses automated data pipelines for ingesting, validating, and transforming data from various national and international sources777. This is often referred to as an ETL (Extract, Transform, Load) process8.
    
- **Integration Adapters:** The system includes specific logic to act as connectors to external datasets and APIs from other national systems, ensuring interoperability9.
    

### 2.3 Asynchronous Processing

To ensure the user interface remains responsive, the application layer includes logic for handling long-running, computationally intensive tasks.

- **Background Jobs:** For heavy analyses that might take several minutes, the request is sent to a background task runner or message queue. This allows the application to process the task asynchronously without making the user wait for it to finish, improving the overall user experience11.

### 3. Data Tier (Database Layer)

This tier is responsible for the persistent storage and management of all data used by the application. It's designed to handle a variety of data types, especially large and complex geospatial datasets15.

- **Purpose:** To provide secure, durable, and performant storage for spatial data (vectors and rasters), analytical results, and user information16.
    
- **Key Technologies:** The core of this tier is a relational database with spatial capabilities, specifically **PostgreSQL with the PostGIS extension**. This is the industry standard for handling authoritative vector data like administrative boundaries and exposure assets18. For serving map tiles efficiently, a GIS server like **GeoServer** is proposed. The proposal also mentions the potential for using **Microsoft SQL** as a database.
    
### Development and Deployment
The proposal also outlines a modern, agile software development process to build and maintain this architecture . It emphasizes iterative sprints, continuous integration/continuous deployment     (**CI/CD**) pipelines, and comprehensive testing (unit, integration, performance, and security) to ensure high quality and reliability.

 


## Task 2: Development of climate-related risk maps and databases to report various types of hazards and specify risk areas at a sub-provincial level 

This task focuses on enhancing Thailand’s climate risk information systems by developing detailed, GIS-based risk maps and an underlying database to identify hazard-prone areas at sub-provincial levels. Our approach for Task 2 is both technical and collaborative.

**Phase 1 - Inception phase**

The Inception Phase will outline the detailed methodology and work plan in close consultation with DCCE and other relevant stakeholders. This phase will also include identifying user requirements through stakeholder engagement and jointly defining the system concept and requirements of the Climate-related Risk Mapping System.

**Phase 2 -** **Data Collection, Database Development and Risk Analytics**

Following the Inception Phase, a consultation meeting/workshop with key stakeholders (e.g., DCCE, DDPM, DMR, etc.) will be convened to discuss data collection and database development. During this phase, existing national datasets on climate-related hazards (floods, droughts, heatwaves, storms, landslides, and coastal erosion) and disaster impacts will be reviewed, with attention to gender and social inclusion where possible. Gaps in data will be supplemented using relevant datasets from international sources, ensuring consistency and compatibility with national datasets.

**Phase 3 -** **Development of Climate-related Risk Dashboard**

The proposed Climate-related Risk Mapping System (Appendix A-0) will serve as a web-based application to strengthen risk-informed decision-making in Thailand. The system will provide a GIS-enabled platform with a responsive design to display hazard and exposure data, incorporating an interactive map viewer, data filters, dashboards, reporting (with export functions), and user management to ensure practicality and user-friendliness. All validated data will be integrated into the platform, with information presented at least at the district level nationwide and further disaggregated to the subdistrict level where data availability permits.

The approach for the **Development of Climate-related Risk Dashboard** is to build an open-source and modular platform. This open-source approach not only reduces costs but also enhances flexibility and integration with existing disaster management systems.

The proposed **Comprehensive Climate-related Risk Dashboard** will be developed using Next.js for the frontend and Python-based frameworks (FastAPI) for backend APIs. The system will integrate multi-source datasets (satellite, multi-hazard, and socioeconomic data) and apply GIS techniques for real-time risk analysis.

Role-based user access, secure API communication, and encrypted storage will ensure data security and controlled access. Development will follow an Agile process with iterative releases, continuous stakeholder feedback, and CI/CD pipelines for efficient delivery. Quality will be assured through unit, integration, and user acceptance testing, with deployment on containerized infrastructure (Docker) for scalability. Post-implementation, the system will include training, documentation, and maintenance support.

The proposed main features of Climate-related Risk Mapping Dashboard Module are:

**Table** **4** Climate-related Risk Mapping Dashboard Module

|**Feature Category**|**Key Capabilities**|
|---|---|
|Multi hazard overlay visualisation|·         Real-time hazard status display<br><br>·         Hazard exposure & vulnerability visualization|
|Interactive map viewer|·         Customized UI/UX for decision-makers<br><br>·         Real-time hazard status display<br><br>·         Interactive Online Map (zoom in/out, Pan to)|
|Data filters|·         Anticipatory action support tools<br><br>·         Hazard exposure & vulnerability visualization|
|Reports (exporting data)|·         Downloadable/printable reports<br><br>·         Standardized reporting templates<br><br>·         Reports, charts, statistics, and printable templates|
|Dashboard|·         Integration of statistics and descriptive analytics<br><br>·         Customized UI/UX for decision-makers<br><br>·         Present at least at the district level nationwide, and disaggregated to the subdistrict level where data is available|

**Phase 4 –** **Final Release and User Acceptance Testing (UAT)**

The Final Release and UAT will validate the Climate-related Risk Dashboard before deployment. The process will confirm that the platform delivers the intended user benefits, performs reliably under operational conditions, and scales to meet peak demand during emergencies. Testing will focus on system usability, performance, and stability. Stress testing will simulate high usage to confirm the platform’s ability to operate under pressure. User acceptance testing will verify that core functions meet the needs of DCCE, and public users.

The methodology combines system-level validation with structured user testing. The system will first be deployed in a controlled environment that mirrors production. Functional, performance, and scalability tests will be conducted before end-users participate in UAT. This approach ensures that the technology platform works as designed and that users can operate it effectively for landslide monitoring, risk analysis, and emergency coordination.

**Phase 5 –**  **Transfer all the Source Codes, Maintenance and monitoring System Performance and Providing Technical Support**

The transfer process will be carried out in a structured and secure manner to ensure DCCE receives full ownership of the Climate-related Risk system, including source codes, access credentials, and technical documentation. All codebases will be maintained in version-controlled repositories (e.g., GitHub/GitLab), ensuring traceability, transparency, and long-term maintainability. Access credentials and configuration details will be documented and securely shared. A knowledge transfer session will be conducted with the DCCE technical team to walk through the repository, system architecture, deployment processes, and backup/upgrade strategies.

**Operations and Maintenance Services**

The maintenance and support phase will ensure the system remains fully operational and secure up to 14 months[[SS2]](#_msocom_2) [[BY3]](#_msocom_3)  after the handover. A proactive approach will be adopted to monitor system performance, address technical issues, and implement necessary enhancements in response to user feedback or evolving requirements. The system will follow a structured maintenance lifecycle, including preventive maintenance, corrective troubleshooting, and adaptive modifications to integrate new features or datasets. Regular updates will be scheduled to patch vulnerabilities, upgrade dependencies, and optimize performance while ensuring minimal downtime.

---

 [[SS1]](#_msoanchor_1)[@Creagy-Boonrod](mailto:boonrod@thecreagy.com) I added and formatted ADPC’s content. The content is split and put separately in these sections  
1. Approach and Methodology  
2. Quality assurance (2.5.4)  
3. APPENDIX A-0: detailed proposed solution

 [[SS2]](#_msoanchor_2)The TOR states the delivery date by 30 Sep 2026 and the end of maintenance on 15 Dec 2027. So 14 months

 [[BY3]](#_msoanchor_3)ok