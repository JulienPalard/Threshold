import tornado.ioloop
import tornado.web

import threshold
from threshold.item import ArgumentItem

class MainHandler(tornado.web.RequestHandler):

    items = [
        ArgumentItem("test", int,
                     check_functions=[(lambda x: x > 100, None, "error message")],
                     after_handler_functions=[((lambda x: x * 10), None, "handler error")]
                 ),
        ArgumentItem("test1", int, require=False, default=1
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
