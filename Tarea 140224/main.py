import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import makeblobs

#Generar datos sintéticos
X,  = makeblobs(n_samples=1000, centers=4, cluster_std=0.60, random_state=0)

#Aplicar el algoritmo de k-means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

#Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')


#Visualizar los centroides
centers = kmeans.cluster_centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.show()