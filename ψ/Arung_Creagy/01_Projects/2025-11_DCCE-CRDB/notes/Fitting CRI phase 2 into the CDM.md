---
status: archived
tags: []
created: 2026-02-11
last_updated: 2026-02-11
AI_prompt: false
AI_output: false
project:
  - DCCE_CRDB
type: note
---
[[Conceptual Data Model for climate risk and adaptation data system]]

In this sense, the Resilience_Index is an outcome of the intervention result which is an action of adaptation. however, I think CRI phase 2 frame the Resilience Index not as just an outcome but also a tool to guide actions of local government. Or it does not matter, this nuance will result in the same CDM?

There is a distinction between an **Index as a Result** (retrospective/M&E) and an **Index as a Decision Support Tool** (prospective/planning).

While both nuances can technically reside within the same schema, this shift in perspective—from a static score to a "Structural Readiness" profile—actually strengthens the utility of the **Recursive Pattern** in your CDM.

### 1. How the CDM Accommodates Both Perspectives

The CDM handles this by separating the **Structure** (the logic) from the **Assessment** (the data snapshot).

- **As an Outcome (M&E):** The `RESILIENCE_ASSESSMENT` entity captures a "Point-in-Time" snapshot after an `ADAPTATION_PROJECT` has been completed. This proves that the `INTERVENTION_RESULT` successfully improved the score.
    
- **As a Planning Tool (CRI Phase 2):** The `RESILIENCE_STRUCTURE` acts as a **Gap Analysis Template**. By examining which "Tags" (indicators) are missing, the local government identifies precisely which structural mechanisms they lack (e.g., "We have 0% on Land Use Planning Enforcement").
    

### 2. The Nuance: "Structural Readiness" vs. "Operational Excellence"

The CRI Phase 2 methodology explicitly frames the index as a measure of **Structural Readiness** (the existence of mechanisms) rather than just "Operational Excellence".

This has a critical impact on your data architecture:

- **The CDM remains the same**, but the **input values** for `RISK_METRIC` change. Instead of measuring a variable that changes daily (like water levels), you are measuring the **existence of a governance process** (a binary "Yes/No").
    
- The `COMPOSITE_INDEX` is no longer just an "Outcome Score"; it becomes a **Maturity Level**.
    

### 3. Bridging the Gap: The "Profile" Logic

CRI Phase 2 focuses on **"Capacity Profiles"** via Radar Charts rather than a single rank. This is where the CDM’s recursive logic becomes a powerful tool for local government guidance:

|**Feature**|**Outcome Focus (Standard Index)**|**Guidance Focus (CRI Phase 2)**|
|---|---|---|
|**Logic**|"How much did we improve?"|"Where is our greatest structural deficit?"|
|**CDM Entity**|`INTERVENTION_RESULT` updates the `COMPOSITE_INDEX`.|`RESILIENCE_STRUCTURE` highlights missing `VULNERABILITY_DETERMINANT` links.|
|**Action**|Report to DCCE.|Local Governor reallocates budget based on the **Radar Chart axes** (e.g., pivot from Coping to Transformative).|

### 4. Technical Conclusion

The nuance **does not require a change to the CDM tables**, but it requires a specific **metadata configuration**:

1. You must treat the `RESILIENCE_FRAMEWORK` not as a static formula, but as a **Policy Roadmap**.
    
2. The `VULNERABILITY_DETERMINANT` entity must be able to link to **"Soft" attributes** (governance, power, agency) as highlighted in the literature, which your "Capacity Tagging" protocol addresses by categorizing administrative data.
    

By keeping the CDM as is, you ensure that the system can serve the **DCCE** (for national reporting and M&E) and the **Local Government** (for identifying planning gaps) simultaneously.