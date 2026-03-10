---
created: 2026-02-18
status: archived
type: execution_checklist
source_plan: Plan - 18 Feb Afternoon session 1.md
project: DCCE_CRI
---
# Execution Checklist: 18 Feb 2026 - CRI Phase 2 methodology hypothesis testing

## Inputs

- Source plan: [Plan - 18 Feb Afternoon session 1](Plan - 18 Feb Afternoon session 1.md)
- Methodology: [CRI Phase 2 Methodology](../01_Projects/2025-11_DCCE-CRI/output/CRI%20Phase%202%20Methodology.md)
- Critique: [Critique of CRI Phase 2](../01_Projects/2025-11_DCCE-CRI/notes/Critique%20of%20CRI%20Phase%202.md)
- Literature source: Validating a Management Science Approach to Measuring Coping, Adaptive, and Transformative Capacities in Municipal Climate Resilience Using Administrative Data (locate or ingest if missing)

## Execution checklist

- [x] Locate the literature source; add it to sources if missing and record the citation.
- [x] Extract literature-backed process metrics and constraints (frequency, friction, agility) and note candidate proxy fields.
- [x] Map CRI Phase 2 indicators to capacity tiers; flag static/binary indicators and missing time/flow metrics.
- [x] Translate critique risks into explicit corrections (static/dynamic mismatch, tagging subjectivity, actionability gap, transformative mis-measurement).
- [x] Draft a tagging dictionary with explicit rules and a governance review step.
- [x] Draft the data analysis plan: datasets, required fields, transformations, computed indicators, and QA checks.
- [x] Synthesize implementation strategies that address each critique risk while preserving the middle-path objective.
- [x] Consolidate outputs into a short session summary with decisions, open questions, and next steps.

## Step 1 - Literature source citation (located)

Source file: [Validating a Management Science Approach to Measuring Coping, Adaptive, and Transformative Capacities in Municipal Climate Resilience Using Administrative Data](../01_Projects/2025-11_DCCE-CRI/sources/Validating%20a%20Management%20Science%20Approach%20to%20Measuring%20Coping,%20Adaptive,%20and%20Transformative%20Capacities%20in%20Municipal%20Climate%20Resilience%20Using%20Administrative%20Data.md)

Key citations used for process-metric justification:
- Lowe, M., Bell, S., Briggs, J., McMillan, E., Morley, M., Grenfell, M., Sweeting, D., Whitten, A., & Jordan, N. (2024). A research-based, practice-relevant urban resilience framework for local government. _Local Environment_, 29, 886 - 901. https://doi.org/10.1080/13549839.2024.2318571
- Esposito, D. (2025). A Ladder of Urban Resilience: An Evolutionary Framework for Transformative Governance of Communities Facing Chronic Crises. _Sustainability_. https://doi.org/10.3390/su17136010
- Suárez, M., Benayas, J., Justel, A., Sisto, R., Montes, C., & Sanz-Casado, E. (2024). A holistic index-based framework to assess urban resilience: Application to the Madrid Region, Spain. _Ecological Indicators_. https://doi.org/10.1016/j.ecolind.2024.112293
- Masik, G., & Gajewski, R. (2021). Working towards urban capacity and resilience strategy implementation: Adaptation plans and strategies in Polish cities. _Cities_. https://doi.org/10.1016/j.cities.2021.103381
- Al-Humaiqani, M., & Al‐Ghamdi, S. (2022). The built environment resilience qualities to climate change impact: concepts, frameworks, and directions for future research. _Sustainable Cities and Society_. https://doi.org/10.1016/j.scs.2022.103797
- Mehryar, S., Sasson, I., & Surminski, S. (2022). Supporting urban adaptation to climate change: What role can resilience measurement tools play?. _Urban Climate_. https://doi.org/10.1016/j.uclim.2021.101047

## Step 2 - Process metrics and candidate proxy fields

|Process metric|Capacity emphasis|Administrative proxy fields (candidates)|Source cue|
|---|---|---|---|
|Procurement lead time / approval duration|Coping and adaptive (friction)|Procurement log timestamps: request date, approval date, contract award date|Al-Humaiqani & Al‐Ghamdi (2022)
|Approval steps / signatures (red tape)|Coping (friction)|Workflow step counts; number of approvals per transaction|Al-Humaiqani & Al‐Ghamdi (2022)
|Own-source revenue ratio|Adaptive (agency/autonomy)|Budget files: own-source revenue, total revenue|Masik & Gajewski (2021)
|Unrestricted vs earmarked transfer share|Adaptive (agency/autonomy)|Financial statements: transfer categories and restrictions|Masik & Gajewski (2021)
|Emergency spending authorized without council approval (frequency/size)|Coping (agility)|Emergency spending records; decree metadata; approval authority|Masik & Gajewski (2021)
|In-year budget amendment frequency|Adaptive (learning/adjustment)|Budget amendment logs with dates and initiator|Masik & Gajewski (2021)
|Diversity of budget codes used|Adaptive (flexibility)|Annual budget line items; functional code counts/diversity|Lowe et al. (2024)
|Plan revision frequency / last update age|Transformative (learning cycle)|Plan metadata: revision dates, version numbers|Lowe et al. (2024); Suárez et al. (2024)
|After-action review compliance rate|Adaptive/transformative (learning)|Incident reports: event date, after-action report date|Suárez et al. (2024)
|Cross-department collaboration frequency|Transformative (integration)|Interagency meeting logs; joint project records|Suárez et al. (2024)

## Step 3 - CRI Phase 2 indicator mapping and gap flags

|CRI Phase 2 indicator (current)|Capacity tier|Type risk|Process metric gap to flag|Candidate proxy field(s)|
|---|---|---|---|---|
|Emergency budget reserves|Coping|Stock/static|Disbursement rate and speed|Emergency budget disbursement dates, % spent by quarter|
|Disaster relief equipment stocks|Coping|Stock/static|Readiness and mobilization speed|Inventory age, deployment time records|
|Early warning system coverage|Coping|Binary/coverage|Warning timeliness and reach|Alert issuance logs, response time, coverage uptime|
|Existence of provincial development plans integrating climate|Adaptive|Binary/exists|Plan revision frequency / learning loop|Plan revision dates, update count over 5 years|
|Education levels and technical training programs|Adaptive|Stock/static|Training frequency and completion rates|Training roster dates, certification counts per year|
|Healthcare system reach and flexibility|Adaptive|Stock/static|Surge capacity and response speed|Response time logs, staffing surge activation records|
|Agricultural diversification rates|Adaptive|Slow-moving stock|Rate of change over time|Crop mix change over multi-year window|
|Land use planning enforcement|Transformative|Binary/ambiguous|Actual enforcement outcomes|Variance approvals/denials, enforcement actions|
|Innovation budgets or Smart City participation|Transformative|Stock/static|Innovation cycle frequency|Pilot cycle frequency, R&D project counts per year|
|Cross-jurisdictional governance mechanisms|Transformative|Binary/exists|Collaboration frequency and outputs|Interagency MoU dates, joint project records|

## Step 4 - Corrections from critique and tagging rules

### Critique risk → correction mapping

|Critique risk|Concrete correction|Evidence cue|
|---|---|---|
|Static vs dynamic mismatch|Replace “existence” indicators with time/flow metrics where possible; introduce rate-of-change proxies|Process metrics: plan revision frequency, procurement lead time|
|Tagging subjectivity|Define a deterministic tagging dictionary and publish for review before scoring|Rule-based tagging dictionary|
|Actionability gap|Add friction diagnostics (time-lags, approval steps, disbursement speed) alongside scores|Bottleneck indicators highlight operational frictions|
|Transformative mis-measurement|Shift from budget size to integration/learning cycle indicators; use collaboration frequency and plan revisions|Transformative capacity emphasized via integration/learning|

### Tagging dictionary (draft rules)

- **Coping:** Indicators measuring immediate response readiness, emergency execution, and short-cycle operational continuity.
  - Rule: Keywords or metadata implying emergency response, relief, response equipment, immediate budgets.
- **Adaptive:** Indicators reflecting learning, adjustments, and resource allocation within the current system.
  - Rule: Plan revision, budget amendment, training cadence, flexibility of allocation.
- **Transformative:** Indicators reflecting cross-sector integration, structural change, and institutional redesign.
  - Rule: Cross-agency coordination, governance restructuring, multi-year innovation cycles.

### Governance review step

- Circulate tagging dictionary to DCCE + key line agencies prior to scoring.
- Collect objections and document accepted changes.
- Freeze the dictionary as a controlled artifact before data processing.

## Step 5 - Data analysis plan (draft)

|Dataset|Required fields|Transformations|Computed indicators|QA checks|
|---|---|---|---|---|
|LPA / administrative KPI records|Indicator ID, province, year, value, metadata|Normalize fields; map to tagging dictionary|Capacity sub-scores by tier|Missingness rate by province; outlier review|
|Budget & finance (DCCE/Interior)|Budget line items, approval dates, disbursement dates, revenue sources|Compute time-to-disburse; derive own-source ratio|Disbursement speed; autonomy ratio|Date validity; negative/zero checks|
|Procurement logs|Request date, approval date, award date, agency|Compute lead time and approval steps|Procurement friction score|Lead-time distribution anomalies|
|Planning documents registry|Plan name, revision dates, version|Calculate revision frequency/age|Learning cycle indicator|Revision date consistency|
|Interagency collaboration records|MoU dates, joint project counts, meeting logs|Count collaborations per year|Integration frequency score|Duplicate MoUs; agency ID consistency|

## Step 6 - Implementation strategies (aligned to critique)

- **Middle-path + process emphasis:** Keep existing datasets but add process proxies (timeliness, frequency, friction) to avoid “compliance-only” scores.
- **Defensible tagging:** Use the dictionary + governance review to reduce subjectivity and political pushback.
- **Actionability layer:** Pair each capacity score with at least one bottleneck metric (e.g., procurement lead time) and a corresponding “fix lever.”
- **Transformative realism:** Prioritize integration/learning indicators over large-budget proxies; include collaboration frequency as a core transformative measure.

## Step 7 - Session summary (draft)

**Decisions:**
- Use the existing literature synthesis to justify process metrics and move beyond binary existence indicators <!--note:  where possible-->.
- Adopt a rule-based tagging dictionary with formal review before scoring.

**Open questions:**
- Which agencies can provide procurement and plan revision timestamps at province level?<!--note:  No. We cannot access to the timestamp information-->
- Are interagency collaboration logs structured enough to compute annual frequencies?<!--note:  No. They cannot be used-->

**Next steps:**
- Confirm data access and field availability for process proxies.
- Validate tagging dictionary with DCCE/line agencies and freeze for scoring.

# Reflection
- Tagging dictionary must derive from case studies and literature review
- The indicator lists in [[CRI Phase 2 Methodology]] are just illustrative. They need revision.
- The analysis table of Step 3 is very useful. I would like to keep this as a good practice for indicator review and analysis. 
- The applicability of the candidate proxy fields needs to be tested against the existing datasets
- The actionability of the outputs need further research. I agree that radar chart night not best suit and high-level guideline may still be insufficient. However, the format of the output is tied to data availability 
- Need more brainstorming on the transformative characteristics of an urban system. Require more inputs from case studies and research.
