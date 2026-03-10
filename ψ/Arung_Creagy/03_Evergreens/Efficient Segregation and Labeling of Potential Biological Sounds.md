---
parent: "[["
tags:
  - Bioacoustics
  - Underwater_Acoustics
date: 2025-06-19T22:04:00
---
The concept of **Efficient Segregation and Labeling of Potential Biological Sounds** refers to a novel methodology designed to detect and categorize sound events in long-term underwater recordings with significantly reduced human input. This approach is particularly useful in environments where many sound sources are unidentified, aiming to provide insight into recurrent sound sources and their spatio-temporal patterns.

The methodology is inspired by how human annotators screen for unidentified sounds, by first looking at temporal-spectral shape, duration, and frequency limits on a spectrogram before assigning labels.

The multi-step approach involves:

1. **Deep Learning Object Detection (YOLOv8)**: An object detection algorithm, typically used in computer vision, is retrained to detect any short acoustic event by converting audio into spectrograms using sliding windows that are longer than the expected sound events. This allows for the detection of multiple simultaneous events and provides their time and frequency limits.
2. **Active Learning Approach**: To minimize the human effort required for manual annotation, an active learning approach selects the most "informative" audio files for manual annotation in an iterative process. This method helps to enrich the training dataset more efficiently than random file selection.
3. **Feature Extraction with BioLingual Model**: Detected events are converted into a multidimensional embedded feature space using the pre-trained BioLingual model, which is designed for classifying different biological sounds.
4. **Unsupervised Clustering**: The extracted high-dimensional features are reduced to a smaller feature space using UMAP (Uniform Manifold Approximation and Projection) to address the "curse of dimensionality." These reduced features are then clustered in an unsupervised manner using HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise), aiming to group similar sound events into sound classes.
5. **Manual Revision of Clusters**: The resulting sound classes are manually reviewed to assign labels and potential sources. Temporal patterns of the obtained clusters are then plotted to aid in source identification and provide insight into soundscape dynamics.

**Advantages of this methodology include**:

- **Reduced Human Effort and Time Savings**: The method significantly reduces the time and labor bioacousticians spend manually screening long acoustic recordings and annotating sound events, even when the sounds are unknown or sparse. This allows for a more targeted analysis.
- **Automated Detection and Categorization**: It automates the detection and initial categorization of acoustic events, making it possible to analyze large volumes of Passive Acoustic Monitoring (PAM) data.
- **Handling Unknown Sounds**: It provides a framework to monitor soundscapes regardless of whether the sound sources are known or not, which is crucial for poorly described environments. Documenting these sounds before identification establishes a baseline for their presence and aids in later source identification.
- **Detection of Simultaneous and Variable Events**: The object detection approach can effectively detect multiple sound events happening simultaneously in different frequency bands and can handle signals of varying lengths, which is difficult for traditional segmentation methods.
- **Robustness Across Environments**: The detection model has proven robust across different locations and ecosystems, performing well even on data from unseen environments like freshwater, indicating its generalizability.
- **Improved Training Efficiency**: The active learning approach leads to faster improvement in model performance compared to random sampling, especially when human annotation time is limited, by selecting more acoustically complex and diverse files for annotation.
- **Ecological Insight**: It enables the characterization and quantification of unknown sound events, which can be used as a proxy for biodiversity and ecosystem health. The analysis of spatio-temporal patterns of sound types provides ecological information even without identified sources.
- **Foundation for Future Research**: It contributes to filling the knowledge gap on sound types and facilitates the creation of databases of well-described unidentified sounds that can serve as future references.

