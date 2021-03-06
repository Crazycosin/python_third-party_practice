import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form method="POST">'
        '<input type="text" name="message">'
        '<input type="submit" value="Submit">'
        '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

def make_app():
    return tornado.web.Application([(r"/get", MainHandler), ], debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
