
class FilterException(Exception):
    def __init__(self, argument, message):
        super.__init__(message)
        self.name = name
        self.message = message
        print("error:", name, "message:", message)
