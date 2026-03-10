---
type: strategy
status: current
version: 5
last_updated: 2026-02-18
project:
  - DCCE_CRI
related_hypothesis: "[[ ]]"
---
>[!note] Change Log
>- v1: project proposal submission
>- v2: Update reflecting "Middle Path" strategy (Capacity Tagging) and confirmation of full provincial data availability.
>- v3: include more detail of phase 1 implementation
>- v4: Integrated Inception Report deadline (Jan 7) and Gap Analysis milestones per 2026 Roadmap.
>- v5: Minor alignment with SES pivot documentation and Working Status Brief (no structural change to WPs).





## 1. Overview and Approach

The **Climate Risk Index (CRI) Phase 2** project builds on Phase 1 to develop a more comprehensive, spatially resolved and policy‑relevant index for Thailand. The project lasts **240 days (≈8 months)** and is divided into five work packages (WPs) that align with the Terms of Reference (TOR). The proposal explains that the project will run for 240 days and is broken into five groups—planning, review of Phase 1, development of an improved index, stakeholder engagement and dissemination, and final reporting. This implementation plan converts those groups into self‑contained WPs and clarifies dependencies, deliverables, team roles, technical requirements and quality‑control steps. The plan is intended for the project team to guide execution and remove ambiguity.

## 2 Work Package Structure

### WP 1 – Project Planning and Inception

**Objective** – Establish a clear roadmap for CRI Phase 2 by reviewing the TOR, defining the scope and schedule and producing the Inception Report. The proposal states that the purpose of this group is to review TOR tasks and outline the work plan.

**Scope and Key Activities**

- Review TOR requirements (Items 5.1–5.9) and clarify deliverables.
- Develop a detailed work plan for all WPs, including tasks, timelines and resource allocation.
- Analyze gaps and lessons from CRI Phase 1 to ensure the plan addresses limitations and integrates both top‑down and bottom‑up approaches.
- Prepare and submit the **Inception Report**, summarizing the work plan, methodology and initial findings.
    
**Inputs / Dependencies** – None. This package starts the project and informs later WPs.

**Expected Outputs / Deliverables**
- Inception Report (Thai language with digital copies) delivered within 30 days (**Jan 7, 2026**).
- Detailed project schedule and risk register.
    
**Team Roles and Responsibilities** – Project Manager leads planning, with input from climate‐change, policy‑planning and natural‑resource experts. Research assistants compile data and prepare the report.

**Technical Requirements** – Project management tools (e.g., Gantt charts, spreadsheets), a shared document repository and version control for collaborating on planning documents.

**Quality Assurance and Review** – Conduct an internal review of the Inception Report before submission. Hold a kick‑off meeting with DCCE to ensure alignment and confirm scope.

**Timeline and Milestones** – Month January 2026: finalize work plan and submit Inception Report.

### WP 2 – Review of Phase 1 and Additional Data Analysis

**Objective** – Review international indices (Germanwatch CRI, CVI, ND‑GAIN, INFORM Risk Index) and Phase 1 results to identify data gaps and methodological limitations. Provide a foundation for developing improved impact, resilience and readiness indices.

here is a document on [[CRI Phase 1 Methodology]]

**Scope and Key Activities**
- **Execute "Data Definition & Formula Audit":** Systematically review the Phase 1 Pilot file. Verify the specific sources of population data (Census vs. DOPA) and confirm the alignment of economic denominators (e.g., ensuring Agricultural Relief is divided by Agricultural GPP, not Total GPP).
    
- **Validate "Zero" vs. "Gap" (Data Quality Flagging):** Cross-reference the "Relief Payment" datasets with historical Hazard Maps (Flood/Drought rasters).
    - _Action:_ Create a **"Data Quality Flag"** for every province/year. If a hazard occurred (Satellite = True) but relief was zero (Admin = 0), flag as **"Administrative Gap"** rather than "Low Risk."
        
- **Methodology Refinement & Communication:**
    - Draft a **"Hybrid Data Methodology Note"** for the Inception Report. This note must explicitly frame the use of Global Data (WorldPop/ESA) as a tool to _disaggregate_ official DOPA statistics ("Constrained Redistribution"), not to replace them.
    - Formalize the **"Fiscal Relief Index"** renaming strategy. <!--todo:  to discuss with the team-->

- **Gap Analysis Report:** Summarize the confirmed data availability (all provinces) and detail the strategy for addressing the "Urban Blindspot" (lack of relief data in non-agricultural zones) using proxy exposure layers

**Inputs / Dependencies** – Inception Report and planning outputs from WP 1.

**Expected Outputs / Deliverables**
- Gap Analysis Report detailing data deficiencies and recommendations for improved CRI.
- Compiled dataset of ancillary spatial data for subsequent modelling.
    

**Team Roles and Responsibilities** – Climate‑change expert leads the review; policy‑planning and natural‑resource experts contribute sector‑specific analyses; research assistants collect and validate datasets.

**Technical Requirements** 
1. Access to CRI pilot datasets. Every dataset from raw to final
2. Python


**Quality Assurance and Review** – Cross‑validate findings with domain specialists and DCCE. Maintain a data‑provenance log documenting sources and quality checks.

**Timeline and Milestones** – Months November 2025 - February 2026: complete literature review and gap analysis (Deliver Gap Report by **Feb 28**).


### WP 3 – Development of Improved Impact and Resilience Indices

**Objective** – Develop the Impact Index and the **Resilience Capacity Profile** by synthesizing administrative data into a Social-Ecological System (SES) framework.

**Scope and Key Activities**

- **Impact Index (Fiscal Relief) Improvement:**
    - **Constrained Redistribution (Human Impact):** Execute spatial disaggregation of DOPA district-level population counts using **WorldPop (100m Constrained)** as a weighting mask.
        - _Constraint:_ Ensure the sum of all pixels in a district **exactly equals** the official DOPA "House Registration" count to ensure auditability.
        - _Latent Population:_ Generate a secondary "Emergency Layer" showing the difference between Satellite estimates and Official counts, labeled as "Latent Population" (Prachakon Faeng) for non-budgetary planning.
            
    - **Sector-Specific Economic Disaggregation:**
        - Use **GISTDA/LDD "Agri-Map"** to define the _economic value potential_ (Crop Type Zones).
        - Use **ESA WorldCover (10m)** to refine the _physical extent_ (removing roads/farmhouses from the Agri-Map zones).
            
    - **Urban Exposure Proxy:** Incorporate Commercial Land Use and Industrial GPP layers for non-agricultural zones.

- **Resilience Index (Capacity Profiling):** [[CRI Phase 2 Methodology]]
    - **Indicator Tagging:** Apply the Capacity Tagging framework to the compiled administrative data (LPA, DOPA, etc.).
    - **Composite Scoring:** Aggregate binary (Yes/No) administrative indicators into composite scores for Coping, Adaptive, and Transformative capacities.
    - **Visualization Design:** Develop "Capacity Radar Charts" (Spider Webs) to visualize the three capacities side-by-side for each province, rather than a single aggregate ranking.
        
- **Prototype Construction:**
    - Build the 6 maps of the improved Impact Index.
    - Create the data pipeline to automate the aggregation of LPA/DOPA data into the Resilience Index.
    - Develop the "Data Investment Roadmap" to identify which process-based indicators DCCE should prioritize for future collection.
        

**Inputs / Dependencies** – Data and findings from WP 2.

**Expected Outputs / Deliverables**
- Improved Impact Index with district-level human impact layers.
- **Resilience Capacity Index** structured by SES principles.
- Prototype visualizations (Radar Charts and Maps).
- Policy recommendations for data system improvements.
    

**Timeline and Milestones** – Months February 2026: methodology refinement; Months April - May 2026: build prototype indices.

### WP 4 – Stakeholder Engagement and Pilot Area Implementation

**Objective** – Engage stakeholders to validate the "Capacity Profile" approach and collect feedback on the utility of distinguishing between Coping, Adaptive, and Transformative capacities.

**Scope and Key Activities**

- **Consultations**: <!--note: need team's buy-in first-->
    - **First Consultation (March 2026):** Present the "Middle Path" strategy. Explain the shift from "Risk Ranking" to "Capacity Profiling." Educate stakeholders on the definitions of Coping vs. Adaptive vs. Transformative.
    - **Second Consultation:** Present prototype Capacity Profiles and the Fiscal Relief Index.
        
- **Pilot‑area activities**:
    - Select three high‑risk pilot areas.
    - **Ground-Truthing:** During site visits, validate the "Binary vs. Reality" gap. (e.g., If the database says a province has a 'Climate Plan,' verify if it is operational/funded).
    - Collect qualitative feedback on the "Data Investment Roadmap."
        
- **Feedback integration** – Document feedback to refine the weighting of the Capacity indicators.
    

**Inputs / Dependencies** – Methodological outputs from WP 3; data and gap analysis from WP 2.

**Expected Outputs / Deliverables**
- Meeting minutes and feedback reports.
- Updated index methodologies reflecting stakeholder inputs.
    

**Timeline and Milestones** – March 2026: first consultation workshop; Months April 2026: pilot‑area visits; Month May 2026: second consultation; Month July 2026: dissemination event.

### WP 5 – Finalization, Reporting and Dissemination

**Objective** – Consolidate results from all WPs, finalise the improved CRI, produce reports and communication materials and integrate the index into DCCE’s data systems.

**Scope and Key Activities**

- Compile and edit findings from previous WPs into a **Draft Final Report**, ensuring clarity and alignment with TOR requirements.
- Produce the **Final Report** (Thai language), **Executive Summary** (Thai–English) and digital copies.
- Design and produce communication materials: booklets (A5), exhibition set, ≥3‑minute CRI video, infographics/articles and promotional items.
- Integrate the improved index and risk‑assessment tool into the DCCE Data Center; provide user documentation and data‑entry interface.
- Organise a public dissemination event and final project steering committee meeting.
    

**Inputs / Dependencies** – Finalised indices and feedback from WP 4.

**Expected Outputs / Deliverables**

- Draft Final Report and Final Report with executive summary.
- Communication materials (booklets, exhibition set, video, infographics, promotional items).
- Updated CRI dataset and user‑friendly tool accessible via DCCE Data Center.
    

**Team Roles and Responsibilities** – All experts contribute to report writing; communication specialists (if available) design materials; project coordinator ensures printing and distribution.

**Technical Requirements** – Document editing software, graphic design tools, video production resources, web/data‑portal integration technology.

**Quality Assurance and Review** – Draft report and materials are internally reviewed, then submitted to DCCE for comments before finalisation. Final outputs are checked for accuracy, completeness and accessibility.

**Timeline and Milestones** – Month 7: draft final report; Month 8: final report, communication materials and dissemination.

## 3. Dependency Mapping

| Dependent WP                     | Depends on | Rationale                                                                                    |
| -------------------------------- | ---------- | -------------------------------------------------------------------------------------------- |
| WP 2 – Review and Data Inventory | WP 1       | Requires work plan approval.                                                                 |
| WP 3 – Index Development         | WP 2       | Needs the "Tagged" administrative database and "Urban Proxy" selection to build the indices. |
| WP 4 – Stakeholder Engagement    | WP 3       | Consultations will focus on validating the new "Capacity Profile" outputs.                   |
| WP 5 – Finalisation              | WP 4       | Final report depends on stakehold                                                            |
## 4 Data and Tool Requirements

- **Data Sources** 
    - _Fiscal Relief Index:_ Dept of Provincial Administration (DOPA), Office of Agricultural Economics (Relief Payments), GPP data (NESDC), Land Use (LDD).
    - _Resilience Capacity Index:_ Local Performance Assessment (LPA) from DOPA, Sustainable City Assessment (DCCE), Development Plans (Interior).
    - _Human Impact:_ DOPA Population Registration or Census data.
        
- **Software and Tools** 
    - GIS (QGIS) for dasymetric mapping.
    - Statistical software (Python/R) for normalization and composite scoring.
    - Database systems for managing the "Tagged" indicator library.

## 5 Risk and Mitigation

| Risk                                     | Likely Impact                                                                                                                                              | Mitigation                                                                                                                                                                                                                                               |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metric Validity (Fiscal vs Physical)** | Stakeholders may reject the index if they confuse "Relief Payment" with "Total Damage."                                                                    | Explicitly rebrand the economic component as "**Fiscal Relief Index**" and clearly communicate what it measures. Supplement with Exposure proxies.                                                                                                       |
| **Binary Data Limitations**              | LPA/Administrative data is often Yes/No, leading to low differentiation (clumping) in scores.                                                              | Use **Composite Scoring** (summing multiple binary indicators) and weighted aggregation to create variance.                                                                                                                                              |
| **Stakeholder Confusion**                | The shift from "Risk Map" to "Capacity Profile" may be confusing to technocrats.                                                                           | Develop clear visual aids (Radar Charts) and use the "Capacity Dictionary" to translate academic terms into bureaucratic language.                                                                                                                       |
| **Urban Blindspot**                      | Bangkok/Industrial zones may score "Low Risk" due to lack of agricultural relief data.                                                                     | Mandatory inclusion of **Urban Exposure Proxies** (Commercial Land Use/Industrial GPP) to force recognition of urban economic risk.                                                                                                                      |
| **Line Agency Data Rejection**           | Officials may reject the index if "Satellite Population" contradicts their "House Registration" (Tabien Baan), viewing it as an attack on their authority. | **Strategy: "Constrained Redistribution."** We use satellite data _only_ to distribute their official numbers spatially. We frame the method as "High-Resolution Visualization of Official Statistics," ensuring the totals match their records exactly. |
