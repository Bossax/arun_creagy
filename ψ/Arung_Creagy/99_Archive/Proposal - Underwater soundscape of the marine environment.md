
## 1. Executive Summary

This proposal outlines a project aimed at characterizing the underwater soundscapes of Thailand's coastal waters. The initiative seeks to address the critical need for innovative, scalable, and cost-effective monitoring solutions to combat threats to marine biodiversity and livelihoods from unsustainable human activities. The project will establish an open-access underwater sound database from selected location of Thailand’s coast, develop machine learning models for sound classification, and demonstrate the utility of acoustic data in complementing existing environmental monitoring techniques. This foundational research will contribute to marine conservation and management efforts by providing baseline knowledge of the acoustic characteristics of the marine environment and enabling authorities and researchers the detection of potentially harmful activities.

## 2. Introduction and Background

Thailand's coastal ecosystems are vital for both biodiversity and human well-being, supporting diverse marine life and providing livelihoods for millions. However, these ecosystems face significant threats from various human activities, including over-tourism and destructive fishing practices. Traditional methods for monitoring marine environments, such as vessel-based surveys, are often expensive, labor-intensive, and limited in their spatial and temporal coverage. This necessitates the search of complementary monitoring approaches to enhance our knowledge of the ecosystem.

Passive acoustic monitoring (PAM) offers a promising solution by providing a non-invasive and continuous method for observing marine environments. Underwater soundscapes, which encompass all sounds within a marine environment, can reveal crucial information about biological activity, geological processes, and anthropogenic activities. By analyzing these soundscapes, researchers can gain insights into ecosystem health, species presence, and human disturbances.

This project builds upon the recognition of the urgent need for enhanced marine monitoring capabilities in Thailand for a more sustainable management practice in the future. This project pioneers the ocean acoustics research in the country and establishes solid a foundation for long-term capacity building.   

## 3. Project Goals and Objectives

The goal of this project is to gain the understanding of the characteristics of underwater soundscapes of Thailand's coast to support marine conservation and management. This will be achieved through the following specific objectives

1. **Demonstrate the Use of Acoustic Data for Biodiversity and Marine Animal Monitoring:** Showcase how acoustic data can complement existing survey techniques done by marine biologists. This includes inferring environmental changes from the changes in soundscape, exploring the temporal patterns of biological acoustic features, and gaining fundamental understanding of spatial variation within a habitat.
2. **Develop Machine Learning Models for Detection and Classification:** Create and train machine learning models capable of clustering underwater sounds of similar patterns and detecting surface vessel presence. The model can also detect and classify the type of surface vessel from its sound. These models will enable automated analysis of large datasets of underwater sounds in the future
3. **Develop an Open-Access Underwater Sound Data Database:** Establish an open-access database of underwater acoustic data collected from the site. The repository will include clusters of sounds of the same patterns with labels from the best available knowledge and sounds of different types of surface vessels.

## 4. Methodology

### 4.1 Hardware Development

The project will commence with the development of a hydrophone rig. The rig will be constructed using commercially available hydrophones and integrated with mechanical structures to ensure durability in the field. The selection criteria for the hydrophone are based on the expected frequency range of the acoustic signal of interest and the constraints of the field trips to retrieve the data, such as the availability of professional divers at the site. The design of the rig will be influenced by the specificity of the deployment sites and the maintenance plan.

The hydrophone will be tested to ensure accuracy in data sampling and functionality before deployment.

In addition to the hydrophone rig, an onshore camera module will be installed near the hydrophone locations. The camera will take images of passing surface vessels in hydrophone proximity. The camera module will be designed to be hazard-proofed and remotely controlled. The images from the camera can complement the acoustic data to make the labelling process more reliable for the machine learning training process.


### 4.2 Acoustic Data Collection

Three hydrophones will be deployed at the selected site where existing data collection routines are in place (eg. site survey, water sampling), allowing for cross-referencing and validation of acoustic data with other environmental parameters. The deployment of multiple hydrophones is necessary to capture acoustic variations within the habitat. The separation distances between hydrophones will be determined by the a priori knowledge of the chosen habitat, such as ecological gradient and surrounding persistent human activities.

Preliminary data collection will be conducted to assess the promise of the selected locations. Two configurations for hydrophone locations will be created. For each configuration, data collection will be conducted to obtain 48 hours of records. The records from each configuration will then be assessed to determine the deployment configuration of the study. The selection criteria include the range of sound pressure levels, noise levels, and the presence of acoustic features of interest, for example.

When the hydrophone locations are finalized, continuous underwater recordings will commence over a period of at least six months to capture seasonal variations in biological and human activities. Data will be gathered from the deployment sites every month, depending on the weather conditions and team availability.


### 4.3 Data Analysis

**4.3.1 Machine Learning Model Development**

Collected acoustic data will undergo a rigorous analysis process, beginning with sound data pseudo-labeling. This involves clustering acoustically similar events through feature extraction from spectrograms image, starting from utilize dimensionality reduction techniques (e.g., UMAP), and then perform density-based clustering (e.g., HDBSCAN) to group the similar sound pattern. Some known sound that have open-data available such as various type of boat, can be confirm with the similarity retrieval technique (utilize foundational model for data embedding process)

Potential vessel sound clusters will be identified based on their acoustic characteristics, and auxiliary data such as AIS ship tracks, camera imagery, and satellite imagery will be used to assign specific vessel-type labels if needed (e.g., trawler, speedboat).

Sound clusters will be further labeled by expert analysts through auditory and visual inspection, cross-referencing with other available data sources (e.g., visual data, weather radar, seismic activity data, other underwater sound libraries). The goal is to identify potential sources of sound clusters, specifying whether they are biological, geological, or atmospheric, and to pinpoint exact sources or processes where _possible_. Criteria for sound source identification will be developed to systematically build the sound database with traceable uncertainties.

Subsequently, classification models will be developed and trained using the vessel-labeled events and categorized soundscapes. The performance of these models will be tested with additional collected data to ensure accuracy and robustness. More over than that, this trained model can be also use as foundational model for sound embedding generation for Thailand marine space.


**4.3.2 Soundscape Characterization and Baseline Establishment**

Characterization of the underwater soundscape involves these acoustic features and parameters

1. Overall Long-Term Power Spectral Density (LT-PSD):
    
    The power spectral density of an appropriate time window (e.g. 5-min length) of the record will be computed. The distribution of spectral power levels of each 1/3 octave band will be calculated.
    
2. Biological background noise - fish chorus power spectral density
    
    the machine learning model will separate the biological background noise - or fish chorus - from anthropogenic transient sources, geological transient sources, and biological transient sounds. The power spectral density of the fish chorus within an time unit will be computed. This time unit is different from the time unit for the overall LT-PSD.
    
3. Transient sounds:
    
    1. Biological sound: distinct transient biological sounds will be clustered to form a bioacoustic repository.
    2. Geological sound:
    3. Anthropogenic sound
        1. Surface vessel
4. Acoustic indices:
    
    Intensity index and diversity index of the biological sound (background noise and transient sounds) in each appropriate time window will be calculated for the selected range of frequency bands.
    
5. Surface vessel sound:
    
    The events of a surface vessel passing the site will be recorded. The acoustic data will be labeled with the help of the imagery data from the surface camera.
    
6. Temporal patterns of the acoustic variables:
    
    The next step is to establish a linkage between the soundscape characteristics mentioned above with the changes in the surrounding environments. This step combines data collected at the site from other sources such as
    
    1. Imagery data from the surface camera
    2. Temperature and salinity of the seawater
    3. Wind and rain data
    4. Visual Biological Surveys
    5. Economic activity
    
    Analysis techniques such as statistical testing, regression, and frequency analysis will be applied to understand the temporal patterns and correlations of the
    
7. Spatial replication
    
    Analysis on the differences among the records of different hydrophones will be conducted. The result will sheds some light on spatial patterns of the habitat
    

### **4.5 Data Repository Development and Deployment**

To manage the significant volume of acoustic data generated by the hydrophone network, we propose a robust and scalable cloud-based data architecture. This architecture is designed to handle the entire data lifecycle, from raw ingestion to curated public release, while ensuring data integrity, security, and accessibility for researchers and machine learning practitioners.

To handle the initial intake of large, unprocessed raw data, a more foundational storage solution is required. Our proposed architecture consists of a three-stage pipeline:

**Stage 1: Raw Data Ingestion and Archival Storage**

We will leverage a cloud object storage solution as our primary data lake.

- **Technology:** We will utilize a secure, cost-effective object storage service such as **Google Cloud Storage (GCS)** or **Amazon S3 (Simple Storage Service)** on free tier. These services offer virtually unlimited scalability, high durability, and are optimized for storing large, unstructured data.
- **Process:**
    1. Raw audio files (in `.wav` format or converted to lossless `.flac` for ~40-60% size reduction) will be automatically uploaded from the hydrophone data loggers to a designated "raw-data" bucket.
    2. Each audio file will be accompanied by a corresponding metadata file (e.g., in JSON format). This file will capture all surrounding environmental and operational data, including:
        - Precise GPS Coordinates (Latitude, Longitude)
        - Coordinated Universal Time (UTC) timestamp of recorded sound
        - Date-time of data retrieved
        - Hydrophone Device ID
        - Water temperature, salinity, and depth (if available)
        - Recording settings (e.g., sample rate, bit depth)
- **Structure:** Data will be organized chronologically and by source for easy querying (e.g., `gs://bucket-name/raw/device-01/2025/07/23/`).

**Stage 2: Data Processing and Curation**

Raw data is often too large and noisy for direct use in analysis or model training. This stage transforms the raw archive into a structured and analysis-ready collection.

- **Technology:** An event-driven processing pipeline will be implemented using serverless functions (**Google Cloud Functions** or **AWS Lambda**). These functions will automatically trigger whenever a new raw audio file is uploaded to the storage bucket.
- **Process:**
    1. **Validation:** Check files for corruption and completeness.
    2. **Preprocessing:**
        - Noise reduction or filtering using standard acoustic libraries.
        - Normalization of audio levels.
    3. **Segmentation:** Long multi-hour recordings will be segmented into smaller, uniform chunks (e.g., 5-10 seconds). This is critical for creating manageable samples for machine learning models.
    4. **Initial Feature Extraction:** For each segment, we can pre-compute common audio features like spectrograms or Mel-Frequency Cepstral Coefficients (MFCCs) and store them.
- **Output:** The processed segments, their extracted features, and enriched metadata will be saved to a separate "processed-data" bucket in the cloud storage. This curated data forms the basis for the final public dataset.

**Stage 3: Public Dataset Deployment and Egress**

This stage focuses on making the curated data accessible to the broader scientific and AI community, fulfilling the original goal.

- **Technology:** We will use the **Hugging Face Hub** (specifically, the `datasets` library) as our primary platform for data deployment.
- **Process:**
    1. Periodically, a versioned, well-documented dataset will be compiled from the "processed-data" bucket.
    2. This dataset, including the segmented audio clips and rich metadata, will be uploaded to a dedicated Hugging Face repository.
    3. A comprehensive "dataset card" (README) will be created, detailing the data collection methodology, structure, fields, potential biases, and providing code snippets for easy loading and use.
- **Benefits:**
    - **Accessibility:** Researchers can stream or download the data with a single line of code.
    - **Interoperability:** Seamless integration with popular ML frameworks like PyTorch and TensorFlow.
    - **Collaboration:** The platform facilitates community discussion, annotation, and model sharing.

**Data Versioning and Governance**

A systematic approach to data versioning is essential for reproducibility.

- **Raw Data:** The versioning feature of the cloud object storage (GCS/S3) will be enabled to track all changes and prevent accidental deletion.
- **Processed Data:** Datasets published on Hugging Face will be version-controlled using its underlying Git-based system. New releases of the dataset will be tagged with semantic version numbers (e.g., v1.0, v1.1, v2.0).

By implementing this multi-stage architecture, we create a robust data infrastructure that efficiently manages large-scale raw acoustic data while providing the scientific community with a high-quality, accessible, and analysis-ready resource. This addresses the need for secure storage, efficient processing, and systematic data egress.

## 5. Expected Outputs and Outcomes

This project is anticipated to yield several key outputs and contribute to significant outcomes for marine conservation and management in Thailand:

### Expected Outputs:

1. **Baseline Acoustic Features and Patterns of the Soundscape:** Summary of the soundscape characteristics, including informative acoustic features, acoustic parameters, and analysis of the temporal variations correlated with the environment’s dynamics.
2. **Open-Access Thai Underwater Sound Library with Labeled Datasets:** A publicly accessible database of underwater acoustic recordings for scientific studies and labeled sound clusters. The surface vessel sound sub-library will include sounds of vessel archetypes and images.
3. **Trained AI Models for Sound Classifications:** Robust machine learning models capable of detecting and classifying various underwater sounds and surface vessel types.
4. **System Design Documentation for Hardware and Data Analysis Workflow:** Detailed documentation outlining the design and construction of the hydrophone modules and the workflow for data analysis model development
5. **Reports and Presentations for Stakeholders:** Regular reports and presentations, including case studies and practical recommendations, demonstrating how acoustic monitoring can be integrated into existing marine management frameworks.

### Expected Outcomes and Impact:

1. **Increased Awareness of Acoustic Monitoring:** The project will raise awareness among marine biologists, conservationists, and policymakers regarding the importance and utility of acoustic monitoring as a tool for environmental monitoring.
2. **Enhanced Marine Conservation and Management:** By providing new insights into marine soundscapes and human impacts, the project will contribute directly to more informed and effective conservation strategies and management decisions.
3. **Proof of Concept for Acoustic Analysis:** The project will demonstrate the practical application of acoustic parameters, and ship sound detection as valuable analytical tools.
4. **Leveraging Open Access Databases:** The project will showcase the integration of open-access databases like 'Hear my ship' and 'Fish sounds' to enrich data analysis and model development.

## 6. Timeline

The project is planned to be executed over a 12-month period, with the following key phases and activities:

|Phase|Key Activities|
|---|---|
|**Months 1–3**|Procurement, Testing, and Hydrophone deployment|
|**Months 4–11**|Data collection|
|**Months 5–10**|AI training: Vessel classification + sound categorization.|
|**Months 9–12**|Field validation; Stakeholder feedback integration.|

Given the one-year timeline, a focused approach will be adopted to ensure the delivery of meaningful results. The initial phase will concentrate on procuring and testing the necessary hardware, followed by the deployment of hydrophones at the selected sites. The subsequent months will be dedicated to continuous data collection and the parallel development of AI models for sound classification. The final phase will involve validating the models in the field and integrating feedback from stakeholders to refine the outputs and ensure their practical relevance.

## 7. Budget

The initial seeding fund provided by the Department of Marine and Coastal Resources (DMCR) for this project is 500,000 THB. This fund is specifically allocated as part of the broader underwater pinnacle survey initiative. This initial budget will primarily cover the costs associated with hardware procurement, initial deployment logistics, and preliminary data collection and analysis efforts. Further funding will be sought to expand the project's scope, particularly for long-term data collection, extensive model development, and comprehensive biodiversity acoustic index calculations.

| Category                | Description                                 | Estimated Cost (THB) | Output                          |
| ----------------------- | ------------------------------------------- | -------------------- | ------------------------------- |
| Hydrophone              | 3 commercially available hydrophones        | 280,000              | Tax-included hydrophones        |
| Mechanical Rig          | Mechanical structure of the hydrophone rigs | 80,000               | Ready-to-deploy hydrophone rigs |
| Deployment & Field Work | Travel allowance and accommodation          | 20,000               |                                 |
| Data Infrastructure     |                                             | 20,000               | Data repository                 |
| Data Analysis           | Data analysis and report                    | 100,000              | Presentation<br>Study report    |
