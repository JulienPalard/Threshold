import tornado.ioloop
import tornado.web

import threshold
from threshold.item import ArgumentItem
from threshold.utils import Check

class MainHandler(tornado.web.RequestHandler):

    items = [
        ArgumentItem("test", str,
                     check_functions=[(Check.is_phone, None, "phone error")],
                 ),
    ]

    @threshold.knock_door(items)
    def get(self, params=None):
        print("result: ", params)
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
