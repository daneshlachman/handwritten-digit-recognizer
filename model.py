from keras.datasets import mnist
import tensorflow as tf
import numpy as np


class Model:
    def __init__(self):
        self.model = None
        self.probability_model = None
        self.number_of_epochs = 2

    def define_and_train_model(self):
        # loading the MNIST dataset for handwritten digits
        (train_data, train_labels), (test_data, test_labels) = mnist.load_data()

        # defining the model
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

        # compiling the model
        self.model.compile(optimizer='adam',
                           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                           metrics=['accuracy'])

        # training the model with MNIST dataset
        self.model.fit(train_data, train_labels, epochs=self.number_of_epochs)
        test_loss, test_acc = self.model.evaluate(test_data, test_labels, verbose= 0)

        self.probability_model = tf.keras.Sequential([self.model,
                                                      tf.keras.layers.Softmax()])
        # print test accuracy
        print(test_acc)

    def make_prediction(self, predicting_image):
        # reshape data so that it satisfies with the flattened input layer, and then make a prediction
        reshaped_predicting_image = np.reshape(predicting_image, (1, 784))
        prediction = np.argmax(self.probability_model.predict(reshaped_predicting_image))
        predication_percentage = self.probability_model.predict(reshaped_predicting_image)[0][prediction] * 100
        return prediction, predication_percentage

