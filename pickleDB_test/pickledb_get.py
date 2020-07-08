# - * - coding: utf-8 - * -

import pickledb
db = pickledb.load('./db_location/example.db', False)
print(db.get('key'))