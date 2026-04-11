# CRI Phase 2 — Immediate Blocks and Design Rationale

## 1. Immediate Blocks to Move Phase 2 Forward

- **Evidence spine not fully wired**
  - E-CRI-010..015 entries for Hearing 1 are only partially populated in [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md).
  - [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md) does not yet systematically reference those IDs across dimensions.

- **Capacity-tagging contract not fully locked in use**
  - Concept and rules are defined in [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md), but:
    - V1.x still needs a short, explicit "current contract" paragraph for how helpers should treat LPA/Sustainable City/admin datasets.
    - Transformative capacity stance and spatial-resolution contract need to be written explicitly into [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md) and then referenced from the registry/coverage map.

- **Profile-first output not yet demonstrated end-to-end**
  - `plan.md` expects at least one fully worked example profile (one province) with:
    - Coping/Adaptive/Transformative scores.
    - Asset vs process grouping.
    - Data-richness/confidence overlay.
    - Narrative gap diagnostics.
  - This prototype is not yet frozen as a reference artifact in `ψ/incubate/DCCE/CRI/output/`.

- **Phase 1 / Phase 2 linkage not operationalized in data**
  - Concept is clear in [`ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%201%20Methodology.md) and [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md), but:
    - Gap-flag protocol ("Administrative Gap" vs low risk) needs a concrete, documented rule + example note in the Phase 1 pipeline.
    - At least one pilot analysis slice (a few provinces) should exercise this rule and be logged as evidence.

## 2. Why Phase 2 Steers Away from a TOR-Style CRI

### 2.1 Explicit Objectives (from the current stack)

From [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md) and [`ψ/incubate/DCCE/CRI/plan.md`](ψ/incubate/DCCE/CRI/plan.md):

- **Deliver a policy tool, not just a ranking**
  - TOR asks for a "National Index"; the methodology reframes this as **capacity profiles + impact context** so provincial actors know _what to change_, not just where they sit in a league table.

- **Stay honest about data reality**
  - Available datasets (LPA, Sustainable City, admin systems) are largely binary or asset-like; treating them as high-fidelity process measures would be misleading.
  - The two-speed Baseline/Target design plus data-richness/confidence scores is a deliberate response to this constraint.

- **Align with SES and governance evidence**
  - Literature and syntheses (e.g. [`ψ/incubate/DCCE/CRI/output/CRI_capacity_concepts_synthesis.md`](ψ/incubate/DCCE/CRI/output/CRI_capacity_concepts_synthesis.md), resilience-measurement notes, process-based frameworks) show that **process-based, governance-oriented indicators** better track real resilience than static asset stocks.
  - The capacity categories (Coping/Adaptive/Transformative) are defined as process/governance constructs first, with assets treated as enablers, not the core measure.

- **Avoid the "ranking trap" and perverse incentives**
  - A single composite score encourages gaming (optimising visible assets or easy check-box actions).
  - Profile-first visuals, explicit gap reports, and an attached "data investment roadmap" are meant to change conversations from "who is #1" to "what institutional capacities and data systems must we upgrade".

### 2.2 Implicit Objectives (reading across retros, handoffs, and design notes)

- **Political defensibility and audit trail**
  - The move to an evidence spine (registry + coverage map) and CRI ledgers reflects an implicit goal: any contentious design choice (indicator, weight, capacity stance) should be traceable to explicit evidence and hearings.
  - Steering away from a black-box composite CRI reduces accusations of arbitrariness.

- **Cross-project coherence (CRDB / BTR / CRI)**
  - CRI is positioned as "the product" that consumes curated data and governance structures emerging from CRDB and BTR.
  - A process/governance-centric CRI meshes better with CRDB’s catalog-and-govern role and BTR’s DRS/DRM contracts than a pure impact ranking would.

- **Education of counterparts**
  - The methodology explicitly states an educational purpose: to move DCCE from disaster-loss thinking to a staged view of capacities (Coping → Adaptive → Transformative) and to make process quality visible.
  - Designing the index around capacity categories and process indicators is itself a teaching device.

## 3. Actionable Todo List (for implementation modes)

- [x] **Wire Hearing 1 fully into the evidence spine**
  - [x] Complete E-CRI-010..015 rows in [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) for all Hearing 1 artifacts.
  - [x] Update [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md) so each dimension references these IDs and states their contribution.

- [ ] **Lock and broadcast the capacity-tagging contract**
  - [ ] Add a short "current contract" section to [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md) (Baseline/Target + data-richness + asset vs process grouping).
  - [ ] In [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md), encode the current Transformative capacity stance and spatial-resolution contract, with explicit links back to hearing evidence.

- [ ] **Demonstrate the profile-first product on one province**
  - [ ] Select a pilot province with reasonable data coverage.
  - [ ] Compute Coping/Adaptive/Transformative scores with confidence overlay using the tagging rules.
  - [ ] Produce a radar/profile visualization plus a short narrative gap note under `ψ/incubate/DCCE/CRI/output/`, then register it as evidence.

- [ ] **Operationalize Phase 1–Phase 2 linkage in data**
  - [ ] Create a short "Administrative Gap" protocol note inside the Phase 1 pipeline, with at least one worked example using hazard vs relief series.
  - [ ] Run a narrow pilot analysis (a few provinces) applying this rule; log results as a new output and wire it into the evidence registry and coverage map.
