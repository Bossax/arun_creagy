# Learning — Foresight grounding audit should separate stable prose from unstable citation mechanics

## Pattern

When grounding a research-heavy report like the foresight 2590 draft, draft prose, research notes, and citation-system tables should not all be edited with the same operational pattern. If table-heavy citation files become mechanically unstable, the workflow should split:

1. **Stable prose track** — keep section files in the v4 working set stable as audit copies.
2. **Citation mechanics track** — update the canonical registry, artifact-paragraph map, and claim-evidence map first.

## Why it works

- It protects readable section drafts while evidence traceability catches up.
- It reduces accidental corruption risk in long-named prose files.
- It makes progress measurable: the citation chain either exists in the citation files or it does not.
- It fits the human’s insistence on read-before-edit discipline and safer repository operations.

## Operational Rule

- Treat v4 prose files under [`ψ/lab/foresight-report-wrting/artifacts/2026-04-03_v4-grounding-audit-working-set/`](ψ/lab/foresight-report-wrting/artifacts/2026-04-03_v4-grounding-audit-working-set/) as stable unless wording itself is the problem.
- Land `SRC_ID` → `ART_PAR_ID` → `CLAIM_ID` updates in the citation system first.
- Only revise prose after the mapped evidence shows overclaim, ambiguity, or unsupported synthesis.
- Use heavier replacement tactics only on citation-system files when normal patching repeatedly fails.

## Applied Here

Relevant artifacts and plans:
- [`plans/2026-04-03_foresight-citation-trace-method-plan.md`](plans/2026-04-03_foresight-citation-trace-method-plan.md)
- [`plans/2026-04-03_draft2-grounding-audit-and-citation-trace-plan.md`](plans/2026-04-03_draft2-grounding-audit-and-citation-trace-plan.md)
- [`ψ/lab/foresight-report-wrting/artifacts/2026-04-03_v4-grounding-audit-working-set/`](ψ/lab/foresight-report-wrting/artifacts/2026-04-03_v4-grounding-audit-working-set/)
- [`ψ/lab/foresight-report-wrting/citations/citation-registry.md`](ψ/lab/foresight-report-wrting/citations/citation-registry.md)
- [`ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md`](ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md)
- [`ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md`](ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md)

## Takeaway

In this repo, safe evidence work is not just about what claims are true. It is also about matching each file type to the right update strategy so that the repository stays more trustworthy after the edit than before it.

---
*Added via Oracle Learn*
