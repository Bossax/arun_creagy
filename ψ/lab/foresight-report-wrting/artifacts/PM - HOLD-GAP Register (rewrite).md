# PM - HOLD-GAP Register (rewrite)

Purpose
- Internal register to prevent unsourced specifics from leaking into chapter prose.
- Each HOLD/GAP item must be referenced by chapter writers and either closed with evidence or explicitly caveated.

How to use
- Chapter writers may append new items only (append-only).
- If an item is closed, mark it Closed and link to the source location.

---

## Register

Legend
- Type: HOLD (needs a traceable source before making a specific claim) | GAP (missing information and requires collection)
- Severity: High (high-stakes, likely to be challenged) | Medium | Low

| ID | Type | Severity | What is missing / at risk | Where it affects the base structure | Closure plan (minimum) | Owner | Status |
|---|---|---|---|---|---|---|---|
| HG-001 | GAP | High | Clear scope definition of target groups and vulnerable segments used in the report (beyond generic terms) | Ch.1 ขอบเขตกลุ่มเป้าหมายและผู้มีส่วนได้ส่วนเสีย | Confirm definitions and segmentation used by the project; document in a short scope note and reuse consistently | TBD | Open |
| HG-002 | HOLD | High | Any quantitative baseline on orphans, OOSC, learning outcomes, welfare coverage in 3 จชต. | Ch.1–Ch.2 (context + lived reality) | Add official stats/research citations; map each number to a source and date | TBD | Open |
| HG-003 | HOLD | High | Legal feasibility statements about education decentralization, sandbox, and who can provide education | Ch.4 (strategy feasibility) | Cite relevant laws and interpret carefully; link to repo copies and authoritative sources | TBD | Open |
| HG-004 | GAP | Medium | Clear list of data sources used for horizon scanning and selection criteria | Ch.2 2.1 การกวาดสัญญาณ | Produce an internal source ledger and include a high-level summary in prose | TBD | Open |
| HG-005 | GAP | Medium | Scenario axes justification traced from impact × uncertainty and system tensions | Ch.3 แกนตรรกะฉากทัศน์ | Create a short logic sheet: drivers → tensions → axes → descriptors | TBD | Open |
| HG-006 | GAP | Medium | Scenario descriptor matrix agreed and frozen | Ch.3 ตัวบ่งชี้ฉากทัศน์ + Ch.4 robustness | Define descriptor columns once; reuse across all scenarios and stress-tests | TBD | Open |
| HG-007 | GAP | Medium | Actor landscape in 3 จชต. for education, welfare, livelihoods, youth support, and governance | Ch.4 actor mapping | Produce an actor map note with roles: owner, broker, enabler | TBD | Open |
| HG-008 | HOLD | Medium | Specific historical events referenced as analogies (e.g., particular flood events, dates) | Ch.2 เหตุไม่คาดฝัน | Source any named event; otherwise keep it as an illustrative hypothetical | TBD | Open |
| HG-009 | GAP | Low | Editorial rules for handling the two empty heading slots in Chapter 1 without drifting structure | Ch.1 two empty ## slots | Decide what content belongs there based on existing evidence; keep headings blank if required | TBD | Open |

---

## Closure log (append-only)

| ID | Closed date | Evidence link(s) | Notes |
|---|---|---|---|

Notes (append-only)
- 2026-03-31: Chapter 1 drafting uses the two Empty heading slots in [`ψ/lab/foresight-report-wrting/artifacts/base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md) as containers for (1) reader-primer definitions and (2) how-to-read + evidence hygiene, without introducing new titled headings. This preserves the required structure positionally but leaves an editorial dependency on HG-009 for final layout decisions.

- 2026-03-31: Chapter 2 rewrite v1 treats field/interview notes as non-citable in sponsor-facing prose (qualitative synthesis only). This maintains evidence hygiene but leaves an explicit dependency on a traceable source ledger for scanning outputs (HG-004) and on baseline numeric claims (HG-002) before the chapter can safely include any statistics.

- 2026-03-31: Chapter 3 rewrite v1 fixes one scenario set for Chapter 3–4 continuity: axes are (1) education governance and the real-world connectivity of learning pathways, and (2) household economic pathways (traditional low-value/volatile vs higher-value pathways linked to halal, creative, and digital economies). The scenario titles are stabilized as: (1) กรอบเดียว โอกาสติดหล่ม, (2) โตแต่ไหลออก, (3) ยืนบนราก รายได้บาง, (4) นูซันตาราบนฐานราก. A fixed descriptor set is defined in-prose to support comparison and later robustness testing, but remains an explicit dependency until fully agreed and frozen under HG-006. Legal feasibility claims and numeric baselines remain held under HG-002 and HG-003, and the axes justification remains tracked under HG-005.

- 2026-03-31: Chapter 4 rewrite v1 operationalizes the Chapter 3 scenario set into strategy pathways, leverage points, portfolio logic, and actor-role framing. It keeps legal feasibility and institutional mandate claims cautious (HG-003), uses actor categories rather than a complete named actor list (HG-007), and relies on the frozen descriptor set for robustness comparisons (HG-006). The chapter avoids budget-effectiveness assertions and any numeric baselines pending HG-002.

- 2026-03-31: Chapter 5 rewrite v1 synthesizes Chapters 1–4 into policy-relevant implications without introducing quantified baselines or legal-feasibility assertions. It frames implications as sequencing and conditions for access and robustness, and keeps any claims that would require numbers or legal interpretation within existing constraints tracked under HG-002 and HG-003.

