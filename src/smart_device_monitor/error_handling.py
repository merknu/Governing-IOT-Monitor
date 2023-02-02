# error_handling.py
import logging

def handle_error(error_message):
    # Log the error message
    logging.error(error_message)

    # Handle the error in a way that makes sense for your program
    # Example: Display an error message to the user
    print("An error has occurred: " + error_message)
