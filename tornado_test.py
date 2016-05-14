import tornado.ioloop
import tornado.web

import threshold
from threshold.item import ArgumentItem

class MainHandler(tornado.web.RequestHandler):

    items = [
        ArgumentItem("test", int)
    ]

    @threshold.knock_door(items)
    def get(self, params=None):
        print(params)
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
