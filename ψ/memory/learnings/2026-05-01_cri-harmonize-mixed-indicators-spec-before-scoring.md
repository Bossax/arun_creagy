# CRI — Harmonize mixed indicators: write the spec before scoring

CRI Phase 2 capacity profiles combine heterogeneous administrative indicators (binary “existence” checks, small ordinal ladders, counts, ratios). If we score/aggregate them without an explicit harmonization spec, implementation will drift and cross-pillar consistency will break.

**Lesson**: Before computing any composite score, define per-indicator:

- `indicator_type` (binary / ordinal / count / ratio)
- `polarity` (higher is better vs lower is better)
- `bounds` or `cap` (goalposts for min–max, caps for counts)
- `missingness_rule` (missing vs true zero; never default missing→0)
- `baseline_data_richness_0_3` and how it will be communicated (overlay vs weighting)

Then apply the same transform families across pillars and run basic sensitivity checks (outliers, missingness, normalization choice).

Anchors:
- Method’s binary mitigation + confidence overlay: [`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md:318)
- Pilot warning: missing treated as zero can skew min–max results: [`Climate Risk Index (CRI) Pilot Methodology.md`](ψ/incubate/DCCE/CRI/inbox_source/Climate%20Risk%20Index%20(CRI)%20Pilot%20Methodology.md:149)
- Session scoring note: [`2026-05-01_harmonizing-mixed-indicators_scoring-note.md`](ψ/incubate/DCCE/CRI/output/2026-05-01_harmonizing-mixed-indicators_scoring-note.md:1)

