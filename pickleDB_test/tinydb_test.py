from tinydb import TinyDB, Query, where


db = TinyDB('default.json')
# 插入记录
db.insert({
    "name": 'john',
    'age': 23
})

db.insert({
    "name": 'apple',
    'age': 12
})

# 输出所有记录
print(db.all())

# 查询
User = Query()
print(db.search(User.name == 'john'))

# query
print(db.search(where('name') == 'john'))

# update
db.update({'age':10}, where('name') == 'john')

# remove
db.remove(where('age') > 20)

# 清空
db.truncate()
