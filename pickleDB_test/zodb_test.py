# - * - coding: utf-8 - * -
from ZODB import FileStorage, DB
import transaction

class MyZODB(object):
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.db_root = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()


def create_data():
    db = MyZODB('./db_location/data.fs')
    db_root = db.db_root
    db_root['a_number'] = 3
    db_root['a_string'] = 'Gift'
    db_root['a_list'] = [1, 2, 3, 5, 7, 12]
    db_root['a_dictionary'] = {1918: 'Red Sox', 1919: 'Reds'}
    db_root['deeply_nested'] = {
        1918: [('Red, Sox', 4), ('Cubs', 2)],
        1919: [('Reds', 5), ('White Sox', 3)]
    }
    transaction.commit()
    db.close()


def get_zodb_data():
    db = MyZODB('./db_location/data.fs')
    db_root = db.db_root
    for key in db_root.keys():
        print(f"{key}: {db_root[key]}")
    db.close()


def alter_zodb_data():
    db = MyZODB('./db_location/data.fs')
    db_root = db.db_root
    db_root['a_string'] = 'Something Else'
    transaction.commit()
    db.close()

    # 但是需要显式地将对列表或字典的更改告诉zodb，下面代码将不会修改zodb中对应的内容
    a_dictionary = db_root['a_dictionary']
    a_dictionary[1920] = 'Indians'
    transaction.commit()
    db.close()

    # 如果打算更改而不是完全替换，则需要设置数据库根的属性_p_changed,以通知它需要重新存储其下的属性
    a_dictionary = db_root['a_dictionary']
    a_dictionary[1920] = 'Indians'
    db._p_changed = 1
    transaction.commit()
    db.close()


def delete_zodb_data():
    db = MyZODB('./db_location/data.fs')
    db_root = db.db_root
    del db_root['a_number']
    transaction.commit()
    db.close()


create_data()
get_zodb_data()
alter_zodb_data()
delete_zodb_data()