import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

    # Cargar el conjunto de datos Iris
    iris = load_iris()
    X = iris.data[:, :2]  # Tomar solo las dos primeras características para la visualización
    y = iris.target

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un clasificador k-NN con k=3
    knn_classifier = KNeighborsClassifier(n_neighbors=3)

    # Entrenar el clasificador con los datos de entrenamiento
    knn_classifier.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = knn_classifier.predict(X_test)

    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")

    # Visualizar los datos y las regiones de decisión
    sns.set(style="white", palette="muted")

    # Crear una malla para visualizar las regiones de decisión
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Realizar predicciones en la malla
    Z = knn_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Visualizar las regiones de decisión
    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

    # Visualizar los puntos de datos
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y], palette="Set1", edgecolor="k", s=100)
    plt.title("Regiones de decisión del clasificador k-NN")
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.show()
