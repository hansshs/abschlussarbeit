import numpy as np
from tensorflow import keras
import time

# Load the dataset
data = np.load(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Sandbox\data_party1.npz")
x_train, y_train = data['x_train'], data['y_train']
x_test, y_test = data['x_test'], data['y_test']
print(len(x_train), len(y_train))
# Define your model architecture
model = keras.models.load_model(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\monolythic\compiled_keras.h5")

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Measure training time
start_time = time.time()

# Train the model
model.fit(x_train, y_train, epochs=20, batch_size=128, validation_data=(x_test, y_test))

# Compute training time
end_time = time.time()
training_time = end_time - start_time
print(f"Training time: {training_time} seconds")

# Save the trained model to .h5 format
model.save('trained_model.h5')