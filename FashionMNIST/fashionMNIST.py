# dataset of models
from tensorflow.keras.datasets import fashion_mnist
# модель нейронной сети с последовательным соединением нейронов
from tensorflow.keras.models import Sequential
# подключаем полносвязную нейронную сеть (dense)
from tensorflow.keras.layers import Dense
# утилиты для keras
from tensorflow.keras import utils

# отрисовка изображений
import matplotlib.pyplot as plt


# Загрузка данных
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Преобразование размерности изображения (из картинки в плоскую последовательность "плоский вектор")
x_train = x_train.reshape(60000, 784)
# Нормализуем данные: делим на 255 градаций серового. Таким образом данные будут в диапазоне от нуля до 1
x_train /= 255

# Преобразуем метки в формат one hot encoding
y_train = utils.to_categorical(y_train, 10)

# Работа с правильными ответами

# Правильный ответ в формате one hot encoding

# классификация выходных данных
classes = ['футболка', 'брюки', 'свитер', 'платье', 'пальто', 'туфли', 'рубашка', 'кроссовки', 'сумка', 'ботинки']

# примеры изображений
plt.figure(figsize=(10,10))
for i in range(100,150):
    plt.subplot(5,10,i-100+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(classes[y_train[i]])

