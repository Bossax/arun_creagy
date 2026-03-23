# CRDB interview ingestion traceability note — FTI, UDDC, BMA, DPT

Purpose: record how the four newer interview summaries were ingested into downstream CRDB outputs without overwriting earlier drafts.

## Source interview notes

- FTI: [Interview Summary - FTI.md](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md)
- UDDC: [Interview Summary - UDDC.md](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md)
- BMA: [Interview Summary - BMA.md](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20BMA.md)
- DPT: [Interview Summary - DPT.md](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md)

## Downstream artifacts updated or created for ingestion

- Comparison addendum: [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
- Need-cluster refresh: [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
- Design-facing update: [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)

Note: a report-facing Chapter 2 successor draft was created during an earlier pass, but it is intentionally excluded from the final ingestion set for this task. The source-of-truth ingestion outputs are the ground materials listed above.

## Evidence mapping by interview

### FTI

Main evidence ingested:

- need for a verified **single source of truth** for hazard data
- poor government UX, broken websites, weak contact pathways, and knowledge loss from staff turnover
- need to translate hazard signals into **business interruption / financial impact** evidence
- demand for sector- and location-specific risk products and incentives for private-sector data sharing

Downstream placement:

- comparison row in [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
- trusted baseline, discoverability, tiered service, and business-translation clusters in [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
- private-sector sharing and industrial planning implications in [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)

### UDDC

Main evidence ingested:

- local downscaled flood modeling and high-resolution NbS design workflows
- “double vulnerability” framing that combines hazard and socio-economic exposure
- severe proactive-budgeting barrier and need for DCCE-authoritative maps to justify spending
- explicit requirement for **raw-data/API** and **executive dashboard** tiers

Downstream placement:

- comparison row in [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
- planning-grade data, granularity, budget-defense, and tiered-service clusters in [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
- urban planning / local design additions in [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)

### BMA

Main evidence ingested:

- city-generated operational data for rainfall, flooding, canals, heat index, and environmental monitoring
- weak API-based interoperability and ongoing manual checking of external sources
- need for localized extreme-rainfall forecasting and stronger urban heat analytics
- requirement for role-specific services for operators and decision-makers

Downstream placement:

- comparison row in [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
- interoperability, service design, and granularity clusters in [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
- new urban operations/planning use case in [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)

### DPT

Main evidence ingested:

- multi-scale planning mandate and dependence on fragmented external data
- urgent need for climate-adjusted rainfall, fine-scale heat data, and GIS-ready spatial datasets
- need for infrastructure geometry and engineering-ready inputs
- requirement for planning-grade discoverability rather than high-level thematic maps only

Downstream placement:

- comparison row in [2026-03-23-Chapter2-interview-comparison-matrix-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
- planning-grade, engineering-ready, interoperability, and granularity clusters in [2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
- planning-grade local design additions in [NCAIF_Use_Cases.md](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)

## Scope note

This ingestion update intentionally does **not** rewrite the full CRDB implementation plan or MVP framing. The newer interviews strengthen and sharpen already established directions—especially clearinghouse logic, tiered services, planning-grade data, and trusted baseline endorsement—without changing the Phase 1 architectural stance.
