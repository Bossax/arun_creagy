# CRI Phase 1 — Data Review and Pre‑Processing Pipeline

Scope: Data review and pre‑processing steps needed to make Phase 1 (Impact / Fiscal Relief Index) ready for analysis and visualization.

This pipeline assumes the dependencies listed in [`ψ/incubate/DCCE/CRI/plan.md`](ψ/incubate/DCCE/CRI/plan.md), especially DDPM impact series, fiscal relief streams, GPP denominators, population data, and global/spatial layers.

The strategy of CRI Phase 1 is deliberately **minimal change**:

- Reuse as much as possible from the **CRI Pilot** (TEI) datasets and structure.
- Request **updated versions of the same datasets** from line agencies where needed.
- Introduce **new datasets only where necessary** to:
  - increase spatial resolution via dasymetric mapping, and
  - add explicit gap and data‑quality governance.

---

## High‑Level Stages (Minimal‑Change View)

1. **Reuse and inventory pilot datasets** (DDPM, OAE relief, NESDC GPP, DOPA population, pilot sheets) and request updated extracts where needed.
2. **Schema harmonization and cleaning** of these pilot‑derived tables, without changing their underlying meaning.
3. **Impact variable construction** using pilot logic where sound, with explicit corrections (Fiscal Relief Index, clarified GPP denominator).
4. **Denominator and exposure preparation** by formalizing GPP and population denominators and introducing new spatial layers for dasymetric mapping.
5. **Constrained redistribution** from province level to finer spatial units using exposure proxies derived from the new spatial layers.
6. **Gap‑flagging and data‑quality labelling** (0 vs missing, administrative gaps) as a new governance layer.
7. **Evidence registration** (E‑CRI IDs) and coverage mapping across both reused and new components.
8. **Assembly of analysis‑ready tables** for modeling and visualization.

---

## Stage 1 — Inventory and Ingest (Pilot First)

- [ ] Start from the 7 pilot datasets described in [`ψ/incubate/DCCE/CRI/inbox_source/Climate Risk Index (CRI) Pilot Methodology.md`](ψ/incubate/DCCE/CRI/inbox_source/Climate Risk Index (CRI) Pilot Methodology.md) and the pilot Excel file referenced in [`ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%201%20Methodology.md).
- [ ] List all current and requested datasets in a small inventory table (source, owner, years, spatial unit, update status).
- [ ] For each dataset, capture where the raw files live under `ψ/incubate/DCCE/CRI/inbox_source/` and assign or confirm an `E‑CRI‑###` ID in [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md).
- [ ] Confirm for each stream whether we have **final official** extracts, **pilot‑era TEI working tables**, or **new CRI 2 updates** from agencies.
- [ ] Record any contractual / confidentiality constraints that may affect how fields can be transformed or published.

Output: a one‑page inventory note under `ψ/incubate/DCCE/CRI/inbox_note/` plus updated registry entries.

---

## Stage 2 — Schema Harmonization and Cleaning (Pilot‑Derived Tables)

- [ ] For DDPM / disaster impact series:
  - [ ] Standardize event and time keys (event ID, year, disaster type, province code, etc.).
  - [ ] Normalize province codes to the canonical code list used in CRI (linkable to DOPA and NESDC codes).
  - [ ] Clean and document units (counts vs rates) and any top‑coding or aggregation rules.

- [ ] For fiscal relief streams (central emergency funds, OAE agricultural relief, others):
  - [ ] Normalize date fields and fiscal year mapping.
  - [ ] Clean currency fields (numeric types, inflation adjustment decision recorded even if not yet applied).
  - [ ] Align beneficiary location attributes to the same province code scheme as DDPM.

- [ ] For denominators (GPP) and population:
  - [ ] Confirm total vs sectoral GPP availability per year; document gaps.
  - [ ] Align GPP and population tables to the same province code and year range.

Output: cleaned, schema‑harmonized tables for DDPM, fiscal relief, GPP, and population in a consistent format (e.g. long tables with `year`, `province_code`, `value`), with a short cleaning note.

---

## Stage 3 — Impact Variable Construction (Pilot Logic, Corrected)

- [ ] Define and implement the **human impact measure(s)** (e.g. deaths, affected people, composite index):
  - [ ] Decide whether to use separate indicators or a simple composite for Phase 1 outputs.
  - [ ] Document the formula and rationale in [`ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%201%20Methodology.md).

- [ ] Define and implement the **Fiscal Relief Index** numerator(s):
  - [ ] Choose the preferred cross‑sector relief proxy (e.g. central emergency funds) and how OAE agricultural relief is used (subset vs supplement).
  - [ ] Specify whether relief figures are used as‑is or adjusted (e.g. per event, per incident type).

- [ ] Implement Phase 1 impact measures at the **province × year** level:
  - [ ] Human impact series.
  - [ ] Fiscal relief series.
  - [ ] Any combined impact indicator, if needed, with clear documentation.

Output: a set of province‑level impact tables and updated formulas in the Phase 1 methodology.

---

## Stage 4 — Denominator and Exposure Preparation (Pilot Denominators + New Spatial Layers)

- [ ] Prepare **GPP denominators** for fiscal measures:
  - [ ] Decide on total GPP vs sectoral GPP; document the bias where only total GPP is available, as called out in [`ψ/incubate/DCCE/CRI/plan.md`](ψ/incubate/DCCE/CRI/plan.md).
  - [ ] Compute GPP‑normalized indicators (e.g. relief per unit GPP).

- [ ] Prepare **population denominators** for human impact measures:
  - [ ] Use DOPA population registration totals as the primary denominator.
  - [ ] Create per‑capita versions of key impact indicators.

- [ ] Prepare **exposure proxies** for spatial redistribution and blind spots:
  - [ ] Derive exposure layers from WorldPop, ESA WorldCover, and any hazard masks (e.g. flood‑prone areas from GISTDA).
  - [ ] Create separate proxies for agricultural vs urban/industrial exposure.

Output: standardized denominator tables and raster/vector layers ready for constrained redistribution and blind‑spot analysis.

---

## Stage 5 — Constrained Redistribution (Province → Finer Units)

- [ ] Decide target spatial units for Phase 1 outputs (e.g. sub‑districts, grid cells, or custom zones aligned to later capacity profiles).
- [ ] For each impact measure (human impact, fiscal relief):
  - [ ] Design redistribution weights using the chosen exposure proxies.
  - [ ] Implement constrained redistribution so that sums at finer units equal the original province totals.

- [ ] Document the redistribution method in the Phase 1 methodology, including:
  - [ ] Choice of weights (which proxy, how combined).
  - [ ] Any thresholds or masking rules (e.g. excluding uninhabited areas).

Output: spatially refined impact datasets that preserve province‑level totals and are ready for mapping.

---

## Stage 6 — Gap‑Flagging and Data‑Quality Labels

- [ ] Implement the **gap‑flag protocol** described in [`ψ/incubate/DCCE/CRI/plan.md`](ψ/incubate/DCCE/CRI/plan.md):
  - [ ] Define rules for when `0` is treated as true low impact vs administrative gap (e.g. hazard present AND admin relief = 0 ⇒ `AdministrativeGap = 1`).
  - [ ] Cross‑check against hazard masks and exposure layers to avoid mis‑labelling genuinely hazard‑free areas.

- [ ] Add data‑quality fields to the impact tables, such as:
  - [ ] `DataSource` (official series, TEI extract, inferred).
  - [ ] `AdminGapFlag` (0/1).
  - [ ] `CompletenessScore` (simple categorical rating per province × year).

- [ ] Draft a short **Data Quality Flag** note under `ψ/incubate/DCCE/CRI/output/` referenced by the Phase 1 methodology.

Output: enriched impact tables with gap and quality labels, plus a concise narrative note.

---

## Stage 7 — Evidence Registration and Coverage Mapping

- [ ] For each major step (cleaning, construction, redistribution, flagging):
  - [ ] Ensure the underlying datasets and key scripts/notebooks are registered in [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) with `E‑CRI‑###` IDs.
  - [ ] Update [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md) to show where Phase 1 is well‑supported vs thin.

- [ ] Link the completed pipeline description from this plan into the Phase 1 methodology as the canonical description of data processing steps.

Output: registry and coverage map updated so that every Phase 1 indicator and map has traceable evidence.

---

## Stage 8 — Analysis‑Ready Tables and Outputs

- [ ] Assemble a set of **analysis‑ready tables**, including at minimum:
  - [ ] `province_year_impact.csv` (human impact, fiscal relief, denominators, per‑capita and per‑GPP metrics, gap flags).
  - [ ] `spatial_unit_impact.csv` or geopackage (redistributed impact metrics with quality flags).

- [ ] Confirm that these tables:
  - [ ] Align with the definitions in [`ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%201%20Methodology.md).
  - [ ] Can be directly consumed by mapping tools and simple statistical analysis without further cleaning.

- [ ] Optionally, create a minimal **Phase 1 data dictionary** note that lists variables, units, and definitions for all analysis‑ready fields.

Output: stable, documented input tables for Phase 1 analysis and visualization; Phase 1 is ready for model exploration and stakeholder‑facing products.
