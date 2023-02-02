# tts_models.py
class TTSModels:
    def __init__(self):
        self.models = {
            "google": "Google Text-to-Speech API",
            "amazon": "Amazon Polly API",
            "ibm": "IBM Watson Text-to-Speech API",
            "microsoft": "Microsoft Azure Text-to-Speech API"
        }

    def get_model(self, model_name):
        if model_name in self.models:
            return self.models[model_name]
        else:
            return "Model not found. Please choose from the following options: {}".format(", ".join(self.models.keys()))
