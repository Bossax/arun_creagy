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
# "Search for any hints or rules about the 'acoustic footprint' or 'listening radius' of a single hydrophone in shallow water. How far away can a sensor actually 'hear' the low-frequency fish or high-frequency shrimp before the sound fades?"

**Atomic Note 1: High-Frequency Invertebrate Sound (Rapid local attenuation vs. long-range chorus)** High-frequency sounds produced by snapping shrimp (typically 2–20 kHz) have a dual nature regarding detection. Individual, distinct transient snaps attenuate very rapidly close to the source; measurements show high-frequency sound levels drop by 5 dB within just 50 meters of leaving the reef structure, and by 10 dB at 125 meters, with detectable snap rates dropping four-fold (Lillis et al., 2018). However, the massive aggregated "chorus" or ambient noise level of these invertebrates (specifically in the 3.5–5.5 kHz band) can propagate as a blended background signal for 65–90 km under flat sea conditions (Raick et al., 2021).

- _Hint:_ If your goal is to monitor specific, localized micro-habitat activity (like counting individual shrimp snaps), your hydrophone's effective listening footprint is incredibly small—you must place the rig within 50 meters of the target. If you only need to detect the general presence of a reef via its blended ambient chorus, the sensor can hear it from kilometers away (Lillis et al., 2018; Raick et al., 2021).

**Atomic Note 2: Low-Frequency Fish Sound Range** Low-frequency fish choruses and calls (typically 200–1000 Hz) propagate differently than the high-frequency invertebrate noise. In optimal, flat-sea conditions, the low-frequency fish chorus generally fades into the background noise at a maximum of 1.5 km from the reef crest (Raick et al., 2021). For distinct, individual fish calls, the functional listening radius is even tighter; drifting hydrophone studies noted that distinct fish vocalizations disappeared from recordings once the sensor drifted roughly 50 to 100 meters away from the active reef structure (Lillis et al., 2018).

- _Rule:_ Do not assume a single hydrophone will "hear" individual fish calls across an entire bay. The effective footprint for recording distinct fish vocalizations is limited to the immediate hundreds of meters, and the overall chorus drops off entirely past 1.5 km (Lillis et al., 2018; Raick et al., 2021).

**Atomic Note 3: Environmental Masking Drastically Shrinks the Footprint** The listening radius of a hydrophone is highly dynamic and contracts heavily in the presence of abiotic noise (wind, waves) or anthropogenic noise (vessels). For example, an average wind speed of just 6 knots reduces the propagation detection distance of the low-frequency fish chorus by a factor of nearly 7—dropping the detection range from 1.5 km down to roughly 180–217 meters (Raick et al., 2021). Vessel traffic causes a similar drastic reduction in the acoustic footprint (Raick et al., 2021).

- _Warning:_ When planning sensor spacing, you must account for the _noisiest_ typical conditions, not the quietest. If your deployment area regularly experiences 6-knot winds, swell, or routine boat traffic, your rig's low-frequency listening footprint will shrink to just a few hundred meters (Raick et al., 2021).

**Atomic Note 4: The "Reef Effect" and Non-Spherical Spreading** Sound attenuation around an extended coral reef or shallow coastal environment does not perfectly follow standard spherical or cylindrical spreading models (Kaplan & Mooney, 2016). Because a reef acts as an extended area of multiple interacting sound sources rather than a single point, sound levels remain higher than expected immediately adjacent to the reef, but can drop unpredictably as you move away due to shallow-water bathymetry and the ambient noise floor (Kaplan & Mooney, 2016; Raick et al., 2021).

- _Hint:_ Theoretical acoustic spreading models will likely miscalculate your hydrophone's actual footprint. To accurately know how far your specific rig can "hear" before sound fades, you should conduct localized mobile surveys (such as using a drifting hydrophone) to empirically map the actual propagation drop-off in your specific deployment environment (Kaplan & Mooney, 2016; Lillis et al., 2018).

# "Look for observations on how far apart multiple hydrophones need to be placed within the same habitat. What hints do authors give about spacing replicates so they capture the true variety of the reef without just recording the exact same sounds twice?"

**Atomic Note 1: Explicit Rule for Spatial Independence** To ensure acoustic recordings are truly independent and not capturing the exact same soundscape footprint, explicit rules from biodiversity acoustic sampling dictate that recording sites must be located at least 180 meters apart (Mitchell et al., 2020).

- _Rule:_ If your goal is complete spatial independence between multiple hydrophones in a varied habitat mosaic, space the rigs at a minimum distance of 180 meters from one another.

**Atomic Note 2: Redundancy at the 20-Meter Scale** Researchers deploying multiple hydrophone transects in a shallow sandy/reef edge environment separated their replicate transects by only 20 meters, with the furthest stations separated by 40 meters (Azofeifa-Solano et al., 2025). They observed that all three transects displayed the exact same acoustic patterns and anomalies, likely because they were close enough to share identical sediment types and sound speed profiles (Azofeifa-Solano et al., 2025).

- _Warning:_ Placing hydrophone replicates only 20 meters apart over a uniform micro-habitat (like a sand edge) will likely result in highly redundant data. You must space them further apart or place them across distinct structural transitions.

**Atomic Note 3: Drastic Variation at 30-to-50-Meter Scales** Acoustic characteristics can vary considerably over extremely short distances (less than 50 meters) within a single reef depending on the underlying structure (Lillis et al., 2018). For example, biological sound levels dropped by nearly 5 dB simply by moving over a 30-meter gap in reef material (Lillis et al., 2018).

- _Hint:_ Standard monitoring often assumes a hydrophone placed 20 to 50 meters away represents an entire reef area, but this is a mistake (Lillis et al., 2018). Because soundscapes change drastically over these small tens-of-meters distances, spacing hydrophones 30 to 50 meters apart _can_ capture true variety, provided they are placed in different habitat patches (e.g., one in the reef, one over a sand gap).

**Atomic Note 4: Micro-Habitat Targeting at 100-Meter Scales** To capture the true acoustic variety of a single reef, researchers successfully placed multiple stationary recorders within a small 100 m x 20 m segment (Lillis et al., 2023). By placing the recorders on specifically chosen targets within that close footprint (e.g., live pillar corals vs. dead skeleton vs. soft coral patches), they captured significantly different sound pressure levels and diel patterns without just recording the same chorus twice (Lillis et al., 2023).

- _Observation:_ If your deployment plan requires spacing hydrophones relatively close together (e.g., within a 100-meter footprint), you can avoid redundancy by anchoring them directly to distinctly different biological micro-habitats (e.g., one on live coral, one on adjacent rubble) rather than deploying them randomly or at uniform distances.

# "Extract any findings on 'edge effects' or habitat boundaries. For example, if a hydrophone is placed on the edge of a reef near sand, how does that skew the representativeness of the recording? Where do papers suggest the 'sweet spot' is for a sensor to represent the whole habitat?"


**Atomic Note 1: Severe Attenuation and Skew at Sand-Reef Boundaries**

- _Observation:_ Soundscapes drop off sharply at physical habitat boundaries. Moving a sensor off the reef structure and over a small 30-meter sand gap can reduce biological sound levels by nearly 5 dB (Lillis et al., 2018). Similarly, high-frequency snapping shrimp sounds diminish rapidly, dropping by 5 dB within the first 50 meters of moving off the reef into the open sand (Kaplan & Mooney, 2016).
- _Warning:_ Placing a hydrophone on the sandy edge of a reef to represent the whole habitat will heavily skew your data. A sensor placed just 20 to 50 meters away from the structure in the sand will lose high-frequency invertebrate cues and completely mischaracterize the acoustic richness of the actual reef (Lillis et al., 2018).

**Atomic Note 2: Sensor Directivity at the Reef/Sand Interface**

- _Observation:_ When hydrophones are placed in the sand at 1 m, 2 m, and 5 m from the edge of a fringing reef, the recorded sound levels can behave counterintuitively due to the steep angle of the incoming sound from benthic organisms interacting with the hydrophone's directivity "blind spots" (Azofeifa-Solano et al., 2025).
- _Hint:_ If you must deploy right at a reef/sand boundary, orient the hydrophone horizontally facing the reef rather than vertically. Vertical placements at the edge skewed data, artificially showing lower high-frequency sounds close to the reef and higher sounds further away, whereas horizontal placements captured the true acoustic gradient (Azofeifa-Solano et al., 2025).

**Atomic Note 3: The Danger of "Snapshot" Representativeness in Heterogeneous Habitats**

- _Observation:_ A single stationary hydrophone is often incorrectly assumed to represent an entire reef site, but reefs are highly heterogeneous mosaics. For example, placing a hydrophone next to a live pillar coral yields a completely different acoustic signature (4–7 dB louder) than placing it next to an adjacent dead coral skeleton or a soft coral patch just meters away (Lillis et al., 2023).
- _Rule:_ There is no single "sweet spot" that perfectly represents a highly patchy, heterogeneous habitat on its own. To capture the whole habitat without skew, you must either use an array of spatially replicated sensors anchored to distinctly different micro-habitats, or conduct initial mobile "drifter" surveys to map the acoustic boundaries and gradients before choosing your permanent deployment sites (Lillis et al., 2018; Lillis et al., 2023).

**Atomic Note 4: The "Acoustic Reef Effect" and Integration Area**

- _Observation:_ Because a reef is an extended area of multiple interacting sound sources rather than a single point, sound levels recorded right on the reef edge are dominated by the immediate, localized organisms in the acoustic near-field. Conversely, sound recorded further away represents a blended chorus of the whole reef, known as the "acoustic reef effect" (Kaplan & Mooney, 2016; Raick et al., 2021).
- _Hint:_ If your goal is to record a blended, integrated soundscape representing the whole reef rather than the individual nearest snapping shrimp, the theoretical "sweet spot" is spaced slightly back from the immediate physical structure or elevated in the water column. However, because backing too far into the sand (e.g., >50m) causes you to lose the high-frequency cues due to rapid attenuation, the sweet spot must be a careful balance between blending the aggregate signal and staying close enough to prevent attenuation (Kaplan & Mooney, 2016).
