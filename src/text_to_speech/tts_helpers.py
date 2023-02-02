# tts_helpers.py
import os
import pyttsx3

class TTSHelpers:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def set_voice(self, voice_index):
        self.engine.setProperty('voice', self.voices[voice_index].id)
        
    def get_voices(self):
        voices = []
        for voice in self.voices:
            voices.append(voice.name)
        return voices
