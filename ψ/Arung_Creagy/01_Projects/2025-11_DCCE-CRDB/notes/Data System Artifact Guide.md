---
status: archived
tags: []
created: 2026-01-09
last_updated: 2026-01-18
AI_prompt: false
project:
  - DCCE_CRDB
type:
  - Artifact
aliases:
  - Idea / note
color: var(--mk-color-green)
---
>[!important] Update
>- [[Reframe the scope of data system]] according to the reframing


# Summary of Artifacts
### 1. Data Modeling Artifacts 
These artifacts define the structure and relationships of the data ecosystem.

1. **NCAIF Business Artifact:** The "Business Logic" layer. A hierarchical knowledge structure mapping the TOR domains (Meteorology, Risk, Adaptation, Results) to standard definitions.
	- **Meteorology & Risk (Stages 1 & 2):** Develop full granular hierarchies (e.g., Flood -> Fluvial vs. Pluvial -> Depth/Duration). This is where you spend 80% of your modeling effort.
    
	- **Adaptation & Results (Stages 3 & 5):** Keep these high-level. Do not attempt to model every "Adaptation KPI." Instead, model them as **"External Consumption Points"**—placeholders where the M&E system _connects_ to the Risk system.
	    
2. **Enterprise Data Model (EDM):**
	1.  **Conceptual Layer:** Show the "Risk Data Store" as the central engine. Show M&E and GHG as _external systems_ that consume data from it.
    
	2. **Logical Layer:** You only build Logical Models (Entities, Attributes, Keys) for **Risk Assessment Inputs** (Hazards, Exposures, Vulnerabilities) and **Loss & Damage**. **Stop** trying to build Logical Models for "Adaptation Projects" or "Finance Flows"—leave that to the CU team.
            
3. **Loss & Damage Logical Model:** Formerly the "MVD," this details the specific entities (events, impacts) required for Sendai Framework reporting.
    
4. **Business Glossary:** A dictionary of business terms (e.g., "Flood Exposure") linked to the NCAIF structure.
    

### 2. Data Assets & Catalog 

These are the tangible deliverables that allow users to find and understand data.

1. **Baseline Data Inventory:** A **Data Catalog** implemented as a structured spreadsheet. It registers raw datasets with metadata like provenance and resolution.
	- For the "Risk" datasets, you need **Technical Metadata** (Resolution, File Format, Coordinate System). 
	- For "M&E" datasets, you only need **Business Metadata** (Name, Owner, Description) so people know they exist, but you don't need to document their columns.
	    
2. **Information Product Inventory:** A catalog of analytical products (indices, maps) describing business value and lineage.
    
3. **Technical Data Dictionaries:** Detailed technical descriptions (tables, columns, types) specifically for risk assessment datasets.
    

### 3. Governance & Architecture 

These artifacts define how the system operates and is controlled.

1. **Data Management Framework:** A conceptual design for a **Data Lakehouse** using Medallion Architecture (Bronze/Silver/Gold layers). <!--comment: this could be low priority-->
    
2. **Data Governance Framework:**
    
    - **Role Definitions:** Specifications for **Data Owner** vs. **Data Custodian**. <!--comment: this is necessary-->
        - Instead of writing a "DCCE-wide Data Policy" (which no one will read), write the **"Governance Charter for the Risk Database."**
    	- Define who owns the **Risk Baseline**: Is it the Risk Division? Or do they aggregate it from GISTDA?
		- Define the **Service Level Agreement (SLA):** "We promise to update the Hazard Map once a year so M&E can use it."
            
    - **Data Quality Standards:** Validation rules and standards. <!--comment: note sure how to do it-->
        
    - **Data Lineage Documentation:** Documentation of data flow from source to product. <!--comment: this is crucial-->