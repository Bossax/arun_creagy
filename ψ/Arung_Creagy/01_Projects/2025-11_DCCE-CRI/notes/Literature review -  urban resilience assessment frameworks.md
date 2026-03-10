---
status: evergreen
tags:
  - literature-review
  - urban-resilience
  - frameworks
  - AI_prompt
  - NotebookLM
created: 2026-02-26
last_updated: 2026-02-26
AI_prompt: true
AI_output: false
project:
  - DCCE_CRI
type: note
---

# Literature review — Urban resilience assessment frameworks (prompt pack)

This note contains **research + extraction prompts** for reviewing **urban resilience assessment frameworks** and translating them into inputs for CRI Phase 2.

Anchors:

- Session plan: [`src/plans/2026-02-26-research-urban-resilience-framework.md`](=plans/2026-02-26-research-urban-resilience-framework.md)
- Methodology context: [`src/01_Projects/2025-11_DCCE-CRI/output/CRI Phase 2 Methodology.md`](01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md)

Tooling assumptions:

- **Consensus / Elicit**: best for *discovery* (finding candidate papers/frameworks).
- **NotebookLM**: best for *extraction + synthesis across a curated corpus*.

Key requirement: emphasize the **chronological evolution** of “urban resilience” (definitions, dominant dimensions, and methods), because the topic is dynamic and frameworks are shaped by their era.

## NotebookLM configuration (chat behavior) — atomic note extraction mode (tailored for subsequent analysis)


### Recommended “chat contract” (paste as the first message)

> You are my **literature review extraction engine** for *urban resilience assessment frameworks*.
>
> **Hard rules**
> 1) Use **ONLY** the sources I uploaded to this notebook. Do not use outside knowledge.
> 2) Every non-trivial claim must have a **citation** in APA 7 style in-text citations as (Author, Year) instead of numbers to a specific source (and page/section if available). However, keep original numeric links for sources. This is mandatory. 
> 3) Prefer **direct quotes** for:
>    - definitions of resilience
>    - framework dimensions/pillars
>    - evidence that a framework was applied to a real city
> 4) Separate **(a) extraction** from **(b) synthesis/inference**. Label synthesis clearly.
> 5) Always capture **chronological context**:
>    - year of publication
>    - what prior framing it reacts to / differs from (if stated)

> **Output style **
> Each atomic note must include an **Implication for downstream analysis** in one sentence.
> The implication should be written to support the next tasks in the session plan (curate frameworks, understand data requirements, interpret key dimensions including governance, and build the evolution timeline).

> **Atomic note template (fixed structure; tailored to the session tasks)**
> Each atomic note must follow this structure exactly so it can be curated into the framework review and analysis artifacts.
>
> - Framework name:
> - Evidence of real-city application: (city/case + quote + page/section)
> - Definition of resilience: (quote)
> - Key dimensions / aspects: (list; include governance placement)
> - Data collection method(s): (admin/statistical | survey | expert scoring | participatory | remote sensing | mixed)
> - Data analysis method(s): (scoring/weighting/aggregation; qualitative rubric; index construction)
> - Use of results: (planning | budgeting | monitoring | stakeholder engagement | other)
> - Data requirements / burden: (granularity + cadence + feasibility; low/medium/high)
> - Chronological context: (year/period + what this framework reacts to)
> - Implication for subsequent analysis: (one sentence linking to the session tasks)
> - Citation: (source + page/section)


### Operating tips (to keep NotebookLM “conducive”)

- Keep one notebook per objective: **Urban resilience frameworks (applied)**.
- Upload sources in 2 tiers:
  - Tier A: papers/framework docs that define the framework
  - Tier B: case study applications (the “proof of use”)
- Run in this order:
  1) **Proof-of-application audit** (filter out conceptual-only frameworks)
  2) **Atomic notes extraction** (definitions, dimensions, methods, data requirements)
  3) **Evolution timeline** (chronology-first)
  4) **Framework matrix** (comparative extraction)

- If NotebookLM starts summarizing generically, re-issue the constraint: “quote + cite; otherwise mark not supported.”



---

## 1. Core literature scan: frameworks used on real cities

**Prompt 1 – “Find urban resilience assessment frameworks applied to real cities”**

> I am looking for **urban resilience assessment frameworks** that have been **applied empirically to real cities or metropolitan regions**, not just proposed conceptually.  
>   
> Please search for peer‑reviewed articles, technical reports, or grey literature that:  
> - Explicitly describe an **urban resilience assessment framework, index, or scorecard**, and  
> - Show **applications to at least one real city** (case study) where results are reported.  
>   
> For each framework, summarize in a table with columns:  
> 1. Framework name  
> 2. Lead institution / authors  
> 3. Type (index / scorecard / diagnostic toolkit / qualitative framework)  
> 4. Cities/regions where it has been applied (with country)  
> 5. Year(s) of main publication or application  
> 6. Main purpose (e.g. diagnostic, benchmarking, planning support, monitoring)  
>   
> Prioritize frameworks that focus on **climate‑related urban resilience**, but include general urban resilience frameworks if they are widely used.  
>   
> Output: a concise table + short narrative highlighting 5–10 of the **most influential or widely applied** frameworks.

This feeds your Task 1 bullets on “review frameworks used to assess real cities.”

---

## 1.1 NotebookLM extraction: chronological evolution + evidence

### Prompt 1A — “Evolution timeline (concept + methods)” (NotebookLM)

> Using ONLY the sources I uploaded, build a **chronological timeline** of how the concept of **urban resilience** and **urban resilience assessment** evolved.
>
> Requirements:
> - Timeline entries must include: **year (or period)**, **what changed**, **why it changed**, and **2–3 citations** (source title + short quote).
> - Explicitly track evolution in:
>   - definitions (engineering resilience → ecological → social-ecological → urban systems)
>   - dominant dimensions (infrastructure/engineering → governance/service delivery → equity/justice → ecosystems)
>   - methods (qualitative diagnostics → scorecards → composite indices → hybrid mixed-method assessments)
>   - data regimes (primary surveys/participatory → administrative/statistical → remote sensing → multi-source fusion)
> - End with: “What changed in what gets measured (dimensions) and how it gets measured (methods/data) over time?”

### Prompt 1B — “Proof of real-world application audit” (NotebookLM)

> For every framework mentioned in my sources, classify it as:
> - **Applied to real city/cities** (with evidence), or
> - **Conceptual only** (no clear application evidence).
>
> For each “applied” entry, extract:
> - framework name
> - city/case study
> - exact supporting quote + page/section
>
> If evidence is ambiguous, mark as “uncertain” and explain why.

## 2. Data requirements focus

**Prompt 2 – “Extract data requirements and practicality”**

> From the most widely applied **urban resilience assessment frameworks** (indices/scorecards/tools) that have been used on real cities, I want to understand their **data requirements and practicality**.  
>   
> For each major framework you find, extract:  
> 1. **Indicator types** used (e.g. administrative data, survey data, remote sensing, qualitative expert judgment).  
> 2. **Data sources** typically required (e.g. municipal statistics, census, infrastructure inventories, hazard models).  
> 3. **Level of spatial granularity** (city / district / neighborhood).  
> 4. **Frequency** of data collection (one‑off vs. ongoing).  
> 5. Any notes on **data availability challenges** reported in the case studies.  
>   
> Please present the result in a comparative table, and then add a short narrative answering:  
> - Which frameworks are **most feasible if only existing administrative and statistical data are available**, with **no new primary data collection**?  
> - Which frameworks are **data‑intensive** and would be difficult to implement under tight time and budget constraints?

Use this to directly support “understand data requirements of these frameworks.”

---

## 3. Conceptual structure: what “urban resilience” means in practice

**Prompt 3 – “Compare how frameworks conceptualize urban resilience”**

> I want to compare how different urban resilience assessment frameworks **define and structure** resilience.  
>   
> For the main frameworks you identify (especially those applied to real cities), please extract:  
> 1. The **definition of urban resilience** used or implied.  
> 2. The **key dimensions / pillars / domains** (e.g. infrastructure, environment, economy, governance, social, institutional).  
> 3. Whether governance is treated as:  
>    - a separate pillar,  
>    - a cross‑cutting theme, or  
>    - only indirectly represented.  
> 4. Any explicit linkage to **social‑ecological systems (SES)** thinking or **systems / management science** concepts.  
>   
> Summarize in a table plus a narrative that answers:  
> - In practice, which dimensions consistently appear across frameworks?  
> - To what extent do frameworks **weight or emphasize governance** relative to other dimensions?  
> - Which frameworks are conceptually closest to a **capacity‑based view** (coping / adaptive / transformative capacities)?

This supports your objective to “understand key aspects that constitute urban resilience … to be emphasized in [`CRI Phase 2 Methodology`](src/01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md:37).”

---

## 4. Methodology and use of results (for alignment with CRI)

**Prompt 4 – “Methods and how results are used by cities”**

> For urban resilience assessment frameworks applied to real cities, I want to understand **how they are implemented and how results are used**.  
>   
> For each major framework, please summarize:  
> 1. **Data collection methods** (administrative data, household surveys, expert workshops, participatory processes, remote sensing, etc.).  
> 2. **Data analysis methods** (e.g. scoring / rating, normalization and weighting, composite index construction, qualitative scoring, multi‑criteria analysis).  
> 3. The **main outputs** (indices, scores, dashboards, profiles, qualitative narratives).  
> 4. Documented examples of **how city governments actually used the results**, such as:  
>    - informing strategic plans or investment decisions,  
>    - prioritizing interventions,  
>    - monitoring progress,  
>    - engaging stakeholders.  
>   
> Then answer:  
> - Which approaches to analysis and communication seem to be **most useful for local decision‑making** (not just ranking)?  
> - What design choices help **avoid the “ranking trap”** and instead support capacity‑building and learning?

This connects directly to section 4 of [`CRI Phase 2 Methodology`](src/01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md:126) (capacity profiles vs simple ranks).

---

## 5. Alignment with CRI Phase 2 strategy (SES & capacity tagging)

**Prompt 5 – “Identify frameworks compatible with CRI Phase 2 methodology”**

> Given the following constraints and design choices, I want to know which urban resilience assessment frameworks are **most compatible** with this approach:  
>   
> - **capacity‑based framework** (Coping, Adaptive, Transformative capacities) and is grounded in **social‑ecological system (SES)** thinking and **management science**.  
> - It relies mainly on **existing administrative and statistical data**, tagged into capacity categories, with **limited or no new primary data collection**.  
> - The goal is to produce **capacity profiles** and **policy‑relevant insights**, not just rankings.  
>   
> Based on the literature on urban resilience assessment frameworks:  
> 1. Which frameworks are conceptually closest to a **capacity‑based, governance‑oriented** perspective?  
> 2. Which ones demonstrate **successful use of administrative data** for resilience assessment?  
> 3. What **design patterns** (in terms of domains, indicators, and aggregation) could be adapted into a provincial‑scale index similar to CRI?  
> 4. What common **pitfalls or criticisms** should we avoid (e.g. overly technocratic indices, data requirements that are unrealistic for provincial governments, weak governance representation)? 
>   
> Please provide a short list (3–5) of the **most suitable frameworks or design patterns**, and explain why they are good candidates to inspire the next iteration of the CRI Phase 2 methodology.

Use this to feed the task “suggest the approach of urban resilience assessment that align with [`CRI Phase 2 Methodology`](src/01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md:35)’s framing (social-ecological system and management science).”

---

## 6. One consolidated “session driver” prompt

If you want a single, all‑in‑one prompt to drive an initial AI research pass before you go into detailed sub‑questions:

**Prompt 6 – “Integrated review prompt”**

> I am preparing a literature review on **urban resilience assessment frameworks** as part of designing a national‑scale **Climate Resilience Index (CRI) Phase 2** for provinces in Thailand.  
>   
> Please:  
> 1. Identify key **urban resilience assessment frameworks** that have been applied to real cities.  
> 2. For each, summarize:  
>    - conceptual definition of resilience,  
>    - key dimensions/pillars,  
>    - data requirements (types and sources),  
>    - analysis method,  
>    - how results were used by city governments.  
> 3. Highlight which frameworks are:  
>    - most feasible when limited to **existing administrative & statistical data**,  
>    - most aligned with a **capacity‑based, governance‑oriented view** (coping/adaptive/transformative),  
>    - most compatible with **social‑ecological system** thinking and **management‑science framing**.  
> 4. From these, propose **2–3 design patterns** that could be adapted for a provincial‑level resilience index similar to CRI Phase 2 (no new primary data, emphasis on capacities and governance, outputs as capacity profiles not just rankings).  
>   
> Output:  
> - A comparative table of frameworks.  
> - A narrative synthesis (1–2 pages).  
> - Explicit recommendations on which patterns to adapt and what pitfalls to avoid.

Using these prompts with Consensus/Elicit will give you:
- The comparative framework table for your “report of urban resilience framework” in `src/01_Projects/2025-11_DCCE-CRI/output/`.
- Focused material for the analysis artifact that interprets frameworks through the CRI Phase 2 capacity‑based, SES‑oriented lens described in [`CRI Phase 2 Methodology`](src/01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md:22).
