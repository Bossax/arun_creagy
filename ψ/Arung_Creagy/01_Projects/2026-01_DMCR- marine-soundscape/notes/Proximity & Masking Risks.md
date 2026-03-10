---
status: current
tags: []
created: 2026-02-22
last_updated: 2026-02-22
AI_prompt: false
AI_output: true
project:
  - DMCR_Soundscape2026
type: artifact
---
# "Look for examples of recordings being masked, clipped, or overpowered by local noise, particularly from snapping shrimp or macroalgae. What hints do the papers give about spacing the sensor to get a balanced soundscape rather than just the closest organism?"

**Atomic Note 1: The "Reef Effect" and Acoustic Blending**

- _Observation:_ A hydrophone placed directly on or immediately adjacent to a reef will primarily record the loudest, closest individual organisms. Conversely, a hydrophone placed further away records a blended acoustic signature coming from a larger portion of the habitat, a phenomenon known as the "acoustic reef effect" (Raick et al., 2021).
- _Hint:_ If you want a balanced soundscape representing the entire ecosystem rather than the isolated acoustic behavior of a single nearby crab or fish, you must space the sensor at a moderate distance (e.g., elevated in the water column or spaced a few meters horizontally) so that individual nearby sources do not overpower the aggregate signal (Raick et al., 2021).

**Atomic Note 2: Snapping Shrimp Transients and Near-Field Overpowering**

- _Observation:_ Snapping shrimp produce extremely loud, broadband transient snaps (with peak-to-peak source levels up to 183–189 dB re 1 µPa at 1 m) that dominate the 2–20 kHz high-frequency band (Azofeifa-Solano et al., 2025; Lillis et al., 2018),. When a recorder is placed very close to the benthos, sound levels and variability are at their absolute highest due to the unpredictable nature of the acoustic near-field and the dense localized aggregations of these invertebrates (Lillis et al., 2023).
- _Warning:_ Placing the hydrophone directly inside the reef structure or too close to the bottom risks having your data completely overpowered or clipped by the closest individual snapping shrimp. Elevating the sensor slightly (e.g., 1 to 5 meters off the bottom) reduces this extreme near-field variability and prevents a single nearby invertebrate from dominating your entire high-frequency dataset (Lillis et al., 2023).

**Atomic Note 3: Constant Noise Masking Acoustic Indices**

- _Observation:_ Algorithms designed to measure biodiversity, such as the Acoustic Complexity Index (ACI), rely on detecting variations in signal intensity over time. However, loud, continuous local background noises—such as heavy flow/running water, mechanical wave heave, or overwhelming insect/invertebrate choruses—can completely override the biological signals of interest, dampening the signal variation and rendering the index useless (Mitchell et al., 2020).
- _Rule:_ You must carefully survey the immediate micro-habitat for continuous, overpowering noise sources (like turbulent flow channels or mooring chain noise) before finalizing the rig's placement. If the sensor is placed too close to a continuous noise source, it will mask the transient biological sounds (like specific fish calls) needed to accurately measure biodiversity (Lillis et al., 2018; Mitchell et al., 2020),.

**Atomic Note 4: Balancing Attenuation vs. Integration Space**

- _Observation:_ While moving the rig away from the reef helps blend the soundscape, high-frequency sounds (like shrimp snaps) attenuate very rapidly. Measurements show that these high-frequency sound levels can drop significantly within just the first 50 to 125 meters of moving away from the structure (Kaplan & Mooney, 2016; Lillis et al., 2018),,.
- _Hint:_ You must balance integration with attenuation. If you space the rig _too_ far from the habitat (e.g., >50 meters into the sand) to avoid local overpowering, you will lose the high-frequency invertebrate chorus entirely. The optimal deployment is a "sweet spot"—close enough to capture the high-frequency cues, but spaced just far enough off the physical structure to integrate the broader reef chorus without being deafened by a single organism (Kaplan & Mooney, 2016).

