# chatbot_responses.py
class ChatbotResponses:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey there! What's up?"],
            "farewell": ["Goodbye! Have a great day.", "See you later! Take care.", "Bye for now! Have a good one."],
            "confirm": ["Yes, I understand.", "Got it!", "Understood."],
            "deny": ["No, I don't understand.", "Sorry, can you repeat that?", "I'm sorry, I don't get it."],
            "ask_name": ["What's your name?", "Can I have your name please?", "Can you tell me your name?"],
            "tell_name": ["Nice to meet you, {}!", "It's a pleasure to meet you, {}!", "Hi {}, it's great to meet you!"],
            "ask_age": ["How old are you?", "Can you tell me your age?", "What's your age?"],
            "tell_age": ["Wow, you're {} years old!", "That's cool, you're {} years old!", "Awesome, you're {} years old!"],
            "ask_location": ["Where are you from?", "Can you tell me your location?", "What's your location?"],
            "tell_location": ["Wow, you're from {}!", "That's cool, you're from {}!", "Awesome, you're from {}!"],
            "default": ["I'm sorry, I didn't understand what you mean. Can you rephrase that?", "I'm not sure what you're trying to say. Can you give me more context?", "Sorry, I don't understand. Can you please clarify?"]
        }

    def get_response(self, intent):
        if intent in self.responses:
            return random.choice(self.responses[intent])
        else:
            return random.choice(self.responses["default"])
