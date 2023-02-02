import os
import sys
import time
import speech_recognition as sr
import pyttsx3

class Chatbot:
    def __init__(self, name, voice=None, avatar=None):
        self.name = name
        self.voice = voice
        self.avatar = avatar

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        # lip movement of avatar would go here

    def listen(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            self.speak("I'm sorry, I didn't understand what you said.")
        except sr.RequestError as e:
            self.speak("I'm sorry, I had some trouble connecting to the service. Please try again later.")
        return None

if __name__ == '__main__':
    bot = Chatbot("Cogz", voice='com.apple.speech.synthesis.voice.Alex', avatar=None)
    bot.speak("Hello, I am Cogz. How may I assist you?")
    while True:
        text = bot.listen()
        if text:
            if "exit" in text:
                bot.speak("Goodbye.")
                sys.exit()
            else:
                bot.speak("You said: " + text)
