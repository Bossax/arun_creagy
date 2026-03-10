---
type:
  - note
status: evergreen
tags:
  - fish-chorus
  - signal-processing
  - machine-learning
  - RRPCA
created: 2025-08-14
last_updated: 2026-02-11
AI_prompt: false
AI_output: false
project: "[[DMCR Marine Soundscape Project]]"
---
# Characteristic features of fish calls
These features are typically low frequency (generally less than 3-5 kHz, often 40–1000 Hz), short duration (less than 5 seconds), repetitive sound elements, and often exhibiting multiple frequency harmonics

# Criteria for a chorus, such as 
1. observing **overlapping calls from many individuals** (to the extent that individual calls cannot be distinguished)
2. continuous **increase in background sound levels** within a characteristic frequency band (observable, often >3 dB, for an extended period, e.g., an hour or more)
3. distinct **temporal variation** on diel, lunar, seasonal, or annual scales


**Denoising and Decomposition (RRPCA)**: The first analytical step, Randomized Robust Principal Component Analysis (RRPCA), decomposes the soundscape into "low rank" (chronic) and "sparse" (transient) matrices
- fish choruses are "chronic" signals, while sounds like vessel cavitation, whales, and sonar are "transient"
- output clusters must then be **manually pooled** by human experts into definitive "**chorus**" and "**noise**" classes for training a neural network

**Neural Network Training and Validation**: The neural network is trained using these manually curated "chorus" and "noise" classes
