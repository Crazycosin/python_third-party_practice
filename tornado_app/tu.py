from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
from settings import settings

class MediaHandler(RequestHandler):
    def get(self):
        self.write("<img src='/static/h6.jpg'/>")


app = Application(
    [
        (r"/stt", MediaHandler),
        (r"/static/(.*)", StaticFileHandler, {"path": settings['static_path']})
    ],
)

if __name__ == '__main__':
    app.listen(8888)
    IOLoop.instance().start()