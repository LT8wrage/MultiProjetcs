import idx2numpy # convert idx files into numpy arrays (images and labels)
import os #to set up the base path of the file 
import keras
import matplotlib.pyplot as plt #image visualisation
import tensorflow as tf
from keras import models, layers
import numpy as np


base_path = os.path.dirname(__file__) #setting the base path to the file's path to avoid further problems regarding the path

x_train = idx2numpy.convert_from_file(
    os.path.join(base_path, 'train-images.idx3-ubyte')
)

y_train = idx2numpy.convert_from_file(
    os.path.join(base_path, 'train-labels.idx1-ubyte')
)

x_test = idx2numpy.convert_from_file(
    os.path.join(base_path, 't10k-images.idx3-ubyte')
)

y_test = idx2numpy.convert_from_file(
    os.path.join(base_path, 't10k-labels.idx1-ubyte')
)
#converting data bases into code readable images and propts


x_train = x_train / 255.0
x_test = x_test / 255.0
#normalising images so it can give us a value between 0 and 1 for easier manipulation while working with neurons

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc*100:.2f}%")

model_save_path = os.path.join(base_path, 'my_model.keras')
keras.saving.save_model(model, model_save_path)
