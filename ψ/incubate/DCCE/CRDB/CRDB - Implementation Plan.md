---
type: strategy
status: current
version: 9
created: 2025-12-16
last_updated: 2026-02-10
project:
  - DCCE_CRDB
related_hypothesis:
---
>[!note] Change log
v2: update the plan per latest proposal
v3: include specific timeline
v4: increase temporal resolution to week
v5: Realigned deliverables to Enterprise Data Architecture standards.
v6: Incorporated synchronization with UNDP/ADPC BTR Project.
> v7: After KO meeting
> v8: revise focus group meeting agenda and progress meeting timelines
> v9: change after [[Reframe the scope of data system]]
> v10: Updated timeline and deliverables per 2026 Integrated Project Roadmap. Included Inception submission, Joint Risk Review, and "January Brain Drain" mitigation.



***Key changes***
- **NCAIF** is now defined as the **Enterprise Data Model (EDM)**.
- Scope shifted to **Conceptual and Logical Models**; Physical schemas are explicitly out of scope (except for Data Products).
- **Data Catalog** implementation defined as a low-code **Spreadsheet** solution.
- Distinct separation of **Business Metadata** (Glossary) and **Technical Metadata** (Data Dictionaries).

This implementation plan translates the Terms of Reference (TOR) and the accompanying technical proposal into a coherent technical roadmap. It emphasizes designing conceptual frameworks, metadata specifications and workflows rather than building software. The goal is to create a shared understanding among the project team, DCCE and stakeholders about how climate‑adaptation data and knowledge should be organized, catalogued and governed. The structure mirrors the key deliverables identified in the TOR, reframed in data‑engineering terminology.

## Strategic Alignment with UNDP-BTR (ADPC)

To ensure efficiency and avoid duplication with the parallel **UNDP-BTR Project (Task 2 implemented by ADPC)**, this project adopts a specific "Curator vs. Manager" distinction:

| Feature     | **ADPC (BTR Project)**                                                            | CRDB                                                                                                               |
| :---------- | :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Role**    | **The Builder & Curator**                                                         | **The Architect & Librarian**                                                                                      |
| **Scope**   | **Visualizing** 5 Official Historical Hazards (Flood, Drought, Heat, Storm, SLR). | **Managing** the full Adaptation Data Ecosystem (Risk gaps, Future projections, Vulnerability, Strategy, Results). |
| **Output**  | **Physical Risk Platform** (The "Showroom").                                      | **Enterprise Data Model & Governance** (The "Archive System").                                                     |
| **Synergy** | ADPC collects the specific files; CRDB catalogs them.                             | CRDB codifies ADPC's operational rules into long-term DCCE policy.                                                 |
|             |                                                                                   |                                                                                                                    |

## Relationship with adaptation M&E

| **Component**     | **BTR Project (WP-3 & WP-4)**                                                                                                                                                                                               | CRDB Project                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **M&E Framework** | **The Lead Designer (WP-4):** Developing the Data Reference Sheet, Translation Matrix, and prioritizing CU indicators.                                                                                                      | **The Data Supplier:** CRDB focuses solely on architecting the **"Physical Baselines"** (Hazard/Climate Data) that BTR WP-4 requires to calculate its "Climate Baseline" indicators. |
| **Action**        | **CRDB Outcome:** We effectively "outsource" the M&E taxonomy work to BTR WP-4. Our deliverables will reference the BTR M&E Toolkit as the standard for Stage 5 (Results), while we focus our effort on **Stage 2 (IVRA)**. |                                                                                                                                                                                      |

---


## Key Project Deliverables and Strategic Framing

**Strategic Focus: IVRA-First Architecture**

This project adopts an **incremental, use-case-driven approach** to data architecture design. Rather than attempting enterprise-wide transformation, we focus on establishing the **IVRA (Identification, Vulnerability & Risk Assessment) data system** as the foundational layer. This system will serve as the "prime example" of modern data management within DCCE, with future divisions linking their systems to this core.

The deliverables are designed as **System Requirements** for future IT infrastructure procurement, not software implementations. They provide the conceptual and logical blueprints that will enable DCCE to request budget for a modern Data Lakehouse in subsequent fiscal years.
### 1. National Climate Adaptation Information Framework (NCAIF)

**Type:** Business Taxonomy / Knowledge Hierarchy

**Purpose:**
- Enable non-technical stakeholders to navigate climate adaptation concepts
- Provide consistent terminology (Business Glossary)
- Organize data catalog tags

**Scope:**
- **Deep Modeling:** IVRA domains (Meteorology, Hazards, Exposure, Vulnerability, Impacts, Loss & Damage)
- **Shallow Modeling:** Adaptation actions and M&E results (external integration points)

**Artifacts:**
- Hierarchical knowledge structure document
- Business Glossary spreadsheet

**NOT Included:** Entity relationships, cardinality, data flows


### 2. Conceptual Data Model (CDM) for IVRA System

**Type:** Entity-Relationship Model

**Purpose:**
- Define the core entities and relationships for risk assessment data
- Establish business rules governing data integrity
- Serve as foundation for Logical and Physical models

**Scope:**

- **Primary Focus:** Risk assessment workflow entities
    - Climate/Meteorological Events
    - Hazard Events
    - Exposed Assets (Population, Infrastructure, Agriculture)
    - Vulnerability Factors
    - Adaptive Capacity Indicators
    - Impact Assessments
    - Response Actions
    - Loss & Damage Records

**Derivation Method:**
- **Use-Case Driven:** Model entities based on actual risk assessment questions:
    - "Which areas are exposed to flood hazards?"
    - "What is the economic loss from drought in agricultural sector?"
    - "How does adaptive capacity reduce vulnerability?"

**Artifacts:**
- **Conceptual ERD:** High-level entity-relationship diagrams
- **Entity Definitions:** One-paragraph description of each entity's purpose
- **Relationship Specifications:** Cardinality and optionality rules
- **Business Rules Document:** Constraints and validation requirements

### 3. Data and Knowledge Assets

**A. Risk Assessment Data Catalog**

A structured spreadsheet-based catalog registering datasets essential to IVRA workflows:

- **Coverage:** Hazard, exposure, vulnerability, and climate projection datasets
- **Metadata Depth:** Full technical specifications
    - Spatial: Resolution, coordinate system, coverage extent
    - Temporal: Time period, update frequency, temporal resolution
    - Format: File type, schema, access method
    - Quality: Completeness, accuracy assessments, known limitations
    - Provenance: Source agency, collection methodology, version history
- **Taxonomy:** Tagged according to NCAIF risk assessment categories

**B. Information Product Inventory (Business Context)**
Catalog of analytical products with emphasis on risk outputs:

- **Priority Products:**
    - Spatial Climate Risk Map (lineage traced to Bronze/Silver layers)
    - Climate Risk Index (source datasets linked to Baseline Inventory)
    - Sector risk assessments
- **Metadata:** Purpose, business value, analytical methods, version, owner, use cases

**C. External System Assets (Lightweight Cataloging)**
For M&E and adaptation datasets:
- **Business Metadata Only:** Name, owner, description, thematic category
- **Purpose:** Enable discovery and avoid duplication, not full technical documentation
- **Rationale:** Detailed data dictionaries are the responsibility of respective system owners (CU team for M&E)

**Artifacts:**
- **Risk Assessment Data Catalog:** Spreadsheet with ~50-100 essential datasets
- **Information Product Inventory:** ~20-30 products with full lineage for risk outputs
- **External System Registry:** Lightweight catalog of M&E/GHG datasets for cross-reference

### 4. Minimum Viable Dataset for Loss & Damage Reporting

Framed as the **Logical Data Model for the Loss & Damage subject area** within the EDM:

**A. Core Entities**
- **Event:** Disaster type, location, date, intensity, duration
- **Impact:** Affected population, infrastructure damage, economic losses by sector
- **Response:** Emergency actions, evacuation statistics, relief distribution
- **Recovery:** Reconstruction costs, timeline, resilience improvements

**B. Alignment**
- **DDPM PDNA Framework:** Mapped to post-disaster assessment phases
- **Sendai Framework:** Indicators for disaster loss reporting (Targets A-G)
- **International Standards:** DesInventar, UNDRR guidelines

**C. Implementation**
- Logical model (entities, attributes, relationships)
- Validation through pilot data collection from ≥3 historical events
- Integration with DDPM's existing reporting workflows

**Artifacts:**
- **Loss & Damage Logical Data Model:** Entity-relationship diagrams with attribute specifications
- **Pilot Report:** Validation results from historical disaster events


### 5. Data Governance Framework (Risk Database Charter)

Rather than an unreadable enterprise-wide policy, this deliverable provides **actionable governance for the Risk Assessment Database:**

**A. Role Definitions (Specific Assignments)**
- **Data Owner:**
    - Who owns the Risk Baseline? (Risk Assessment Division vs. source agencies)
    - Decision authority for data access, retention, quality standards
- **Data Custodian:**
    - IT responsibilities for storage, backup, security
    - Technical maintenance of catalog and metadata
- **Data Steward:**
    - Subject matter experts responsible for validation
    - Quality checks before Silver layer promotion

**B. Service Level Agreements**
- **Update Frequency:** "Hazard maps updated annually; baseline exposure every 2 years"
- **Availability:** "Risk data accessible to M&E system via API with 99% uptime"
- **Response Time:** "Data requests processed within 5 business days"

**C. Data Quality Standards**
- **Completeness:** Minimum coverage requirements (e.g., "85% of provinces")
- **Accuracy:** Validation rules (e.g., "Exposure totals reconcile with NSO census")
- **Timeliness:** Age thresholds (e.g., "Climate projections <5 years old")

**D. Data Lineage Documentation**
- **Bronze → Gold Traceability:** Document transformations for key indicators
- **Provenance Tracking:** Source agency, collection date, processing history
- **Audit Trail:** Changes to datasets logged with justification

**Artifacts:**
- **Risk Database Governance Charter:** 10-15 page document with role assignments and SLAs
- **Data Quality Rule Book:** Validation checklist for Silver layer promotion
- **Lineage Documentation Template:** Standard format for tracing data flows


### 6. Stakeholder Engagement (Validation & Buy-In)

Engagement activities are strategically sequenced to build incremental consensus:

**A. Internal DCCE Focus Groups (Iterative Validation)**
- **FGD 1 (Late-Jan):** Ecosystem mapping with GHG/M&E/Risk Index project owners
    - Goal: Position NCAIF as integration hub, not competitor
    - Output: Technical constraints checklist, interface requirements
- **FGD 2 (Early-Mar):** Prototype validation with Risk Assessment Division
    - Goal: Test "seed use cases" (e.g., flood risk workflow)
    - Output: Validated conceptual model, revised metadata requirements
- **FGD 3 (Mid-May):** Governance roadmap finalization
    - Goal: Agree on Data Owner/Custodian roles, SLAs
    - Output: Endorsed governance charter

**B. External Stakeholder Workshops**
- **Public Hearing (April):** Present NCAIF and architecture to 50+ stakeholders
    - Gather feedback on practicality and completeness
    - Validate integration points with partner agencies (GISTDA, DDPM, TMD)
- **Dissemination Event (June-July):** Showcase catalog and governance framework
    - Demonstrate data lineage tracing
    - Training on using the spreadsheet catalog

**Deliverables:**
- FGD summary reports with validated artifacts
- Public hearing feedback synthesis
- Training materials for catalog usage


---
## Work Packages and Activities

The project is organized into six work packages (WPs) that collectively deliver the above components. Each package describes objectives, key tasks and deliverables.


## Work Package 1 – Project Initiation and Inception

**Objective:** Establish a shared understanding of project scope, refine TOR language into technical terms and develop detailed plans.

### Key activities and timeline

- [x] **Kick‑off and scope refinement (Dec 2025).** Review the TOR with DCCE to clarify expectations. Note that project outputs are now framed as "System Requirements" for a future IT infrastructure implementation phase.

- [x] **Work plan and inception report (Dec 2025 – Jan 2026).** Develop a work breakdown structure and draft the inception report. The inception report is targeted for delivery by **7 January 2026**.
    
- **Stakeholder mapping and engagement plan (Jan 2026).** Identify data owners, stewards, users and influencers and draft a stakeholder‑engagement plan covering interviews, focus groups and dissemination events. The mapping runs from late December through the second week of January.
    
- [x] **Baseline review of international platforms and DCCE systems (Dec 2025 – Jan 2026).** Conduct desk research on adaptation information platforms and DCCE systems to inform conceptual model. This aligns with task 5.2.1 and now concludes by January 2026
    
- [x] **Joint Risk Review (Jan 2026):** Collaborate with BTR/CRI teams to review climate risks across 6 NAP Sectors (Water, Agriculture, Tourism, Health, Natural Resources, Human Settlement) to inform the initial Data Landscape.

**Deliverable:** Inception report (submitted Jan 7, 2026) and stakeholder engagement plan.

### Timeline

| Month        | Activities                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Nov 2025** | scope refinement; begin work plan & inception report (mid‑month); stakeholder mapping; baseline review begins    |
| **Dec 2025** | Kick‑off & Complete work plan & inception report; finalize stakeholder engagement plan; continue baseline review |
| **Jan 2026** | **Submit Inception Report (Jan 7)**; Joint Risk Review; Complete baseline review                                 |

## Work Package 2 – Data Landscape and Requirements Assessment

**Objective:** Understand existing data flows, systems and user needs to inform the NCAIF, data‑system design and inventories.

### Key activities and timeline

- [x] **Desk research & benchmarking (Dec 2025 – Jan 2026).** Analyze international adaptation platforms’ data models and governance structures and compare these with DCCE’s current systems. This work overlaps with the end of task 5.2.1 and the start of tasks 5.3.1–5.3.2. Document Business Logic

- [ ] **Preliminary Use Case Drafting (Jan – Feb 2026).** Develop "seed" use cases (e.g., specific flood risk scenarios) to guide stakeholder discussions, ensuring they can react to concrete examples rather than abstract concepts.

- [x] **Disaster Risk Management Landscape research (Dec 2025 - Jan 2026):** review DDPM's documents on disaster data collection and PDNA [[Post Disaster Needs Assessment report by DDPM]] implementation progress. Linked to the ongoing PDNA capacity building in the human settlement sector

- [x] **Current‑state assessment (Dec 2025 – Jan 2026).** Document existing datasets, data flows, storage formats and metadata practices at DCCE and partner agencies. Task 5.3.1 in the workplan begins in December.
    
- [ ] **User‑requirement interviews (Feb – Mar 2026).** Conduct at least ten interviews with data producers and consumers, capturing use cases, pain points and required metadata. Interview activities now commence in the first week of February and extend through March.
    
- [ ] **Data Quality & Schema Assessment (Feb 2026):** Evaluate "Risk Assessment" datasets to prepare for Technical Metadata extraction.
    

**Deliverable:** Data landscape & gap report, interview summaries and system diagrams, due by the second week of March 2026.

### Timeline

| Month        | Activities                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| **Jan 2026** | Begin desk research & benchmarking; current‑state assessment                                                |
| **Feb 2026** | Begin user interviews and focus groups; perform GIS readiness assessment; start synthesising early findings |
| **Mar 2026** | Finalise interviews; synthesise findings; draft and deliver the data landscape & gap report                 |

## Work Package 3 – Data Model (EDM) & NCAIF Design

**Objective:** Develop conceptual models for the Data Lakehouse,  Business Artifacts, Conceptual Models, and specific Logical Models.

### Key activities and timeline

1. **Develop NCAIF Business Taxonomy (Jan-Feb 2026):**
    - **Drafting NCAIF (Jan):** Principal Researcher defines the business logic/hierarchy.
    - Create hierarchical knowledge structure
    - Produce Business Glossary

2. **Design Conceptual Data Model for IVRA (Feb-Mar 2026):**
    - **Use-Case Workshops:** Run 3-5 "seed scenarios" with Risk Assessment Division
        - Scenario 1: Flood risk assessment in coastal provinces
        - Scenario 2: Drought impact on agriculture
        - Scenario 3: Heat wave effects on public health
    - **Entity Identification:** Extract entities from use cases (Hazard Event, Exposed Asset, etc.)
    - **Relationship Mapping:** Define how entities connect (affects, has, results_in)
    - **Business Rule Capture:** Document constraints and validation requirements
    - **ERD Production:** Create conceptual entity-relationship diagrams

3. **Develop Logical Model for Loss & Damage (Mar-Apr 2026):**
    - Translate CDM's LOSS_DAMAGE_RECORD entity into detailed specifications
    - Align with DDPM PDNA and Sendai Framework

4. **Map CDM to Data Lakehouse Architecture (Mar-Apr 2026):**
    - Show how Bronze raw data feeds Silver CDM entities
    - Define Gold layer products derived from CDM relationships

    
5. **Execute Strategic Internal Focus Groups (Jan – May 2026).** Three sessions designed to iterate the NCAIF by engaging DCCE staff:
	- **FGD 1 (Late-Jan): Exploratory Ecosystem Mapping.** Engage Project Owners of parallel initiatives (GHG, M&E, Risk Index) to map technical constraints. Understand their lessons from implementing data platforms. Probe in to potential integration while central data governance and models do not exist yet. Learn their needs, treat them as our customers
	    
	- **FGD 2 (Early March): Prototype Pre-Validation.** Walk through "Seed Use Cases" and the Draft NCAIF Business Artifact to "bulletproof" the design internally before the Public Hearing.
	    
	- **FGD 3 (Mid-May): Governance & Roadmap.** Synthesize feedback from the April Public Hearing to finalize the Governance Framework and agree on the "Data Owner" vs. "Custodian" roles for future implementation.

6. **Conduct a public hearing event on draft NCAIF & architecture (April 2026**): engage a broad group of stakeholder to present the landscape of climate change adaptation information that DCCE will use as a blueprint to develop data system in the future. 

**Deliverables:**
- NCAIF Business Taxonomy (hierarchy + glossary)
- Conceptual Data Model for IVRA (ERD + entity definitions + business rules)
- Logical Data Model for Loss & Damage
- Data Lakehouse Architecture linked to CDM
- Governance Charter with entity-based role assignments

    
### Timeline

| Month        | Activities                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jan 2026** | Begin refining NCAIF ontology and conceptual data flows; draft data system artifacts ; hold the first focus group                                 |
| **Feb 2026** | Continue ontology & data‑flow design; start drafting the data‑governance framework; continue metadata service design; hold the second focus group |
| **Mar 2026** | Continue metadata and governance design; produce the conceptual data‑architecture document                                                        |
| **Apr 2026** | Conduct a public hearing event on draft NCAIF & architecture                                                                                      |
| **May 2026** | Revise NCAIF and governance framework; hold the third focus group on the revised NCAIF and data governance                                        |
| **Jun 2026** | Finalise and deliver the NCAIF specification, metadata schema and governance framework                                                            |

## Work Package 4 – Development of Data Assets (Catalog & Dictionaries)


**Objective:** Populate the Baseline Data Inventory and Information Product Catalog, design the MVD schema and perform gap analysis.

### Key activities and timeline

- **Create Business Glossary (Jan 2026):** Define business terms associated with the NCAIF entities.
- **Draft Technical Metadata & Data Dictionaries (Jan – Apr 2026):** Create detailed data dictionaries for the identified "essential risk assessment" areas.
    
- **Dataset and product registration (Jan – Apr 2026).** Collect datasets from DCCE, DDPM, GISTDA, universities and partners; populate the Baseline Data Inventory and register products in the Information Product Catalog.
    
- **Implement Data Catalog (Apr – May 2026):** Build the **Spreadsheet-based Data Catalog** that allows users to search through the Data Dictionaries and Data Products.
    
- **Gap analysis (late Apr – early May 2026).** Compare user requirements with populated inventories to identify missing datasets, insufficient metadata or unaddressed use cases. This analysis begins in the last week of April and continues into the first week of May.
    
- **Prototype demonstration & focus group (Apr – Jun 2026).** A focus group on the prototype is held in late April; the demonstration itself runs through May and early June, piloting the MVD and inventories using a past disaster event and tracing data lineage through the NCAIF. Feedback is collected to refine templates.

- **Map Data Lineage (May 2026):** Document the flow from Bronze (Raw) to Gold (Product) for key indicators.
    
- **Finalise inventories and MVD (May – Jul 2026).** Compile final inventories with recommendations and integrate them into the data‑governance framework. Work begins in the third week of May and concludes by mid‑July.
    

**Deliverables:** 
1. Business Glossary.
2. Technical Data Dictionaries.
3. Functional Spreadsheet Data Catalog.
4. Gap analysis & pilot report (mid Jun 2026)
5. Final inventories with recommendations (mid Jul 2026).

### Timeline

| Month        | Activities                                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Mar 2026** | Data product spread sheet design; dataset & product registration                                                                   |
| **Apr 2026** | Complete data product spread sheet ; continue registration; host prototype focus group and climate‑data use‑case workshop          |
| **May 2026** | Conduct gap analysis (last week of April and first week of May); begin finalising inventories & MVD; start prototype demonstration |
| **Jun 2026** | Continue finalising inventories & MVD; deliver pilot demonstration results                                                         |
| **Jul 2026** | Complete inventories and provide recommendations (deliverable mid‑Jul)                                                             |

## Work Package 5 – Knowledge Synthesis, Stakeholder Engagement and Dissemination

**Objective:** Synthesize adaptation knowledge (specifically IVRA) to support the BTR Adaptation Chapter, design communication materials, and validate outputs.

**Key activities and timeline**

- **Knowledge synthesis & IVRA Review (Jan – Feb 2026):** Conduct a systematic review of the _Climate Change Risk and Impact (IVRA)_ study and other government reports. **This activity has been front-loaded to January** to directly feed into the UNDP-BTR Task 1 (Adaptation Chapter) and CRI project gap analysis.
- **Communication materials (late Apr – Jun 2026):** Develop infographics and mock-ups illustrating how the NCAIF supports policy.
- **Dissemination events (Jun – Jul 2026):** Support DCCE in hosting dissemination workshops.
    

**Deliverables:** 
1. Knowledge synthesis report
2. validated inventories & MVD
3. training materials, 
4. communication products and workshop summary, due July 2026.

### Timeline
| **Month**    | **Activities**                                                                             |
| ------------ | ------------------------------------------------------------------------------------------ |
| **Jan 2026** | **Begin comprehensive IVRA & Knowledge Synthesis (High Priority);** Identify stakeholders. |
| **Feb 2026** | **Complete initial IVRA review for BTR input;** conduct focus-group sessions.              |
| **Mar 2026** | Integrate insights from user interviews into synthesis.                                    |
| **Apr 2026** | Conduct workshops on NCAIF & data architecture; host prototype focus group.                |
| **May 2026** | Develop communication materials; conduct third focus group.                                |
| **Jun 2026** | Publish draft communication products; prepare dissemination event.                         |
| **Jul 2026** | Host dissemination workshop.                                                               |
|              |                                                                                            |
## Work Package 6 – Evaluation, Recommendations and Closure

**Objective:** Evaluate project outputs, consolidate recommendations for future implementation and ensure knowledge transfer.

### Key activities and timeline

 - **Evaluation (Jun – Aug 2026):** Assess if the Spreadsheet Catalog and Logical Models effectively support DCCE's data discovery needs.
- **Recommendations (Aug 2026):** Roadmap for future _Physical_ implementation (e.g., moving from Spreadsheet to a dedicated Data Catalog software, or implementing the Data Lakehouse)
- **Final documentation (Aug – Sep 2026).** Compile all deliverables into a final project report and executive summary. The final report is due **4 September 2026** but we must submit 2 weeks earlier. 
- **Knowledge transfer (Aug 2026).** Conduct handover sessions with DCCE staff to explain how to maintain and update the inventories and apply the MVD and governance guidelines.
    

**Deliverables:** Project evaluation report, recommendations & roadmap, final project report and executive summary, and knowledge‑transfer materials, due August 2026.

### Timeline

|Month|Activities|
|---|---|
|**Jun 2026**|Begin evaluation and draft final documentation|
|**Jul 2026**|Continue evaluation; compile documentation|
|**Aug 2026**|Complete evaluation; deliver recommendations & final reports; conduct knowledge‑transfer sessions|

## Summary Timeline by Work Package
| **Deadline**    | **Project** | **Deliverable / Milestone**                                   |
| --------------- | ----------- | ------------------------------------------------------------- |
| **07 Jan 2026** | **CRDB**    | **Milestone 1: Inception Report**                             |
| **07 Apr 2026** | **CRDB**    | **Milestone 2: Interim Report** (Covers TOR 5.2/5.3 Progress) |
| **06 Jul 2026** | **CRDB**    | **Milestone 3: Draft Final Report**                           |
| **04 Sep 2026** | **CRDB**    | **Milestone 4: Final Report **                                |
#### Interim Report
** Note that the practical submission deadline is on 27 March since DCCE request us to submit the bill and get paid by the end of March 2026
- interview results
- the first 2 internal DCCE focus group discussions results
- drafted NCAIF
- data landscape review
- IVRA review

#### Draft Final Report
- public hearing and brainstorming workshops results
- baseline data inventory
- information product inventory
- Minimum Viable Dataset for Loss and Damage
- Output from TOR 5.5
- Data gap analysis
- Improved NCAIF

---
# Engagement & Workshop Schedule

| **Month**      | **Project / Lead** | **Event Name**                     | **Purpose**                                                                 |     |
| -------------- | ------------------ | ---------------------------------- | --------------------------------------------------------------------------- | --- |
| **Jan 2026**   | **CRDB**           | **Focus Group #1 (Internal)**      | Ecosystem Mapping & Technical Constraints (with GHG & M&E owners).          |     |
| **Feb 11**     | **BTR (ADPC)**     | **Consultation Meeting**           | Validate datasets with DCCE/DDPM. (CRDB Team observes for Metadata).        |     |
| **Mar ( 4th)** | **CRDB**           | **Focus Group #2**                 | Internal check on Data Landscape & Prototype Validation.                    |     |
| **Apr (Late)** | **CRDB**           | **Public Hearing & Brainstorming** | Present NCAIF Data Architecture and engage stakeholders on the value chain. |     |
| **Jun (Late)** | **CRDB**           | **Dissemination Meeting**          | Hand over platform/catalog and closure.                                     |     |

---

# Risks and Mitigation

| Risk                                       | Potential Impact                                              | Mitigation                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Limited data sharing**                   | Incomplete inventories; delays in cataloguing datasets        | Leverage ADPC data collection process                                                                                                                    |
| **Heterogeneous data quality**             | Difficulties in standardising datasets; unreliable analyses   | Leverage ADPC data collection process                                                                                                                    |
| **Confusion over "Logical" vs "Physical"** | Stakeholders expect a built database but get a diagram/model. | **Early Expectation Management:** Explicitly define "EDM" and "Logical Model" in the Kick-off. Emphasize that physical data stays in source databases.   |
| **Spreadsheet Limitations**                | The catalog becomes too large or complex for a spreadsheet.   | **Strict Scope Control:** Focus the catalog on "Essential Risk Assessment" areas first. Design the spreadsheet with a future database migration in mind. |
| **Complexity of Business Logic**           | NCAIF hierarchy becomes too academic and unusable.            | **User-Centric Validation:** Treat the NCAIF as a "Business Artifact" and validate it with non-technical staff early (WP3).                              |
