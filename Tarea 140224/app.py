import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(42)
data = np.concatenate([np.random.normal(0, 1, (100, 2)),
                       np.random.normal(5, 1, (100, 2)),
                       np.random.normal(10, 1, (100, 2))])

# Definir el número de clusters (k)
k = 3

# Aplicar K-Means
kmeans = KMeans(n_clusters=k)
kmeans.fit(data)

# Obtener los centroides y las etiquetas de los clusters
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualizar los datos y los clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='red')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
