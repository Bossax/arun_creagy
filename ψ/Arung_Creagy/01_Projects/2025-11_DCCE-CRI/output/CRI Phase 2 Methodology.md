---
type: strategy
status: current
version: 4
created: 2026-01-21
last_updated: 2026-02-27T08:40:00.000Z
project:
  - DCCE_CRI
related_hypothesis: "[[CRI pivoting to social-ecological system and context focused]]"
color: var(--mk-color-purple)
---


>[!note] Change Log
>- v1: project kick-off - Readiness and Resilience
>- v2: After pivoting the project's strategy [[CRI pivoting to social-ecological system and context focused]]
>- v3: update after TEI meeting
>- v4: KO&I pass — align Phase 2 with Baseline/Target (two-speed) measurement stance, add data-richness overlay, and add LPA dataset analysis



# 1. Strategic Context: Balancing Rigor and Reality

The objective of CRI Phase 2 is to deliver a policy-relevant tool for local decision-makers (municipalities/provinces) while adhering to the Terms of Reference (TOR) which mandates a "National Index."

In this phase we explicitly move **beyond a pure loss/risk ranking** toward a **Resilience Capacity Profile**, accepting a managed trade‑off between strict cross‑provincial comparability and richer context‑specific insight.

We recognize a spectrum of implementation approaches:

1. **Universal Comparability (The "Technocratic" End):** Standardized, asset-based indices (e.g., Germanwatch). Easy to rank, but often lacks local context and actionable insight.
    
2. **Context Specificity (The "Local" End):** Deep, process-based qualitative assessments (e.g., interviews, participatory workshops). Highly actionable, but impossible to scale to 76 provinces within the 8-month timeline.
    

**The Strategy:** We adopt a **"Middle Path."** We will deliver the standardized index required by the TOR, but we will restructure its internal logic to reflect rigorous Social-Ecological System (SES) principles. We will not collect new primary data for all provinces; instead, we will apply a novel **"Capacity Tagging"** framework to existing national datasets.

**Operational stance (two-speed measurement):** Phase 2 will explicitly separate:

1. **Baseline proxies (secondary / administrative data):** what can be measured now, at scale (often binary / registry-based).
2. **Target process / quality metrics:** what we would like to measure later to evaluate “process quality” and real performance.

To keep interpretation honest, each Baseline proxy should carry a **data-richness / confidence score (0–3)** as specified in [`CRI_Capacity_Tagging_Dictionary.md`](../output/CRI_Capacity_Tagging_Dictionary.md).

# 2. Conceptual Framework: Defining the Capacities

Phase 2 builds directly on the **Impact Index (Fiscal Relief)** and hybrid spatial methodology defined in Phase 1. The Fiscal Relief Index answers **“Where and how heavily has the public budget been strained by climate‑related disasters?”**. The new Capacity Profiles answer **“How structurally ready is each province to cope, adapt, and transform?”**. Together they support more actionable decisions than a single composite risk score.

To transition DCCE from a "Disaster Management" mindset to a "Resilience" mindset, we establish three distinct tiers of capacity. These will form the sub-indices of the CRI.

>[!important] 
>Unlike asset‑based vulnerability indices, these capacity tiers are **process‑ and governance‑oriented**: they prioritise mechanisms such as planning, coordination, information flows and institutional agency over static stocks of infrastructure or capital.

>[!note] Design tracking
>The research plan and evolution notes are tracked in [[2026-02-18-CRI2-planning-and-structuring-of-research-plan]] and the tagging implementation rules are tracked in [`CRI_Capacity_Tagging_Dictionary.md`](../output/CRI_Capacity_Tagging_Dictionary.md).

## 2.1 Coping Capacity 

- **Concept:** The ability to withstand immediate shocks using _existing_ resources without changing the system.
- **Bureaucratic Translation:** Emergency Management & Relief.
    
- **Key metrics (Baseline proxy vs Target):**
    - **Baseline proxies (existing administrative data):**
        - Existence of disaster prevention / mitigation plan; existence of emergency procedures; existence of coordination mechanisms.
        - Emergency budget lines / accumulated fund levels and rules for rapid deployment.
        - Coverage of early warning / communication mechanisms.
    - **Target process/quality metrics (future / harder):**
        - Drill frequency and after-action review quality.
        - Response time and relief fund disbursement timeliness.
        - Evidence of inter-agency coordination during real events.
        

## 2.2 Adaptive Capacity

- **Concept:** The ability to learn and adjust processes to changing baselines to maintain the current trajectory.
    
- **Bureaucratic Translation:** Development Planning & Resource Allocation.
    
- **Key metrics (Baseline proxy vs Target):**
    - **Baseline proxies (existing administrative data):**
        - Integration of climate risk into development plans (existence + documented references).
        - Existence of data systems / registers relevant for risk management (open data, risk registers, inventories).
        - Existence of training programmes / technical staffing mandates.
    - **Target process/quality metrics (future / harder):**
        - Evidence of plan review cycles, learning loops, and budget reallocation based on new risk information.
        - Monitoring indicators and use of evaluation findings in decision-making.
        

## 2.3 Transformative Capacity (The "Evolution")

- **Concept:** The ability to fundamentally restructure the system when the status quo is untenable.
    
- **Bureaucratic Translation:** Structural Reform & Long-term Strategy.
    
- **Key metrics (Baseline proxy vs Target):**
    - **Baseline proxies (existing administrative data):**
        - Existence of land-use / zoning instruments and evidence of updates.
        - Existence of long-term strategic plans that explicitly consider climate limits.
        - Participation in innovation / smart city programmes; existence of reform-oriented committees.
    - **Target process/quality metrics (future / harder):**
        - Enforcement evidence (e.g., zoning enforcement actions; compliance rates).
        - Demonstrated policy reforms that shift development pathways (not just documents).
        

> **Educational Goal:** We use the Index to teach DCCE that _Coping_ is necessary but insufficient. True resilience requires _Adaptive_ and _Transformative_ scores.

---
# 3. Operational Methodology: The "Tagging" Protocol

Since creating new data streams is outside the scope/timeline, we will execute a **Systematic Categorization** of available administrative data.

> **Tagging Dictionary (v1):** The classification rules and nominal indicator list are documented in [`CRI_Capacity_Tagging_Dictionary.md`](../output/CRI_Capacity_Tagging_Dictionary.md). This dictionary is grounded in municipal governance case studies and process-indicator literature, and will be used as the baseline for tagging LPA and other administrative indicators.

>[!note] Implementation reference
>Use the current dictionary version (v1.1) which encodes the **Baseline proxy / Baseline data-richness (0–3) / Target metric** pattern.

## Step 1: Data Inventory & Review

We will compile datasets from all relevant line agencies. Key sources include:

- **DLA (Department of Local Administration):** Local Performance Assessment (LPA) data.
- **DCCE (Dept of Climate Change and Environment):** Sustainable City Assessment indicators.
- **NESDC:** Socio-economic development data.
- **Interior Ministry:** Budgetary and planning records.
- **TEI CRI Pilot and Phase 1 Impact Index:** Use the pilot and refined Fiscal Relief datasets as **context layers** to interpret capacity scores (e.g. provinces with high impact but weak adaptive or transformative capacity), not as capacity indicators themselves.

### 3.1 LPA dataset analysis (fitness for Phase 2) 👈

This section summarizes what LPA can and cannot do for CRI Phase 2, and how we will operationalize it without over-claiming.

**What LPA is (as a dataset)**

- An ongoing, nationwide assessment used by DLA to evaluate Local Administrative Organizations (LAOs) across multiple domains.
- Contains a mixture of:
  - **Binary / check-box indicators** (existence of plans, committees, registers, systems).
  - **Threshold indicators** (e.g., % of roads maintained).
  - **Registry / document-evidence requirements** (some indicators are tied to specific registers and centralized systems).

**Why LPA is valuable for CRI Phase 2 (baseline)**

- Already institutionalized, repeatable, and broad-coverage.
- Strong alignment with **governance and process** proxies (planning, registers, reporting systems) that are otherwise expensive to measure nationwide.
- Provides a tractable baseline for “**structural readiness**” across Coping/Adaptive/Transformative tiers.

**Primary limitations (interpretation constraints)**

- Self-reporting and incentive structure can produce **check-box behavior** and gaming.
- Many items measure the **existence** of a mechanism, not the **quality** of implementation.
- Some infrastructure-type indicators correlate with fiscal capacity (risk of conflating “wealth” with “resilience”).
- Climate-specific signal is indirect: many relevant items are DRM, water management, risk management, or planning system indicators rather than explicit adaptation outcomes.

**Data-richness expectation (0–3, baseline proxy)**

- Typical LPA baseline proxies should be treated as **data-richness 1–2**.
  - **1** when evidence is primarily self-asserted or lightly documented.
  - **2** when there is a clear audit trail (registers, standardized forms, central systems).
- **3** should be reserved for indicators with strong, routine, independently verifiable administrative traces.
- Many desired “process quality” variables are effectively **0 at baseline** (not collected / not feasible at scale).

**How CRI will use LPA in Phase 2 (method rule)**

- Use LPA as a **baseline proxy layer** only, tagged via [`CRI_Capacity_Tagging_Dictionary.md`](../output/CRI_Capacity_Tagging_Dictionary.md).
- Report capacity results as a **profile + gap report**, not as an “actual performance score”.
- Add a **data investment roadmap**: highlight which high-value process-quality indicators should be collected later to move from “structural readiness” to “process quality”.

**Mitigations / QA strategies**

- Triangulate LPA with:
  - Budget and expenditure records.
  - DCCE Sustainable City Assessment where overlapping constructs exist.
  - Selected sample audits / site visits (spot-check “plan exists” vs “plan used”).
  - Central system traces where available (e.g., e-LAAS, INFO, registries).

<!--note: We to to review more datasets such as [[ข้อมูลความจำเป็นพื้นฐาน (จปฐ.) ]], SDG indicators, and other social research-->


## Step 2: The "Capacity Tagging" Process

We will filter and "tag" each indicator based on its functional role in the SES framework:
- _Example 1:_ "Does the province have an emergency broadcast tower?" $\rightarrow$ Tag: **Coping Capacity**.
- _Example 2:_ "Does the local development plan mention 'Climate Change'?" $\rightarrow$ Tag: **Adaptive Capacity**.
    
- _Example 3:_ "Has the province revised its zoning map in the last 5 years?" $\rightarrow$ Tag: **Transformative Capacity**.
    

## Step 3: Addressing Data Quality (The "Binary" Challenge)

**Challenge:** Much of the administrative data (specifically LPA) is **Binary (Yes/No)** or check-box based. It measures the _existence_ of a mechanism, not its _quality_.

- _Mitigation:_ We will aggregate these binary indicators to create **Composite Scores**.
    
    - _Logic:_ A province with 8 out of 10 "Adaptive" mechanisms present has higher potential than one with 2.
        
    - _Transparency:_ We will explicitly communicate to DCCE that this measures "Structural Readiness" (existence of mechanisms), not necessarily "Operational Excellence."

**Additional mitigation (two-speed + confidence overlay):**

- For each indicator, we will record:
  - A **Baseline proxy** (what we can measure now)
  - A **Baseline data-richness / confidence** score (0–3)
  - A **Target metric** (what we would like to measure later)

This reduces the risk that stakeholders interpret low-quality proxies as fully reliable measures of governance performance.
        

# 4. The Output: Policy-Relevant Visualization

To avoid the "Ranking Trap" where officials simply look for who is #1, we will change the visualization strategy.

## 4.1 From "Single Rank" to "Capacity Profile"

Instead of a single map, we will produce **Radar Charts (Spider Webs)** for each province.

- **Axes:** Coping, Adaptive, Transformative, Ecosystem Health (Natural Capital).
- **Confidence overlay:** Apply a visual confidence cue (e.g., shading / hatching) based on the composite data-richness score of the underlying indicators.
    
- **Insight:**
    
    - _Scenario A:_ High Coping / Low Transformative $\rightarrow$ "This province is good at fighting fires but is not preventing them. **Recommendation:** Invest in Land Use Planning."
        
    - _Scenario B:_ High Transformative / Low Coping $\rightarrow$ "This province has great long-term plans but is vulnerable to immediate shocks. **Recommendation:** Increase Emergency Reserves."
        

## 4.2 The "Data Investment Roadmap"

We acknowledge that current data is imperfect. Therefore, a key deliverable of Phase 2 is not just the Index, but a **Gap Analysis Report**.

- **Site Visit Role:** We will use the pilot site visits to validate the "Binary vs. Reality" gap.
    
    - _Task:_ Interview officials to see if the "Climate Plan" (marked 'Yes' in the database) is actually used or just sits on a shelf.
        
- **Final Output:** A "Roadmap for National Data Collection" recommending which _process-based_ indicators DCCE should invest in collecting next to move from "Quantity" to "Quality."
    

# 5. Strategic Benefits of this Approach

1. **TOR Compliance:** We deliver the "National Index" and "Database" as promised.
    
2. **Feasibility:** We rely on _available_ data, mitigating the risk of scope creep or timeline failure.
    
3. **Educational Value:** The structure of the index itself educates the client on the hierarchy of resilience (Coping < Adaptive < Transformative).
    
4. **Policy Utility:** The "Capacity Profiles" give specific, actionable direction to local governors, moving beyond simple risk identification.
