# voice_recognition_helpers.py
class VoiceRecognitionHelpers:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()
        
    def listen_for_speech(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
        
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print("Request error from Google Speech Recognition service: {}".format(e))
            return None
