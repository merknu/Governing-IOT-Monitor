# chatbot_helpers.py
import os
import pyttsx3

class ChatbotHelpers:
    def __init__(self, voice=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty("voice", voice or self.get_default_voice())
    
    def get_default_voice(self):
        voices = self.engine.getProperty("voices")
        return voices[0].id

    def set_voice(self, voice):
        self.engine.setProperty("voice", voice)
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

