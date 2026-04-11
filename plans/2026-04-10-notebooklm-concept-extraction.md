# Plan: NotebookLM Concept Extraction for CRI v3 Dictionary

## Background
In the previous session, we locked the structure of the `CRI_Capacity_Tagging_Dictionary_v3.md` using the "Institutional Readiness" lens and mapped the indicator concepts to 6 functional governance pillars. 

While some concepts (e.g., 'Plan revision cycle', 'Risk-informed planning', 'Policy Integration', 'Post-event review completion rate', 'Multi-stakeholder collaboration', 'Emergency budget flow', and 'Climate budget tagging') have already been defined via NotebookLM and documented in `ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`, the remaining concepts require literature-backed definitions to ensure clarity during the data vetting phase.

## Pending from Last Session
- Detailed concept descriptions: Need to "harden" what the remaining concepts mean by extracting definitions from the literature pool via NotebookLM.
- Indicator Vetting: The worksheet is ready but empty; need to map actual dataset codes (LPA, etc.) to the concepts.

## Next Session Goals

### 1. Execute NotebookLM Queries for Missing Concepts
We will use NotebookLM (adhering to `notebooklm-rules` for source-fidelity) to extract definitions for the remaining concepts. The queries will be grouped by their source literature to minimize context switching and ensure fidelity.

**Query Pack A: Strategy& and Serdar et al. 2021**
- Concepts: `Resource allocation scale`, `Service delivery timeliness`, `Case throughput rate`, `Staff Training frequency`
- Sources: Strategy& (Institutional Readiness), Serdar et al. 2021

**Query Pack B: Consensus.ai, Zeng et al. 2022, and Sharifi 2023**
- Concepts: `Asset Mobilization Velocity`, `Distributed Command Agility`, `Transboundary Feedbacks`, `Digital Social Mediation`, `Infrastructure robustness`, `Digital climate services`
- Sources: Consensus.ai validation, Zeng et al. 2022, Sharifi 2023, Riaz et al. 2023

**Query Pack C: Urban.org, MDPI, Feldmeyer, Moench**
- Concepts: `Formal coordination bodies`, `Data interoperability`, `Risk Assessment depth`, `Emergency staff capacity`
- Sources: Institutionalizing Urban Resilience (Urban.org), Prioritizing Core Data Sets (MDPI), Feldmeyer et al. 2019, Tyler & Moench 2012

### 2. Update the Concept Check Document
Append the extracted definitions, their conceptual significance, and how they are typically measured to `ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`.

### 3. Harden the v3 Dictionary
Summarize the extracted definitions into concise, actionable descriptions and update `CRI_Capacity_Tagging_Dictionary_v3.md` (or a linked definitions reference) to guide the vetting process.

### 4. Begin Indicator Vetting
With hardened definitions, begin mapping specific Thai administrative traces and LPA dataset codes to the concepts in the v3 worksheet.

## Reference
- Handoff: `ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md`
- Concept Check Doc: `ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`
- Dictionary: `ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md`