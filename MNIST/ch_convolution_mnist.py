import numpy as np
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
import matplotlib.pyplot as plt


print("Загружаю сеть из файлов")
# Загружаем данные об архитектуре сети
json_file = open("convolution_mnist_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель
loaded_model = model_from_json(loaded_model_json)
# Загружаем сохраненные веса в модель
loaded_model.load_weights("convolution_mnist_model.h5")
print("Загрузка сети завершена")


# Компилируем загруженную модель
loaded_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

img_path = "2.jpg"
img = image.load_img(img_path, target_size=(28, 28), grayscale=True)
plt.imshow(img, cmap='gray')
plt.show()

x = image.img_to_array(img)
x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)

# Нейронная сеть предсказывает класс изображения
prediction = loaded_model.predict(x)
# Преобразуем ответ из категориального представления в метку класса
prediction = np.argmax(prediction, axis=1)
# Печатаем результат
print(prediction)
