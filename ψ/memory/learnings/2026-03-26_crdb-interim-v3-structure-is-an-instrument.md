# Learning: CRDB interim v3 — Structure is an instrument, not a template

## Context
In CRDB Interim Report v3 drafting, style drift came from treating a “TOR subsection template” literally. That produced bullet-heavy partitions and unwanted micro-subsections, diverging from the v1 report voice.

## Pattern
Use structure only where it is the deliverable:
- **Hierarchy bullets**: only for sitemap / navigation structures (e.g., NCAIF sitemap).
- **Tables**: only for summary artifacts (consultation summary, interview pattern summary, product landscape status/gaps) and for inventories (literature inventory, key studies).
- **Everything else**: paragraph-first Thai prose under a single TOR clause heading.

## Guardrails
- Each clause file: exactly one `##` heading (TOR-only) and no `###`.
- No visible internal repo paths or markdown links in public prose; keep provenance in an HTML comment block.
- If a section claims an “inventory” exists, the public-facing **table must enumerate the inventory** (don’t keep completeness only in narrative).

## Why it works
It preserves v1-style readability while still making committee-reviewable artifacts (sitemaps, summaries, inventories) inspectable and auditable.


---
*Added via Oracle Learn*
