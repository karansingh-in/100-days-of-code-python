import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.losses import BinaryCrossentropy
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data() # digits dataset

filtered_train = (y_train == 0) | (y_train == 1) # extracting only data which have 1 or 0 as label
filtered_test = (y_test == 0) | (y_test == 1)

X_train = X_train[filtered_train]/255.0 # normalising
y_train = y_train[filtered_train] # do not normalise y since they are 0 or 1, you will change the label and the model will not be able to predict it
X_test = X_test[filtered_test]/255.0
y_test = y_test[filtered_test]

model = Sequential([
    tf.keras.layers.Flatten(),   # imp step
    Dense(25, activation='sigmoid'),
    Dense(15, activation='sigmoid'),
    Dense(1, activation='sigmoid')])

model.compile(
    loss=BinaryCrossentropy(),
    metrics=['accuracy']) # imp to print accuracy

model.summary()
model.fit(X_train, y_train, epochs=10, batch_size=64) # epochs = no. of iteration for gradient descent to run
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}")

y_pred = model.predict(X_test)




