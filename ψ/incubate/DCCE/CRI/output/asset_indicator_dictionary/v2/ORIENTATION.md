# CRI Asset Dictionary v2 — Working Area Orientation

Location: `ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/v2/`

This working area supports the **service-oriented CRI asset dictionary v2** workflow. It is intentionally scoped to: raw extractions, intermediate transforms, conceptual notes, reflection, and the final dictionary outputs.

## Subfolders

- `notebooklm_raw/`
  - Purpose: Store **verbatim** NotebookLM outputs (raw excerpts / answers) used as upstream evidence for v2.
  - Notes: Avoid content edits beyond file naming and minimal metadata headers.

- `flattened/`
  - Purpose: Store normalized/flattened representations derived from raw sources (e.g., consistent tables, CSV/JSON exports, line-oriented text suitable for diffing).

- `concepts/`
  - Purpose: Store concept definitions and mappings used by the service-oriented dictionary (e.g., “asset”, “service”, “indicator”, “function”, “failure mode”).

- `reflection/`
  - Purpose: Store reasoning notes, design decisions, open questions, and v2-specific audit trails.

- `dictionary/`
  - Purpose: Store assembled v2 asset–indicator dictionary outputs (drafts and finalized versions).

## Fixed NotebookLM parameters (do not change for this workflow)

- `notebook_id = urban-resilience-infrastructur`

Session note:
- The original planned session id was `cb4bff4b`, but after the Chrome-profile reset + re-auth, a new working session id was issued by a successful test query: `6085058f`.
- Use `session_id = 6085058f` for subsequent runs unless we deliberately start a fresh session.

Canonical source-title record (resolved list used for title normalization):
- `ψ/incubate/DCCE/CRI/output/notebooklm_runs/2026-05-01_urban-resilience_title-resolution_raw.md`

## Guardrails for this working area

- Do not place synthesized narrative drafts here unless they directly support v2 dictionary assembly.
- Keep raw vs. derived outputs separated (raw in `notebooklm_raw/`, derived in `flattened/` or downstream folders).

