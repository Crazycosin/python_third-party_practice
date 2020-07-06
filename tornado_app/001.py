"""
tornado是facebook开源的非阻塞web容器，
类似java的netty，tornado.options是负责解析tornado容器的全局参数的，
同时也能够解析命令行传递的参数和从配置文件中解析参数。使用步骤如下：
"""

import os
from re import template
from tornado import (
    httpserver, ioloop, web)
import tornado
from tornado.options import define, options
from tornado.web import Application
from settings import settings


define("port", default=8001, help="运行在指定端口", type=int)

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class PoemPageHandler(web.RequestHandler):
    def post(self):
        noun1 = self.get_argument("noun1")
        noun2 = self.get_argument("noun2")
        verb = self.get_argument("verb")
        noun3 = self.get_argument("noun3")
        self.render("poem.html", roads=noun1, wood=noun2, made=verb, difference=noun3)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/poem", PoemPageHandler)
            ],
            template_path=settings['template_path']
    )
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()