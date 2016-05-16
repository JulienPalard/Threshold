import logging

class CheckException(Exception):
    def __init__(self, name, message):
        self.name = name
        self.message = message
        logging.error(("error check function:", name, "message:", message))

class NotExistsArgument(Exception):
    def __init__(self, name, message):
        self.name = name
        self.message = message
        logging.error(("error handle function:", name, "message:", message))
