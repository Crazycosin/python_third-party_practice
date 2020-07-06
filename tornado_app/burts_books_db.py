import os
from tornado import(
    auth,
    escape,
    httpserver,
    ioloop,
    options,
    web
)
import pymongo
from settings import settings

options.define(
    "port", default=8001, help="请运行在给定的端口", type=int
)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/recommended", RecommendedHandler),
        ]
        conn = pymongo.MongoClient("localhost", 27017)
        self.db = conn["bookstore"]
        web.Application.__init__(self, handlers, 
                            template_path=settings['template_path'],
                            static_path=settings['static_path'],
                            ui_modules={"Book": BookModule},
                            debug=True)


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("index.html", page_title="图书管理|主页", header_text="欢迎使用图书管理系统")
    

class RecommendedHandler(web.RequestHandler):
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render(
            "recommended.html",
            page_title="图书系统|图书信息",
            header_text="图书信息",
            books=books
        )


class BookModule(web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book
        )
    
    def css_files(self):
        return "css/recommended.css"
    
    def javascript_files(self):
        return "js/recommended.js"


def main():
    options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()