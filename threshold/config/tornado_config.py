from threshold.config import BaseConfig


class TornadoConfig(BaseConfig):
    def __init__(self, request):
        self.request = request

    def get_argument(self, name):
        return self.request.get_argument(name, None)

    def post_argument(self, name):
        return self.request.get_argument(name, None)

    def is_get_method(self):
        return self.request.request.method == "GET"

    def is_post_method(self):
        return self.request.request.method == "POST"


