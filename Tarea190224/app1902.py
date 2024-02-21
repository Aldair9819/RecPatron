import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Reducir la dimensionalidad a 2 para visualización
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Crear un clasificador KNN
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo
knn_classifier.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = knn_classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Visualizar el conjunto de datos y las predicciones
plt.figure(figsize=(10, 6))

# Plot puntos de entrenamiento
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=60, label='Train')
# Plot puntos de prueba con predicciones
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis', marker='X', s=100, label='Test Predictions')

plt.title('KNN Classifier - Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()


