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
color: ""
---
# "What does the text say about acoustic boundary layers, seabed reflections, or vertical differences in sound? I am looking for any hints on how high off the seabed we should place the hydrophone to get clean data."

**Atomic Note 1: Near-Field Variability and Vertical Gradients** Sound pressure levels and frequency compositions change significantly over small vertical distances in shallow water. Low-frequency acoustic energy (<400 Hz) can be 5–8 dB louder near the benthos than at the surface, but this benthic region lies within the acoustic near-field where sound is highly unpredictable due to complex interference patterns (Lillis et al., 2023).

- _Hint:_ If you need stable, uniform low-frequency measurements, avoid placing the hydrophone extremely close to the seabed, as near-field effects create high spatial variability that can skew data (Azofeifa-Solano et al., 2025; Lillis et al., 2023).

**Atomic Note 2: Seafloor Reflections and Standing Waves** Acoustic waves interacting with the seafloor create multi-path interference, standing waves, and areas of high and low pressure that are heavily frequency-dependent (Azofeifa-Solano et al., 2025). These seabed reflections cause coherent peaks and deep valleys (nulls) in the received sound spectrum depending on the hydrophone's depth and the grazing angles of the sound (Ainslie et al., 2024).

- _Warning:_ A specific height off the bottom (e.g., researchers noted issues at 60 cm) can inadvertently place the hydrophone in a phase-cancellation "minimum" for certain frequencies, effectively deleting that frequency band from your data (Azofeifa-Solano et al., 2025).

**Atomic Note 3: Sensor Directivity Relative to the Seabed** Hydrophones are rarely perfectly omnidirectional and suffer from frequency-dependent directivity (e.g., a sensitivity drop starting around a 90-degree angle for 2–5 kHz sounds). When a hydrophone is placed low to the seabed (e.g., 60 cm) and oriented vertically, the steep incident angle of sounds originating from benthic organisms (like snapping shrimp) hits the sensor's directional "blind spots," artificially lowering recorded levels (Azofeifa-Solano et al., 2025).

- _Hint:_ If the hydrophone must be close to the bottom, orient it horizontally toward the target habitat rather than vertically. Alternatively, elevate it high enough so that benthic sounds hit the sensor at a shallower, more favorable angle (Azofeifa-Solano et al., 2025).

**Atomic Note 4: Wave-Induced Vertical Motion** Surface wave action transmits physical up-and-down motion down the mooring line to the sensor. This non-acoustic vertical velocity introduces heavy contamination into low-frequency data, typically below 100 Hz (Kaplan & Mooney, 2016; Lillis et al., 2018).

- _Rule:_ You must decouple surface motion from the benthic sensor. Use elastic shock absorbers (e.g., an "Anchor Buddy") at the top and bottom of the mooring line, and affix heavy weights (e.g., 2-lb lead) directly adjacent to the hydrophone to ensure it remains strictly vertical and physically stable against wave heave (Kaplan & Mooney, 2016).

**Atomic Note 5: Surface vs. Benthic Placement Trade-Offs** Placing a hydrophone near the surface (e.g., 1 m depth) can reduce the total acoustic energy received from the reef by half (6–7 dB lower) compared to a benthic placement (Lillis et al., 2023). However, placing it too close to the surface increases data ruin from wind, breaking waves, and flow noise (Lillis et al., 2018; Raick et al., 2021).

- _Observation:_ Standard, successful stationary deployments in shallow reef environments commonly anchor the hydrophone between 60 cm and 1 m off the sandy seafloor. This height acts as a sweet spot that balances close proximity to biological sound sources with physical clearance from the immediate bottom (Azofeifa-Solano et al., 2025; Kaplan & Mooney, 2016; Radford et al., 2014).



# "Are there any observations about how bottom-mounted frames compare to mid-water suspensions, especially regarding current drag or sediment noise?"


**Atomic Note 1: Absence of Explicit "Sediment Noise" or "Frame Drag" Data**

- _Observation:_ The provided literature does not contain explicit measurements of physical current drag on bottom-mounted frames, nor does it explicitly mention "sediment noise" (such as saltating sand grains striking the hydrophone). However, the sources extensively document the differing physical and acoustic vulnerabilities of mid-water suspension lines versus benthic mounts.

**Atomic Note 2: Cable Strumming and Wave Heave in Mid-Water Suspensions** Mid-water suspensions, particularly those connected to surface buoys, are highly vulnerable to physical up-and-down motion and "strumming noise" vibrating down the line. This mechanical interference creates severe low-frequency artifacts (typically below 200 Hz) that can render data in that band unusable (Kaplan & Mooney, 2016; Raick et al., 2021).

- _Rule:_ If using a mid-water suspension in areas with swells or high sea states, you must decouple the hydrophone from the surface using elastic shock absorbers (e.g., bungee material or an "Anchor Buddy") and heavy weights to dampen wave-driven vertical movements (Kaplan & Mooney, 2016; Lillis et al., 2018). Alternatively, use a buoyancy-controlled subsurface float to eliminate surface wave action entirely (Lillis et al., 2018).

**Atomic Note 3: Flow Noise Masking** Fast-flowing water creates constant, broadband geophonic background noise that can easily override biological signal variations, essentially breaking algorithms designed to measure biodiversity, such as the Acoustic Complexity Index (Mitchell et al., 2020).

- _Hint:_ If your rig must be deployed in an area with high currents or flow, orient the hydrophone away from the dominant direction of the flow to minimize direct hydrodynamic noise across the sensor (Mitchell et al., 2020).

**Atomic Note 4: Mid-Water Vulnerability to Distant Vessel Noise** While elevating a hydrophone mid-water might seem like a good way to escape bottom interference, it can inadvertently position the sensor in an optimal receiving pathway for distant anthropogenic noise. In vertical array tests, mid-water recorders (e.g., 5 m depth) actually captured the highest levels of low-frequency ship thruster noise compared to recorders at the surface or the benthos (Lillis et al., 2023).

- _Warning:_ Do not assume mid-water suspension will inherently "clean" your data; it trades benthic near-field variability for an increased susceptibility to propagating vessel noise.

**Atomic Note 5: Benthic Proximity and Sediment Acoustic Properties** Bottom-mounted frames place the sensor in the acoustic near-field of the reef, capturing the highest levels of biological acoustic energy (5–8 dB higher than the surface at low frequencies) (Lillis et al., 2023). However, the seafloor sediment heavily influences the local sound speed profile and how sound waves reflect into the receiver (Azofeifa-Solano et al., 2025).

- _Hint:_ When mounting directly to the bottom (e.g., on a T-bar 5 cm off the seafloor or a star-picket 60 cm off), recognize that the acoustic properties of the sediment itself—combined with the sensor's height and orientation—will dictate frequency-dependent phase cancellations and sensitivities. Small changes in position or sediment type across your deployment area will drastically alter the received soundscape (Azofeifa-Solano et al., 2025; Lillis et al., 2023).