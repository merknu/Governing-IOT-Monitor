# chatbot_intents.py
# This file contains the implementation for different intents the chatbot can handle.
# Each intent is defined as a method, such as greet_user, get_devices, turn_on_device, and turn_off_device.
# These methods use the parse_input and get_response functions from chatbot_helpers.py to process the user's input and generate a response.
# The response is then sent to the user using the send_message function.
import os
import json
import re

from chatbot_helpers import parse_input, get_response, send_message

class ChatbotIntents:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = user_id

    def greet_user(self, message):
        response = "Hello! How can I help you today?"
        send_message(self.client, self.user_id, response)

    def get_devices(self, message):
        device_list = self.client.get_devices()
        response = "Here are the devices currently connected: \n"
        for device in device_list:
            response += "{}: {}\n".format(device.id, device.name)
        send_message(self.client, self.user_id, response)

    def turn_on_device(self, message):
        device_name = parse_input(message, "turn on")
        if device_name:
            device = self.client.get_device_by_name(device_name)
            if device:
                device.turn_on()
                response = "Turned on {}".format(device_name)
            else:
                response = "Device not found"
        else:
            response = "Please specify which device you would like to turn on"
        send_message(self.client, self.user_id, response)

    def turn_off_device(self, message):
        device_name = parse_input(message, "turn off")
        if device_name:
            device = self.client.get_device_by_name(device_name)
            if device:
                device.turn_off()
                response = "Turned off {}".format(device_name)
            else:
                response = "Device not found"
        else:
            response = "Please specify which device you would like to turn off"
        send_message(self.client, self.user_id, response)
