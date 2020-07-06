import tornado.ioloop
import tornado.web
import tornado.escape


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("odn_cookie", tornado.escape.url_escape("未加密cookie串"))
        self.set_secure_cookie("src_cookie", "加密scure_cookie串")
        self.write("<a href='/shcook'>查看设置的cookie</a>")


class ShcookHandler(tornado.web.RequestHandler):
    def get(self):
        odn_cookie = tornado.escape.url_escape(self.get_cookie("odn_cookie"))
        scr_cookie = self.get_secure_cookie("src_cookie").decode("utf-8")
        self.write(f"普通cookie:{odn_cookie}<br/> 安全cookie: {scr_cookie}")


def make_app():
    app = tornado.web.Application(
    [(r"/sscookie", CookieHandler),
    (r"/shcook", ShcookHandler),
    ],
    cookie_secret="abc123",
    debug=True
    )
    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()