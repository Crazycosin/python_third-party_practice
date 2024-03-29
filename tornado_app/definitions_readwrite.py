from tornado import(
    web, ioloop, options,
    httpserver
)
import pymongo

options.define(
    "port", default=8000,
    help="run on the given port",
    type=int
)

class Application(web.Application):
    def __init__(self) -> None:
        handlers = [
            (r"/(\w+)", WordHandler)
        ]
        conn = pymongo.MongoClient("localhost", 27017)
        self.db = conn["definitions"]
        web.Application.__init__(self, handlers=handlers, debug=True)


class WordHandler(web.RequestHandler):
    def get(self, word):
        coll = self.application.db.words
        word_doc = coll.find_one({"word": word})
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)
        else:
            self.set_status(404)
        
    def post(self, word):
        definition = self.get_argument("definition")
        coll = self.application.db.words
        word_doc = coll.find_one({"word": word})
        if word_doc:
            word_doc["definition"] = definition
            coll.save(word_doc)
        else:
            word_doc = {
                "word": word,
                "definition": definition
            }
            coll.insert(word_doc)
        del word_doc["_id"]
        self.write(word_doc)


if __name__ == "__main__":
    options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.options.port)
    ioloop.IOLoop.instance().start()