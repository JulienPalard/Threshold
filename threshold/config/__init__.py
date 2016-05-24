
class BaseConfig():

    def __init__(self, request):
        self.request = request

    def get_argument(self, name):
        raise NotImplementedError

    def post_argument(self, name):
        raise NotImplementedError

    def is_get_method(self):
        raise NotImplementedError

    def is_post_method(self):
        raise NotImplementedError
