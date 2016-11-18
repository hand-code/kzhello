# coding:utf-8

import tornado.web
from modules.article_module import Article


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        Article.delete(1)
        self.write("index_handler")