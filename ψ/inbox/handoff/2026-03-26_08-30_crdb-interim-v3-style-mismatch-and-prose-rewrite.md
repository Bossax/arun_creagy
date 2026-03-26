# Handoff: CRDB Interim Report v3 — Drafts created but style is wrong (needs prose rewrite)

**Date**: 2026-03-26 08:30 (Asia/Bangkok)
**Context**: We produced TOR-ordered subsection drafts quickly, but the output format is not appropriate for DCCE (bulleted/partitioned, includes repo-internal references and internal “missing data” notes inside the main text). Next session must convert this into coherent paragraph-based report prose (like v1) and separate internal traceability from the audience-facing draft.

## What We Did
- Confirmed workflow: one file per TOR subtopic draft under [`ψ/incubate/DCCE/CRDB/output`](ψ/incubate/DCCE/CRDB/output)
- Created a shared Thai style pack (intended as drafting reference): [`ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md)
- Appended Thai outline to the anchor plan: [`ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md)
- Drafted 9 TOR subsection drafts (Thai, ≤5 pages each) but the style is not DCCE-ready:
  - [`ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.2.2-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.2-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.2.3-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.3-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.2.4-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.4-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.2.5-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.5-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.3.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.3.1-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.3.2-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.3.2-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.5.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.5.1-Interim-Report-v3-draft.md)
  - [`ψ/incubate/DCCE/CRDB/output/5.5.2-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.5.2-Interim-Report-v3-draft.md)

## What Went Wrong (Root Cause)
- Output was optimized for **internal traceability** (repo links, segmented sections, “to verify” blocks) rather than **audience-facing report prose**.
- Too much **bulleting and partitioning**; DCCE expects coherent paragraphs similar to v1.
- Repo-internal markdown links are meaningless to DCCE recipients (they don’t have this repo context).
- Internal uncertainty tracking (“ข้อมูลที่ต้องยืนยัน/ยังขาด”) was embedded in the main body instead of being separated into an internal QA log.

## Pending
- [ ] Create a DCCE-facing **main-body draft** with paragraph-based prose (v1-like), with minimal bullets (only where appropriate).
- [ ] Remove repo-internal “evidence links” from the audience-facing text.
- [ ] Split deliverables into two layers:
  - **Public/DCCE draft**: readable narrative, no repo links, no internal notes.
  - **Internal traceability appendix**: mapping each paragraph/claim to the source artifact (repo links OK).
- [ ] Decide citation strategy for DCCE-facing version (e.g., “ภาคผนวก: รายการหลักฐาน” with human-readable labels instead of file paths).
- [ ] Mechanical integration file requested earlier was not completed (combined main body file not yet created).

## Next Session (Concrete Steps)
1) Establish the target output format by using v1 as the reference style (paragraph-first; bullets only for brief executive summary or lists).
2) Create a new file (DCCE-facing) and rewrite subsection-by-subsection:
   - Keep TOR order and headings.
   - Convert each subsection’s executive bullets into 1–2 coherent intro paragraphs.
   - Convert “หลักฐานอ้างอิง” sections into narrative with “อ้างอิง: ภาคผนวก/ตาราง/เอกสารประกอบ” using human labels.
   - Move “ข้อมูลที่ต้องยืนยัน/ยังขาด” into a separate internal QA log file.
3) Create an internal “traceability map” table (claim → source artifact) for review only.
4) After prose rewrite, do a single consistency pass (terminology, tense, tone, duplication across TOR clauses).

## Key Files
- Anchor plan (source of truth for scope + TOR): [`ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md)
- Style pack (should be updated to emphasize paragraph prose, and “no repo links in DCCE-facing drafts”): [`ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md)
- v1 reference narrative:
  - [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md)
  - [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-appendix.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-appendix.md)
- Evidence plan (internal): [`ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Evidence-Gathering-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Evidence-Gathering-Plan.md)

## Repo State Notes
- `git status` shows many modified + untracked artifacts (draft files + evidence tables/notes). Next session should commit in a clean, logical chunk after confirming rewrite approach.

