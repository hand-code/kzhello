# coding:utf-8

import tornado.web
import tornado.ioloop
from views.index_handler import IndexHandler


def make_app():
    return tornado.web.Application([
        (r'/', IndexHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
