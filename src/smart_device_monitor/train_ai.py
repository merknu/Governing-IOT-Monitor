import os
import importlib

MODEL_FOLDER = 'models'

def train_ai(data, labels):
    models = []
    
    # List all the models in the MODEL_FOLDER
    for filename in os.listdir(MODEL_FOLDER):
        if filename.endswith('.py'):
            models.append(filename[:-3])

    # Import the models dynamically
    for model_name in models:
        module = importlib.import_module(MODEL_FOLDER + '.' + model_name)
        model = module.create_model()
        model.fit(data, labels)
