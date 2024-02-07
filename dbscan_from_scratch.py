# -*- coding: utf-8 -*-
"""DBSCAN_from_Scratch

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OEVXN5RxN-lV4N95H9RHmcmbmdU-9j-_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
import math

drive.mount('/content/drive', force_remount = True)
iris_directory = '/content/drive/MyDrive/irisData/iris.data'

dataset = pd.read_csv(iris_directory, header = None)
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset.columns = column_names

# data pre-processing to remove/handle missing/null/duplicate values if any

dataset.dropna()  # remove all the missing values and return the new series

#check for null values

if dataset.isnull().values.any():
    print("The dataset contains null values.")
else:
    print("The dataset does not contain null values.")

#check for duplicates

dataset.drop_duplicates()

if dataset.duplicated().any():
      print("The dataset contains duplicate values.")
else:
    print("The dataset does not contain duplicate values.")

# data visualization

# print the whole file
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(dataset)

# print max number of rows and columns
# num_rows = dataset.shape[0]
# num_columns = dataset.shape[1]

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)

import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Generate random dataset
np.random.seed(0)
n_samples = 200
centers = [[-1, -1], [0, 0], [1, 1]]
X = []
for i in range(len(centers)):
    X.extend(np.random.randn(n_samples, 2) + centers[i])
X = np.array(X)

# Perform DBSCAN clustering
db = DBSCAN(eps=0.3, min_samples=5).fit(X)
labels = db.labels_

# Plot the resultant graph
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]  # Black color for outliers
    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    plt.scatter(xy[:, 0], xy[:, 1], color=tuple(col), label='Cluster {}'.format(k))

plt.legend()
plt.title('DBSCAN Clustering Result')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Generate random dataset
np.random.seed(0)
n_samples = 200
centers = [[-1, -1], [0, 0], [1, 1]]
X = []
for i in range(len(centers)):
    X.extend(np.random.randn(n_samples, 2) + centers[i])
X = np.array(X)

# Perform DBSCAN clustering
db = DBSCAN(eps=0.3, min_samples=5).fit(X)
labels = db.labels_

# Plot the initial dataset
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1])
plt.title('Initial Dataset')
plt.xlabel('X')
plt.ylabel('Y')

# Plot the resultant graph
plt.subplot(122)
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]  # Black color for outliers
    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    plt.scatter(xy[:, 0], xy[:, 1], color=tuple(col), label='Cluster {}'.format(k))

plt.legend()
plt.title('DBSCAN Clustering Result')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def dbscan(X, eps, min_samples):
    labels = np.zeros(len(X))
    cluster_label = 0

    for i, x in enumerate(X):
        if labels[i] != 0:
            continue

        neighbors = find_neighbors(X, x, eps)
        if len(neighbors) < min_samples:
            labels[i] = -1  # Mark as noise
        else:
            cluster_label += 1
            expand_cluster(X, labels, i, neighbors, cluster_label, eps, min_samples)

    return labels

def find_neighbors(X, x, eps):
    neighbors = []
    for i, neighbor in enumerate(X):
        if euclidean_distance(x, neighbor) <= eps:
            neighbors.append(i)
    return np.array(neighbors)

def expand_cluster(X, labels, x_idx, neighbors, cluster_label, eps, min_samples):
    labels[x_idx] = cluster_label

    i = 0
    while i < len(neighbors):
        neighbor_idx = neighbors[i]
        if labels[neighbor_idx] == -1:
            labels[neighbor_idx] = cluster_label
        elif labels[neighbor_idx] == 0:
            labels[neighbor_idx] = cluster_label
            x_neighbor = X[neighbor_idx]
            neighbor_neighbors = find_neighbors(X, x_neighbor, eps)
            if len(neighbor_neighbors) >= min_samples:
                neighbors = np.concatenate((neighbors, neighbor_neighbors))
        i += 1

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Considering only the first two features for visualization purposes

# Set DBSCAN hyperparameters
eps = 0.5
min_samples = 5

# Perform DBSCAN clustering
labels = dbscan(X, eps, min_samples)

# Plot the original dataset
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=iris.target)
plt.title('Original Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Plot the clustered dataset
plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title('DBSCAN Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def knn(X_train, y_train, X_test, k):
    predictions = []
    for x_test in X_test:
        distances = [euclidean_distance(x_test, x_train) for x_train in X_train]
        sorted_indices = np.argsort(distances)
        k_nearest_labels = [y_train[i] for i in sorted_indices[:k]]
        prediction = max(set(k_nearest_labels), key=k_nearest_labels.count)
        predictions.append(prediction)
    return np.array(predictions)

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Considering only the first two features for visualization purposes
y = iris.target

# Split the dataset into training and test sets
train_size = 100
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# print(y_train)
# print("/////////////////////////")
# print(y_test)

# Set the value of k for KNN
k = 3

# Perform KNN classification on the test set
y_pred = knn(X_train, y_train, X_test, k)
print("PREDICTED VALUES ARE")
print(y_pred)
print(type(y_pred))

# Plot the original dataset
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Original Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Plot the classification result
plt.subplot(122)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred)
plt.title('KNN Classification Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()