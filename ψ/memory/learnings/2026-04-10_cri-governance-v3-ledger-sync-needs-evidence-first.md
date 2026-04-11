---
type: learning
project:
  - DCCE_CRI
date: 2026-04-10
concepts:
  - project-management
  - ledger-discipline
  - governance
  - evidence
  - markdown-tables
---

# CRI governance-v3 ledger sync needs evidence-first sequencing

When a conceptual state becomes the active contract for a project, the most reliable PM update sequence is **evidence → trigger → deliverable → claim → change**, with plan/navigation updates afterward. This worked cleanly for the CRI v3 governance freeze because the work already had concrete artifacts: [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md), [`ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`](ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md), and [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md). Registering these first made every downstream row more stable and explainable.

A secondary learning is procedural: when editing ledger tables in this repo, the reliable method is not patching rows but replacing the full table block using [`replace-md-table.ts`](.roo/skills/markdown-table-edit/scripts/replace-md-table.ts). The combination of full table reconstruction plus anchor-based replacement reduces context-match failures and makes operation receipts easier to reason about afterward.

Practical rule: if the human asks to “update ledgers,” treat it as a request to synchronize the artifact-centered PM system, not just to write a prose note or plan. First make the new artifacts visible in the evidence spine, then propagate that state through trigger, deliverable, claim, and change surfaces.
