---
status: archived
tags: []
created: 2026-02-16
last_updated: 2026-02-16
AI_prompt: false
AI_output: false
project:
  - DCCE_CRDB
type: note
---
Here is the chronological summary of the architectural refinement steps we have taken for the  (Subject Area 4)** of the National Climate Adaptation Information System.

### Phase 1: Diagnosis & De-Linearization

**The Starting Point:** The initial CDM treated Adaptation Planning as a linear list of projects (`ADAPTATION_PROJECT`) derived simply from risk metrics.

**The Critique:** We identified that this structure failed to capture the **iterative** and **cyclic** nature of decision-making described in the IPCC and CRM frameworks.

**Key Realization:** The model needed to support **Risk Layering** (treating low vs. high risks differently) and **Adaptive Pathways** (sequencing decisions over time).

### Phase 2: The "Strategic Lock-in" Pivot

**The Proposal:** We initially considered hard-coding entities like `RISK_LAYER` and `TIPPING_POINT` to force these advanced methodologies.

**The Constraint:** You correctly identified that Thailand’s current management context is not ready for "Deep Uncertainty" frameworks like DAPP, and hard-coding them would create "strategic lock-in" and empty tables.

**The Refinement:** We shifted to a **"Descriptive, Not Prescriptive"** architecture. We decided to model the _properties_ that enable these advanced methods without enforcing them as constraints.

- **Action:** Replaced rigid `RISK_LAYER` entities with flexible **Taxonomies** to categorize projects.
    
- **Action:** Replaced complex "Pathways" with simple **Dependency Links** (`prerequisite_id`) to allow phasing without complexity.
    

### Phase 3: Decoupling "Project" from "Value" (The Appraisal Engine)

**The Problem:** We faced the challenge of "Varying Frames." Different researchers use different methods (CBA, MCA, Robustness) to evaluate projects, meaning we couldn't just add a `bcr_ratio` column to the project table.

**The Solution:** We elevated **Appraisal** to a first-class entity to separate the _engineering potential_ from the _policy value_.

- **New Entity:** **`APPRAISAL_EVENT`** (The Header: Who/When/Method).
    
- **New Entity:** **`APPRAISAL_METRIC`** (The Detail: Key-Value pairs for scores).
    
- **Benefit:** This creates a **Decision History**, allowing the system to store multiple evaluations for the same project over time (e.g., "Economically Viable" in 2025 vs. "Socially Preferred" in 2027).
    

### Phase 4: Integrating Deep Research (Context & Portfolios)

**The Input:** The "Deep Research" report highlighted that decision-making starts with defining the _problem_ (Cynefin framework) and often involves selecting _bundles_ of actions (Portfolios).

**The Refinement:** We added wrapper entities to structure the inputs and outputs of the planning process.

- **New Entity:** **`DECISION_CONTEXT`** to define the scope (e.g., "National Flood Plan") and uncertainty type (Simple vs. Complex).
    
- **New Entity:** **`ADAPTATION_PORTFOLIO`** to group multiple options (Green + Grey + Soft) for collective evaluation.
    
- **New Entity:** **`RISK_TOLERANCE_PROFILE`** to explicitly encode stakeholder risk appetite, ensuring the system is "value-based" as required by the CRM synthesis.
    

### Summary of the Current Architectural State

We have moved from a **"Project List"** model to a **"Decision Support"** model. The current design allows the DCCE to:

1. **Define the Problem** (`DECISION_CONTEXT`).
    
2. **Define the Rules** (`RISK_TOLERANCE`).
    
3. **Bundle the Options** (`PORTFOLIO`).
    
4. **Record the Evidence** (`APPRAISAL`).
    
5. **Track the Execution** (`PROJECT` with `CLASSIFICATION` tags).


# My critique 
1. RISK_TOLERANCE is not a familiar concept and I am certain that risk tolerance has never been documented or understood in any climate change adaptation projects. Risk tolerance for line agencies who are the main adaptation project implementors is unclear since they are not the beneficiaries or the affected by climate impacts
2. The concept of `Portfolio` has never been established. The closet we have had is [[Analysis of NAP Indicators and Adaptation M&E Contribution (TDRI version)]] which still treats adaptation projects as separate individuals and has no concept of 'uncertainty' in the planning
