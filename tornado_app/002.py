from re import A, template
from typing import Text
import tornado
from tornado.options import define, options
from tornado.web import RequestHandler, Application
from settings import settings
from tornado import (
    httpserver, ioloop, web)

define("port", default=8001, help="运行给定的端口", type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.render("002_index.html")


class MungedPageHandler(RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(" ") if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped
    
    def post(self):
        source_text = self.get_argument("source")
        text_to_change = self.get_argument("change")
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split("\r\n")
        self.render("munged.html", source_map=source_map, change_lines=change_lines)


if __name__ == "__main__":
    options.parse_command_line()
    app = Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/poem", MungedPageHandler)
        ],
        template_path=settings['template_path'],
        static_path=settings['static_path'],
        debug=True
    )
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()