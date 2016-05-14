
class Config():
    def __init__(self, request):
        self.request = request
        print(request.request.arguments)

    def get_argument(self, name):
        print("name:", name)
        return self.request.get_argument(name)

    def post_argument(self, name):
        return self.request.get_argument(name)

    def is_get_method(self):
        return self.request.request.method == "GET"

    def is_post_method(self):
        return self.request.request.method == "POST"


