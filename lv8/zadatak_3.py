import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from PIL import Image
from keras.models import load_model

model = keras.models.load_model('zadatak_1_model.keras')

def do_prediction(path):
    image = Image.open(path).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image)

    image_array = image_array.astype("float32") / 255
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    predicted_label = np.argmax(model.predict(image_array))
    print(f"Predicted: {predicted_label}")

for i in range(10):
    print("===================================")
    print(f"Testing on number {i}")
    do_prediction(f"tests/test_{i}.png")
    print("===================================")
    print()
