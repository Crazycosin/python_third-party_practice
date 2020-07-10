# - * - coding: utf-8 - * -
from random import randint
import pymongo
import datetime
from random import randint

conn = pymongo.MongoClient("localhost", 27017)
db = conn.example
db.words.insert({
    "word": "oarlock",
    "definition": "A device attached to a rowboat to hold the oars in  place"
})
db.words.insert({
    "word": "seminomadic",
    "definition": "Only partially nomadic"
})
db.words.insert({
    "word": "perturb",
    "definition": "Bother, unsettle, modify"
})

# 插入图书内容
db = conn.bookstore
db.books.insert_many([
    {
    "title": "Python开发从入门到精通",
    "subtitle": "Python",
    "image": "python.gif",
    "author": "浪潮",
    "date_added": datetime.datetime.now().strftime("%Y%m%d"),
    "date_released": f"{datetime.datetime.now().month}/{datetime.datetime.now().year}",
    "isbn": f"{randint(100, 999)}-{randint(0,9)}-{randint(10000,99999)}-{randint(0,9)}",
    "description": "<p>...</p>"
    },
    {
    "title": "Php从入门到精通",
    "subtitle": "Web服务",
    "image": "php.gif",
    "author": "学习php",
    "date_added": datetime.datetime.now().strftime("%Y%m%d"),
    "date_released": f"{datetime.datetime.now().month}/{datetime.datetime.now().year}",
    "isbn": f"{randint(100, 999)}-{randint(0,9)}-{randint(10000,99999)}-{randint(0,9)}",
    "description": "<p>...</p>"
    },
    ])
