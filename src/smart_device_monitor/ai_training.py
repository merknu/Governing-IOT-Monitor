# ai_training.py
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier

def train_ai(X, y):
    # Train the AI on the given data using a multi-layer perceptron classifier
    mlp = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=500, alpha=0.0001,
                        solver='sgd', verbose=10, tol=1e-4, random_state=1,
                        learning_rate_init=.1)
    mlp.fit(X, y)
    return mlp

def predict_with_ai(ai_model, X):
    # Use the trained AI model to make predictions on new data
    return ai_model.predict(X)
