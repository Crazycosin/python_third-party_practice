from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, RedirectHandler


class DistA(RequestHandler):
    def get(self):
        self.write("redirect optional page !")


class SrcA(RequestHandler):
    def get(self):
        self.redirect("/dist")

app = Application(
    [
        (r"/dist", DistA),
        (r"/src", SrcA),
        (r"/rdrt", RedirectHandler, {"url": "/src"}),
        ],
        debug=True
)

if __name__ == "__main__":
    app.listen(8888)
    IOLoop.instance().start()