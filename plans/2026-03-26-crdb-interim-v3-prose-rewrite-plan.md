# Plan: CRDB Interim Report v3 — Fix drafting mistake (rewrite into DCCE-facing prose)

## Background
Drafts exist for all TOR subsections (5.2.1–5.2.5, 5.3.1–5.3.2, 5.5.1–5.5.2) but are not DCCE-ready: overly bulleted/partitioned and contain repo-internal references + internal QA notes.

Reference handoff: [`ψ/inbox/handoff/2026-03-26_08-30_crdb-interim-v3-style-mismatch-and-prose-rewrite.md`](ψ/inbox/handoff/2026-03-26_08-30_crdb-interim-v3-style-mismatch-and-prose-rewrite.md)

## Goals (Next Session)
1) Produce a DCCE-facing paragraph-based report draft (v1-like voice) that is coherent and readable.
2) Separate internal traceability from the DCCE-facing text.

## Workplan
1) Define “DCCE-facing draft rules”
   - Paragraph-first narrative; bullets limited to a short executive summary (if needed) and true lists.
   - No repo paths / no markdown links in the audience-facing draft.
   - Evidence referenced as “ภาคผนวก/ตาราง/เอกสารประกอบ” with human-readable labels.

2) Create two deliverables
   - **DCCE-facing main body**: a single draft file (TOR order) with coherent prose.
   - **Internal traceability map**: table mapping major claims/paragraphs → internal artifact file.

3) Rewrite subsections iteratively
   - Start with Section 1 (5.2.1–5.2.5) using v1 narrative style as baseline.
   - Continue Section 2 (5.3.1–5.3.2).
   - Finish Section 3 (5.5.1–5.5.2).

4) QA pass
   - Consistency of terminology (DCCE / NCAIF / CRDB / รายการองค์ความรู้)
   - Remove internal “to verify” blocks from main body; relocate to internal QA log.
   - Ensure TOR compliance headings and minimum counts (List A/B ≥10) remain satisfied.

## Key Inputs
- Anchor plan: [`ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md)
- Style pack: [`ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md)
- v1 report: [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md)

