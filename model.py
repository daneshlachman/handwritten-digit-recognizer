from keras.datasets import mnist
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
print(train_data.shape)

plt.figure()
plt.imshow(train_data[0])
plt.colorbar()
plt.grid(False)
plt.show()
# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10)
# ])
#
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])
#
# model.fit(train_data, train_labels, epochs=7)
# test_loss, test_acc = model.evaluate(test_data, test_labels, verbose=2)
#
# print(test_acc, test_loss)


