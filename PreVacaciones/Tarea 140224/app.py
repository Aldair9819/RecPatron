import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
from flask_cors import cross_origin
app = Flask(__name__.split('.')[0])
app.config['SAVE_DIR'] = 'instance/uploads'
# Generar datos de ejemplo

#Defaults
@app.route('/')
def home():
    """
    Página inicial
    """
    return "<h1>Bienvenidos a ApiPersonText v0.11<h1>"

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
