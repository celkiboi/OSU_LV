from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential()
model.add(layers.Input(shape=(100,100,3)))
model.add(layers.Conv2D(10, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(15, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(100, activation="relu"))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(10, activation="softmax"))

my_callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", patience = 12, verbose = 1),
    keras.callbacks.TEnsorBoard(log_dir = 'logs/cnn', update_freq = 100)
]

model.fit(X_train_n, y_train, epochs = 50, batch_size = 64, callbacks = my_callbacks, validation_split = 0.1)