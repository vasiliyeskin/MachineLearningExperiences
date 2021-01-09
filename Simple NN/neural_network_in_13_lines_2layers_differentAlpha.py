import numpy as np

alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]


# подсчитаем нелинейную сигмоиду
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output


# преобразуем результат сигмоиды к производной
def sigmoid_output_to_derivative(output):
    return output * (1 - output)


X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

for alpha in alphas:
    print("\nТренировка с alpha:" + str(alpha))
    np.random.seed(1)

    # случайная инициализация весов со средним 0
    synapse_0 = 2 * np.random.random((3, 4)) - 1
    synapse_1 = 2 * np.random.random((4, 1)) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)

    for j in range(60000):

        # Прямое распространение по уровням 0, 1 и 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # как сильно ошиблись?
        layer_2_error = y - layer_2

        if (j % 10000) == 0:
            print("Error:" + str(np.mean(np.abs(layer_2_error))))

        # в каком направлении цель?
        # уверены ли мы? Если да, то не нужно слишком сильных изменений
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # насколько каждое значение из l1 влияет на ошибку в l2 (в соответствии с весами)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # в каком направлении цель l1?
        # уверены ли мы? Если да, то не нужно слишком сильных изменений
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

        if (j > 0):
            synapse_0_direction_count += np.abs(
                ((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(
                ((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update

        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    print("Synapse 0")
    print(synapse_0)

    print("Synapse 0 Update Direction Changes")
    print(synapse_0_direction_count)

    print("Synapse 1")
    print(synapse_1)

    print("Synapse 1 Update Direction Changes")
    print(synapse_1_direction_count)