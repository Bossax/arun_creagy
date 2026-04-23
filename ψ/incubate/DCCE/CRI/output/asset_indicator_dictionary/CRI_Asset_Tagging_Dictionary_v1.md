---
type: knowledge_artifact
status: frozen_structure
version: 1.0-phase4
created: 2026-04-22
last_updated: 2026-04-22
project:
  - DCCE_CRI
title: CRI Phase 4 Asset Tagging Dictionary v1 (Stock-Focused Thai Scan Worksheet)
tags:
  - cri
  - phase4
  - asset_stock
  - sets_framework
  - worksheet
---

# CRI Asset Tagging Dictionary v1

## 1) Methodological conclusion: stock-first, activation-required

This worksheet treats each asset concept as **enabling stock** (structural potential), not realized resilience performance.
All rows are interpreted through a three-part chain:
1. stock evidence,
2. governance activation evidence,
3. service continuity plausibility.

## 2) Frozen worksheet schema (v1)

| hardened_asset_concept | capacity_role_or_functional_relevance | sets_domain | governance_activation_link | proposed_thai_anchor | evidence | candidate_indicator_or_data_field | stock_side_interpretation_note | normalization_or_equity_note | threshold_lockin_flag | scan_or_selection_decision |
|---|---|---|---|---|---|---|---|---|---|---|

## 3) Phase 4 worksheet rows (hardened concepts + Thai-anchor scan)

### 3.1 Ecological-primary concepts


| hardened_asset_concept | capacity_role_or_functional_relevance | sets_domain | governance_activation_link | proposed_thai_anchor | evidence | candidate_indicator_or_data_field | stock_side_interpretation_note | normalization_or_equity_note | threshold_lockin_flag | scan_or_selection_decision |
|---|---|---|---|---|---|---|---|---|---|---|
| Urban green ecological cooling stock | Coping, Adaptive | Ecological (primary); Technological, Social (linked) | Land-use protection + O&M budgeting + stewardship + monitoring workflow | DPT municipal green-area layers; city tree inventories (where available); ONEP/PCD urban environmental layers (mixed open/request-based) | McPhearson et al. 2022; Sharifi 2023; Feldmeyer et al. 2019 | Canopy/green continuity; maintenance continuity proxy; population-weighted access to cooling stock | Cooling potential stock only; do not infer realized resilience from volume alone | Normalize against heat exposure and vulnerable-group concentration; check distribution/access equity | potential | PRIORITY_SCAN |
| Coastal socio-ecological buffer and EbA stock | Adaptive, Transformative | Ecological (primary); Social linkage explicit | Multi-level coastal governance + cross-sector coordination + ecosystem O&M finance continuity | DMCR mangrove/coastal condition datasets; protected coastal ecosystem boundaries; restoration registries (mixed open/request-based) | IPCC AR6 WGII CCP2 (2022); Sharifi 2023 | Habitat condition index; continuity/fragmentation of coastal buffers; restoration continuity | Nominal designation is insufficient without condition and continuity evidence | Normalize by exposed coastal settlements and service dependency; retain access/distribution checks | none_to_potential | PRIORITY_SCAN |
| Urban ecological form-function stock (biodiversity + ventilation corridors) | Adaptive | Ecological | Land-use control enforcement for corridor integrity | Comprehensive-plan corridor layers (where present); land-use maps; morphology proxies (mostly proxy/request-based) | Feldmeyer et al. 2019; Sharifi 2023 | Corridor continuity score; fragmentation ratio; ventilation-form proxy | Proxy-dependent row; keep as potential until direct functional evidence improves | Normalize by heat hotspots and exposed population; avoid proxy-only overclaiming | potential | PROVISIONAL_PROXY |

### 3.2 Technological-primary concepts


| hardened_asset_concept | capacity_role_or_functional_relevance | sets_domain | governance_activation_link | proposed_thai_anchor | evidence | candidate_indicator_or_data_field | stock_side_interpretation_note | normalization_or_equity_note | threshold_lockin_flag | scan_or_selection_decision |
|---|---|---|---|---|---|---|---|---|---|---|
| Urban stormwater and flood-routing stock system (gray + nature-based) | Coping, Adaptive | Technological + Ecological | Drainage standards + inspection cadence + retrofit enforcement + cross-agency flood-routing protocols | Municipal drainage inventories; RID drainage scheme layers; DDPM flood incident logs (fragmented/request-based) | McPhearson et al. 2022; IPCC AR6 WGII CCP2 (2022); Feldmeyer et al. 2019 | Asset network coverage (capture/convey/store/route); inspection compliance; event service interruption proxy | Asset presence alone is weak without condition and maintenance evidence | Normalize by hazard intensity and exposed service demand; map service-gap distribution | none_to_potential | PRIORITY_SCAN |
| Coastal protection and accommodation built stock | Coping, Adaptive | Technological (primary); Ecological (linked) | Coastal permitting + safeguard compliance + stage-gate review + revision/retrofit governance loop | DMCR coastal protection inventory; marine/provincial public works records; EIA-tracked structures (mostly request-based) | IPCC AR6 WGII CCP2 (2022); Kim et al. 2022 | Shoreline protection coverage by type/age; safeguard compliance signal; flexibility provision flag | Conditionally beneficial stock; possible exposure transfer and rigidity must remain explicit | Normalize by protected population exposure and displacement burden distribution | high_concern | SCAN_WITH_INTEGRATION_CAVEAT |
| Built-form thermal safety and inclusive public-realm stock | Coping, Adaptive | Technological (primary); Social (linked) | Building code enforcement + retrofit incentives + accessibility implementation + continuity protocols | Building permit/control retrofit attributes (where available); municipal cooling-capable facilities; walkability/public-realm datasets (fragmented/proxy-heavy) | Sharifi 2023; McPhearson et al. 2022; Feldmeyer et al. 2019 | Thermal-supportive retrofit coverage; inclusive access feature coverage; cooling usability proxy | Amenity indicators can drift from climate function; keep climate-service interpretation explicit | Normalize by heat exposure and vulnerable-group accessibility distribution | potential | PROVISIONAL_PROXY |
| Infrastructure resilience architecture stock (robustness, redundancy, flexibility) | Coping, Adaptive, Transformative | Technological | Capital-renewal criteria + anti-lock-in review + redundancy/flexibility standards + periodic revision cycle | Utility/infrastructure master plans; capital plans; contingency network design records (mostly request-based/proxy-derived) | Kim et al. 2022; Sharifi 2023; Zeng et al. 2022 | Redundancy design-feature presence; flexibility provisions; renewal pipeline signal | Paper design claim is insufficient without operational corroboration | Normalize by critical service dependency and hazard stress profile; avoid CAPEX-size scoring | high_concern | PROVISIONAL_PROXY |
| Energy, utility, mobility, and communication enabling networks | Coping, Adaptive, Transformative | Technological (primary); Social (linked) | Reliability standards + interoperability rules + emergency deployment protocols | Utility outage/reliability logs (where accessible); utility registries; transport/telecom continuity statistics (mixed/request-based) | Zeng et al. 2022; Kim et al. 2022; Feldmeyer et al. 2019 | Reliability continuity metric; interoperability/failover proxy; emergency-mode operability | Stock scale is insufficient without continuity and inclusion evidence | Normalize by service dependency and inter-district access inequality | potential | PRIORITY_SCAN |

### 3.3 Social-primary and cross-domain concepts


| hardened_asset_concept | capacity_role_or_functional_relevance | sets_domain | governance_activation_link | proposed_thai_anchor | evidence | candidate_indicator_or_data_field | stock_side_interpretation_note | normalization_or_equity_note | threshold_lockin_flag | scan_or_selection_decision |
|---|---|---|---|---|---|---|---|---|---|---|
| Food-system and productive bio-resource stock | Coping, Adaptive | Social + Ecological (primary); Technological (linked) | City-region coordination + logistics governance + stewardship/extension systems | NSO/MOAC agricultural and land-use statistics; market/logistics facility inventories; urban agriculture registries (integration-heavy/mixed) | Sharifi 2023; Zeng et al. 2022; McPhearson et al. 2022 | Productive stock diversity/continuity; distribution-node robustness; logistics continuity proxy | Productive stock presence does not guarantee access continuity | Normalize by food-access vulnerability and affordability stress across areas/groups | none_to_potential | SCAN_WITH_INTEGRATION_CAVEAT |
| Financial and economic resilience buffer stock system | Coping, Adaptive | Social + Technological | Fiscal transfer rules + social-protection delivery + risk-transfer governance + uptake mechanisms | Public reserve/contingency budget lines; emergency disbursement datasets; insurance/community finance uptake statistics (mixed/request-based) | World Bank 2024; IMF 2021; Sharifi & Yamagata 2016 | Multi-layer buffer availability (macro/public/household/community); uptake/translation proxy | Keep scale layers explicit; avoid direct macro-to-local inference | Normalize by hazard-exposed low-income populations and effective access to transfers | high_concern | SCAN_WITH_INTEGRATION_CAVEAT |
| Human and social capability stock (skills, literacy, connectedness, collective assets) | Coping, Adaptive, Transformative | Social | Competency system continuity + community organization support + inclusion governance quality | Education/skills statistics; upskilling participation; civic/community registries; volunteer preparedness logs (mixed/proxy-involved) | Sharifi & Yamagata 2016; World Bank 2024; Zeng et al. 2022 | Capability distribution metric; collective-asset presence; connectedness/participation proxy | Avoid narrow HR-only proxying; include collective and reciprocity dimensions | Normalize by vulnerable-group inclusion and participation distribution | none_to_potential | SCAN_WITH_INTEGRATION_CAVEAT |

## 4) Decision code legend

- `PRIORITY_SCAN`: stronger immediate feasibility for first-pass Thai data scanning.
- `SCAN_WITH_INTEGRATION_CAVEAT`: usable anchors exist but require cross-system harmonization.
- `PROVISIONAL_PROXY`: weak direct inventory evidence or high proxy dependence; keep visible and do not overclaim.

## 5) Scope boundary

This artifact completes the Phase 4 worksheet drafting step only.
Final structural alignment verification is intentionally deferred to the next workflow step.
