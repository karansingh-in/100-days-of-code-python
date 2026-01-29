import tensorflow as tf

(X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train/255.0
X_test = X_test/255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(25, activation='relu'),
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy']
)

model.fit(X_train, Y_train, epochs=10, batch_size=128)

test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=0)
print(f"Test accuracy: {test_acc*100:.4f} %")

y_pred = model.predict(X_test)

# this is normally 
# Test accuracy: 95.7500 %

# this is after increasing number of layers form 3 to 4 with 15 neurons
# Test accuracy: 95.9100 %

# this is after increasing number of layers form 4 to 5 with 15 neurons
# Test accuracy: 95.5200 %

# this is after changing hidden layer activation from relu to softmax
# Test accuracy: 85.7000 %

