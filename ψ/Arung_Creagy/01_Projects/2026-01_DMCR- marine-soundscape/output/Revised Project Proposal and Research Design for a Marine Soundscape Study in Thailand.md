---
type: strategy
status: raw
version:
created: 2025-09-30
project:
  - DMCR_Soundscape2026
related_hypothesis: "[[ ]]"
---
>[!note] Change Log



## Introduction

Thailand’s Department of Marine and Coastal Resources (DMCR) has asked for a revision of the initial soundscape‑monitoring proposal. The original plan sought to build an open‑access sound library, develop machine‑learning detectors and document vessel noise. In feedback, DMCR emphasized that the first national project should aim for a **clear, demonstrable outcome** rather than trying to address multiple objectives. They suggested refocusing on showing that acoustic data can inform assessments of ecological status. This document distils knowledge from ecoacoustic literature and the original proposal, and presents a streamlined plan centred on demonstrating how underwater sound can distinguish between healthy and degraded marine ecosystems.

## Assessing Ecological Status from Acoustic Data

### *Hypothesis testing*
- Information in frequency bands can infer ecological state: The power spectral density (PSD) and related sound pressure level (SPL) metrics describe how acoustic energy is distributed across frequencies and time. Studies show that **high SPL or PSD values in low frequencies (< 1 kHz) are associated with healthy reefs** rich in reef‑fish calls. Conversely, **elevated SPL or acoustic complexity in higher frequencies (> 2 kHz) often indicate degraded ecological state** dominated by snapping shrimp or macroalgal gas‑bubbles. 
- Temporal patterns in SPL (hourly, diel or seasonal) also carry ecological information; for example, nocturnal fish choruses or dawn and dusk choruses correspond to behavioral cycles.

- ACI measures variability of amplitude across time and frequency and has been used as a proxy for biological activity. On reefs ACI can differentiate fish calls from anthropogenic noise. 

- An optimized sampling scheme using five combinations of SPL and ACI across specific frequency bands was found to reliably discriminate coral‑reef ecological state. 

- Usefulness of ACI: Comparative studies also show that ACI and entropy indices often fail to correlate with fish abundance; their performance varies across habitats. 


## Contextual and non‑acoustic data
Acoustic levels alone can be ambiguous because similar SPLs may arise from different sources. Collecting contextual data (e.g., wind, tide, AIS vessel tracks) alongside acoustic recordings is therefore critical for evaluating **whether soundscape differences reflect ecological status or external noise.**

**Sound categories and source separation.** 
- Because anthropogenic and abiotic sounds mask biological signals, methods such as long‑term spectrograms, PSD probability plots and unsupervised clustering ==can help separate dominant sources==. 
- Manual inspection or semi‑automated detectors may still be needed due to limited bioacoustic expertise in Thailand, but focusing on coarse categories (fish choruses, shrimp snaps, vessel noise, wind/raindrop noise) can provide meaningful ecological indicators.

### Suitability of variables for ecological status

1. **Low‑frequency SPL/PSD (< 1 kHz).** Strong indicator of reef‑fish assemblages and habitat complexity; higher values suggest healthy reefs.
    
2. **High‑frequency SPL/PSD (> 2 kHz).** Elevated levels typically indicate degraded habitats due to dominance of snapping shrimp and macroalgae.
    
3. **Acoustic complexity/entropy indices.** Useful proxies when used in combination with SPL and when computed in multiple frequency bands; interpret with caution due to bias when sound sources overlap.
    
4. **Temporal patterns (diel, lunar, seasonal).** Night‑time sampling often provides greater discriminative power and requires less effort; recording across different cycles helps capture behavioural rhythms and improve reliability.
    
5. **Source identification metrics.** Detection of key biological sounds (e.g., fish grunts or choruses) and anthropogenic sounds (e.g., vessel engines) via clustering or simple detectors can contextualize SPL differences.
    
6. **Contextual covariates.** Wind speed, tidal flow and proximity to human activities must be recorded and accounted for to avoid misinterpreting anthropogenic noise as ecological change.
    

## Site Selection for the Demonstration

DMCR asked how to choose two sites representing “healthy” and “unhealthy” marine ecosystems. Because DMCR’s existing assessments may be limited, the following **selection criteria** are proposed:

1. **Ecological status.** Select one reef with high live‑coral cover, structural complexity and diverse fish assemblages as the “healthy” site, and another area with known degradation (e.g., macroalgae dominance, rubble, high turbidity) as the “unhealthy” site. Visual surveys or available DMCR reports can guide this choice. For example, a remote marine protected area (MPA) could represent the healthy condition, while a tourist‑heavy island near shipping lanes (e.g., a site similar to Ko Lan) could represent the degraded condition.
    
2. **Human‑use gradient.** To ensure comparability, select sites along a clear gradient of anthropogenic activity: one with minimal vessel traffic and fishing and another adjacent to a port or tourist area. Integrating AIS data or local knowledge can verify the gradient.
    
3. **Environmental similarity.** Control for abiotic factors by choosing sites with similar depth, substrate type and exposure. This reduces variability in sound propagation and strengthens comparisons.
    
4. **Logistical feasibility.** Sites should be accessible for deployment and retrieval, within DMCR’s jurisdiction, and safe for divers. Existing monitoring stations (e.g., where DMCR already collects coral reef data) may simplify logistics and provide complementary data.
    
5. **Scientific interest.** Prioritize habitats where acoustic baseline data are valuable (e.g., coral reefs, seagrass beds or pinnacles). If DMCR plans to expand the network, selecting sites that are representative of broader ecosystems will maximise transferability.
    

If DMCR lacks documented “healthy” sites, a pilot assessment using short‑term recordings and rapid visual surveys can rank candidate locations. The project can then focus on the highest‑contrast pair for the full deployment.

## Project Objectives

1. **Demonstrate the ability of acoustic data to differentiate ecological status.** Collect and analyse underwater sound at two contrasting sites to determine whether SPL, PSD and ACI metrics can discriminate between healthy and degraded habitats.
    
2. **Establish baseline acoustic indices for Thai coastal ecosystems.** Generate night‑time and diel PSD/ACI profiles across multiple frequency bands and document temporal patterns. Record contextual data (wind, tide, vessel traffic) and compile visual observations when possible.
    
3. **Assess the reliability of acoustic indices.** Compare acoustic metrics across sites and seasons; evaluate the relationship between indices and known ecological characteristics; identify biases (e.g., due to snapping shrimp). Use clustering and simple detectors to categorise dominant sound sources.
    
4. **Develop guidelines for future monitoring.** Recommend sampling protocols (duration, frequency bands, seasons) and provide a roadmap for scaling PAM across additional sites. Summarise lessons learned and propose improvements (e.g., need for cross‑disciplinary datasets or capacity building).
    

## Research Design and Risk Management

### Data Collection Strategy

1. **Pilot deployment and site verification (Months 1–2).** Conduct short (one‑week) test deployments at several candidate sites using portable recorders. Check data quality, ambient noise levels and logistical feasibility. Select the final “healthy” and “unhealthy” sites based on the pilot.
    
2. **Continuous passive acoustic monitoring (Months 3–9).** Deploy autonomous hydrophones at the selected sites for nine months to capture seasonal and diel variability. Use sampling rates sufficient to cover frequencies up to 20 kHz (to include fish, shrimp and vessel noise). Retrieve data at regular intervals (every 6–8 weeks) for storage and maintenance.
    
3. **Contextual data recording.** Install simple instruments (e.g., temperature loggers, tide gauges) and log AIS vessel data, wind speed and weather conditions. Conduct visual snorkel/diver surveys at each retrieval to document coral cover, fish assemblages and anthropogenic activities.
    
4. **Biofouling and equipment reliability.** Apply anti‑fouling coatings or housings and schedule mid‑deployment cleaning to reduce biofouling risk. Use redundant sensors where possible.
    

### Data Analysis Plan

1. **Pre‑processing.** Segment recordings into uniform time windows (e.g., 1 min). Remove periods dominated by rain or equipment noise by cross‑referencing weather data.
    
2. **Compute acoustic metrics.** For each segment, compute PSD with 1 Hz resolution and derive SPL in octave and broadband bands. Calculate ACI and entropy indices in multiple bands (< 1 kHz, 1–2 kHz, > 2 kHz) using the optimized settings identified by Elise et al. (2019). Emphasise night‑time data for index computation.
    
3. **Identify source categories.** Use unsupervised clustering on long‑term spectrograms to group similar sound segments, as recommended by Mooney et al. (2020). Manually label clusters as fish chorus, snapping shrimp, vessel noise or abiotic sounds. Simple detectors (e.g., energy thresholds in specific bands) can support recognition of ship passages and fish grunts. Document context using AIS data and visual observations.
    
4. **Statistical comparisons.** Compare SPL/PSD/ACI distributions between sites across frequency bands and time periods. Test whether low‑frequency indices are higher at the healthy site and high‑frequency indices are higher at the degraded site. Assess seasonal stability and diel patterns. Evaluate whether ACI correlates with fish assemblage observations and identify when it fails (e.g., during dense choruses).
    
5. **Integrate contextual data.** Use wind and tide data to control for abiotic noise; filter out periods with high wind or strong currents when comparing sites. Relate vessel‑traffic data to high SPL periods to separate anthropogenic contributions.
    

### Risk Mitigation

- **Reliability of indices.** Combine multiple metrics and focus on frequency‑specific patterns. If ACI or entropy indices show inconsistent trends, rely on PSD/SPL and source‑category analysis.
    
- **Limited bioacoustic expertise.** Prioritise coarse categorisation (fish chorus vs. shrimp vs. vessel noise) and engage with regional experts or open databases for species identification. Document limitations and avoid over‑interpretation.
    
- **Variability and sample size.** Ensure recordings span multiple cycles (diel, lunar, seasonal). Include replicates (two sensors per site) to capture spatial heterogeneity.
    
- **Site access and equipment loss.** Choose sheltered deployment locations, consult local communities and schedule regular maintenance.
    

## Revised Methodology

The methodology is streamlined to focus on ecological status assessment rather than building a comprehensive sound library:

1. **Site selection and pilot testing** – choose contrasting healthy and degraded sites based on ecological surveys and human‑use gradients, conduct pilot recordings, and finalise deployment design.
    
2. **Hydrophone deployment** – deploy two hydrophones per site at appropriate depths (e.g., 5–10 m for reef habitats). Use mooring systems tailored to site conditions (e.g., bottom‑mounted frames or mid‑water suspensions) and include anti‑fouling measures. Confirm nominal frequency range (~20 Hz–20 kHz) and sampling rate (e.g., 48 kHz) based on expected species and anthropogenic noise.
    
3. **Data acquisition and contextual measurements** – collect continuous recordings over nine months, retrieving data regularly. Record environmental parameters and vessel traffic. Conduct visual surveys at the start and end to document coral cover and fish assemblage.
    
4. **Acoustic analyses and index computation** – process recordings to compute PSD, SPL (broadband and octave bands) and ACI in low (< 1 kHz) and high (> 2 kHz) bands. Use the optimized sampling scheme (5 min windows for low frequencies and 5 s windows for high frequencies) for ACI calculations.
    
5. **Source identification and clustering** – apply unsupervised clustering to long‑term spectrograms to categorize sound events. Cross‑reference with AIS and visual observations to assign categories. Use results to interpret indices and to separate biotic from anthropogenic contributions.
    
6. **Statistical analysis and reporting** – compare metrics across sites and time, evaluate the ability of indices to discriminate ecological states, and interpret results in light of contextual data. Produce seasonal and diel plots, PSD probability distributions, and cluster summaries.
    
7. **Capacity building and knowledge sharing** – train DMCR personnel in deployment, retrieval and basic analysis; develop easy‑to‑follow protocols; and share tools and scripts for index computation.
    

## Revised Outputs and Outcomes

The following deliverables align with the new goal of demonstrating ecological assessment via acoustics:

1. **Site‑selection report and pilot data (Month 2)** – summary of candidate sites, pilot recording results, and rationale for final site choices.
    
2. **Baseline acoustic datasets with contextual metadata (Month 9)** – cleaned PSD/SPL/ACI datasets for both sites, annotated with environmental and human‑use information. Raw wav files will be stored securely but are not the primary deliverable.
    
3. **Comparative analysis report (Month 11)** – statistical comparison of acoustic indices across sites and seasons; evaluation of index reliability; identification of dominant sound sources and their ecological implications.
    
4. **Practical monitoring guidelines (Month 11)** – recommendations for sampling duration, frequency bands, and index selection; guidance on integrating contextual data; standard operating procedures for future DMCR deployments.
    
5. **Final stakeholder presentation and technical report (Month 12)** – accessible summary for DMCR leadership and local communities, explaining how acoustic metrics reflect ecological status and outlining next steps for scaling up monitoring.
    

## Revised Timeline

| Month     | Milestone/Deliverable                        | Description                                                                                                                                                                   |
| --------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1–2**   | Site selection & pilot testing               | Identify candidate sites, conduct one‑week test recordings, evaluate data quality and logistical feasibility; deliver site‑selection report.                                  |
| **3**     | Final deployment preparation                 | Procure and test hydrophones, finalize deployment rig and anti‑fouling measures, prepare environmental sensors.                                                               |
| **3–9**   | Continuous monitoring & data retrieval       | Deploy hydrophones at both sites; retrieve data every 6–8 weeks; conduct concurrent visual surveys and record contextual data.                                                |
| **5–10**  | Data processing & index computation          | Pre‑process recordings, compute PSD/SPL/ACI, perform clustering and source categorisation. Provide interim feedback to DMCR if necessary.                                     |
| **9–11**  | Comparative analysis & guideline development | Analyse differences between sites, assess reliability of indices, and draft monitoring guidelines. Deliver comparative analysis report and draft protocols.                   |
| **11–12** | Final reporting & stakeholder engagement     | Prepare final technical report and presentations for DMCR and local stakeholders; incorporate feedback; train DMCR staff on methodology. Deliver final report and guidelines. |

## Conclusion

This revised proposal streamlines the original plan to deliver a clear demonstration of how underwater acoustics can indicate ecological status. By focusing on two contrasting sites and combining PSD/SPL measures, ACI across multiple bands, and contextual data, the project will show whether soundscape metrics can reliably distinguish healthy from degraded habitats. The design acknowledges uncertainties in the utility of acoustic indices by employing multiple metrics and clustering, controlling for environmental factors and emphasising pilot testing. Deliverables are timed to produce tangible outcomes within one year and to provide DMCR with a foundation for expanding passive acoustic monitoring across Thailand’s coastal waters.