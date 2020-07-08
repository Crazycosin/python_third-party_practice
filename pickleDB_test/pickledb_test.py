# - * - coding: utf-8 -*-
import pickledb
db = pickledb.load('./db_location/example.db', False)
db.set('key', 'value')
print(db.get('key'))
# 保存到当前目录
db.dump()