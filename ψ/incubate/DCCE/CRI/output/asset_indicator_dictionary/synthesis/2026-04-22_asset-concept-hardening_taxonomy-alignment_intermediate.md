# Intermediate Synthesis: Asset Concept Hardening + Taxonomy Alignment (Step 22)

- Date: 2026-04-22
- Scope: Intermediate hardening surface for Phase 3 drafting only (no direct drafting of Phase 3/4 deliverables)
- Inputs used:
  - `2026-04-22_asset-governance-framing-rules_phase3-4.md`
  - `2026-04-22_governance-template-audit_for-asset-phase3-4.md`
  - `2026-04-22_asset-source-audit_canonical-concept-candidates.md`
  - `asset_indicator_register.md` (57 rows; AIR-001 to AIR-057)
  - `2026-04-22_asset_governance_mismatch_crosswalk_v3.md` (M-001 to M-022)

## 1) Hardening method used (concise)

1. Collapse near-duplicate labels into canonical stock concepts while preserving AIR-ID lineage.
2. Keep SETS assignment explicit per concept (primary domain + linked domains where needed).
3. Attach likely capacity role(s) (Coping / Adaptive / Transformative) as interpretation guidance.
4. Enforce stock-as-enabling-condition framing (stock ≠ realized resilience).
5. Encode governance activation dependency and guardrails (equity/access/lock-in/threshold).

## 2) Hardened canonical concept groups (Phase 3 drafting surface)

| concept_id | hardened_concept_label_v1                                                              | SETS domain alignment                                       | likely capacity role(s)          | interpretation guardrails (v1)                                                                                                                        | governance-link / activation logic                                                                                                                    | register trace (AIR)                                                   | mismatch hooks             | status                          |
| ---------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------- | ------------------------------- |
| HC-01      | Urban green ecological cooling stock                                                   | Ecological (primary); Technological, Social (linked)        | Coping, Adaptive                 | Do not infer resilience from canopy/green volume alone; pair with access and maintenance continuity; control green-gentrification risk.               | Requires land-use protection, O&M budgets, stewardship, and monitoring/data workflows to convert stock into cooling and heat-risk reduction services. | AIR-001, AIR-002, AIR-014, AIR-017, AIR-018, AIR-043                   | M-001, M-016               | Core                            |
| HC-02      | Urban stormwater and flood-routing stock system (gray + nature-based)                  | Technological + Ecological                                  | Coping, Adaptive                 | Presence of assets is insufficient without maintenance cadence, design compliance, and service continuity checks during extreme events.               | Activated by drainage standards, inspection and retrofit enforcement, and cross-agency flood-routing protocols.                                       | AIR-004, AIR-007, AIR-010, AIR-022, AIR-030, AIR-031, AIR-036          | M-003, M-006, M-008        | Core                            |
| HC-03      | Coastal protection and accommodation built stock                                       | Technological (primary); Ecological (linked)                | Coping, Adaptive                 | High-CAPEX protection can hide exposure transfer and lock-in; include safeguards for displacement and long-run flexibility.                           | Requires coastal risk-informed planning, social safeguard governance, stage-gates for experimental forms, and permit/enforcement loops.               | AIR-020, AIR-021, AIR-023, AIR-024, AIR-026, AIR-028, AIR-029          | M-011, M-012, M-013, M-015 | Core (with provisional subtype) |
| HC-04      | Coastal socio-ecological buffer and EbA stock                                          | Ecological (primary); Social/Institutional linkage explicit | Adaptive, Transformative         | Treat ecological condition and continuity as core; avoid counting nominal designation without management effectiveness and finance continuity.        | Depends on multi-level coastal governance compacts, cross-sector coordination, and dedicated ecosystem O&M financing.                                 | AIR-025, AIR-027                                                       | M-014                      | Core                            |
| HC-05      | Urban ecological form-function stock (biodiversity + ventilation corridors)            | Ecological                                                  | Adaptive                         | Avoid proxy-only interpretation; require evidence that ecological form supports thermal/air-flow service function.                                    | Activated by land-use controls and environmental regulation enforcement for corridor integrity.                                                       | AIR-032, AIR-033                                                       | M-016                      | Core                            |
| HC-06      | Built-form thermal safety and inclusive public-realm stock                             | Technological (primary); Social (linked)                    | Coping, Adaptive                 | Distinguish cooling capacity from equitable usability; walkability/recreation should remain climate-linked, not amenity-only.                         | Requires code/planning integration, retrofit incentives, accessibility standards, and service continuity protocols under climate stress.              | AIR-006, AIR-012, AIR-013, AIR-019, AIR-034                            | M-005, M-010, M-012        | Provisional-leaning             |
| HC-07      | Infrastructure resilience architecture stock (robustness, redundancy, flexibility)     | Technological                                               | Coping, Adaptive, Transformative | Explicitly monitor lock-in and threshold behavior; fail-safe dominance without flexibility is a fragility signal.                                     | Activated through capital-renewal criteria, anti-lock-in checks, redundancy/flexibility standards, and periodic revision cycles.                      | AIR-005, AIR-008, AIR-015, AIR-040, AIR-041, AIR-042                   | M-004                      | Core                            |
| HC-08      | Energy, utility, mobility, and communication enabling networks                         | Technological (primary); Social (linked)                    | Coping, Adaptive, Transformative | Do not score stock scale without reliability, interoperability, and inclusion performance.                                                            | Requires transition sequencing governance, reliability standards, inter-agency interoperability rules, and emergency deployment protocols.            | AIR-009, AIR-035, AIR-038, AIR-039, AIR-044                            | M-007, M-017, M-018        | Core                            |
| HC-09      | Food-system and productive bio-resource stock                                          | Social + Ecological (primary); Technological (linked)       | Coping, Adaptive                 | Separate local stock presence from access and governance quality across urban-rural linkages.                                                         | Activated by city-region coordination, market/logistics governance, local stewardship, and knowledge-extension functions.                             | AIR-003, AIR-016, AIR-037                                              | M-002                      | Core                            |
| HC-10      | Financial and economic resilience buffer stock system                                  | Social + Technological                                      | Coping, Adaptive                 | Wealth-bias and scale-mixing risk: separate macro/public/household/community layers; avoid direct macro-to-local inference without translation logic. | Requires public-finance instruments plus household/community uptake mechanisms and risk-transfer governance.                                          | AIR-045, AIR-047, AIR-048, AIR-049, AIR-052, AIR-053, AIR-054, AIR-057 | M-019, M-021               | Core (with provisional subtype) |
| HC-11      | Human and social capability stock (skills, literacy, connectedness, collective assets) | Social                                                      | Coping, Adaptive, Transformative | Avoid narrow HR proxying; include trust/reciprocity and collective-governance durability dimensions.                                                  | Activated through competency development systems, community organization, and inclusion-oriented collective governance mechanisms.                    | AIR-046, AIR-050, AIR-051, AIR-055, AIR-056                            | M-020, M-022               | Core                            |

## 3) Provisional / weak-evidence handling inside v1 hardening

- **Provisional subtype flags retained inside canonical groups**:
  - Experimental coastal forms (AIR-024) under HC-03.
  - Macro-financial translation sensitivity (AIR-047) under HC-10.
  - Amenity-to-climate service ambiguity (AIR-006, AIR-019) under HC-06.
- **Category-drift handling**:
  - AIR-011 remains non-canonical for asset-stock rows (governance-process evidence); keep only as activation-reference linkage.

## 4) Coverage and traceability check

- AIR coverage in hardened concept groups: **56/57** rows (AIR-001 to AIR-057 excluding AIR-011 by design).
- Governance-process drift row retained as reference-only: **AIR-011** - ==infrastructure regulations and institutions==.
- Full corpus coverage preserved for decision traceability: **57/57** accounted for.

## 5) Ready-to-use drafting boundary

This note provides the immediate Phase 3 drafting surface (hardened concepts + SETS + roles + guardrails + governance-link logic + lineage).
It intentionally does **not** draft:
- `CRI_Asset_Concept_Summary_v1.md`
- `CRI_Asset_Tagging_Dictionary_v1.md`

