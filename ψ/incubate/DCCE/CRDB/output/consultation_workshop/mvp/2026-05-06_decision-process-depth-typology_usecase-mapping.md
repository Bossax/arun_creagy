# Decision-process depth categorization — Information-type mapping per use case (Screening → Detailed analysis → Options)

**Purpose**: for each CRDB use case, identify the **types of information involved** using a **decision-process depth** lens (instead of categorizing the use case itself). Then summarize the distribution of information-types across use cases.

**Primary input**: use-case statements in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

---

## 1) Category definitions (decision-process depth as *information bundles*)

This lens classifies the *information that must be present* by **how mature / high-stakes** the decision process is:

### A. Screening / scoping information

**Definition**: enough information to identify *whether* a risk matters, *where* it might matter, and what should be investigated next. Often tolerates coarser resolution and higher uncertainty, but must be legible and defensible.

**Typical information**
- high-level hazard context, exposure/vulnerability highlights, “what to look at next”, readable briefs.

**CRDB examples (from use-case wording)**
- UC-03 aims at a curated “one-pager + map set” for policy/planning ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:239)).

---

### B. Detailed analysis information

**Definition**: decision requires quantified or engineering-/operations-grade analysis: correct spatial units, explicit assumptions, traceable baselines, and clear uncertainty semantics.

**Typical information**
- analysis-ready datasets, explicit spatial units/crosswalks, event/impact records with revision history, uncertainty semantics.

**CRDB examples (from use-case wording)**
- UC-07b explicitly calls for planning-grade datasets and GIS-ready access across urban operations and design contexts ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:351)).

---

### C. Options / investment evaluation information

**Definition**: the decision is selecting actions (projects, standards, investments) and needs outputs that support comparing options, justifying budgets, and defending trade-offs.

**Typical information**
- investment justification, loss/damage accounting for allocation, comparison of alternatives, decision thresholds/standards.

**CRDB examples (from use-case wording)**
- UC-03b is explicitly a budget justification evidence pack ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:263)).

---

### D. Cross-cutting enabling information (governance prerequisites)

**Definition**: work that does not correspond to a single depth stage, but **enables all stages** by making baselines, methods, access, and accountability legible.

This category is included because several CRDB use cases (notably baseline endorsement/verification) are explicitly about making the system *usable and safe* regardless of whether the user is screening, analyzing, or selecting options.

**CRDB examples (from use-case wording)**
- UC-10 is baseline verification / endorsement with audit trail ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:418)).

---

## 2) Information-type mapping per use case (checkboxes)

Checkbox rule: a category is checked if the use case text implies that information bundle is required to make the outcome credible (even if the Phase 1 deliverable is only a “starter”).

| Use case                                               | A. Screening info | B. Detailed analysis info | C. Options / investment info | D. Enabling (governance) info |
| ------------------------------------------------------ | ----------------: | ------------------------: | ---------------------------: | ----------------------------: |
| UC-01 Post-event impact & Loss/Damage assessment       |                   |                         ✓ |                            ✓ |                             ✓ |
| UC-02 Early warning / preparedness risk context        |                 ✓ |                         ✓ |                              |                             ✓ |
| UC-03 Provincial risk profile                          |                 ✓ |                           |                              |                             ✓ |
| UC-03b LAO budget justification pack                   |                 ✓ |                         ✓ |                            ✓ |                             ✓ |
| UC-04 Vulnerable group mapping & targeting             |                 ✓ |                         ✓ |                              |                             ✓ |
| UC-05 Heat-health surveillance roadmap (gap→plan)      |                 ✓ |                           |                              |                             ✓ |
| UC-06 Cascading impacts explainer + entry point        |                 ✓ |                           |                              |                             ✓ |
| UC-07 Corridor/infrastructure exposure                 |                 ✓ |                         ✓ |                            ✓ |                             ✓ |
| UC-07b Urban ops + planning-grade design               |                 ✓ |                         ✓ |                            ✓ |                             ✓ |
| UC-08 Statistical baselines + thematic tagging         |                   |                           |                              |                             ✓ |
| UC-09 True economic Loss & Damage estimation           |                   |                         ✓ |                            ✓ |                             ✓ |
| UC-10 Baseline verification / “single source of truth” |                   |                           |                              |                             ✓ |
| UC-11 Financial sector risk & stress testing           |                   |                         ✓ |                            ✓ |                             ✓ |

### Concrete examples of “information types” inside each category

- **A (Screening/scoping information)**
  - policy-facing one-pagers; hazard context + exposure/vulnerability highlights; “what this means” narrative.
  - Example UCs: UC-03 ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:239)), UC-06 ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:316)).

- **B (Detailed analysis information)**
  - machine-readable layers, GIS-ready inputs, explicit spatial units and crosswalks, event/impact schemas + revision history.
  - Example UCs: UC-07b ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:351)), UC-11 ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:459)).

- **C (Options/investment evaluation information)**
  - budget justification packs; loss/damage accounting that supports allocation; assumptions registry for defensibility.
  - Example UCs: UC-03b ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:263)), UC-09 ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:392)).

- **D (Cross-cutting enabling information)**
  - baseline endorsement/selection logic; metadata + provenance; limitations statements; governance and audit trail.
  - Example UCs: UC-10 ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:422)).

---

## 3) Statistical summary (distribution of information bundles across use cases)

Total use cases: **13** (UC‑01…UC‑11) from [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

Counts below = “number of use cases that require the stage” (checkbox counting; totals can exceed 13).

- **A. Initial risk screening / scoping**: **8 / 13**
- **B. Detailed risk analysis**: **8 / 13**
- **C. Options / investment evaluation**: **7 / 13**
- **D. Cross-cutting enablers (governance prerequisites)**: **13 / 13**

### Interpretation
- The use-case set is **balanced** between A and B (many UCs start at scoping but also require a path to analysis-ready outputs).
- A majority require **C (options/investment)** because the portfolio is explicitly decision-support and budget/justification-facing (e.g., UC‑03b, UC‑09, UC‑11).
- **D is universal**: without endorsed baselines, boundary/crosswalk rules, metadata/limitations, and uncertainty-safe guidance, neither screening outputs nor detailed analyses are administratively safe or reusable.

