import os #to set up the base path of the file 
import keras
from keras import models, layers
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0
base_path = os.path.dirname(__file__) #setting the base path to the file's path to avoid further problems regarding the path

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax') #comnverts values into probabilities
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=5)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc*100:.2f}%")

model_save_path = os.path.join(base_path, 'my_model.keras')
keras.saving.save_model(model, model_save_path)
