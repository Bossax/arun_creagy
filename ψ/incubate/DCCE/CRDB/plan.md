# plan — DCCE / CRDB

Operational plan for **CRDB-only** scope in this thread.

Anchors:
- Digest (onboarding): [`ψ/incubate/DCCE/CRDB/inbox_source/dcce-crdb_knowledge_digest.md`](ψ/incubate/DCCE/CRDB/inbox_source/dcce-crdb_knowledge_digest.md)
- Decision log (confirmed): [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)
- MVP/workflow patterns (current): [`ψ/incubate/DCCE/CRDB/output/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)
- Interim report writing plan: [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)
- Interim report outline (working): [`ψ/incubate/DCCE/CRDB/inbox_note/CRDB interim report.md`](ψ/incubate/DCCE/CRDB/inbox_note/CRDB%20interim%20report.md)
- Section 1 synthesis analysis: [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md)
- Task 5.5 scope (NCAIF knowledge sets): [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Task 5.5 Scope.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Task%205.5%20Scope.md)
- Interview ingestion traceability (FTI/UDDC/BMA/DPT): [2026-03-23-CRDB-Interview-Ingestion-Traceability-Note.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-CRDB-Interview-Ingestion-Traceability-Note.md)

## Objectives

1) Lock Phase 1 scope as **conceptual + logical architecture** (not a software build).
2) Publish a coherent **NCAIF (EDM)** narrative: taxonomy + glossary + workflow entry points.
3) Convert workflow patterns into a **Phase 1 MVP shortlist** with explicit “what ships” vs “documentation-only.”
4) Define **governance rails + minimum gates (G1–G5)** required for safe publishing and baseline endorsement.
5) Produce a small set of **immediately usable artifacts** (schemas/templates/checklists) that enable execution.
6) Translate **Task 5.5 knowledge sets** into Phase‑1 NCAIF content blocks (explainers, sector briefs, media) without over‑claiming platform features.

## Decisions

Confirmed decisions — user confirmation **2026-03-10 14:03 ICT (07:03Z)**. See [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](phase1_decision_log.md)

- MVP priority: **MVP-3** + **MVP-2** as Phase 1 core; keep MVP-1/MVP-4 lightweight.
- Sitemap: **Option 3 (Hybrid / workflow-pattern-first)**.
- Architecture: **Catalog-first (link-first)**.
- Rails: **Open → data.go.th; Non-open → GDX; Sensitive → internal-only**.
- Governance gates: **G1–G5** (classification; metadata+preview; endorsement registry; boundary+crosswalk; event schema with timeliness/flags).

Confirmed assumptions (Phase 1, locked)

These were previously tracked as “open confirmations”; they are now **confirmed** and should be treated as Phase 1 design constraints.

1) **MVP core**: Phase 1 core is **MVP-3 Recommended Baseline Registry** + **MVP-2 Disaster data ingestion + Loss & Damage groundwork**; keep **MVP-1/MVP-4** as documentation-lite deliverables.
2) **Sitemap stance**: **Option 3 (Hybrid / workflow-pattern-first)**.
3) **Architecture stance**: **Catalog-first (link-first)**.
4) **Publishing rails**: **Open → data.go.th; Non-open → GDX; Sensitive → internal-only**.
5) **Canonical boundary pattern**: primary reporting uses **administrative boundaries**; budget/operations use **LAO/municipality**; small-area baselines use **EA where available**; publish and govern **crosswalks** explicitly.
6) **Endorsement authority pattern**: **interim endorsement panel** (DCCE central data team + source-agency focal point, co-signature) for recommended baselines.
7) **MVP-2 scope**: Phase 1 is **groundwork** (manual/batch intake + quarantine/validation flags + revision policy), not a fully automated pipeline.

## Outputs (what we will produce next)

Phase 1 “ship list” (minimal, high-leverage):

- **Baseline Registry schema** (MVP-3): required fields + versioning + endorsement audit trail.
- **Publishing rails checklist** (Open/GDX/Internal) + minimum metadata/preview requirements.
- **Boundary + crosswalk governance note**: canonical boundary per flagship output + ownership + versioning.
- **Disaster intake + quarantine template** (MVP-2 groundwork): event registry + impact observation template + validation flags + revision policy.
- **Briefing pack templates** (MVP-1 lite): 3–5 export-first templates + “must include” checklist.
- **Uncertainty/publishing standard** (MVP-4 lite): minimum statements + misuse example + tiered guidance.
- **Interim Report Writing Plan** (TOR mapping + evidence map + schedule).
- **Interim Report Outline (working)** aligned to TOR 7.2.
- **Section 1 synthesis analysis** (methodology + CDM/MVP positioning + evidence logic).
- **Task 5.5 Scope note** (knowledge sets → NCAIF content layer).
- **Phase‑1 content gap update** (Pack A integration: risk‑map product + explainers + caveats).

## Latest artifacts (FGD2)

- Project status (current): [`ψ/incubate/DCCE/CRDB/CRDB - Project Status (Current).md`](CRDB%20-%20Project%20Status%20(Current).md)
- FGD2 action summary: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_action_summary.md`](2026-03-11_FGD2_action_summary.md)
- FGD2 transcript (cleaned): [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_transcript_clean.md`](2026-03-11_FGD2_transcript_clean.md)
- 2026-03-23 interview-ingestion update:
  - [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
  - [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
  - [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)


## Next steps

### FGD2-derived action plan (dated)

Grounding: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_action_summary.md:99)

| Due (ICT) | Action | Output artifact (planned) |
|---|---|---|
| **2026-03-12** | Update current CRDB project status (supersede outdated brief) | [`ψ/incubate/DCCE/CRDB/CRDB - Project Status (Current).md`](ψ/incubate/DCCE/CRDB/CRDB%20-%20Project%20Status%20(Current).md:1) |
| **2026-03-14** | MVP‑3: Baseline Registry schema (include endorsement + intended use + recency/version + rail) | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/Baseline_Registry_Schema.md` |
| **2026-03-14** | Publishing rails checklist (Open/data.go.th via SECAN; G2G via GDX; internal-only) | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/Publishing_Rails_Checklist.md` |
| **2026-03-14** | 1‑page narrative: “Backend enables sitemap” (expectation management) | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/Backend_enables_sitemap_one_pager.md` |
| **2026-03-18** | MVP‑2 groundwork: disaster intake + quarantine + validation flags + revision history | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/MVP2_Disaster_Intake_and_Quarantine_Template.md` |
| **2026-03-18** | Sitemap vNext: drill-down sitemap (2–3 levels) + sitemap change process (Pack A risk‑map integration + caveats) | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/Sitemap_vNext_drilldown_and_change_process.md` |
| **2026-03-12** | Interim Report Writing Plan + outline + Section 1 synthesis anchor | [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md) + [`ψ/incubate/DCCE/CRDB/inbox_note/CRDB interim report.md`](ψ/incubate/DCCE/CRDB/inbox_note/CRDB%20interim%20report.md) + [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md) |
| **2026-03-12** | Task 5.5 scope note (knowledge sets → NCAIF content layer) | [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Task 5.5 Scope.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Task%205.5%20Scope.md) |
| **2026-03-20** | Late‑April workshop concept (providers + processors + users; reuse/publishing legality) | (new) `ψ/incubate/DCCE/CRDB/Artifact v1/Late_April_Workshop_Concept.md` |
| **2026-03-23 10:00** | Send requested report (per meeting minutes) | (packaging task; see minutes) |

Notes:
- The “website = platform” expectation and sitemap-first focus are tracked as an info log: [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md:1)
- Participants asked for more sitemap detail and confirmed changeability needs: [`ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md`](ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md:1)
- Pack A evidence locked (risk‑map product + limitations): [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)

### Baseline “always on” next steps (no dates)

1) Draft boundary/crosswalk governance note (one page) + identify owner(s).
2) Add “governance gates” checklist that each published artifact must pass.
