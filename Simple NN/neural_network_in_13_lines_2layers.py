import numpy as np


# подсчитаем нелинейную сигмоиду
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output


# преобразуем результат сигмоиды к производной
def sigmoid_output_to_derivative(output):
    return output * (1 - output)


# входные данные
X = np.array([[0, 1],
              [0, 1],
              [1, 0],
              [1, 0]])

# выходные данные      
y = np.array([[0, 0, 1, 1]]).T

# сделаем случайные числа детерминированными
np.random.seed(1)

# случайная инициализация весов со средним 0
synapse_0 = 2 * np.random.random((2, 1)) - 1

for iter in range(10000):
    # прямое распространение
    layer_0 = X
    layer_1 = sigmoid(np.dot(layer_0, synapse_0))

    # как сильно ошиблись?
    layer_1_error = layer_1 - y

    # умножим ошибку на уклон сигмоиды 
    # со значениями в l1
    layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
    synapse_0_derivative = np.dot(layer_0.T, layer_1_delta)

    # обновим веса
    synapse_0 -= synapse_0_derivative

print("Вывод после тренировки:")
print(layer_1)