import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Función para inicializar los pesos de la red de manera aleatoria
def initialize_weights(input_size, hidden_size, output_size):
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    return weights_input_hidden, weights_hidden_output

# Función de entrenamiento de la red
def train(X, y, learning_rate, epochs):
    input_size = X.shape[1]
    hidden_size = 4
    output_size = 1

    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

    for epoch in range(epochs):
        # Capa de entrada a capa oculta
        hidden_layer_input = np.dot(X, weights_input_hidden)
        hidden_layer_output = sigmoid(hidden_layer_input)

        # Capa oculta a capa de salida
        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
        predicted_output = sigmoid(output_layer_input)

        # Calcular el error
        error = y - predicted_output

        # Retropropagación
        output_delta = error * sigmoid_derivative(predicted_output)
        hidden_layer_error = output_delta.dot(weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

        # Actualizar pesos
        weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
        weights_input_hidden += X.T.dot(hidden_layer_delta) * learning_rate

    return weights_input_hidden, weights_hidden_output

# Función de predicción
def predict(X, weights_input_hidden, weights_hidden_output):
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    return predicted_output

# Ejemplo de uso
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

learning_rate = 0.1
epochs = 10000

trained_weights_input_hidden, trained_weights_hidden_output = train(X_train, y_train, learning_rate, epochs)

# Predicción en nuevos datos
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = predict(X_test, trained_weights_input_hidden, trained_weights_hidden_output)

print("Predicciones:")
print(predictions)
