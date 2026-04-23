# Governance-Template Audit for Asset-Side Phase 3/4 Outputs

## Purpose
Compact transfer note from governance-side templates to asset-side drafting templates for:
- `CRI_Asset_Concept_Summary_v1.md` (Phase 3)
- `CRI_Asset_Tagging_Dictionary_v1.md` (Phase 4)

## Source templates audited
- `CRI_Capacity_Concept_Summary_v3.md`
- `CRI_Capacity_Tagging_Dictionary_v3.md`

## 1) Reusable section structure (carry over)
1. **Frontmatter + explicit scope/version metadata**
   - Keep artifact type, status/version, project tags, and title discipline.
2. **Methodological conclusion / framing choice section**
   - Governance template uses “Institutional Readiness”; asset version should mirror this with an “Asset-Stock Enabling Conditions” lens.
3. **Frozen/canonical structure section**
   - Keep a clearly frozen taxonomy block before worksheet tables.
4. **Worksheet section for screening and coding indicators**
   - Keep pillar/domain subsections with uniform table schema for decision scanning.
5. **Concept definitions section**
   - Keep concise definitions per concept to standardize interpretation.
6. **Next-steps section**
   - Keep explicit implementation trigger: lock dictionary after candidate codes are filled.

## 2) Reusable table logic (carry over)
The governance worksheet table logic is directly reusable:

`indicator_concept | capacity_category | proposed_thai_anchor | evidence | candidate_indicator_code | selection_decision`

Transfer rules:
- Keep `candidate_indicator_code` and `selection_decision` as the operational gate.
- Keep `evidence` as mandatory provenance field.
- Keep per-domain subsection layout (domain/pillar headings + same column order).

For Phase 3 concept summary, keep compact concept table logic:

`indicator_concept | capacity_category | [domain/pillar] | description (summarised) | candidate_indicator (high-level)`

## 3) Fields/columns to carry into asset-side versions
### Phase 3 (`CRI_Asset_Concept_Summary_v1.md`)
- `indicator_concept`
- `capacity_category`
- `description (summarised)`
- `candidate_indicator (high-level)`
- Replace governance grouping column with `sets_domain` (Social/Ecological/Technological).

### Phase 4 (`CRI_Asset_Tagging_Dictionary_v1.md`)
- `indicator_concept`
- `capacity_category`
- `proposed_thai_anchor`
- `evidence`
- `candidate_indicator_code`
- `selection_decision`

## 4) Sections/fields requiring adaptation for stock-focused asset indicators
1. **Grouping axis adaptation**
   - Replace `governance_pillar` with `sets_domain` (and optional `asset_stock_type` where needed).
2. **Interpretation adaptation**
   - Every concept definition should state asset as **enabling stock**, not outcome.
3. **Activation dependency adaptation**
   - Add a required field in Phase 4 worksheet: `governance_activation_link` (which governance function activates this stock).
4. **Safe-interpretation adaptation**
   - Add `normalization_or_equity_note` (hazard exposure, accessibility/distribution caveat).
5. **Nonlinearity adaptation**
   - Add `threshold_lockin_flag` (none / potential / high concern).
6. **Placeholder discipline adaptation**
   - Retain explicit “design placeholder” tagging where evidence is partial, avoiding premature metric hard-locking.

## 5) Recommended target structure for asset outputs
### A. Target structure for Phase 3: `CRI_Asset_Concept_Summary_v1.md`
1. Frontmatter (type/status/version/project/title)
2. Methodological framing (asset stocks as enabling conditions; complement to governance process indicators)
3. Canonical SETS structure (Social / Ecological / Technological)
4. Concept summary table (compact; one row per concept)
5. Short concept definitions by SETS domain
6. Scope/limitations note (stock ≠ realized resilience)

### B. Target structure for Phase 4: `CRI_Asset_Tagging_Dictionary_v1.md`
1. Frontmatter (knowledge artifact, frozen structure status)
2. Methodological conclusion for asset-side worksheet
3. Frozen taxonomy (SETS domains + agreed stock categories)
4. Worksheet tables by SETS domain using core governance-v3 table logic, plus adapted fields:
   - `governance_activation_link`
   - `normalization_or_equity_note`
   - `threshold_lockin_flag`
5. Concept definitions (v1)
6. Next steps (decision-ready scanning and code lock)

## Practical drafting guardrail
Preserve governance-template rigor (frozen structure, evidence traceability, decision columns), but shift semantics from **function-readiness** to **stock enabling conditions + activation dependency**.

