---
type: ai_output
tags: []
status: archived
capture_date: 2026-01-06
origin_prompt: "use the guiding questions to draft a data gap review process doc for CRI both phase 1, improving the granularity of CRI, and phase 2, developing resilience and readiness indices with concept demonstration. Leave the questions about search and discovery of datasets out when crafting the procedural steps\r\rThis  doc aims to guide the project manager and junior analyst to produce useable data requirements to feed to ADPC and CRDB projects"
relevance_to: "[[]]"
---
**Objective:** This is not a general data search. This is an **Audit** of the CRI Pilot assets to answer the 4 Decision Points in [[CRI Phase 1 Methodology]].

Owner: Boss & Tonklar

Timeline: Immediate (Prior to Feb 11 ADPC meeting)

# Step 1: The Raw File Audit  

>[!note] Do we have actual data that is used for the CRI choropleth map?


_Action: Open the CRI Pilot Excel File._
- **Check 1: Human Impact Sparsity (Decides Dasymetric Feasibility)**
    - **Task:** Count the non-zero rows for "Total Deaths" and "Affected People."
    - **Decision Rule:**
        - If **> 50 provinces** have data $\rightarrow$ We **CAN** do Dasymetric Mapping.
        - If **< 20 provinces** have data $\rightarrow$ We **MUST** Model Human Impact (just like Economic Loss).

>[!note] These numbers are made up. Need to discuss

- **Check 2: "Ground Truth" Quality (Decides Modeling Threshold)**
    - **Task:** Isolate the data for the 5 Pilot Provinces (Chumphon, Narathiwat, Krabi, Tak, Chai Nat).
    - **Decision Rule:**
        - If the data is granular (District-level tags present) $\rightarrow$ We can use **Statistical Extrapolation (Path A)**.
        - If the data is only a single Provincial number $\rightarrow$ Statistical correlation is too weak; we must use **Global Curves (Path B)**.
            

#### Step 2: The "Model Driver" Search (External)

_Action: Confirm availability of input variables for the Economic Model._

- **Check 3: Hazard Raster Availability**
    
    - **Task:** Do we have historical **Flood Depth** and **Drought Extent** rasters for 2023 (the pilot year)?
        
    - **Why:** Without _historical_ hazard maps matching the pilot year, we cannot train the model against the pilot data.
        
    - _Target Sources:_ GISTDA, DDPM, or Global Flood Database.
        
- **Check 4: Exposure Proxy Availability (Decides Denominator Source)**
    - **Task:** Download a sample of **Gridded GPP** (e.g., from Kummu et al. or WorldPop).
    - **Test:** Sum the pixel values for "Chiang Mai" and compare it to the official NESDC GPP for Chiang Mai.
        
    - **Decision Rule:**
        - If variance is <10% $\rightarrow$ Use **Gridded GPP (Path A)**.
        - If variance is >20% $\rightarrow$ We must **Calibrate to NESDC (Path B)**.
            

## Step 3: The Validation Feasibility Check

_Action: Determine how we will defend the model to the Board._

- **Check 5: "Third Party" Verification Data**
    - **Task:** Pick 3 random provinces _without_ official data (from the missing 72). Search for news reports or insurance claims regarding "Flood Damage 2023" in those areas.
    - **Goal:** See if we can find _any_ numbers to act as a "Sanity Check" for our future model.

---

## Output: The "Go/No-Go" Matrix

_Upon completing this review, Boss/Tonklar will produce a simple matrix to finalize the Scope of Work:_

|**Component**|**Status**|**Selected Methodology**|
|---|---|---|
|**Human Impact**|_e.g., Data is sparse (<20 provs)_|$\rightarrow$ _Shift to Modeling_|
|**Economic Impact**|_e.g., Pilot data is high quality_|$\rightarrow$ _Statistical Extrapolation_|
|**Denominator**|_e.g., Gridded GPP is inaccurate_|$\rightarrow$ _Calibrate to NESDC_|

This plan moves the team from "guessing" what to do, to making **evidence-based decisions** on the technical approach.