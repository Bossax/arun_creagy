# CRI Asset–Governance Mismatch Crosswalk (M = A - G)

- **Date**: 2026-04-22
- **Conceptual Anchor**: [`2026-04-22-Hardware, Software, and Nonlinear Resilience.md`](../2026-04-22-Hardware,%20Software,%20and%20Nonlinear%20Resilience.md)
- **Theoretical Basis**: The "Hardware/Software" metaphor and the resulting $M = A - G$ (Asset-Governance Mismatch) logic are grounded in Social-Ecological-Technological Systems (SETS) scholarship (McPhearson et al., 2022) and safe-to-fail infrastructure resilience frameworks (Kim et al., 2022).
- **Methodological Standard**: See [Triple-M Taxonomy](#appendix-cri-methodological-standard-the-triple-m-taxonomy) below.
- **Scope**: Crosswalk only (no re-extraction, no register rebuild)
- **Asset source register**: [`asset_indicator_register.md`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/synthesis/asset_indicator_register.md)
- **Governance anchor (current Phase 2)**: [`CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md)

## Crosswalk method (practical)

1. Use grouped asset clusters (not concept collapse) to keep the decision surface readable while preserving lineage.
2. Preserve provenance using register ID sets (`AIR-###`).
3. All entries in this table are classified as **M1: Functional Mismatches** (Gap between Stock and Capability).
4. Classify each M1 sub-type as:
   - `missing`: governance/process logic not represented in current v3 concept set.
   - `weak`: concept exists but is placeholder-level, partially evidenced, or not yet operationalized.
   - `activation-dependent`: governance logic exists but requires bundled cross-pillar activation.

## Mismatch crosswalk table (M1 Type)

| mismatch_id | register_ids                                         | asset cluster (A)                                                                               | nearest governance anchor in v3 (G)                                             | m1_subtype           | mismatch pair statement (M = A - G)                                                                                                                                                        | next governance scan target                                                               |
| ----------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| M1-001      | AIR-001, AIR-002, AIR-014, AIR-017, AIR-018, AIR-043 | Urban cooling and green-system stocks (trees, roofs, inventories, green infra)                  | Pillar 3 **Policy Integration** + Pillar 5 **Digital climate services**         | activation-dependent | Asset evidence is strong, but governance activation requires combined land-use mandate + maintenance finance + digital monitoring workflow not yet encoded as one process indicator chain. | Joint scan of climate/land-use plan clauses + O&M budget lines + urban tree data protocol |
| M1-002      | AIR-003, AIR-016, AIR-037                            | Urban food and city-region food system stocks                                                   | Pillar 3 **Multi-stakeholder collab.** + **Transboundary Feedbacks**            | weak                 | Food-system assets are present, but cross-jurisdiction governance (urban-rural linkage) remains a placeholder concept in v3 and lacks operational anchor mapping.                          | Inter-provincial MoU, food logistics coordination body, local market resilience mandates  |
| M1-003      | AIR-004, AIR-022, AIR-030, AIR-031, AIR-036          | Stormwater and retention stocks (bioswales, storage, wetlands, sewer adaptation)                | Pillar 1 **Risk-informed planning** + Pillar 4 **Infrastructure robustness**    | activation-dependent | Physical drainage/retention assets are identifiable, but governance logic for maintenance cadence and design-standard enforcement is only partially represented.                           | Inspection/maintenance SOP frequency, drainage retrofit compliance records                |
| M1-004      | AIR-005, AIR-008, AIR-015, AIR-040, AIR-041, AIR-042 | Lock-in-prone gray/fail-safe infrastructure systems                                             | Pillar 4 **Infrastructure robustness** + Pillar 1 **Plan revision cycle**       | weak                 | Lock-in risk is explicit in asset evidence, but v3 has no direct anti-lock-in trigger metric (e.g., flexibility/redundancy transition thresholds).                                         | Capital renewal criteria including flexibility/redundancy and safe-to-fail checks         |
| M1-005      | AIR-006, AIR-019                                     | Recreation/public-access and walkability support stocks                                         | Pillar 4 **Service delivery timeliness**                                        | missing              | Equity-sensitive access assets are present, but no direct governance process in v3 tracks inclusive access maintenance/performance under climate stress.                                   | Accessibility compliance + service continuity indicators for parks/public realm           |
| M1-006      | AIR-007                                              | Flood-compatible road redesign stock                                                            | Pillar 3 **Multi-stakeholder collab.** + Pillar 1 **Risk-informed planning**    | activation-dependent | Asset design depends on negotiated trade-offs (mobility vs flood routing), but v3 does not yet encode a trade-off decision protocol indicator.                                             | Traffic/flood trade-off governance protocol and revision cycle                            |
| M1-007      | AIR-009, AIR-035, AIR-044                            | Energy and utility transition stocks (grid backup, renewable diversity, green transport infra)  | Pillar 2 **Resource allocation scale** + Pillar 4 **Infrastructure robustness** | activation-dependent | Technical assets exist, but governance for staged transition sequencing and reliability standards across sectors is not yet concretely measured.                                           | Reliability standard adoption + transition CAPEX/OPEX tracking                            |
| M1-008      | AIR-010                                              | Flood attenuation landscape stock with recreation co-benefits                                   | Pillar 1 **Plan revision cycle** + Pillar 3 **Multi-stakeholder collab.**       | weak                 | Co-benefit asset logic is strong, but community-feedback-to-plan-update loop is not explicitly operationalized in current worksheet fields.                                                | Participatory update cycle evidence tied to hazard plan revisions                         |
| M1-009      | AIR-011                                              | Institutional regulations/institutions framed as “asset”                                        | Pillar 3 **Formal coordination bodies** + Pillar 5 **Data interoperability**    | weak                 | This row is governance-like rather than stock-like; mismatch is category drift between A and G layers, reducing separation clarity.                                                        | Tagging rule to distinguish governance-process evidence from stock evidence               |
| M1-010      | AIR-012, AIR-013                                     | Building thermal adaptation stocks (AC + passive cooling retrofits)                             | Pillar 1 **Risk-informed planning** + Pillar 2 **Climate budget tagging**       | activation-dependent | Asset pathways are known, but no explicit governance indicator for balancing immediate cooling deployment with long-term passive retrofit equity.                                          | Retrofit incentive policy + vulnerable-household targeting mechanism                      |
| M1-011      | AIR-020, AIR-026                                     | Hard coastal defense stocks (seawalls/dikes/giant seawalls)                                     | Pillar 1 **Risk-informed planning** + Pillar 3 **Formal coordination bodies**   | weak                 | Protection assets are represented, but governance safeguards for social side-effects (e.g., involuntary resettlement) are not explicit in v3 concepts.                                     | Safeguard/compensation governance indicators linked to coastal projects                   |
| M1-012      | AIR-021, AIR-034, AIR-052                            | Flood-proof housing and settlement form stocks                                                  | Pillar 1 **Policy Integration** + Pillar 4 **Infrastructure robustness**        | missing              | Built-form assets are present, but no clear governance process indicator ties housing adaptation standards to inclusion and affordability outcomes.                                        | Building code adaptation compliance + vulnerable-group housing support                    |
| M1-013      | AIR-023, AIR-024                                     | Advance coastal form stocks (reclamation, floating structures)                                  | Pillar 1 **Risk-informed planning** + Pillar 5 **Risk Assessment depth**        | weak                 | Experimental/high-uncertainty assets require anticipatory governance gates that are not explicitly represented in current v3 worksheet logic.                                              | Experimental project stage-gate and uncertainty governance criteria                       |
| M1-014      | AIR-025, AIR-027, AIR-029                            | Coastal socio-ecological and EbA system stocks                                                  | Pillar 3 **Transboundary Feedbacks** + Pillar 2 **Resource allocation scale**   | weak                 | Multi-level and cross-sector governance is required, but transboundary concept remains placeholder-level and financing alignment logic is under-specified.                                 | Coastal zone multi-level compact + dedicated ecosystem O&M finance line                   |
| M1-015      | AIR-028                                              | Dense coastal infrastructure exposure stock                                                     | Pillar 1 **Risk-informed planning** + Pillar 5 **Risk Assessment depth**        | activation-dependent | Exposure concentration is explicit, but governance activation depends on linking risk diagnostics to development control and enforcement loops.                                            | Risk-informed permit controls and enforcement closure indicators                          |
| M1-016      | AIR-032, AIR-033                                     | Biodiversity/ventilation structure stocks                                                       | Pillar 1 **Policy Integration** + Pillar 4 **Infrastructure robustness**        | missing              | Ecological form-function assets are visible, but current v3 process anchors do not directly encode ventilation corridor and biodiversity-protection enforcement.                           | Land-use and environmental regulation linkage for ventilation/ecology corridors           |
| M1-017      | AIR-038                                              | Protective infrastructure deployment stock                                                      | Pillar 3 **Distributed Command Agility** + Pillar 2 **Emergency budget flow**   | weak                 | Asset value is tied to command/resource deployment speed, yet distributed command remains a design placeholder in v3.                                                                      | Delegation SOP readiness + rapid deployment budget trigger logic                          |
| M1-018      | AIR-039                                              | Communication technology stock                                                                  | Pillar 5 **Digital climate services** + Pillar 5 **Data interoperability**      | activation-dependent | Digital assets exist, but interoperability, inclusiveness, and operational reliability governance are not yet locked to measurable criteria.                                               | Service reliability KPI + inter-agency data exchange compliance                           |
| M1-019      | AIR-045, AIR-048                                     | Produced/public capital stock base                                                              | Pillar 2 **Resource allocation scale** + Pillar 1 **Plan revision cycle**       | missing              | Macro-level capital stocks are strong asset signals, but governance dictionary has limited process indicators for resilience-quality of capital composition.                               | Capital composition governance (resilient vs lock-in-prone investment share)              |
| M1-020      | AIR-046, AIR-051, AIR-055                            | Human capability stocks (skills/knowledge/literacy)                                             | Pillar 6 **Emergency staff capacity** + **Staff Training frequency**            | weak                 | Human-capital evidence is broad, while v3 HR indicators are narrow (emergency staffing/training frequency) and do not capture wider resilience skill ecology.                              | Cross-sector competency framework and training coverage metric expansion                  |
| M1-021      | AIR-047, AIR-049, AIR-053, AIR-054, AIR-057          | Financial resilience buffer stocks (NFA, support instruments, savings, insurance, microfinance) | Pillar 2 **Emergency budget flow** + **Climate budget tagging**                 | missing              | Financial stocks are evident, but governance process anchors are mostly public-budget-centric and under-represent household/community/private buffer mechanisms.                           | Household/community financial resilience governance and uptake monitoring                 |
| M1-022      | AIR-050, AIR-056                                     | Social capital and collective ownership stocks                                                  | Pillar 3 **Multi-stakeholder collab.** + Pillar 4 **Digital Social Mediation**  | weak                 | Social cohesion assets are present, but v3 lacks concrete process indicators for trust, reciprocity, and collective governance durability in shocks.                                       | Community governance continuity and inclusion performance indicators                      |

## Quick totals

- Total asset register rows covered: **57 / 57** (via grouped provenance sets)
- Total mismatch entries produced: **22 (all M1 Type)**
- M1 sub-type distribution:
  - `missing`: 6
  - `weak`: 10
  - `activation-dependent`: 6

---

# APPENDIX: CRI Methodological Standard: The Triple-M Taxonomy

**Version**: 1.0 (2026-04-23)
**Status**: Frozen Anchor
**Objective**: To prevent "Expert Drift" by explicitly defining the three types of "mismatch" encountered in the CRI framework development.

### 1. M1: Functional Mismatch (The Strategy Layer)
- **Definition**: The gap between an identified system stock (Asset/Hardware) and the institutional capacity to manage it (Governance/Software).
- **Equation**: $M = A - G$
- **Usage**: Used in the Strategic Crosswalk to identify policy blindspots.
- **Example**: A city has high-resolution flood maps (Asset), but no mandate to use them in building-permit enforcement (Governance Gap).

### 2. M2: Anchoring Mismatch (The Empirical Layer)
- **Definition**: The gap between a theoretical concept (derived from literature) and the actual administrative data available in Thailand.
- **Equation**: $M = Concept - Data$
- **Usage**: Used in the Tagging Dictionary to identify "Data Investment" needs.
- **Example**: The literature requires "Community Reciprocity Scales," but the only Thai trace is "Village Fund Participation Rates" (Proxy Gap).

### 3. M3: Fidelity Mismatch (The Forensic Layer)
- **Definition**: A failure in the research or synthesis process where the output deviates from the source evidence or user instructions.
- **Equation**: $M = Synthesis - Source$
- **Usage**: Used in the Workflow Log to track AI errors and corrections.
- **Example**: The AI cites an internal note as "Evidence" instead of the primary literature source (Research Error).

---

## Mandate for the Oracle
Every mention of "mismatch" in CRI deliverables must be prefixed with the corresponding ID (M1, M2, or M3). Any statement failing this protocol is to be treated as a hypothesis until audited.
