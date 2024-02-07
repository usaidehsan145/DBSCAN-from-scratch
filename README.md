# DBSCAN (Density-Based Spatial Clustering of Applications with Noise) Implementation

## Overview
This Python script implements the DBSCAN algorithm from scratch and also demonstrates its usage using the `sklearn` library. DBSCAN is a density-based clustering algorithm that is capable of discovering clusters of varying shapes and sizes in a dataset, while also being robust to noise.

## Code Description
1. **DBSCAN Implementation from Scratch**: The script provides an implementation of DBSCAN algorithm from scratch, including functions for calculating Euclidean distance, finding neighbors, expanding clusters, and performing DBSCAN clustering on a dataset.
2. **DBSCAN Using `sklearn`**: Additionally, the script demonstrates how to use the `sklearn` library to perform DBSCAN clustering on random and real-world datasets (e.g., iris dataset). It visualizes the clustering results using matplotlib.

## How to Use
1. To use the DBSCAN implementation from scratch, you can call the `dbscan` function and provide the dataset along with the desired epsilon (`eps`) and minimum samples (`min_samples`) parameters.
2. To use DBSCAN from the `sklearn` library, you need to import `DBSCAN` from `sklearn.cluster`. You can then create a `DBSCAN` object, fit it to your data, and obtain the cluster labels.

## Prerequisites
- Python 3.x
- Basic understanding of clustering algorithms and their parameters.

## Notes
- DBSCAN is particularly useful for datasets with irregular shapes and varying densities.
- Adjusting the `eps` and `min_samples` parameters is crucial for obtaining meaningful clusters.
- While the implementation from scratch provides insights into the working of DBSCAN, the `sklearn` version is more efficient for practical use cases.

Explore different datasets and parameter settings to observe the behavior of DBSCAN in different scenarios.
