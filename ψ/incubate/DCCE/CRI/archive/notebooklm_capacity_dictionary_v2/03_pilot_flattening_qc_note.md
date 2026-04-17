---
type: knowledge_artifact
status: pilot_qc_completed
created: 2026-04-08
project:
  - DCCE_CRI
title: Pilot flattening and QC note — NotebookLM capacity dictionary v2
---

# Pilot flattening and QC note — NotebookLM capacity dictionary v2

This note records the local flattening of the raw NotebookLM pilot responses and the first QC review against the pilot gates in [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md).

## Scope and flattening method

- Raw inputs reviewed:
  - [`responses/2026-04-08_pilot_pass1_local_raw_rows.json`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass1_local_raw_rows.json)
  - [`responses/2026-04-08_pilot_pass2_methodological_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass2_methodological_notebooklm_raw.md)
  - [`responses/2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass3_frameworks_notebooklm_raw.md)
- Local flattening action:
  1. kept the leading JSON arrays as the row-level evidence payloads;
  2. treated the trailing NotebookLM extraction-note and reference-list text as run-level metadata, not row records;
  3. assigned local row IDs `P2-01` to `P2-12` and `P3-01` to `P3-12` for harmonisation and QC;
  4. used `P1-01` to `P1-13` as shorthand for the existing Pass 1 JSON row order.

## Run-level caveats carried forward into local synthesis

- Both NotebookLM pilot files were already close to the preferred flat schema, so flattening was light-touch rather than a major rewrite.
- Both runs appended markdown text after the JSON array; that wrapper text was preserved in the raw files but excluded from the row inventory below.
- Pass 2 explicitly states that the three requested methodological pilot sources were not present in the uploaded notebook literature and that substitute thematic sources were used instead.
- Pass 3 explicitly states that the requested framework source names were not literal matches to the uploaded notebook literature and that substitute thematic sources were used instead.
- These source-availability notes do not invalidate the saved raw rows, but they do limit the pilot as a scale-up signal because the evidence does not come from the exact intended pilot source packet.

## Flattened Pass 2 row inventory

| row_id | row_kind | source_id_reference | candidate_indicator_or_category | candidate_aspect | candidate_dimension_if_explicit | citation | flattening note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P2-01 | capacity_category_statement | Rogers et al., 2023 | Authority to adapt | not explicit | not explicit | (Rogers et al., 2023, Abstract) | High-level mandate / authorizing-environment framing. |
| P2-02 | capacity_category_statement | Rogers et al., 2023 | Capacity to adapt | access to resources, professional networks, and supportive organizational systems and culture | not explicit | (Rogers et al., 2023, Abstract) | Broad enabling-capacity statement rather than indicator-ready row. |
| P2-03 | aspect_statement | Zeng et al., 2022 | Adaptive capacity | education, health, food, and water | not explicit | (Zeng et al., 2022, Abstract) | Source gives aspect bundle under adaptive capacity. |
| P2-04 | aspect_statement | Zeng et al., 2022 | Absorptive capacity | community support, urban green space, protective infrastructure, access to transport | not explicit | (Zeng et al., 2022, Abstract) | Mixed social and infrastructure aspect bundle. |
| P2-05 | aspect_statement | Zeng et al., 2022 | Transformative capacity | communication technology, collaboration of multi-stakeholders, emergency services of government, community-oriented urban planning | not explicit | (Zeng et al., 2022, Abstract) | Transformative-capacity bundle that crosses technology, service, participation, and planning. |
| P2-06 | capacity_category_statement | Strategy&, n.d. | Capacity to Respond | Anticipate the emergence of a threat/disaster and be prepared | not explicit | (Strategy&, n.d., Exhibit 2) | Competing triad framing; preserve as-is. |
| P2-07 | capacity_category_statement | Strategy&, n.d. | Capacity to Recover | Adjust to a shock in a timely and efficient manner | not explicit | (Strategy&, n.d., Exhibit 2) | Competing triad framing; preserve as-is. |
| P2-08 | capacity_category_statement | Strategy&, n.d. | Capacity to Transform | Innovate continuously and mobilize new systems/tools/structures | not explicit | (Strategy&, n.d., Exhibit 2) | Competing triad framing; overlaps with transformative-capacity language elsewhere. |
| P2-09 | aspect_statement | Tariq et al., 2021 | Human/Health | skills, knowledge, labor and health outcomes | not explicit | (Tariq et al., 2021, Table 6) | Broad human-capital / health aspect statement. |
| P2-10 | aspect_statement | Tariq et al., 2021 | Economic | static assessment of a community's current economy | not explicit | (Tariq et al., 2021, Table 6) | Economic category appears as a standalone resilience dimension. |
| P2-11 | aspect_statement | Valdivieso et al., 2021 | Human resources | staff, work time, managerial, and staff competences | not explicit | (Valdivieso et al., 2021, Section 3.1) | Municipal human-resource capacity statement. |
| P2-12 | indicator_concept_candidate | Valdivieso et al., 2021 | Financial capacities | not explicit | not explicit | (Valdivieso et al., 2021, Section 3.1) | Foundational finance-capacity row; label remains source-near. |

## Flattened Pass 3 row inventory

| row_id | row_kind | source_id_reference | candidate_indicator_or_category | candidate_aspect | candidate_dimension_if_explicit | citation | flattening note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P3-01 | indicator_concept_candidate | OECD, 2018 | Land-use plans that have been developed with reference to local hazard risk assessment | City leadership that has sufficient capacity and flexibility to effectively manage emergencies. | process | (OECD, 2018, Annex 2) | Keep row but treat the aspect field cautiously because it reads like an adjacent framework label rather than a clean restatement of the quoted indicator. |
| P3-02 | indicator_concept_candidate | OECD, 2018 | Proportion of urban solid waste regularly collected | Health and contamination risks. Environmental quality. | output | (OECD, 2018, Annex 2) | Clean framework-specific output candidate. |
| P3-03 | capacity_category_statement | Goonesekera & Olazabal, 2022 | Targets, inputs, outputs, outcomes, and impacts | not explicit | output | (Goonesekera & Olazabal, 2022, Section 2.2) | Use as measurement-architecture evidence only; the row is broader than the `output` tag alone suggests. |
| P3-04 | capacity_category_statement | Brito et al., 2026 | Organizational, spatial, functional, and physical dimensions | governance, social aspects, finance, exposure, impacts, mapping, service management, interdependencies, infrastructure robustness, redundancy | not explicit | (Brito et al., 2026, Abstract) | Framework-level dimensional architecture. |
| P3-05 | aspect_statement | Brito et al., 2026 | Functional dimension | governance of strategic services, planning and risk management, flexibility, autonomy and interdependencies, preparedness to respond | not explicit | (Brito et al., 2026, Section 1.3) | Rich aspect bundle connecting planning, services, and interdependencies. |
| P3-06 | capacity_category_statement | Tariq et al., 2021 | Physical | facilities or structures that form a network | not explicit | (Tariq et al., 2021, Table 6) | Networked infrastructure / systems framing. |
| P3-07 | aspect_statement | Tariq et al., 2021 | Human/Health | skills, knowledge, labor and health outcomes | not explicit | (Tariq et al., 2021, Table 6) | Duplicate of the same Tariq framing already present in Pass 2; useful for cross-pass duplication check. |
| P3-08 | capacity_category_statement | Strategy&, n.d. | CAPACITY TO RESPOND | Anticipate the emergence of a threat/disaster | not explicit | (Strategy&, n.d., Exhibit 2) | Near-duplicate of Pass 2 triad row. |
| P3-09 | capacity_category_statement | Strategy&, n.d. | CAPACITY TO TRANSFORM | Innovate continuously and mobilize new systems/tools/structures | not explicit | (Strategy&, n.d., Exhibit 2) | Near-duplicate of Pass 2 triad row. |
| P3-10 | capacity_category_statement | Econsult Solutions, 2024 | environmental, economic, infrastructural, and social | not explicit | not explicit | (Econsult Solutions, 2024, p. 4) | Top-level analytical bins rather than indicator-ready row. |
| P3-11 | aspect_statement | Kearney, 2025 | INSTITUTIONAL GOVERNANCE | comprehensive institutional frameworks that embed resilience as a core governmental function | not explicit | (Kearney, 2025, Framework for Measuring Cities' Resilience Readiness) | Institutional-governance readiness framing. |
| P3-12 | aspect_statement | Kearney, 2025 | SUSTAINABLE FINANCE AND BUSINESS | business environments, financial mechanisms, and public-private partnerships | not explicit | (Kearney, 2025, Framework for Measuring Cities' Resilience Readiness) | Strong finance/business aspect row. |

## Pilot QC against the plan gates

| QC gate from [`00_query_plan.md`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/00_query_plan.md) | Outcome | Local assessment |
| --- | --- | --- |
| Citation coverage | Pass with caveat | Every Pass 2 and Pass 3 row has a usable citation. Most citations are abstract / annex / exhibit / table / section level rather than page-precise, but they remain usable for local review. |
| Row structure consistency | Pass | Both NotebookLM outputs returned a flat JSON array with the expected fields. The extra markdown note and reference list occurred after the array and were easy to separate locally. |
| Low drift into synthesis | Pass with caution | The responses did not de-duplicate, harmonise into a canonical taxonomy, or rewrite the local register. However, a few fields show mild noise or over-assignment, especially `P3-01` and `P3-03`, so source-near review remains necessary. |
| Manageable local harmonisation effort | Pass | Cleanup burden was low. Local work mainly involved assigning row IDs, ignoring the post-array wrapper text, and clustering obvious overlaps. |
| Boundary compliance | Pass | The workflow remained local for harmonisation/QC, and the raw responses were saved verbatim. No repo-local file was treated as notebook-accessible. |

## Additional scale-up hold point

Formal pilot QC gates were mostly satisfied in shape, but scale-up should still be held for one reason:

- **source-packet fidelity is not yet secure.** Both NotebookLM runs report that the requested pilot source names were missing or not literal matches, and they substituted other uploaded literature. That means the pilot validated the extraction format more than it validated the exact planned source packet.

## Recommendation

Do **not** proceed to full-scale extraction yet.

Before scaling, tighten one of the following:

1. align the pilot prompts with the exact uploaded NotebookLM source titles actually present in the notebook; or
2. adjust the instructions so NotebookLM must fail fast when the requested sources are unavailable, rather than silently substituting nearby literature.

After that adjustment, rerun the pilot passes or at minimum rerun the affected pass before using the pilot as a scale-up green light.
