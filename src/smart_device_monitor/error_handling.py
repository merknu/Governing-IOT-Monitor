# error_handling.py
class ConnectionError(Exception):
    def __init__(self, message):
        self.message = message

class DataError(Exception):
    def __init__(self, message):
        self.message = message
