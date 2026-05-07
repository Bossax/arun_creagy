# Option 4 — Climate Service Format Typology (Maps & Apps / Expert Analysis / Climate-inclusive Consulting / Sharing Practices)

**Purpose**: define the Option 4 categories (service *formats*) with CRDB-relevant examples, then map each CRDB use case to the formats required to deliver it credibly.

**Primary input**: use-case statements in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

---

## 1) Category definitions (service-format lens)

> Note: These categories are **formats of delivery** (how information reaches users), not “types of climate information” (detailed vs trends vs guidance). This makes them useful for climate-service operating model design: staffing, governance, and what can be automated.

### A. Maps & Apps

**Definition (in practice)**: self-serve, repeatable, interface-driven delivery where users can access an output with minimal mediation.

**Typical outputs**
- interactive maps, dashboards, browseable catalogs, export buttons, templated one-pagers.

**CRDB examples (from use-case wording)**
- UC-02 explicitly calls for a **“Risk context” map + briefing export** ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:221)).
- UC-03 calls for a curated **“one-pager + map set”** presented at **3 depths** ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:239)).

**When it fails alone**
- When the core work is *interpretation governance* or *cross-agency endorsement*, not UI.

---

### B. Expert Analysis

**Definition (in practice)**: analyst-mediated synthesis where results depend on judgement, assumptions, validation, and/or method choices that cannot yet be automated safely.

**Typical outputs**
- curated reports with caveats, “which dataset should we use” comparisons, validation flags, assumption registries, method guardrails.

**CRDB examples (from use-case wording)**
- UC-01 requires **validation flags + update history** and standardized post-event reporting (not just a map) ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:189)).
- UC-09 requires “true loss” estimation with **transparent assumptions** and a **methods/coefficients registry** ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:395)).

**When it should evolve**
- As schemas stabilize (MVP-2), baselines are endorsed (MVP-3), and templates become standardized (MVP-1), large parts can become “Maps & Apps”.

---

### C. Climate-inclusive Consulting

**Definition (in practice)**: embedded support inside a broader decision/service context where climate information is only one input. Requires stakeholder engagement, workflow integration, and governance coordination.

**Typical outputs**
- jointly-defined workflows, onboarding + training, integrating outputs into planning/budget cycles, access-control operating rules, institutional role mapping.

**CRDB examples (from use-case wording)**
- UC-04 includes **sensitive data** and requires classification/aggregation/access control rules ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:289)). This is typically not a pure “app” problem.
- UC-07b explicitly spans multi-actor operational + planning-grade needs (BMA/UDDC/DPT) and requires boundary/crosswalk rules and tier separation ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:361)).

**Success condition**
- The service is adopted into real decision routines (not just “published”).

---

### D. Sharing Practices

**Definition (in practice)**: community/coordination formats where value depends on sustained contributions, curation, and governance over time.

**Typical outputs**
- maintained example libraries, shared taxonomies, evolving guidance notes, cross-agency “what good looks like” patterns.

**CRDB examples (from use-case wording)**
- UC-06 requires curated **examples** of cascading impacts and a way to link narratives/datasets ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:318)). This requires ongoing refresh.
- UC-08 involves **tagging frameworks** and ongoing stewardship (FDES/GSBPM-style QA) ([`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:373)).

---

## 2) Use-case mapping (checkbox: “required to deliver credibly”)

| Use case | Maps & Apps | Expert Analysis | Climate-inclusive Consulting | Sharing Practices |
|---|---:|---:|---:|---:|
| UC-01 Post-event impact & Loss/Damage assessment | ✓ | ✓ |  |  |
| UC-02 Early warning / preparedness risk context | ✓ | ✓ |  |  |
| UC-03 Provincial risk profile | ✓ | ✓ |  |  |
| UC-03b LAO budget justification pack | ✓ | ✓ | ✓ |  |
| UC-04 Vulnerable group mapping & targeting |  | ✓ | ✓ |  |
| UC-05 Heat-health surveillance roadmap |  | ✓ | ✓ | ✓ |
| UC-06 Cascading impacts explainer | ✓ | ✓ |  | ✓ |
| UC-07 Corridor/infrastructure exposure |  | ✓ | ✓ |  |
| UC-07b Urban ops + planning-grade design | ✓ | ✓ | ✓ |  |
| UC-08 Statistical baselines + tagging | ✓ | ✓ |  | ✓ |
| UC-09 True economic Loss & Damage estimation |  | ✓ | ✓ |  |
| UC-10 Baseline verification / “single source of truth” | ✓ | ✓ | ✓ | ✓ |
| UC-11 Financial sector risk & stress testing | ✓ | ✓ | ✓ |  |

---

## 3) Statistical summary (distribution by format)

Total use cases: **13** (UC-01…UC-11) from [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md:175).

Counts below = “number of use cases that require the format” (checkbox counting; totals can exceed 13).

- **Maps & Apps**: **8 / 13**
- **Expert Analysis**: **12 / 13**
- **Climate-inclusive Consulting**: **7 / 13**
- **Sharing Practices**: **4 / 13**

### Interpretation
- **Expert Analysis dominates** because nearly every use case contains governance/assumption/validation requirements (e.g., caveats, endorsement, uncertainty semantics) that must be correct before automation.
- **Maps & Apps is still common** because many UCs require an explicit repeatable surface (map, catalog view, exportable pack).
- **Consulting appears whenever institutional constraints dominate** (sensitive data, crosswalk governance, integrating into budget/planning workflows).
- **Sharing Practices appear when the value depends on continuously refreshed examples/taxonomies** (cascading impacts, tagging frameworks, roadmap gaps like heat-health).

