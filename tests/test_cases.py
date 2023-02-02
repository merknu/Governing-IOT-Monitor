# test_cases.py
import unittest
import chatbot
import tts
import lip_sync
import voice_recognition

class TestChatbot(unittest.TestCase):
    def test_greeting_response(self):
        chatbot_instance = chatbot.Chatbot()
        response = chatbot_instance.get_response("greeting")
        self.assertIn(response, chatbot.ChatbotResponses().responses["greeting"])

    def test_farewell_response(self):
        chatbot_instance = chatbot.Chatbot()
        response = chatbot_instance.get_response("farewell")
        self.assertIn(response, chatbot.ChatbotResponses().responses["farewell"])

class TestTTS(unittest.TestCase):
    def test_text_to_speech(self):
        tts_instance = tts.TextToSpeech()
        self.assertEqual(tts_instance.text_to_speech("Hello World"), "Hello World")

class TestLipSync(unittest.TestCase):
    def test_lip_sync(self):
        lip_sync_instance = lip_sync.LipSync()
        self.assertEqual(lip_sync_instance.sync("Hello World"), "Hello World")

class TestVoiceRecognition(unittest.TestCase):
    def test_voice_recognition(self):
        voice_recognition_instance = voice_recognition.VoiceRecognition()
        self.assertEqual(voice_recognition_instance.recognize_voice("Hello World"), "Hello World")

if __name__ == '__main__':
    unittest.main()
