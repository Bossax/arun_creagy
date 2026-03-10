---
type: artifact
status: evergreen
tags:
  - marine-soundscape
  - methodology
  - statistical-analysis
  - acoustic-metrics
  - PSD
capture_date: 2025-08-28
source:
authors: []
year:
relevance_to: "[[DMCR Marine Soundscape Project]]"
key_findings:
  - Statistical tests (Pearson's Chi Square, Kruskal-Wallis) are used to link environmental conditions (wind, light) to sound source presence.
  - Linear regression and correlation coefficients quantify relationships between acoustic metrics (BPL, ACI) and soundscape components (shrimp, fish, wind, vessels).
  - Power Spectral Density methods, including TOB SPLs and exceedance levels, are primary metrics for detailed frequency analysis.
  - LTSAs are used for visualizing long-term acoustic patterns.
---
# 1. Statistical Tests for Environmental Conditions and Sound Source Presence
    
- The [[Biological Sound Sources Drive Soundscape Characteristics of Two Australian Marine Parks]] study used **Pearson's Chi Square tests** to characterize and compare typical wind conditions among different deployment periods and between study sites, linking this environmental factor to observed seasonal soundscape patterns.
- It also employed **Kruskal-Wallis tests** and **Dunn tests (with Holm correction for post-hoc p-values)** to determine significant hourly differences in the presence of vessels, fish choruses, and dolphins across different light regimes (dawn, daylight, dusk, night), effectively quantifying their diel patterns in relation to environmental light conditions.
- The study explicitly states that "seasonal differences in proportional wind speeds at weather stations closest to each site did not correspond to seasonal differences in SPL at either site," directly indicating a **lack of correlation** in that specific instance. Conversely, it notes that soundscape patterns were "driven by seasonal differences in biological contributions rather than anthropogenic sound sources".

# 2. Linear Regression and Correlation Coefficients for Soundscape Components
    
- The [[Temporal patterns in the soundscape of shallow waters medierranian sea]] study extensively used **linear regression equations and correlation coefficients (r-values) along with p-values** to quantify the relationship between Band Pressure Levels (BPLs) and the Acoustic Complexity Index (ACI) against various soundscape components. This allowed them to:
	- Correlate BPL and ACI with **snapping shrimp counts**.
	- Correlate BPL and ACI with **fish sound counts**.
	- Correlate BPL and ACI with **wind speed** (as a proxy for wave noise, a geophonic source).
	- Correlate BPL and ACI with **vessel passages** (anthropophony).

- They concluded that seasonal variability in BPLs was primarily attributable to **sea state (wind speed)** for lower frequencies and **snapping shrimp activity** for higher frequencies.


# 3. Power Spectral Density methods
- **One Third Octave Band Sound Pressure Levels (SPLs)**: These are the primary metrics used, covering frequencies from 10 Hz to 20 kHz. This allows for a detailed analysis of sound energy across different frequency ranges.
- **Exceedance Levels (ELs)**: Calculated for each one-third octave band (**TOB**) to estimate the distribution of sound levels over time.
	- **Median (50 EL)**: Represents the typical sound level.
	- **10 EL**: Indicates rare, high-noise events (exceeded only 10% of the time).
	- **90 EL**: Describes the quietest conditions (exceeded 90% of the time).
	- **1 EL and 99 ELs**: Provide the full range of sound levels observed.
- **Inter Quartile Range (IQR) SPLs**: Used to evaluate the variability of sound pressure levels within a station.
- **Arithmetic Mean (AM) SPLs**: Also calculated, noting that the arithmetic mean is more affected by "brief and high amplitude human-generated events" compared to the median.
- **Broadband SPLs (10 Hz–20 kHz)**: Used for overall comparison of noise levels across stations.
- **Bandwidth Correction**: Applied to the TOB spectra to assess the mean contribution of frequencies within each TOB.

- **Temporal Representation**: The soundscape was characterized over a 16-month period (March 2020 to June 2021), crucially **including the COVID-19 lockdown**. This allowed for:
    - **Yearly** median SPL values and distributions.
    - **Monthly variations** in median SPLs.
    - **Seasonal differences** (spring–summer versus autumn–winter) in sound levels.
    - A direct comparison of the **lockdown period (April 2020) with April 2021** (representing more typical, unlocked conditions) to assess the impact of reduced human activity on the soundscape.

# Descriptive Quantification with Acoustic Metrics
    
- All studies use standardized soundscape metrics like **Broadband Sound Pressure Level (SPL)** and **Power Spectral Density (PSD)** to characterize soundscapes. These metrics are then analyzed in relation to seasonal and diel patterns to observe how sound levels change, indicating the influence of different sound sources.
- **Long-Term Spectral Averages (LTSAs)** were used to visualize longer-term acoustic patterns and compare peaks in sound levels to hourly presence information to determine primary contributors to the soundscape.
