---
parent: "[["
tags:
  - DMCR_project
date: 2025-08-01T21:40:00
---

## 1. Executive Summary

This proposal outlines a project aimed at characterizing the underwater soundscapes of Thailand's coastal waters. The initiative seeks to address the critical need for innovative, scalable, and cost-effective monitoring solutions to combat threats to marine biodiversity and livelihoods from unsustainable human activities. The project will establish an open-access underwater sound data library, develop machine learning models for sound classification, and demonstrate the utility of acoustic data in complementing existing environmental monitoring techniques. This foundational research will contribute to marine conservation and management efforts by providing a baseline understanding of the acoustic environment and enabling the detection of potentially harmful activities.



## 2. Introduction and Background

Thailand's coastal ecosystems are vital for both biodiversity and human well-being, supporting diverse marine life and providing livelihoods for millions. However, these ecosystems face significant threats from various human activities, including overtourism and destructive fishing practices. Traditional methods for monitoring marine environments, such as vessel-based surveys, are often expensive, labor-intensive, and limited in their spatial and temporal coverage. This necessitates the exploration of alternative, more efficient monitoring approaches.

Passive acoustic monitoring (PAM) offers a promising solution by providing a non-invasive and continuous method for observing marine environments. Underwater soundscapes, which encompass all sounds within a marine environment, can reveal crucial information about biological activity, geological processes, and anthropogenic impacts. By analyzing these soundscapes, researchers can gain insights into ecosystem health, species presence, and human disturbances.

This project builds upon the recognition of the urgent need for enhanced marine monitoring capabilities in Thailand. It aims to leverage the power of acoustic data to provide a comprehensive understanding of the underwater soundscape, thereby supporting more effective conservation and management strategies. ~~The Department of Marine and Coastal Resources (DMCR) has expressed interest in this approach, providing initial seeding funds for this initiative, which aligns with their broader efforts, including the survey of underwater pinnacles.~~


## 3. Project Goals and Objectives

The overarching goal of this project is to characterize the underwater soundscapes of Thailand's coast to support marine conservation and management. This will be achieved through the following specific objectives:

1.  **Develop an Open-Access Underwater Sound Data Library:** Establish a comprehensive, open-access repository of underwater acoustic data collected from Thai waters using passive acoustic monitoring systems. This library will serve as a foundational resource for future research and conservation efforts.

2.  **Develop Classification Machine Learning Models:** Create and train machine learning models capable of detecting and classifying various underwater sounds, with a particular focus on identifying surface vessel activities. These models will enable automated analysis of large datasets and provide insights into human impacts on the marine environment.

3.  **Demonstrate the Use of Acoustic Data for Environmental Monitoring:** Showcase how acoustic data can effectively complement existing environmental monitoring techniques. This includes establishing baseline acoustic indices for biodiversity and providing case studies that illustrate the practical application of acoustic monitoring in marine management.

It is important to note that given the initial one-year timeline and the seeding budget of 500,000 THB provided by DMCR, the project may need to focus on a specific area or use case to ensure tangible outcomes within this timeframe. Potential focus areas include hardware development, software/algorithm development, or a selected use case such as illegal fishing activity detection in specific areas like Songkhla Bay. While biodiversity calculations are a long-term goal, initial efforts may concentrate on specific groups or ecosystems, such as coral reefs or pinnacles, where baseline data is either available or urgently needed.


## 4. Methodology

### 4.1 Hardware Development and Deployment

The project will commence with the development and deployment of hydrophone modules designed for continuous underwater acoustic data collection. These modules will be constructed using commercially available components, integrated with custom mechanical structures to ensure durability and optimal performance in marine environments.

**Unresolved Question:** Where to deploy specifically? (Annotation: This decision will be critical for data relevance and project impact. Options include focusing on areas with existing baseline data, such as coral reefs, or newer areas like underwater pinnacles where acoustic data could establish a crucial baseline. A short deployment to check data quality will be conducted prior to full deployment.)

**Unresolved Question:** How to minimize biofouling risk? (Annotation: Biofouling can significantly impact hydrophone performance and data quality. Strategies for mitigation, such as anti-fouling coatings or regular maintenance schedules, need to be determined.)

**Unresolved Question:** What should be the deployment rig? (Annotation: The design of the deployment rig will depend on the chosen deployment sites and environmental conditions, ensuring stability and security of the hydrophones.)

**Unresolved Question:** Which brand and model to procure? (Annotation: The selection of hydrophone brand and model will be based on sensitivity, frequency response, durability, and cost-effectiveness, considering the nominal frequency range of interest for marine soundscapes.)




### 4.2 Acoustic Data Collection

Hydrophones will be deployed at strategic marine sites where existing data collection routines are in place, allowing for cross-referencing and validation of acoustic data with other environmental parameters. Continuous underwater recordings will be collected over a period of at least six months to capture seasonal variations in biological and human activities. Data will be gathered from the deployment sites on a monthly basis.

**Unresolved Question:** Site and deployment criteria? (Annotation: The specific criteria for selecting deployment sites need to be finalized, considering factors such as ecological significance, anthropogenic activity levels, and logistical feasibility. The project aims to propose trying both reef and pinnacle sites.)

**Unresolved Question:** Data acquisition plan? (Annotation: A detailed plan for data acquisition, including sampling rates, recording duration, and data transfer protocols, needs to be established to ensure data quality and consistency.)

**Unresolved Question:** Diver and boat crew? (Annotation: The availability and coordination of diver and boat crew for deployment, maintenance, and data retrieval operations are crucial for the successful execution of the project.)




### 4.3 Data Analysis and Machine Learning Model Development

Collected acoustic data will undergo a rigorous analysis process, beginning with sound labeling. This involves clustering acoustically similar events through feature extraction from spectrograms, dimensionality reduction techniques (e.g., UMAP), and density-based clustering (e.g., HDBSCAN). Potential vessel sound clusters will be identified based on their characteristics, and auxiliary data such as AIS ship tracks and satellite imagery will be used to assign specific vessel-type labels (e.g., trawler, speedboat).

Sound clusters will be further labeled by expert analysts through auditory and visual inspection, cross-referencing with other available data sources (e.g., visual data, weather radar, seismic activity data, other underwater sound libraries). The goal is to identify potential sources of sound clusters, specifying whether they are biological, geological, or atmospheric, and to pinpoint exact sources or processes where possible.

Subsequently, classification models will be developed and trained using the vessel-labeled events and categorized soundscapes. The performance of these models will be tested with additional collected data to ensure accuracy and robustness.

**Unresolved Question:** Where to store raw wav data? (Annotation: A robust data infrastructure plan is needed to manage the large volume of raw acoustic data, ensuring secure storage, accessibility, and efficient processing.)

**Unresolved Question:** Ecoacoustic problem: what to measure? (Annotation: Defining the specific ecoacoustic problems to address, such as the impact of noise on marine life or the detection of illegal activities, will guide the focus of data analysis and model development.)

**Unresolved Question:** Detection and classification: what to find? (Annotation: Clearly defining the specific sound events or categories that the machine learning models should detect and classify is crucial for model training and evaluation. This could include specific vessel types, marine mammal vocalizations, or other anthropogenic noises.)

**Unresolved Question:** What is the nominal frequency range of interest? (Annotation: Determining the optimal frequency range for analysis is essential for capturing relevant acoustic information while minimizing noise and computational burden.)

**Unresolved Question:** What are expected to be heard? (Annotation: An understanding of the expected soundscape components at the chosen deployment sites will help in guiding the labeling process and validating model outputs.)




### 4.4 Soundscape Characterization and Baseline Establishment

Following data analysis and model development, the project will focus on characterizing the soundscape to establish a baseline understanding of the acoustic environment. This will involve calculating seasonal Power Spectral Density (PSD) to understand ambient noise levels and their variations. The characteristics of identified sound clusters will be analyzed to gain insights into dominant sound sources. Additionally, biodiversity acoustic indices, such as intensity indices and acoustic complexity indices, will be computed to assess the health and diversity of the marine ecosystem.

This baseline characterization will be crucial for monitoring changes over time, evaluating the impact of human activities, and informing conservation strategies. The project will also demonstrate the utility of these acoustic metrics in complementing existing environmental monitoring techniques, providing a more holistic view of marine ecosystem health.

**Unresolved Question:** What are available resources that could be utilized to fill in the knowledge gaps? (Annotation: Identifying and leveraging existing open-access databases like 'Hear my ship' and 'Fish sounds' will be crucial for enriching the sound library and improving model training. Collaboration with ongoing research efforts, such as DMCR's acoustic monitoring project with Japan, will also be explored.)




## 5. Expected Outputs and Outcomes

This project is anticipated to yield several key outputs and contribute to significant outcomes for marine conservation and management in Thailand:

### Expected Outputs:
1.  **Open-Access Thai Underwater Sound Library with Labeled Datasets:** A publicly accessible database of underwater acoustic recordings from Thai waters, complete with meticulously labeled sound events. This will serve as a valuable resource for researchers, policymakers, and the public.
2.  **Baseline Acoustic Indices for Biodiversity:** Comprehensive data on baseline acoustic indices, providing a reference point for assessing marine biodiversity and detecting changes over time.
3.  **Trained AI Models for Sound Classifications:** Robust machine learning models capable of accurately classifying various underwater sounds, particularly vessel activities, enabling automated monitoring and analysis.
4.  **System Design Documentation for Hardware and AI Workflow:** Detailed documentation outlining the design and construction of the hydrophone modules and the workflow for AI model development, ensuring reproducibility and future scalability.
5.  **Reports and Presentations for Stakeholders:** Regular reports and presentations, including case studies and practical recommendations, demonstrating how acoustic monitoring can be integrated into existing marine management frameworks.

### Expected Outcomes and Impact:
1.  **Foundational Database for Underwater Sound Research:** The established sound library will serve as a critical foundation for advancing underwater acoustic research in Thailand and the broader region.
2.  **Increased Awareness of Acoustic Monitoring:** The project will raise awareness among marine biologists, conservationists, and policymakers regarding the importance and utility of acoustic monitoring as a tool for environmental assessment.
3.  **Enhanced Marine Conservation and Management:** By providing new insights into marine soundscapes and human impacts, the project will contribute directly to more informed and effective conservation strategies and management decisions.
4.  **Proof of Concept for Acoustic Analysis:** The project will demonstrate the practical application of spectrograms, Power Spectral Density (PSD), acoustic indices, and ship sound detection as valuable analytical tools.
5.  **Leveraging Open Access Databases:** The project will showcase the effective integration of open-access databases like 'Hear my ship' and 'Fish sounds' to enrich data analysis and model development.




## 6. Timeline

The project is planned to be executed over a 12-month period, with the following key phases and activities:

| Phase            | Key Activities                                             |
| ---------------- | ---------------------------------------------------------- |
| **Months 1–3**   | Procurement, Testing, and Hydrophone deployment           |
| **Months 4–11**  | Data collection                                            |
| **Months 4–10**  | AI training: Vessel classification + sound categorization. |
| **Months 11–12** | Field validation; Stakeholder feedback integration.        |

Given the one-year timeline, a focused approach will be adopted to ensure the delivery of meaningful results. The initial phase will concentrate on procuring and testing the necessary hardware, followed by the deployment of hydrophones at the selected sites. The subsequent months will be dedicated to continuous data collection and the parallel development of AI models for sound classification. The final phase will involve validating the models in the field and integrating feedback from stakeholders to refine the outputs and ensure their practical relevance.




## 7. Budget Considerations

The initial seeding fund provided by the Department of Marine and Coastal Resources (DMCR) for this project is 500,000 THB. This fund is specifically allocated as part of the broader underwater pinnacle survey initiative. This initial budget will primarily cover the costs associated with hardware procurement, initial deployment logistics, and preliminary data collection and analysis efforts. Further funding will be sought to expand the project's scope, particularly for long-term data collection, extensive model development, and comprehensive biodiversity acoustic index calculations.




## 8. Key Stakeholders

The success and impact of this project rely on active engagement and collaboration with various key stakeholders:

1.  **Researchers in Marine Science and Conservation:** These individuals and institutions will be primary users of the open-access sound library and the insights derived from the project. Their expertise will be crucial for data interpretation and application.
2.  **Policymakers in Marine and Coastal Management:** Organizations such as DMCR will directly benefit from the project's findings, which will inform policy development and decision-making related to marine conservation and sustainable resource management.
3.  **Local Coastal Communities:** Engagement with local communities is essential for understanding local ecological knowledge, ensuring community buy-in, and facilitating the long-term sustainability of monitoring efforts. Their livelihoods are directly impacted by the health of marine ecosystems.




## 9. Unresolved Project Design Questions (Annotations)

This section consolidates the key project design questions that require further discussion and decision-making. These questions have been annotated throughout the proposal at relevant sections.

### Data Infrastructure:
- Where to store raw wav data?

### Science / Experiment Design:
- Site and deployment criteria?
- Ecoacoustic problem: what to measure?
- Detection and classification: what to find?
- What is the nominal frequency range of interest?
- What are available resources that could be utilized to fill in the knowledge gaps?
- What are expected to be heard?

### Mechanical / Hydrophone Module Design:
- Where to deploy specifically?
- How to minimize biofouling risk?
- What should be the deployment rig?
- Which brand and model to procure?

### Deployment:
- Data acquisition plan?
- Short deployment to check data quality?
- Diver and boat crew?



