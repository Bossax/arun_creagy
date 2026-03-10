---
type: knowledge_artifact
status: current
created: 2026-02-24
last_updated: 2026-02-24
project:
  - DMCR_Soundscape2026
tags:
  - subsea-deployment
  - hydrophone
  - soundscape-analysis
  - KOI
AI_output: false
---

# Deployment configuration factors for shallow-reef PAM hydrophone rigs (DMCR_Soundscape2026)

## Purpose

This synthesis compresses literature-derived findings into an **exhaustive, actionable list of deployment configuration factors** that affect:

- **Acoustic quality** (signal contamination, band loss, masking, clipping, flow noise)
- **Scientific representativeness** (whether a recording reflects a micro-habitat vs an integrated “reef chorus”)

It is written to be directly consumed by:

- Rig design + deployment methodology: [[../task/Hydrophone rig design.md|Hydrophone rig design]]
- Field SOP (EN/TH): [[Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]]
- Evidence traceability: [[DMCR_Hydrophone_Evidence_Index.md|DMCR_Hydrophone_Evidence_Index]]

## Inputs (candidate evidence for this KO&I pass)

AI_output notes (status: current):

- [[../notes/Hydrophone Height & Water Column Placement.md|Hydrophone Height & Water Column Placement]]
- [[../notes/Proximity & Masking Risks.md|Proximity & Masking Risks]]
- [[../notes/Spatial Replication & Acoustic Footprint.md|Spatial Replication & Acoustic Footprint]]
- [[../notes/Topography & Substrate Clues.md|Topography & Substrate Clues]]

Session objective anchor:

- [[../../../plans/2026-02-22-detailed-hydrophone-for-PAM-deployment-consideration-research.md|Session plan (2026-02-22)]]

## Guiding questions (clusters)

1) **Vertical placement & orientation**
   - How high above seabed should the hydrophone be, and how should it be oriented, to avoid near-field instability and frequency-specific nulls?

2) **Proximity vs representativeness**
   - How do we balance capturing high-frequency invertebrate cues (rapid attenuation) vs avoiding near-field “overpowering/clipping” by the closest organism?

3) **Acoustic footprint, habitat size, and replication**
   - How far does one hydrophone effectively “listen”, and what does that imply for spacing and number of deployments?

4) **Topography, substrate, and edge effects**
   - How do walls, reef masses, sand gaps, rubble/sand transitions, and sediment type bias what we record?

## Factor catalogue (habitat + configuration)

The same factor can affect **acoustic quality** and **scientific representativeness** in different ways.

### A) Hydrophone height above seabed (vertical placement)

**Why it matters (acoustic):**

- **Near-field instability / vertical gradients:** SPL and frequency composition can change over very small vertical distances in shallow water. Extremely benthic placements risk high spatial variability.
- **Seafloor reflections / standing-wave nulls:** a “nice round number” height can land the hydrophone in a frequency-dependent phase-cancellation minimum.
- **Flow-noise boundary layer:** very near-bed placements are more exposed to turbulent boundary effects (site-dependent).

**Why it matters (scientific):**

- Height influences whether the recording is dominated by **benthic micro-habitat** activity vs a more blended soundscape.

**Field observables:** seabed roughness; coral head height; presence of sand/rubble; swell; current.

**Controllable by:**

- Rig design: adjustable mast / mount geometry.
- Deployment config: selected mast height.

**Operational rules (working defaults for DMCR pilot):**

- Provide a **discrete height set** (e.g., selectable increments) rather than “one fixed height forever”.
- Treat **~0.6–1.0 m above seabed** as the baseline working band for stationary shallow-reef deployments, but:
  - If near-field dominance/clipping is likely (dense snapping shrimp, “inside reef structure”), prefer either **slightly higher** or **slightly more offset** (see Section C).
  - If wave zone motion contaminates low frequencies, avoid placing the sensor too near the surface.

### B) Hydrophone orientation (directivity + incident angles)

**Why it matters (acoustic):**

- Hydrophones are not perfectly omnidirectional; orientation can create frequency-dependent sensitivity loss for sound arriving at steep angles.

**Why it matters (scientific):**

- Orientation can bias which habitat components appear “loud” or “quiet”, especially at reef edges.

**Field observables:** reef edge geometry; dominant source direction (reef side vs open sand); current direction.

**Controllable by:** rig mount options and a repeatable orientation-setting process.

**Operational rules:**

- For edge deployments, include an option to mount the hydrophone **horizontally facing the reef** (not only vertical).
- Record orientation as metadata (compass bearing + mount style).

### C) Horizontal distance to reef structure / hotspots (masking vs integration)

**Why it matters (acoustic):**

- Very close placements can be dominated by the nearest loud invertebrates (e.g., snapping shrimp) causing **masking** or even clipping.
- Too far from structure (over sand) can lose high-frequency cues quickly.

**Why it matters (scientific):**

- Close = micro-habitat “microscope”.
- Slightly offset / elevated = more integrated “reef effect” chorus.

**Field observables:** snapping shrimp intensity; fish chorus audibility; distance to prominent coral heads or rubble; sand gap width.

**Controllable by:** diver placement choices; deployment SOP decision rules.

**Operational rules:**

- Avoid placing the hydrophone **inside the densest, loudest micro-habitat pocket** if the objective is an integrated habitat soundscape.
- Avoid placing the rig **tens of meters into open sand** expecting it to represent the reef—edge effects can strongly skew recordings.
- Use a “candidate-spot + short test recording” approach when practical to choose the **integration sweet spot** for a given site.

### D) Acoustic footprint / listening radius (frequency- and noise-dependent)

**Why it matters (acoustic):**

- Effective listening radius is **not fixed**; it shrinks dramatically under wind/wave or vessel noise.
- High-frequency transient cues (snaps/clicks) are highly localized; low-frequency choruses can propagate further *in quiet conditions*.

**Why it matters (scientific):**

- Determines whether one rig can represent a whole habitat or whether you need multiple rigs.

**Operational rules:**

- When planning site coverage, design for **noisy typical conditions**, not ideal calm.
- Do not assume one hydrophone represents an entire bay/reef system.

### E) Spatial replication / sensor spacing (independence vs micro-habitat contrast)

**Why it matters (scientific):**

- Too-close replicates can be redundant; conversely, reefs can vary sharply over tens of meters.

**Operational rules (two regimes):**

- **Spatial independence:** if you want independent samples of a habitat, treat **≥180 m** as a conservative working minimum spacing.
- **Micro-habitat contrast:** if you want to sample heterogeneity inside one reef segment, you can deploy closer (e.g., **30–50 m**) *only if* the sites are intentionally in different micro-habitats (live coral vs rubble vs sand-gap, etc.).

### F) Topography & habitat boundaries (walls, masses, gaps)

**Why it matters (acoustic):**

- Reef masses/walls create complex near-field interference; open sand can be markedly quieter.
- Small gaps can cause noticeable drops in biological sound levels.

**Why it matters (scientific):**

- “Reef edge” vs “inside reef” vs “sand flat” are fundamentally different acoustic samples.

**Operational rules:**

- Document whether the rig is at: **reef wall / reef top / rubble slope / sand edge / sand gap**.
- Treat sand-edge placements as a different category; do not label them “reef representative” unless you intend an edge sample.

### G) Substrate type and seabed profile

**Why it matters (acoustic):**

- Sediment type influences local reflection behavior and thus frequency-dependent peaks/nulls.

**Why it matters (deployment feasibility):**

- Substrate dictates leg stability and whether point-contact feet can be used without damaging biota.

**Operational rules:**

- Require a quick substrate classification in field logs (sand/rubble/rock/live coral) and note slope/unevenness.

### H) Environmental noise regimes (wind, wave, current, vessels)

**Why it matters (acoustic):**

- Flow noise can become broadband masking; wave motion can contaminate low frequencies; vessel traffic can dominate.

**Operational rules:**

- Avoid channelized high flow if the objective is biological soundscape indices (masking risk).
- Place away from known boat lanes when possible.

## What is controllable (and how to translate it)

### Controllable by rig design

- Adjustable height (mast) with repeatable increments.
- Mount options enabling horizontal/reef-facing orientation.
- Flow/noise mitigation: shielding and vibration isolation.
- High stability + low drag profile; no strumming lines.
- Footing/leveling that works on uneven reef (minimizes toppling risk without causing damage).

### Controllable by deployment procedure (SOP)

- Candidate-spot reconnaissance and test recording.
- Choosing distance to reef structure and avoiding continuous noise sources.
- Choosing spacing regime (independence vs micro-habitat contrast) depending on study aim.
- Logging metadata (height, orientation, substrate, topography, conditions).

### Not controllable (must be recorded/managed)

- Wind/wave regime during deployment window.
- Vessel traffic intensity.
- Site-specific interference and phase-cancellation patterns.

## Implications for DMCR methodology documents

Downstream documents should:

1) Explicitly state **which type of representativeness** is intended (micro-habitat vs integrated chorus).
2) Convert factors into **decision rules** with “if/then” logic for field use.
3) Use the evidence index to keep provenance auditable:
   - [[DMCR_Hydrophone_Evidence_Index.md|DMCR_Hydrophone_Evidence_Index]]

## Limitations / open questions

- Quantitative evidence on “sediment noise” (saltating sand grain impacts) is not yet explicit in the current working inputs; treat as a future evidence gap to fill.
- Thai-site specifics (seasonal winds, typical boat traffic, local bathymetry) should be captured via pilot test recordings and appended as local calibration notes.

