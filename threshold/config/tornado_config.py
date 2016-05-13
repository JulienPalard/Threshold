
class Config(Object):
    def __init__(self, request):
        self.request = request

    GET_POST_ARGUMENT = self.request.get_argument
    GET_GET_ARGUMENT = self.request.get_argument
