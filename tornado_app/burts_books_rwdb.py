from tornado import(
    web, ioloop,
    options, httpserver
)
import pymongo
from settings import settings
import datetime

options.define(
    "port", default=8001,
    help="请运行在给定的端口",
    type=int
)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/recommended", RecommendedHandler),
            (r"/edit/([0-9Xx\-]+)", BookEditHandler),
            (r"/add", BookEditHandler)
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


class BookEditHandler(web.RequestHandler):
    def get(self, isbn=None):
        book=dict()
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({"isbn": isbn})
        self.render("book_edit.html",
            page_title="图书系统",
            header_text="编辑图书信息",
            book=book)
        
    def post(self, isbn=None):
        book_fields = ["isbn", "title", "subtitle", "image", 
                        "author", "date_released", 
                        "description"]
        coll = self.application.db.books
        book = dict()
        if isbn:
            book = coll.find_one({"isbn": isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)
        if isbn:
            coll.save(book)
        else:
            book["date_added"] = datetime.datetime.now().strftime("%Y%m%d")
            coll.insert(book)
        self.redirect("/recommended/")




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

# todo 缺失index.html, recommended.html两个页面
# 书籍中未提供，计划自己写一个简单的

if __name__ == "__main__":
    main()