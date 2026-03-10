---
status: archived
tags: []
created: 2026-03-06
last_updated: 2026-03-06
AI_prompt: false
AI_output: false
project: DCCE_CRDB
type: note
---
##  Evolution of the DCCE Data Ecosystem

### Step 1: Establishing the Foundation (Federation over Centralization)

We began by analyzing the overarching constraint of **Strategy v3**: _"Do not build redundant government data infrastructure"_.

- **The Logic:** We adopted a federated **Data Mesh** approach utilizing DGA's "Default Rails" (data.go.th and GDX). We defined **Canonical Boundaries** and **Crosswalks** as the governed mapping layer to translate disparate agency languages into a unified format "just in time".
    

### Step 2: The Reality Check (Critiquing the MVPs for a Low-Literacy Context)

Before refining any specific tool, you asked me to play devil's advocate and prove why the original MVP designs were actually a _low priority_ and _not useful_ for a country with low climate risk and adaptation literacy.

- **The Logic:** The original MVPs assumed a mature, data-literate user base capable of navigating a self-service clearinghouse. We established that deploying advanced data governance tools to an uneducated user base is counterproductive.
    
- **The Critique:**
    
    - **MVP-4 (Uncertainty Standard):** Demanding that users understand "exceedance probabilities" guarantees catastrophic cognitive overload.
        
    - **MVP-3 (Registry):** Solves a problem ("choice paralysis" among competing datasets) that low-literacy users do not have. They want a single, prescriptive answer, not a catalog to browse.
        
    - **MVP-2 (Reporting Pack):** Given that DDPM data has "lag/noise" and is biased by relief fund incentives, standardizing this intake without massive quarantines just creates a highly governed database of "Garbage-In, Garbage-Out."
        
    - **MVP-1 (Generator):** Giving users a tool to pull "probabilistic + projected" layers enables the weaponization of misunderstood data. They will ignore the limitations text and generate dangerously flawed policy documents.
        
- **The Conclusion:** This critique forced us to realize that a Self-Service Data Mesh is the wrong _front-end_ topology for this specific audience. We needed a highly prescriptive Hub-and-Spoke user experience, even if the back-end remained federated.
    

### Step 3: The Literacy Pivot (The Redesign of MVP-1)

_Building directly on the critique from Step 2..._

- **The Logic:** To prevent the weaponization of data by low-literacy users, we had to remove their ability to configure the analysis.
    
- **The Evolution:** We pivoted MVP-1 from a self-service generator into a **Curated Data Product**. The DCCE Central Data Team now acts as the sole operator of the generator, using the crosswalks to batch-produce locked, static "1–2 page packs". The provincial planners merely download the final, safe result.
    

### Step 4: The Bimodal Strategy (Rescuing MVP-3 & MVP-4)

_Addressing the needs of advanced users..._

- **The Logic:** We realized we have a bimodal user base: low-literacy policymakers and high-literacy analysts (e.g., commercial banks, NESDC) who explicitly need searchable datasets and uncertainty handling.
    
- **The Evolution:** We established a **Tiered Dissemination Architecture**. Tier 1 provides the locked MVP-1 static packs (with plain-language MVP-4 educational caveats) for local planners. Tier 2 opens the MVP-3 Registry and raw probabilistic layers to the advanced financial and macroeconomic sectors, strictly governed by the MVP-4 scientific standards.
    

### Step 5: The Quarantine & Reconstruction Engine (Evolving MVP-2)

_Fixing the operational disaster data..._

- **The Logic:** We returned to MVP-2, knowing the input data was flawed. NESDC needed "true economic damage," but DDPM only had raw casualty counts and compensation payouts.
    
- **The Evolution:** We redefined MVP-2 as an **Ingestion, Transformation, and Quarantine Gateway**. By designing a strict schema with "validation flags" and fields separating `Official_Compensation` from `Estimated_True_Loss`, MVP-2 becomes the structural foundation required for the **Historical L&D Estimation project** (enabling the Proxy, Satellite, and Econometric Modeling methods).
    

---

Thank you for catching that omission. Step 2 is arguably the most important architectural pivot in the entire project, as it aligns the theoretical governance framework with the sociological reality of the end-users.

---

## Steering principles for revising MVPs (grounded in interviews)

This section converts the 5-step narrative above into explicit **design constraints** for Phase 1 MVPs to propose in FGD2.

### Principle S1 — Design for *mixed literacy* by default (Tier 1 vs Tier 2)

- **Tier 1 (low-to-mixed literacy)** must be **prescriptive** and **export-first** (briefing packs, one-pagers, printable). Users should not need to “configure analysis.”
- **Tier 2 (advanced analysts)** can access probabilistic layers, registries, and deeper metadata (with gates).

Grounding signals:
- LAO / local planners need digestible evidence for budgets; hazard data is fragmented and difficult to interpret (DLA).
- MSDHS has no climate data scientists; needs municipality/sub-district resolution and clear “how to read” guidance (MSDHS).
- Banks need asset-level probabilistic semantics and are at high risk of misinterpretation (TBA).

### Principle S2 — “Curated operator model” for anything risky

If an output can be weaponized or misunderstood (e.g., probabilistic/projection layers), Phase 1 should favor:

- **central-team operated generation** of standardized packs, and
- **locked templates** with mandatory caveats,

rather than a self-service public tool.

Grounding signals:
- Fear of accountability for publishing predictive data; paralysis unless systems remove personal liability and make limitations explicit (NXPO).

### Principle S3 — Catalog-first and link-first (don’t duplicate national infrastructure)

- Prefer **linking to authoritative sources** (NSO model) and using existing national rails.
- Treat “recommendation/endorsement” as the value-add, not “rehosting everything.”

Grounding signals:
- NSO’s environment statistics center links to GD Catalog and agency URLs instead of duplicating data (NSO).
- DGA recommends using **data.go.th** and **GDX**, plus classification support, and warns architecture affects readiness KPIs (DGA).

### Principle S4 — Publishing safety is a *product requirement*

Any MVP that results in published outputs must include:

- **limitations + uncertainty statement** (required)
- **draft → review → publish** workflow (or an explicit operating rule)
- named owners for sign-off (domain + comms/PR + governance)

Grounding signals:
- FGD1 publishing bottleneck; need review-before-public and clearer QA/QC accountability (FGD1).
- NXPO accountability culture around forecasts (NXPO).

### Principle S5 — Boundary + crosswalk governance is non-negotiable

- Choose canonical boundary units per product (province/district/LAO/EA) and publish crosswalk guidance.
- Align “minimum viable granularity” to **budget holders** (municipality/LAO) where possible.

Grounding signals:
- DLA + MSDHS require LAO/municipality and sub-district alignment for budgets/service delivery.
- NSO’s EA concept is a candidate for consistent small-area baselines.

### Principle S6 — Treat event/impact data as “quarantine + revision,” not a clean feed

- Model post-event data as **lagged, noisy, revisable**.
- Make **validation flags + revision history** first-class.
- Separate **relief payouts** from **estimated true loss** (method-dependent).

Grounding signals:
- DDPM one-way pipeline (LAO → district → province → center), late/incorrect entries, and lack of ground-truth (DDPM).
- NESDC’s urgent need for “true economic loss” vs compensation payouts (NESDC).

### Principle S7 — “Accepted projections” is a roadmap promise, not an MVP dependency

- Phase 1 should not promise nationwide high-res modeling (OTP reality).
- Phase 1 can still deliver value by: cataloging projection assets, endorsing baselines, and packaging guidance for budget allocators.

Grounding signals:
- OTP requires authoritative projections and struggles to justify worst-case adaptation budgets (OTP).
