# ai_training.py
import tensorflow as tf
import numpy as np

# Load and preprocess the data
x_train, y_train = load_data('./data/training_data.csv')
x_test, y_test = load_data('./data/test_data.csv')

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
