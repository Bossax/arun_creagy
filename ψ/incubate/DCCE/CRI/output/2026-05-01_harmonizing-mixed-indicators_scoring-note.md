# Harmonizing mixed indicators for CRI Phase 2 capacity scoring (baseline)

**Date**: 2026-05-01  
**Scope**: DCCE / CRI Phase 2 capacity profiles (Coping / Adaptive / Transformative)  

## Why this note exists

CRI Phase 2 capacity indicators come from heterogeneous administrative sources (LPA-style checklists, registers, counts, ratios). Many Baseline proxies are **binary** (exists / not exists) or small-range counts (0–1, 0–5, 0–4, etc.).

If we aggregate these without an explicit harmonization policy, we risk:

- **Indicator dominance** (wide-range indicators overpower binary ones)
- **Outlier distortion** (min–max “squishes” everyone because one province is extreme)
- **False precision** (binary “existence” interpreted as process quality)
- **Missing-as-zero error** (a known failure mode in the CRI pilot)

This note defines a **single, cross-pillar consistent** harmonization pipeline that keeps Phase 2 defensible.

## Non-negotiable constraints from CRI Methodology

These are already stated in the Phase 2 method and must remain true:

1) **Two-speed measurement**: Baseline proxies now; Target process-quality metrics later ([`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md:59)).
2) **Binary challenge mitigation**: binary indicators are aggregated into **Composite Scores** ([`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md:318)).
3) **Data-richness / confidence (0–3)** recorded per Baseline proxy and shown as an overlay ([`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md:328)).

## Recommended harmonization pipeline (baseline scoring)

### Step 0 — metadata per indicator (before any math)

For each indicator we must record:

- `polarity`: higher is better (+) vs lower is better (−)
- `indicator_type`: one of `{binary, ordinal, count, ratio}`
- `unit` and `denominator` (if any)
- `missingness_rule`: what is “missing” vs what is a “true 0” (explicit)
- `baseline_data_richness_0_3`: confidence score (0–3) per dictionary rules ([`CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md:55))

### Step 1 — standardize each indicator onto a common 0–1 scale

Use **type-specific transforms**, applied consistently across pillars.

#### A) Binary (0/1)

- `score = raw` (0 or 1)
- Interpretation rule: this is **structural readiness**, not operational quality.

#### B) Ordinal (0..N) maturity ladders

- `score = raw / N`
- If ordinal is defined as 1..N, convert to 0..N first.

#### C) Counts / frequencies (unbounded or long-tailed)

Counts should not be allowed to dominate. Use one of the two defensible rules:

1) **Cap then scale** (preferred when there is a policy-relevant “enough” threshold):

- choose `cap` (e.g., drills/year cap)
- `score = min(raw, cap) / cap`

2) **Log-saturating** (preferred when there is heavy skew and no clear cap):

- `score = log(1+raw) / log(1+cap)`

#### D) Ratios / percentages

Ratios and percentages should use bounded transforms:

- if naturally bounded (0–100%), scale directly with bounds
- if not naturally bounded, use **fixed goalposts** when a policy/engineering bound exists; otherwise use robust empirical bounds (e.g., p05–p95) and clamp.

#### E) “Lower is better” variables

Apply the same transform first (min–max, cap, etc.), then invert:

- `score = 1 - score`

### Step 2 — treat missingness explicitly (never default to zero)

Do **not** repeat the Phase 1 pilot failure mode where “missing was treated as zero” under min–max scaling ([`Climate Risk Index (CRI) Pilot Methodology.md`](ψ/incubate/DCCE/CRI/inbox_source/Climate%20Risk%20Index%20(CRI)%20Pilot%20Methodology.md:149)).

Baseline rule:

- If an indicator is missing for a province, it is **unknown**, not 0.

Aggregation rule:

- Within a sub-dimension composite, compute the mean across **available** standardized indicator scores.
- Publish a `coverage` statistic (e.g., share of indicators present) alongside every composite score.

### Step 3 — compute composite scores (binary + mixed types)

For each unit (province), compute:

- Sub-dimension composites: e.g., `Coping-Asset`, `Coping-Process`, etc.
- Pillar/category composites: `Coping`, `Adaptive`, `Transformative`.

Default aggregation operator:

- **Arithmetic mean** of standardized 0–1 indicator scores inside each composite.

Optional alternative (only if we want to penalize “weakest-link” failures):

- **Geometric mean** at the pillar level to reduce compensability across sub-dimensions.

### Step 4 — integrate data-quality without hiding the score

Maintain a strict separation:

1) **Score math**: use standardized indicator values as above.
2) **Quality communication**: show a **confidence overlay** based on mean/median `baseline_data_richness_0_3` for the indicators contributing to the composite, as already required ([`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md:352)).

If we later choose to weight by data-richness, it must be explicitly disclosed and stress-tested (sensitivity analysis).

### Step 5 — QA / robustness checks (minimum)

Before publishing profiles:

- Sensitivity: compare results under (a) sample min–max vs (b) fixed/robust bounds.
- Outlier check: confirm no single province sets the entire scale.
- Missingness check: report coverage, ensure missing is not silently converted to 0.

## Alignment with external methodological guidance (evidence anchor)

This pipeline is consistent with the composite-indicator best-practice guidance summarized in [`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:7), including:

- outlier handling (winsorization/log transforms) ([`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:73))
- fixed goalposts for min–max stability (HDI-style) ([`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:29))
- explicit missing vs zero treatment ([`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:102))

Primary references (links embedded in that note):

- OECD: *Handbook on Constructing Composite Indicators* (Nardo et al., 2008) ([`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:159))
- World Bank: WGI methodology paper (uncertainty / error bars) ([`Harmonizing Mixed Indicators for Composite Indices.md`](ψ/incubate/DCCE/CRI/inbox_source/Harmonizing%20Mixed%20Indicators%20for%20Composite%20Indices.md:162))

## Practical next work items (implementation)

1) Define `indicator_type`, `polarity`, and `cap/goalposts` for each adopted Phase 2 indicator.
2) Add an explicit `missingness_rule` per indicator (“missing vs true zero”).
3) Implement standardized scoring functions (binary/ordinal/count/ratio) in the Phase 2 scoring pipeline.
4) Ensure outputs always include both:
   - composite score(s)
   - coverage + confidence overlay.

