from tinydb.storages import MemoryStorage
from tinydb import TinyDB, where

def testBasicOperation():
    def addone(x):
        x['int'] +=1
    default_db = TinyDB('./db_location/default.json')
    real_table = default_db.table('real')
    print(f"{'*'*20}打开了数据库{default_db.name}{'*'*20}")
    for i in range(7):
        default_db.insert({"int": i+1, "char": chr(65+i)})
    print("对每一个元素进行打印操作：")
    print("default_db 中每一个int字段加1")
    default_db.update(addone)

    print("对每一个元素进行打印操作：")

    print("default_db中的所有表段为：", default_db.tables())
    print("default_db中所有的数据为：", default_db.all())

    default_db.truncate()
    print(f"{'*'*20}清除了所有表{'*'*20}")
    print("db中所有的表段为：", default_db.tables())
    print("default_db中所有的数据为：", default_db.all())

    print(f"{'*'*20}关闭了表{default_db.name}{'*'*20}")
    default_db.close()


def testMemoryStorage():
    db = TinyDB(storage = MemoryStorage)
    db.insert({'data': 5})
    print(db.search(where('data') == 5))

# testBasicOperation()
testMemoryStorage()
