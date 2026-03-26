Timestamp: 2026-03-25-2000

The evolution of Thailand’s climate policy from a peripheral environmental concern to a central tenet of national economic and security planning is most visibly manifested in the digital infrastructure managed by the Department of Climate Change and Environment (DCCE). Following the high-level commitments made during the 26th Conference of the Parties (COP26), Thailand established an ambitious roadmap toward carbon neutrality by 2050 and net-zero greenhouse gas (GHG) emissions by 2065. Central to this transition is the development of a robust, web-based Monitoring, Reporting, and Verification (MRV) system, anchored by the `clim-webbased.dcce.go.th` domain and its associated portals. This architecture represents the institutionalization of climate transparency, moving from fragmented data collection to a unified, technical workflow designed to meet the requirements of the Enhanced Transparency Framework (ETF) under the Paris Agreement.

The DCCE, established under the Ministry of Natural Resources and Environment (MNRE), was tasked with a specific mandate: to track GHG emissions at both national and provincial levels while coordinating the country's adaptation strategies. In 2021, Thailand’s emission profile revealed approximately 270 $MtCO_{2}eq$ of total emissions, with an abatement of approximately 60 $MtCO_{2}eq$ against a national budget of 380 $MtCO_{2}eq$. This significant data load requires an information architecture that is not only scalable but also capable of integrating diverse sectoral inputs into a single, streamlined workflow. The `clim-webbased.dcce.go.th` system serves as the operational engine for this mission, providing the technical platform for the Thailand Greenhouse Gas Emissions Inventory System (TGEIS).

## Institutional Transition and the Digital Mandate

The establishment of the DCCE marks a pivotal moment in Thailand’s environmental governance. Previously, climate coordination was the responsibility of the Office of Natural Resources and Environmental Policy and Planning (ONEP). The elevation of these responsibilities to a dedicated department underscores the government's recognition that climate action requires specialized, high-capacity institutional oversight. This institutional shift was accompanied by a digital transformation strategy aimed at centralizing climate data to support the 20-Year National Strategy (2018–2037), which embeds sustainability and climate resilience as foundational goals for the kingdom’s development.

On the mitigation front, the updated Nationally Determined Contribution (NDC), submitted in November 2022, commits Thailand to reducing GHG emissions by 30% below business-as-usual (BAU) levels by 2030, with a potential increase to 40% contingent on international support. In absolute terms, this requires capping 2030 emissions at approximately 222,300 $ktCO_{2}e$, compared to a projected BAU of 388,500 $ktCO_{2}e$. Managing such precise targets necessitates a web-based ecosystem that can handle high-frequency data entry, rigorous quality control, and international auditability.

|**National GHG Emission and Reduction Targets (2030)**|**Value (ktCO2​e / %)**|
|---|---|
|Business-As-Usual (BAU) Projection (2030)|388,500 $ktCO_{2}e$|
|NDC Target (30% Reduction)|~271,950 $ktCO_{2}e$|
|Conditional NDC Target (40% Reduction)|222,300 $ktCO_{2}e$|
|Baseline Year for Comparison|2005|
|Scope of Coverage|Energy, Transport, Industry, Agriculture, Waste|

Sources:

The transition to a digital MRV system is also linked to the Bio-Circular-Green (BCG) Economy model, which promotes sustainable growth through biotechnology and circular economy practices. The information architecture of the DCCE’s web platforms is designed to reflect these cross-cutting priorities, integrating data from the Ministry of Agriculture and Cooperatives, the Ministry of Energy, and the Ministry of Public Health, among others.

## Structural Analysis of the DCCE Web Ecosystem

The sitemap and information architecture of the DCCE's digital presence reveal a highly organized "hub-and-spoke" model. The primary URL, `dcce.go.th`, acts as the public-facing gateway, while the `clim-webbased.dcce.go.th` environment and other subdomains (e.g., `ccic.dcce.go.th`, `dgf.dcce.go.th`) host specialized functional modules. This separation of concerns allows the department to manage public information, technical data entry, and sectoral reporting as distinct but interoperable layers.

### Primary Navigation and Portal Hierarchy

The core navigation of the DCCE website is organized into several key categories that define the information architecture:

1. **Climate Change Information Center (CCIC)**: The primary data hub for climate science, national reports, and policy updates.
    
2. **CCE Information System (สารสนเทศ CCE)**: A portal that links to various technical web-based systems used for reporting and monitoring.
    
3. **National Reporting and Data Centers**: Sections dedicated to the Climate Change Act, the National Committee on Climate Change Policy (NCCC), and international reporting (e.g., Biennial Transparency Reports).
    
4. **Specialized Technical Portals**: Independent systems for spatial risk mapping, green area tracking, and hospital emissions management.
    

|**Functional Domain**|**System / Portal Name**|**Primary Target Audience**|
|---|---|---|
|National MRV|TGEIS (Thailand GHG Inventory System)|Line Ministries, UNFCCC Auditors|
|Public Knowledge|CCIC (Climate Change Info Center)|Researchers, General Public|
|Adaptation|Risk MAP (Spatial Risk Database)|City Planners, Disaster Response|
|Sectoral Reporting|THEMS (Thai Hospital Emissions)|Healthcare Administrators|
|Data Governance|DGF (Data Catalog System)|Data Analysts, Policy Makers|
|Capacity Building|e-Learning / Seminar Systems|Local Officials, Environment Officers|

Sources:

The `clim-webbased.dcce.go.th` system, while often requiring authentication for internal administrative use, is the logical host for the "back-end" operations of the TGEIS. This system is designed to institutionalize the GHG inventory process, ensuring that every data point—from fuel consumption in transport to methane emissions from rice cultivation—is captured in a standardized format.

## Technical Architecture of the National GHG Inventory (TGEIS)

The Thailand Greenhouse Gas Emissions Inventory System (TGEIS) is the centerpiece of the DCCE’s web-based infrastructure. It is a centralized digital platform managed by the DCCE to calculate emissions based on activity data provided by line ministries. The system's architecture is built to align with IPCC (Intergovernmental Panel on Climate Change) methodologies, specifically focusing on the 2006 IPCC Guidelines for National Greenhouse Gas Inventories.

### The Data Entry Template (DET) Workflow

The technical logic of the TGEIS relies on the use of standardized Data Entry Templates (DET). For the energy and transport sectors, which contribute 65.8% of national emissions, the workflow is meticulously documented in official operational manuals. The process begins with the identification of emission source categories and ends with the formal upload of data into the TGEIS web portal.

The operational steps for the national GHG inventory in the energy and transport sectors, as specified on page 4 of the manual, follow a rigorous timeline:

- **Step 1: Activity Data Verification**: Checking historical activity data against the current reporting period.
    
- **Step 2: Source Category Mapping**: Assigning data to specific IPCC categories (e.g., stationary combustion vs. mobile combustion).
    
- **Step 3: DET Completion**: Entering raw activity data (e.g., fuel consumption in terajoules) into the DET.
    
- **Step 4: Quality Control (QC)**: Initial technical review to ensure data consistency.
    
- **Step 5: TGEIS Importation**: Uploading the completed DET into the `clim-webbased` system.
    

This structured approach ensures that the "bottom-up" data collected from the field matches the "top-down" requirements of national policy and international reporting. The use of a centralized system like TGEIS allows for the application of local emission factors, provided by the Thailand Greenhouse Gas Management Organization (TGO), ensuring that calculations reflect the unique carbon intensity of Thailand’s energy mix and industrial processes.

### Sectoral Modules and Calculation Engines

The information architecture of the TGEIS is modular, with separate calculation engines for different sectors:

1. **Energy and Transport**: Focusing on fuel combustion and fugitive emissions.
    
2. **Agriculture**: Utilizing data from the Ministry of Agriculture and Cooperatives to track emissions from livestock, rice cultivation, and managed soils.
    
3. **Industrial Processes and Product Use (IPPU)**: Monitoring chemical processes, mineral production, and refrigerant usage.
    
4. **Waste Management**: Tracking methane from landfills and wastewater treatment facilities.
    
5. **LULUCF**: Monitoring land use, land-use change, and forestry to calculate the carbon sequestration potential of Thailand’s natural resources.
    

This modularity is critical because each sector requires different types of activity data and employs different emission factors. For instance, in the agriculture sector, rice cultivation is the main source of national methane emissions, requiring a sophisticated data flow that includes paddy field acreage, water management practices, and organic fertilizer usage.

## Sectoral Integration: The Healthcare Case Study (THEMS)

A prime example of how the DCCE’s web-based architecture extends into specific sectors is the Thai Hospitals Emissions Management System (THEMS). Launched in October 2025 by the Ministry of Public Health (MOPH) in collaboration with the DCCE, THEMS is a national web database that requires 904 public healthcare facilities to report and monitor their quarterly emissions.

### Methodology and Data Granularity

THEMS employs a hybrid reporting system. Most emissions data are estimated using a "bottom-up" approach, relying on actual activity data from the healthcare facilities themselves. However, emissions from extra supply-chain activities are estimated using a "top-down" approach, leveraging hospital expenditure data. This granularity allows the system to cover Scope 1 (fuel, refrigerants, anesthetic gases), Scope 2 (electricity consumption), and Scope 3 (supply chain, waste, travel) emissions.

|**Emission Scope in THEMS**|**Key Data Points Monitored**|**Estimation Approach**|
|---|---|---|
|Scope 1 (Direct)|Fuel for boilers/generators, anesthetic gases, on-site medical waste.|Bottom-up (Activity-based)|
|Scope 2 (Indirect)|Purchased electricity from the national grid.|Bottom-up (Utility billing)|
|Scope 3 (Value Chain)|Supply chain procurement, travel, off-site waste disposal.|Top-down (Expenditure-based)|

Sources:

The architecture of THEMS is designed to support more than just monitoring; it is a tool for strategic intervention. By identifying "emission hotspots," the system enables the MOPH to measure the cost-effectiveness of decarbonization efforts and recognize facilities that achieve significant reductions. This sectoral data is then synthesized and fed into the broader national baseline managed by the DCCE, illustrating the "nested" nature of the department’s information architecture.

## The Adaptation Layer: Spatial Risk and Early Warning Systems

While mitigation systems like TGEIS and THEMS focus on emission reduction, a significant portion of the DCCE’s web architecture is dedicated to climate adaptation. Thailand's vulnerability—shaped by an extensive coastline, rural agricultural dependence, and urban centers on flood-prone plains—necessitates a data-driven approach to resilience.

### Risk MAP and CCIC Adaptation Portals

The "Spatial Risk Database System" (Risk MAP) and the "Climate Change Information Center" (CCIC) are the primary portals for adaptation data. These systems are designed to strengthen Thailand's capacity for "risk-informed anticipatory actions" to floods and droughts. Supported by the Green Climate Fund (GCF) and the Asian Disaster Preparedness Center (ADPC), these portals facilitate cross-sector coordination and identify systemic gaps for priority investment.

The adaptation information architecture is structured around six priority sectors identified in the National Adaptation Plan (NAP):

1. **Water Resources Management**: Tracking water availability and flood risk.
    
2. **Agriculture and Food Security**: Monitoring crop vulnerability and soil degradation.
    
3. **Tourism**: Assessing the impact of climate change on coastal and natural attractions.
    
4. **Public Health**: Tracking climate-sensitive diseases and heat-related risks.
    
5. **Natural Resources Management**: Monitoring biodiversity and ecosystem health.
    
6. **Human Settlements and Security**: Analyzing urban resilience and infrastructure vulnerability.
    

By integrating GIS data with climate projections, these systems provide local authorities with the tools needed to develop climate-resilient project concepts. For example, the Risk MAP portal allows users to visualize severe flooding patterns in the South, enabling practical, actionable planning for community resilience.

## Data Governance and the DGF Data Catalog

The integrity of Thailand's climate response rests on the transparency and accessibility of its data. The DCCE manages this through the "Data Catalog System" (DGF), which serves as the official data inventory for the department. This system is critical for aligning national data management with international standards, such as the UN’s Sustainable Development Goals (SDGs).

### Metadata Standards and Open Data

The DGF portal uses standardized metadata to organize environmental datasets, making them searchable for researchers, international organizations, and the private sector. This catalog includes information on:

- **National Reports**: Access to Biennial Update Reports (BUR) and the forthcoming Biennial Transparency Reports (BTR).
    
- **Greenhouse Gas Inventories**: Raw and processed data on sectoral emissions.
    
- **Policy Documents**: The Climate Change Master Plan (2023–2027) and the Agriculture Strategic Plan on Climate Change (2023–2027).
    
- **Open Data Sets**: General environmental quality monitoring reports and urban green area tracking.
    

This emphasis on open data is driven by the Ministry of Digital Economy and Society (MDES), which provides cross-cutting support to enhance Thailand’s data infrastructure, including smart grids and open data platforms. The goal is to move toward a "Unified MRV" system where data is not only reported but is also used for real-time monitoring and public accountability.

## Regulatory and Financial Drivers of Digital Architecture

The future of the DCCE’s web-based systems is being shaped by two major forces: the draft Climate Change Act and the emergence of sustainable finance. These drivers will transform the `clim-webbased` system from a reporting tool into a mandatory regulatory and financial verification platform.

### The Draft Climate Change Act

Expected to be enacted by 2025, the Climate Change Act will mandate annual GHG reporting for major emitters. This will require a fundamental upgrade to the DCCE’s web architecture to support:

- **Electronic GHG Reporting Platforms**: Standardizing data collection across the entire economy.
    
- **Emissions Trading Systems (ETS)**: Integrating a registry for carbon credits and allowance trading.
    
- **Enforcement and Auditing**: Automated systems for verifying the accuracy of reports submitted by the private sector.
    

### Sustainability-Linked Finance

The Department of Climate Change and Environment's data is already being used to support Thailand’s sustainable finance initiatives. The Public Debt Management Office (PDMO) has issued Sustainability-Linked Bonds (SLB) whose Key Performance Indicators (KPIs) are directly tied to national GHG emission reduction targets.

|**Sustainable Finance Instrument**|**KPI Source**|**Verification System**|
|---|---|---|
|Sustainability-Linked Bonds (SLB)|National GHG Emissions (excluding LULUCF)|TGEIS / DCCE|
|Sustainable Financing Framework|Project-level social and environmental impact|DGF / Monitoring Systems|
|Carbon Credits (Article 6)|Mitigation activity outcomes|TGO / SPAR6C|

The PDMO’s Sustainability-Linked Financing Framework, announced in October 2024, relies on the DCCE's data to ensure the "credibility and appropriateness" of its targets, aligning with international principles such as those of the International Capital Market Association (ICMA). This creates a direct causal link between the accuracy of the `clim-webbased` digital platform and Thailand's access to international capital markets.

## International Interoperability and Article 6 Preparedness

As a signatory to the Paris Agreement, Thailand is preparing to engage in international carbon markets under Article 6. This requires its digital MRV systems to be interoperable with international registries to prevent "double counting" of emission reductions.

The "Supporting Preparedness for Article 6 Cooperation" (SPAR6C) program, funded by the German government, is assisting Thailand in this effort. The program provides technical assistance to identify and prepare mitigation activities that can serve as the basis for Article 6 transactions. For the DCCE's web-based systems, this means:

- **IT Infrastructure Alignment**: Ensuring that the TGEIS and TGO registries can communicate with international carbon trading platforms.
    
- **Reporting Standardization**: Adhering to the "Rulebook" for Articles 6.2 and 6.4 established at COP26.
    
- **Technical Capacity**: Training Thai officials to use digital tools for tracking internationally transferred mitigation outcomes (ITMOs).
    

## Analysis of Information Architecture Gaps and Challenges

Despite the sophistication of Thailand’s climate web-based ecosystem, several challenges remain. The initial pilot test of THEMS in January 2025 revealed the need for basic training on how to measure and report facility-related emissions. This suggests that "Capacity Building" is a critical, yet sometimes underdeveloped, layer of the information architecture.

Furthermore, while the TGEIS uses a "bottom-up" approach for many sectors, the agriculture sector—which accounts for 18.1% of emissions—is notoriously difficult to monitor with high precision. The systems-level assessment (SLA) of maize and livestock value chains conducted by the Thailand Development Research Institute (TDRI) highlighted the need for improved manure management and adapted farming practices. Integrating these varied agricultural data points into a unified web portal remains an ongoing technical challenge.

|**Architectural Challenge**|**Impact on System Efficacy**|**Proposed Mitigation**|
|---|---|---|
|Data Granularity in Agriculture|Difficulty in tracking methane from millions of small farms.|Satellite imagery and AI integration.|
|Stakeholder Technical Capacity|Errors in data entry from provincial or facility-level officers.|Expanded e-Learning and help-desk modules.|
|System Interoperability|Fragmented data across different ministry silos.|Unified Data Catalog (DGF) and the Climate Change Act.|
|Financial Verification Rigor|High standards required for sustainability-linked bonds.|Third-party auditing modules in the TGEIS workflow.|

Sources:

## Strategic Synthesis and Future Outlook

The information architecture of the DCCE’s climate web-based systems is a direct reflection of Thailand’s holistic approach to climate governance. By weaving together mitigation (TGEIS, THEMS), adaptation (Risk MAP, CCIC), and data governance (DGF), the department has created a digital foundation for the kingdom's carbon-neutral future.

The system's design emphasizes several core principles:

1. **Centralization for Integrity**: By using the TGEIS as the single source of truth for emissions data, Thailand ensures that its national reports are consistent and credible.
    
2. **Modular Flexibility**: The use of specialized portals for healthcare (THEMS) and urban planning (Green Area) allows for sectoral specialization without losing the ability to aggregate data at the national level.
    
3. **Policy-Driven Design**: The sitemap is not static; it is evolving to meet the needs of the 2nd Updated NDC, the LT-LEDS (Long-Term Low Greenhouse Gas Emission Development Strategy), and the upcoming Climate Change Act.
    
4. **Financial Integration**: The digital platforms are increasingly serving as the data backbone for sustainable finance, linking climate action to national debt management.
    

As Thailand moves toward its 2030 target of reducing emissions by 30-40%, the `clim-webbased.dcce.go.th` portal will likely transition from a primary monitoring tool to a sophisticated regulatory engine. The integration of advanced technologies—such as impact-based forecasting and AI-driven emission modeling—will be essential to manage the increasing complexity of a net-zero economy.

## Conclusions and Recommendations for Digital Governance

The review of the sitemap and information architecture of the DCCE’s web-based ecosystem indicates a high level of institutional maturity and technical sophistication. The department has successfully mapped its physical administrative structures onto a digital platform that serves a wide range of stakeholders, from hospital administrators to international carbon market participants.

To maximize the impact of this digital infrastructure, several strategic directions are recommended:

- **Enhancement of Interoperability**: The DCCE should continue to work with the Ministry of Digital Economy and Society to ensure that climate data flows seamlessly between all relevant agencies, particularly in the agricultural and energy sectors where the highest mitigation potential exists.
    
- **Scaling of Success Stories**: The "hybrid" approach used in THEMS—combining bottom-up activity data with top-down expenditure estimates—should be considered for other sectors, such as small-scale manufacturing or tourism, to increase the granularity of the national inventory.
    
- **Investment in Digital Readiness**: Given the technical nature of systems like TGEIS and THEMS, continued investment in user training and capacity building is vital. The "Readiness" support provided by the Green Climate Fund serves as a valuable model that should be expanded domestically.
    
- **Standardization for Article 6**: As international carbon markets evolve, Thailand must ensure that its digital registries are not only compliant with UNFCCC standards but are also technologically compatible with the platforms used by potential trade partners like those in the SPAR6C program.
    

In conclusion, the `clim-webbased.dcce.go.th` system and its associated digital assets are more than just a collection of websites. They are the technological manifest of Thailand's commitment to the Paris Agreement and the primary mechanism through which the country will monitor, report, and verify its path toward a sustainable, low-carbon future. The continued evolution of this architecture will be the defining factor in Thailand’s ability to meet its mid-century carbon neutrality and net-zero goals.