# Intermediate Synthesis: Thai-Anchor Scan for Hardened Asset Concepts (Step 24)

- Date: 2026-04-22
- Scope: Intermediate bridge note for Phase 4 worksheet construction only (no drafting of `CRI_Asset_Tagging_Dictionary_v1.md`)
- Input basis used directly:
  - `../CRI_Asset_Concept_Summary_v1.md`
  - `2026-04-22_asset-concept-hardening_taxonomy-alignment_intermediate.md`
  - `2026-04-22_asset-source-audit_canonical-concept-candidates.md`
  - `2026-04-22_asset-governance-framing-rules_phase3-4.md`
  - `2026-04-22_governance-template-audit_for-asset-phase3-4.md`
  - `asset_indicator_register.md`

## 1) Purpose and use boundary

This note maps each hardened concept (`HC-01` to `HC-11`) to plausible Thai scanning anchors for Phase 4 pre-drafting.
It is designed as a **scan-target shortlist**, not as a final indicator dictionary.

Interpretation constraints follow the stock-to-process framing:
- Stock presence is treated as enabling condition, not realized resilience.
- Each anchor must be interpreted with governance activation and service-flow plausibility.
- Proxy anchors are explicitly flagged where direct administrative inventories are weak.

## 2) Anchor-type legend

- **Administrative registry**
- **Geospatial layer**
- **Budget/admin dataset**
- **Facility inventory**
- **Environmental dataset**
- **Service/platform log**
- **Proxy**

## 3) Hardened concept → Thai-anchor scan matrix (v0.1)

| hardened_concept_id | hardened_concept_label | likely_thai_anchor_type | plausible_thai_anchor_candidate(s) | likely_spatial_unit_or_admin_level | likely_measurement_or_scan_logic | major_caveat_or_guardrail | governance_process_link_for_interpretation | confidence_readiness_flag |
|---|---|---|---|---|---|---|---|---|
| HC-01 | Urban green ecological cooling stock | Geospatial layer; Administrative registry; Proxy | DPT municipal land-use/green-area layers; Bangkok/BMA tree inventory where available; ONEP/PCD urban environmental layers; local government park/green asset registers | Municipality/LAO; district/subdistrict; 250m–1km grid overlay | Map canopy/green stock extent and continuity, then overlay population heat exposure and access-distance proxies | Green area volume alone can overstate resilience; require accessibility and maintenance continuity checks | Link to local O&M budgeting, tree/green-space stewardship routines, and enforcement of land-use protection | **Medium** (direct anchors exist in some cities; uneven national coverage) |
| HC-02 | Urban stormwater and flood-routing stock system (gray + nature-based) | Facility inventory; Geospatial layer; Service/platform log | Municipal drainage asset inventories; RID/urban drainage scheme layers where available; BMA drainage/flood-control infrastructure logs; DDPM flood incident layers as service proxy | City/municipality; drainage catchment/sub-catchment; district | Scan asset network coverage (capture-convey-store-route), then compare with flood occurrence/service interruption logs | Asset presence without condition/maintenance cadence is weak evidence | Link to inspection cycles, drainage maintenance budgets, and inter-agency routing protocols | **Medium** (administrative assets likely available but fragmented) |
| HC-03 | Coastal protection and accommodation built stock | Facility inventory; Geospatial layer; Budget/admin dataset | DMCR coastal protection project inventory; Marine Department/Harbor-side protection records; provincial public works coastal defense projects; EIA-tracked large coastal adaptation structures | Coastal province; district; shoreline segment | Inventory structural protection/accommodation assets by type and age; map shoreline coverage and adjacent exposed settlements | High-CAPEX structures risk lock-in and exposure transfer; require safeguard and flexibility tagging | Link to coastal permitting, safeguard compliance, stage-gate review, and long-term retrofit/revision processes | **Medium-Low** (anchors plausible, harmonization burden high) |
| HC-04 | Coastal socio-ecological buffer and EbA stock | Environmental dataset; Geospatial layer; Administrative registry | DMCR mangrove/coastal ecosystem condition datasets; protected coastal ecosystem boundaries; provincial coastal resource management plans; restoration project registries | Coastal ecosystem unit; shoreline segment; subdistrict/province | Scan ecological condition + continuity of buffer habitats and active restoration footprint | Nominal designation is not functional performance; condition and continuity are required | Link to ecosystem O&M financing continuity, co-management arrangements, and restoration governance | **Medium** (ecological anchors comparatively stronger than built-stock harmonization) |
| HC-05 | Urban ecological form-function stock (biodiversity + ventilation corridors) | Geospatial layer; Environmental dataset; Proxy | City/provincial comprehensive plan corridor layers (where present); land-use control maps; remote-sensing urban morphology proxies for ventilation continuity | City/metropolitan area; corridor segment; grid-cell analysis | Identify corridor continuity/fragmentation, then infer potential form-function support (airflow/cooling) using morphology proxies | Often proxy-heavy; direct airflow-function evidence may be limited | Link to land-use control enforcement and corridor protection decisions | **Low-Medium** (conceptually strong, data often proxy-based) |
| HC-06 | Built-form thermal safety and inclusive public-realm stock | Facility inventory; Administrative registry; Proxy | Building-control/permit datasets for retrofit attributes (where available); municipal public-facility inventories (cooling-capable public spaces); walkability/public-realm datasets from city platforms | Building/facility level aggregated to district/municipality | Scan presence of thermal-safety-supportive design/retrofit and inclusive access features; pair with service-hour or usability proxies | Amenity indicators can drift away from climate function; equity-access checks mandatory | Link to building code enforcement, retrofit incentive programs, and accessibility standards implementation | **Low-Medium** (fragmented building-level data; many proxies) |
| HC-07 | Infrastructure resilience architecture stock (robustness, redundancy, flexibility) | Facility inventory; Budget/admin dataset; Proxy | Utility and infrastructure master plans (redundancy/flexibility provisions); capital investment plans; contingency network design records from key utilities/agencies | Utility service area; municipality/province; national utility footprint | Score existence of redundancy/flexibility design features and renewal pipeline signals | Paper design claims may not reflect operational reality; require service continuity corroboration | Link to capital-renewal governance, anti-lock-in review criteria, and revision-cycle compliance | **Low-Medium** (high relevance, but operationally hard to verify uniformly) |
| HC-08 | Energy, utility, mobility, and communication enabling networks | Service/platform log; Facility inventory; Administrative registry | Electricity utility outage/reliability logs (where accessible); utility network asset registries; public transport and telecom service continuity statistics; emergency communication platform records | Utility service area; province; metro area | Scan reliability/interoperability continuity and emergency-mode operability, not only asset size | Infrastructure scale without reliability/inclusion evidence is misleading | Link to reliability standards, interoperability rules, emergency deployment protocols | **Medium** (service logs can support activation reading if access is granted) |
| HC-09 | Food-system and productive bio-resource stock | Administrative registry; Facility inventory; Proxy | Agricultural production and land-use statistics (NSO/MOAC relevant datasets); municipal fresh-market and logistics facility inventories; urban agriculture/community production registries where present | City-region; province; district | Map productive stock and distribution nodes, then test robustness proxies for supply continuity | Production stock does not guarantee urban access; distribution and affordability mediators are critical | Link to city-region coordination, logistics governance, and local stewardship/extension systems | **Medium-Low** (multi-agency integration needed) |
| HC-10 | Financial and economic resilience buffer stock system | Budget/admin dataset; Administrative registry; Proxy | Public budget reserve/contingency lines (national/provincial/local); social protection and emergency support disbursement datasets; insurance uptake statistics and community finance program records | National/provincial/municipal; household/community for selected proxies | Separate macro/public/household/community buffers; scan availability + plausible uptake/translation proxies | High wealth-bias and scale-mixing risk; do not infer local resilience directly from macro stocks | Link to fiscal transfer rules, social protection delivery mechanisms, and risk-transfer governance | **Medium-Low** (anchors exist, translation to local resilience remains provisional) |
| HC-11 | Human and social capability stock (skills, literacy, connectedness, collective assets) | Administrative registry; Service/platform log; Proxy | Education/skills statistics (NSO and sector datasets); labor upskilling participation records; local civic organization/community group registries; volunteer/disaster-preparedness participation logs | National/provincial to district/community aggregation | Scan distribution of relevant skills/capabilities and collective-resource presence; add connectedness/participation proxies | Narrow HR metrics can miss trust/reciprocity and governance durability | Link to competency system continuity, community organizing support, and inclusion governance quality | **Medium-Low** (baseline anchors available; social-capital dimensions mostly proxy) |

## 4) Readiness triage for Phase 4 scanning

### Relatively stronger for immediate scan (with caveats)
- HC-01, HC-02, HC-04, HC-08

### Usable but integration-heavy / partially proxy-based
- HC-03, HC-09, HC-10, HC-11

### Weakest and most provisional for first-pass dictionary coding
- HC-05, HC-06, HC-07

## 5) Practical scan guardrails to carry into Phase 4 worksheet drafting

1. Keep `proposed_thai_anchor` explicit about source system and access status (public/open, request-based, or unknown).
2. Add `normalization_or_equity_note` for every row (hazard exposure, service dependency, or accessibility check).
3. Add `threshold_lockin_flag` especially for HC-03 and HC-07 classes.
4. Mark proxy-dependent rows as `provisional` in `selection_decision` until direct inventory/service logs are confirmed.
5. Preserve a three-part interpretation chain whenever feasible: **stock evidence + governance activation evidence + service continuity proxy**.

## 6) Scope boundary

This note only completes the intermediate Thai-anchor scan bridge for Step 24.
It does **not** draft `CRI_Asset_Tagging_Dictionary_v1.md`.

