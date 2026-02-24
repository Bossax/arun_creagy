---
type: evidence_index
status: current
created: 2026-02-24
last_updated: 2026-02-24
project:
  - DMCR_Soundscape2026
tags:
  - hydrophone
  - subsea-deployment
  - KOI
AI_output: false
---

# DMCR hydrophone deployment & rig design — evidence index

## Purpose

This index maps **evidence → synthesis → consuming methodology/SOP** so that key design choices and field rules remain auditable and easy to update.

## Evidence inputs (AI_output notes)

- [[../notes/Hydrophone Height & Water Column Placement.md|Hydrophone Height & Water Column Placement]]
- [[../notes/Proximity & Masking Risks.md|Proximity & Masking Risks]]
- [[../notes/Spatial Replication & Acoustic Footprint.md|Spatial Replication & Acoustic Footprint]]
- [[../notes/Topography & Substrate Clues.md|Topography & Substrate Clues]]

## Synthesis artifacts (KO&I outputs)

- [[Deployment configuration factors.md|Deployment configuration factors (knowledge artifact)]]

## Consuming documents

- Methodology (rig + deployment): [[../task/Hydrophone rig design.md|Hydrophone rig design (methodology)]]
- Field SOP (EN/TH): [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]]

## Guiding questions → sources → synthesis → consumption

### 1) Vertical placement & orientation

- **Evidence**
  - [[../notes/Hydrophone Height & Water Column Placement.md|Hydrophone Height & Water Column Placement]]
  - [[../notes/Spatial Replication & Acoustic Footprint.md|Spatial Replication & Acoustic Footprint]] (edge/orientation notes)
- **Synthesis**
  - [[Deployment configuration factors.md|Deployment configuration factors]] → Sections A–B
- **Consumed by**
  - [[../task/Hydrophone rig design.md|Hydrophone rig design]] → “Operational methodology: height + orientation rules”
  - [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]] → “Decision rules: height & orientation”

### 2) Proximity vs representativeness (masking / clipping risk)

- **Evidence**
  - [[../notes/Proximity & Masking Risks.md|Proximity & Masking Risks]]
  - [[../notes/Topography & Substrate Clues.md|Topography & Substrate Clues]]
- **Synthesis**
  - [[Deployment configuration factors.md|Deployment configuration factors]] → Sections C, F
- **Consumed by**
  - [[../task/Hydrophone rig design.md|Hydrophone rig design]] → “Design choices: representativeness target”
  - [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]] → “Candidate-spot selection + test recording guidance”

### 3) Acoustic footprint & replication / spacing

- **Evidence**
  - [[../notes/Spatial Replication & Acoustic Footprint.md|Spatial Replication & Acoustic Footprint]]
- **Synthesis**
  - [[Deployment configuration factors.md|Deployment configuration factors]] → Sections D–E
- **Consumed by**
  - [[../task/Hydrophone rig design.md|Hydrophone rig design]] → “Study design implications: spacing regimes”
  - [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]] → “Multi-rig spacing checklist”

### 4) Topography, substrate, boundaries

- **Evidence**
  - [[../notes/Topography & Substrate Clues.md|Topography & Substrate Clues]]
  - [[../notes/Hydrophone Height & Water Column Placement.md|Hydrophone Height & Water Column Placement]] (sediment + reflections)
- **Synthesis**
  - [[Deployment configuration factors.md|Deployment configuration factors]] → Sections F–G
- **Consumed by**
  - [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]] → “Visual habitat assessment + boundary rules”

## Open questions / evidence gaps (tracked)

- Quantitative evidence for **sediment noise** mechanisms (sand grain impacts, etc.) is not yet present in the current AI_output inputs; treat as a future evidence gap.
- Thai pilot-specific calibration is needed for:
  - Typical wind and vessel regimes
  - Site-specific phase-cancellation / null patterns
  - “Integration sweet spot” distances for target habitats

