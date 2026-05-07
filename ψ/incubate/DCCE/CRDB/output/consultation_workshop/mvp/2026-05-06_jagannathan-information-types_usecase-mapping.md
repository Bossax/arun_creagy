# Jagannathan et al. — Types *and sub-types* of actionable climate information (mapping per use case)

**Purpose**: identify the **types and sub-types of information involved in each CRDB use case** using Jagannathan et al.’s typology (as captured in [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:23)), then summarize the distribution.

**Primary input**: CRDB use-case statements + embedded “Typology tags” in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

---

## 1) Category + sub-type definitions (Jagannathan et al.)

### A. Detailed data and results

**Definition**: decision-relevant quantified outputs such as:
- changes in decision-relevant metrics (averages/peaks/variability/thresholds/tails/probability distributions)
- decision-relevant events (e.g., max flood / max wind for design parameters)
- drivers and processes (regional climatic processes)

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:29).

#### A1) Changes in decision-relevant metrics
Examples listed in source: averages, peaks, variability, thresholds, tails/probability distributions.

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:31).

#### A2) Decision-relevant events (extremes)
Examples listed in source: max flood event / max wind speed used as design parameters.

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:32).

#### A3) Drivers and process
Examples listed in source: key regional climatic processes (oscillations, atmospheric rivers, antecedent conditions, etc.).

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:33).

**CRDB examples**
- Post-event impact quantities and loss/damage summaries (UC-01) need “Detailed data & results” tags in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:204).

---

### B. Broad trends and patterns

**Definition**: synthesized insights about broad regional hydro-climatological changes (e.g., wetter/drier wet season) rather than decision-parameter-level detail.

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:35).

**CRDB examples**
- Provincial “risk profile” narratives that summarize priority hazards and patterns (UC-03) explicitly tag “Broad trends & patterns” in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:253).

---

### C. Data improvement and guidance

**Definition**: information about how to use data appropriately (credibility, uncertainty, model selection), and what needs improvement in quality/scale to match decisions.

Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:41).

#### C1) Data scale/quality improvements
Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:45).

#### C2) Data credibility and uncertainty guidance (model selection / best practice)
Source: [`Typology of actionable climate information.md`](ψ/inbox/Typology%20of%20actionable%20climate%20information.md:46).

**CRDB examples**
- Many UCs require limitations statements, uncertainty-safe interpretation, validation flags, and governance rails; these map to “Data improvement & guidance” tags throughout [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

---

## 2) Information sub-type mapping per use case (checkboxes)

Checkbox rule: because [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175) only tags *top-level types*, sub-type checkboxes below are assigned by reading each UC’s described outputs/needs:
- **A1** if UC requires long-term changes/statistics (metrics, distributions) as decision inputs.
- **A2** if UC is explicitly event- or extreme-focused (post-event, max events, early warning contexts).
- **A3** if UC requires explaining climate drivers/processes (why patterns occur), not just impacts.
- **B** if UC includes broad synthesized narratives (profiles/explainers).
- **C1/C2** if UC requires improvements to scale/quality OR credibility/uncertainty guidance / governance rails.

| Use case                                               | A1 Metrics change | A2 Events/extremes | A3 Drivers/process | B Trends/patterns | C1 Scale/quality improvement | C2 Credibility/uncertainty guidance |
| ------------------------------------------------------ | ----------------: | -----------------: | -----------------: | ----------------: | ---------------------------: | ----------------------------------: |
| UC-01 Post-event impact & Loss/Damage assessment       |                   |                  ✓ |                    |                   |                            ✓ |                                   ✓ |
| UC-02 Early warning / preparedness risk context        |                   |                  ✓ |                    |                   |                            ✓ |                                   ✓ |
| UC-03 Provincial risk profile                          |                 ✓ |                    |                    |                 ✓ |                              |                                   ✓ |
| UC-03b LAO budget justification pack                   |                 ✓ |                    |                    |                   |                            ✓ |                                   ✓ |
| UC-04 Vulnerable group mapping & service targeting     |                   |                    |                    |                   |                            ✓ |                                   ✓ |
| UC-05 Heat-health surveillance roadmap                 |                 ✓ |                    |                    |                   |                            ✓ |                                   ✓ |
| UC-06 Cascading impacts explainer + entry point        |                   |                    |                  ✓ |                 ✓ |                              |                                   ✓ |
| UC-07 Corridor/infrastructure exposure                 |                 ✓ |                  ✓ |                    |                   |                            ✓ |                                   ✓ |
| UC-07b Urban ops + planning-grade design               |                 ✓ |                  ✓ |                    |                   |                            ✓ |                                   ✓ |
| UC-08 Statistical baselines + thematic tagging         |                   |                    |                    |                   |                            ✓ |                                   ✓ |
| UC-09 True economic Loss & Damage estimation           |                 ✓ |                  ✓ |                    |                   |                            ✓ |                                   ✓ |
| UC-10 Baseline verification / “single source of truth” |                   |                    |                    |                   |                              |                                   ✓ |
| UC-11 Financial sector risk & stress testing           |                 ✓ |                    |                    |                   |                            ✓ |                                   ✓ |

**Trace anchors (examples)**
- UC-01: post-event workflow + validation flags + caveats: [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:182)
- UC-03: one-pager profile: [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:239)
- UC-06: curated explainer: [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:316)
- UC-10: compare candidates + publish endorsed baseline + maintain audit trail: [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:428)

---

## 3) Statistical summary (distribution of sub-types across use cases)

Total use cases: **13** (UC-01…UC-11) from [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

Counts below = “number of use cases that require the sub-type” (checkbox counting; totals can exceed 13).

- **A1 (metrics change)**: **7 / 13**
- **A2 (events/extremes)**: **6 / 13**
- **A3 (drivers/process)**: **1 / 13**
- **B (trends/patterns)**: **2 / 13**
- **C1 (scale/quality improvement)**: **10 / 13**
- **C2 (credibility/uncertainty guidance)**: **12 / 13**

### Interpretation

- **C2 dominates**: most use cases require uncertainty-safe interpretation, provenance, limitations, and governance rails.
- **C1 is also high**: many use cases require improvements in resolution, interoperability, timeliness, or data QA to be usable.
- The portfolio splits between **A1** (long-term/statistical inputs) and **A2** (event/extreme contexts).
- **A3 is rare** in the current UC drafting: driver/process explanations appear explicitly only where the output is an explainer (UC-06).
