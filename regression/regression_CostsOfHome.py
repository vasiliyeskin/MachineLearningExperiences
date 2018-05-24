import numpy as np

from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense

# Загрузка набора данных
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# Нормализация данных
# Среднее значение
mean = x_train.mean(axis=0)
# Стандартное отклонение
std = x_train.std(axis=0)
x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

# Создаем сеть
# Выходной слой с одним линейным нейроном - для задачи регрессии функция активации не используется.
# Функция ошибки - среднеквадратичное отклонение. Метрика - среднее абсолютное отклонение.

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Обучение сети
model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=2)




# Оценка точности работы сети
mse, mae = model.evaluate(x_test, y_test, verbose=0)

print("Средняя абсолютная ошибка (тысяч долларов):", mae)

# Использование сети для предсказания цен недвижимости
pred = model.predict(x_test)
print("Предсказанная стоимость:", pred[1][0], ", правильная стоимость:", y_test[1])