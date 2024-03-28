import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Especifica la ruta del archivo .txt
ruta_archivo = 'Tarea 040224\\PARAMETROS_FINALES_CRUDOS.csv'
encoding = 'latin-1'

# Lee el archivo .txt en un DataFrame de Pandas
data = pd.read_csv(ruta_archivo,encoding= encoding, sep=',' )

# Cargar el conjunto de datos Iris

X = data.drop(['species'], axis=1)
y = data['species']

# Aplicar PCA para reducir la dimensionalidad a 4 componentes
pca = PCA(n_components=4)  # Ajusta el número de componentes según tus necesidades
X_pca = pca.fit_transform(X)

# Aplicar K-means al conjunto de datos reducido
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)

# Asignar las etiquetas de los clusters al conjunto de datos original
labels = kmeans.labels_

# Añadir las etiquetas de los clusters al DataFrame original
iris_df = pd.DataFrame(data=X, columns=data.feature_names)
iris_df['Cluster'] = labels

# Visualizar los resultados
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')  # Utilizando un gráfico 3D para visualizar 4 componentes
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=labels, cmap='viridis', s=50)
ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_zlabel('PCA Component 3')
ax.set_title('K-means Clustering with PCA Components')

# Añadir leyenda
legend = ax.legend(*scatter.legend_elements(), title='Clusters')
ax.add_artist(legend)

plt.show()
