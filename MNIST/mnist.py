import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# Устанавливаем seed для повторяемости результатов
numpy.random.seed(42)