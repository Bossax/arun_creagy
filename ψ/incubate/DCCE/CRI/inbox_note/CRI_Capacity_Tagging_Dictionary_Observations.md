---
status: current
created: 2026-02-27
last_updated: 2026-02-27
project:
  - DCCE_CRI
type: note
source_alignment: "[[01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis]]"
---
# Observations & refinement suggestions — CRI Capacity Tagging Dictionary

This memo records observations and suggested refinements to align the tagging dictionary with the **practical design stance** (“secondary-data-first now; process-quality later”) described in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md).

## Core tension (what changed)
- The original dictionary goal was to reduce subjectivity by preferring **process indicators tied to administrative events** (e.g., “revision cycle”, “disbursement timeliness”, “procurement cycle time”) in [`CRI_Capacity_Tagging_Dictionary.md`](src/01_Projects/2025-11_DCCE-CRI/output/CRI_Capacity_Tagging_Dictionary.md:16).
- The practicality stance from the frameworks analysis explicitly treats CRI Phase 2 as a **two-speed system**: ==a defensible baseline deliverable that relies on **secondary/admin data first**==, and a ==later roadmap toward richer process metrics== (see “Practical design stance” in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](src/01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md:58)).
- Therefore: **capturing process quality is often impossible at baseline** (no event timestamps, no case management logs, fragmented cross-agency data).

>[!comment]
>This is a very good point. Process metrics are mostly not yet captured. Local officials might be able to vaguely inform us about these metrics such as very slow, very quick, etc. We might use the site visits as opportunity to introduce low-friction data collection means in these pilot areas.


## Observations 
1. Many “process” indicators in the v1 table are **implicitly dependent on event logs** (timestamps, case IDs, meeting registers). Without them, the indicator collapses to a binary “exists” proxy, and that shift must be made explicit.

2. Several indicators are best treated as **two variables**, not one:
	- a **structure proxy** (policy/committee/system exists), and
	- a **functionality metric** (frequency/timeliness/coverage/quality).
	Conflating them creates a false sense of measurement maturity.

3. The dictionary needs an explicit “**data-richness/confidence**” overlay to avoid producing a precise-looking profile from weak proxies. This follows the “data richness/confidence overlay (mandatory)” recommendation in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](src/01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md:42).

4. Governance-heavy indicators are politically sensitive. A “baseline-first” approach increases defensibility if the measurement is anchored to **mandate-aligned naming** (official KPI names/registries) and clearly labeled as proxy.

- “Transformative” indicators are especially prone to **measurement drift** if they rely only on existence proxies (e.g., “taskforce exists”). The target functionality metric (activation frequency + outputs) must remain visible in the dictionary as an upgrade path.

>[!comment]
>- yes. Data availability and readiness prevent us from fully implement process-oriented resilience measurement
>- data-richness/confidence is a very good metric to point to possible room for improvement. It roots in academic principle. 
>-  **mandate-aligned naming** (official KPI names/registries) is a good way to mentally bridge stakeholders from their routines to this new concept. We can do the mapping to go Governance indicators in the background
>- Transformative indicators are the most difficult so they risk misrepresentation for sure
## Suggestions for further modification and refinement

### A) Treat every indicator as a Baseline/Target pair

- Keep the process indicator as the **Target** (north star).
- Add a **Baseline proxy** that is realistically measurable in CRI’s current data regime.
- Make it a rule that scoring/profiling always states: “Baseline proxy used” vs “Target metric used”.

### B) Add a 0–3 baseline data-richness/confidence score

- Use a consistent rubric (0=not measurable via secondary data; 3=structured and repeatable).
- Publish the scale definition in the dictionary so interpretation is stable.

### C) Explicitly separate “structure exists” from “process quality”
- Where only binary indicators exist, treat them as **capacity prerequisites**, not evidence of performance.
- In reporting, translate these into **gap diagnostics** (e.g., “Structure exists, but functionality not measurable; needs event log”).

### D) Create a small, defensible “baseline short-list”
- Select a subset of baseline indicators with confidence 2–3.
- Use those for the initial profile; keep 0–1 as “diagnostic only / data roadmap”.
- This helps avoid over-claiming and reduces the risk of a “Potemkin index” critique.

### E) Add an explicit “upgrade path” / data requirement note per indicator
- For each Target metric, specify the minimum additional data needed (e.g., “approval timestamp + disbursement timestamp”).
- This turns the dictionary into a requirements backbone for later data governance work.

### F) Align capacity tiers with a Respond/Recover/Transform crosswalk
- The frameworks analysis recommends capacity buckets like Respond/Recover/Transform (see [`CRI_Urban_Resilience_Frameworks_Analysis.md`](src/01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md:20)).
- Adding an explicit crosswalk in the dictionary would reduce ambiguity when stakeholders expect that language.

## What to watch for (risks)
- **Proxy inflation:** baseline “exists” proxies can artificially elevate scores and hide implementation weakness.
- **Uneven data:** some provinces/municipalities may have more web presence/registry completeness, biasing “confidence” upward unless missingness is surfaced.
- **Over-aggregation:** combining weak proxies into composite scores risks obscuring non-negotiable failures; consider keeping “red flag / threshold” checks separate (see threshold pattern in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](src/01_Projects/2025-11_DCCE-CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md:44)).

