# Learning — Chapter-separated drafting + “real sources only” citations

## Pattern
When producing report prose from a repo workspace that contains many internal analysis markdown files, enforce a two-layer output:

1) **Chapter-separated draft outputs** (one file per chapter / section group)
2) **Chapter-scoped evidence trace ledger** (claim → source mapping), stored alongside the draft

## Rule
Draft prose must **not** cite repo-internal markdown artifacts as final references.

Instead:
- Use internal markdown artifacts as analysis intermediates only.
- Trace every claim to the underlying **real source** (law text, agency dataset page, official report PDF, peer-reviewed article, etc.), usually listed in the bottom “Works cited / References” section of the research artifact.
- If a real source cannot be recovered or verified, mark the draft as **HOLD/GAP** rather than writing with implied certainty.

## Why it works
- Prevents “markdown-to-markdown citation chains” from being mistaken as evidence.
- Makes uncertainty visible and auditable.
- Keeps writing scalable: each chapter becomes a bounded drafting + audit unit.

## Implementation checklist
- Create `YYYY-MM-DD_chX-round1-draft.md`
- Create `YYYY-MM-DD_chX-round1-evidence-trace.md`
- In the draft, allow only academic citations to real sources.
- Any quantitative / legal feasibility claim without a real source → HOLD.

## Applied in
- Foresight report SBP youth futures 2590: chapter-separated Round 1 packages in [`ψ/lab/foresight-report-wrting/artifacts`](ψ/lab/foresight-report-wrting/artifacts:1)


---
*Added via Oracle Learn*
