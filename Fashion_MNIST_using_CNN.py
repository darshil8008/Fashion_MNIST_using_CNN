# -*- coding: utf-8 -*-
"""Fashion_MNIST_using_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bb_CDckEIjRgXzBGEYqMvagyrVNanhSn

# Importing necessary libraries
"""

import tensorflow as tf
import matplotlib.pyplot as plt
from time import time

"""# Load the dataset"""

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

"""# Show few images"""

fig, axes = plt.subplots(nrows=2, ncols=6, figsize=(15, 5))
ax = axes.ravel()
for i in range(12):
    ax[i].imshow(training_images[i].reshape(28, 28))

plt.show()

"""# Reshaping the images for feeding into the neural net"""

training_images = training_images / 255.0
test_images = test_images / 255.0

"""# Creating the model"""

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

"""# Compile the model"""

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

"""# Train the model"""

t1 = time()
model.fit(training_images, training_labels, epochs=10)
t2 = time()

"""# Print the time taken for training"""

print("\nTraining wall clock time: {} seconds\n".format(round(t2 - t1, 3)))

"""# Compute accuracy of the model on the test/validation set"""

test_loss = model.evaluate(test_images, test_labels)
print("\nTest accuracy: ", test_loss[1])

"""# Adding convolution and pooling layers"""

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model2 = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model2.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model2.summary()

t1 = time()
history = model2.fit(training_images, training_labels, epochs=5)
t2 = time()

plt.plot(history.history['accuracy'], c='k', lw=2)
plt.grid(True)
plt.xlabel("Epochs", fontsize=15)
plt.ylabel("Training accuracy", fontsize=15)
plt.ylim(0.9, 1.0)
plt.show()

print("\nTraining wall clock time: {} seconds\n".format(round(t2 - t1, 3)))

test_loss = model.evaluate(test_images, test_labels)
print("\nTest accuracy: ", test_loss[1])