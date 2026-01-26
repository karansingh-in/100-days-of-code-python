import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.losses import BinaryCrossentropy

model = Sequential([
    Dense(25, activation='sigmoid'),
    Dense(15, activation='sigmoid'),
    Dense(1, activation='sigmoid')
])

model.compile(loss=BinaryCrossentropy)

model.fit(x,y, epochs=10) # epochs = no. of iteration for gradient descent to run




