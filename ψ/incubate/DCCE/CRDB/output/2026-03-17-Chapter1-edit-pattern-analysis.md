# Chapter 1 edit-pattern analysis for CRDB interim report

Source comparison:
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.1-1.5-Draft-th.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.1-1.5-Draft-th.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.1-1.5-Draft-th edited.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.1-1.5-Draft-th%20edited.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md)
- [`ψ/incubate/DCCE/CRDB/inbox_note/2026-03-17-Interim-report-writing-pkan-next-step.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-03-17-Interim-report-writing-plan-next-step.md)

## Purpose

This note captures the substantive edits Boss made to the Chapter 1 draft, identifies recurring editorial patterns, flags unclear or risky changes, and translates them into reusable writing rules for the next CRDB drafting passes.

## Section-by-section change map

### Sections 1.1-1.5

| Section | Main edit observed | What changed in practice | Likely intent |
|---|---|---|---|
| 1.1 | Replace generic project wording with formal project naming | Changed from a generic reference to the project into the full Thai project title; reframed some sentences from "what the client expects" to "what the scope requires" | Make the report sound more official, document-based, and less interpretive about stakeholder intention |
| 1.1 | Tighten institutional tone | Replaced casual or expansive wording such as "เชิงผิวหน้า" with more formal phrasing such as "เชิงการนำเสนอ"; added `กรมฯ` in places | Align the prose with government-report voice |
| 1.2 | Expand acronyms and internal references | Replaced `FGD1` with `การประชุมกลุ่มย่อยครั้งที่ 1`; expanded NCAIF into its full Thai title with English in parentheses | Reduce shorthand and make the document readable as a stand-alone report |
| 1.2 | Shift from analyst framing to user-common-needs framing | Changed `ความต้องการซ้ำที่ตรวจพบจากผู้ใช้` to `ความต้องการของผู้ใช้ที่มีร่วมกัน` | Make the prose sound less technical and more natural in Thai |
| 1.3 | Make CDM terminology explicit | Added `Conceptual Data Model` in the heading and `logical data modeling` in the body; changed `โครงสร้างการจัดการข้อมูล` to `โครงสร้างการบริหารจัดการข้อมูล` | Preserve technical precision while keeping the Thai narrative formal |
| 1.3 | Emphasize delivery-to-next-phase logic | Added explicit wording that the current outputs should be usable for future system development | Make the deliverable pathway clearer and more practical |
| 1.4 | Prefer full institutional names over acronyms alone | Replaced short references such as IPCC/WMO with full English names followed by acronym or contextual explanation | Increase report formality and precision |
| 1.4 | Add technical qualifiers and translations | Added terms such as `impact chain analysis`, `subjective`, and `ข้อมูลอภิพันธุ์ (metadata)` | Make the analytical basis more explicit for technical readers |
| 1.5 | Simplify section label and smooth narrative flow | Changed the heading from a long report-specific title to a shorter title; removed explicit statement formatting around some conclusions | Prefer cleaner narrative over overly scaffolded drafting language |
| 1.1-1.5 | Remove the end-of-section source dump | The edited version removes the long reference block at the end of the file | Suggests preference for cleaner chapter prose, with references handled elsewhere or later |

### Sections 1.6-1.12

| Section | Main edit observed | What changed in practice | Likely intent |
|---|---|---|---|
| 1.6 | Reduce citation-heavy prose | Removed inline author-year references from the end of key paragraphs | Keep the report body readable and less academic in texture |
| 1.6 | Use more natural Thai for information architecture issues | Replaced `จุดเข้าสำหรับผู้กำหนดนโยบาย` with `จุดเริ่มต้นการใช้งาน`; removed `area profiles` in English | Prefer plain Thai over imported UX terminology where possible |
| 1.7 | Make the product description more concrete | Reframed the risk-map product around three concrete components and added detail on province-level display, color-based comparison, and 25 x 25 km climate model input | Prefer visible, tangible product explanation over abstract architectural description |
| 1.7 | Keep the analysis anchored to what users can see | Removed the bridging sentence that deferred architectural interpretation to a later section | Keep each subsection self-contained and focused on its own object |
| 1.8 | Minimal editing | Mostly preserved the original argument and structure | Indicates this section already matches the preferred voice reasonably well |
| 1.9 | Reframe CDM as a data-ordering principle | Changed the title and several sentences from architectural abstraction toward `หลักการจัดระเบียบข้อมูล` and explicit metadata linkage | Prefer practical explanation of CDM over abstract systems language |
| 1.10 | Translate MVP framing into user-visible outputs | Replaced abstract MVP categories with concrete outputs such as risk summaries, disaster summaries, certified datasets, and uncertainty standards | Prefer deliverables described from the user or policy side rather than from product jargon |
| 1.10 | Add department-facing operational realism | Rewrote the disaster-data paragraph to frame it as routine intake from DDPM into DCCE scope rather than an abstract groundwork concept | Make the report read as institutionally grounded and implementation-aware |
| 1.11 | Bring FGD discussion closer to managerial concerns | Reworded the section so sitemap, access levels, and public-facing structure are more visible | Emphasize what management can recognize and approve |
| 1.11 | Reduce emphasis on theoretical deliverable language | Removed some explicit phrasing around `business requirements` and `logical structure` | Suggests preference for direct Thai explanation over consulting jargon |
| 1.6-1.12 | Replace the references section with a direct drafting agenda | The edited file ends with `หัวข้อที่ต้องใส่เพิ่ม` covering CDM detail, interview use-case table, sitemap detail, and early data governance | The edit is not only stylistic; it sets concrete expansion requirements for the next revision |

## Recurring editing patterns

### 1. Prefer official and document-ready naming

Boss consistently replaces generic references with formal project names, formal organizational references, and fully expanded program labels. This suggests the report should read as a standalone government-facing document, not as an internal drafting memo.

### 2. Prefer plain, formal Thai over mixed shorthand

Shorthand such as `FGD1`, overly English-heavy terms, and internal drafting jargon are frequently replaced with more explicit Thai phrasing. English can remain when it is a necessary technical label, but it should usually be paired with a Thai explanation or used sparingly in parentheses.

### 3. Prefer visible products over abstract architecture alone

Where the original draft emphasized architecture, logic layers, or generalized analytical framing, the edit often moves toward concrete outputs that a reader can picture: website structure, sitemap, risk map, certified datasets, summaries, access levels, and operational routines.

### 4. Prefer smoother narrative flow over drafting scaffolds

The edits remove heavy reference blocks, reduce explicit meta-commentary about what a section will do next, and simplify long headings. This suggests the report should read as a continuous narrative rather than as a research memo with attached scaffolding.

### 5. Prefer practical institutional relevance

Boss strengthens links to what DCCE, executives, or future implementation teams can actually use. The writing should therefore keep asking: what does this paragraph mean for departmental use, approval, implementation, or data management?

### 6. Prefer readable report prose over citation density

Inline source-heavy phrasing was reduced in the edited text. The likely pattern is to keep evidence in the argument, but avoid making the interim report body read like an academic literature review.

## Provisional long-term writing rules

1. Use the formal Thai project name early when introducing the work, then use a shorter but still formal label afterward.
2. Write as if each chapter may be read independently by managers or external reviewers with limited memory of prior discussions.
3. Minimize shorthand such as `FGD1`, `FGD2`, and internal drafting labels unless they are first expanded.
4. Prefer Thai phrasing for core narrative sentences; keep English terms only when they add technical precision and are hard to replace cleanly.
5. When discussing architecture or data models, explain them through their practical function for the department and the user.
6. Describe proposed outputs in forms that readers can visualize: pages, tables, summaries, registries, rules, or workflows.
7. Reduce explicit drafting scaffolds such as long source dumps inside the chapter body unless the chapter specifically requires them.
8. Keep the tone analytical but not academic-heavy; prioritize clarity, continuity, and policy relevance.
9. Make managerial relevance visible in each major section: what can be seen, used, governed, or developed next.
10. Preserve caution about scope and readiness, but express that caution in plain Thai rather than consultant jargon.

## Unclear or risky edits that need confirmation before being treated as stable rules

1. **Reference style**: the edited files remove most inline citations and all end-of-file reference blocks. This may indicate a style preference, but it may also be temporary editing for readability. Confirm whether Chapter 1 should ultimately keep a light reference apparatus or move all references elsewhere.
2. **Terminology for metadata**: the edits use `ข้อมูลอภิพันธุ์` in some places instead of `เมทาดาทา`. Confirm which term should be the house style, or whether the preferred pattern is Thai term followed by English in parentheses on first use.
3. **Degree of technical specificity**: some edits add detail on the risk-map product and departmental data flows. Confirm whether these additions should be treated as authoritative chapter content or as drafting placeholders to be evidence-checked before reuse.
4. **Use of English institutional names**: several edits expand standards bodies into full English names. Confirm whether this is the preferred pattern everywhere, or only in sections that emphasize methodological grounding.
5. **Tolerance for low-level copy edits**: the edited files include several typos and spacing inconsistencies. These should not be learned as style rules; they should be treated as content-direction signals only.

## What should be learned immediately

The edits are strong enough to adopt the following as current defaults for the next drafting cycle:

- More formal Thai voice
- Less shorthand
- More explicit institutional framing
- More visible user-facing and manager-facing outputs
- Cleaner narrative with fewer inline references
- More practical explanation of CDM, sitemap, and governance

## Immediate implications for next revision pass

The next writing pass for Chapter 1 should:

1. Preserve the edited tone and terminology choices where they clearly improve formality and readability.
2. Add the missing content Boss explicitly requested:
   - fuller CDM walkthrough
   - interview-derived use-case table
   - fuller sitemap explanation
   - early-phase data governance explanation
   - FGD1 results integrated into the narrative, not treated as background only
3. Avoid copying over the edited file's typos, spacing issues, or any unevidenced specificity without verification.

