# - * - coding: utf-8 - * -
import apsw


conn = apsw.Connection(":memory:")
cursor = con.cursor()

# 初始化数据
def init_db():
    for row in cursor.execute(
        "create table foo(x,y,z); insert into foo values(?,?,?)"
        "insert into foo values(?,?,?); select * from foo; drop table foo;"
        "create table bar(x,y); insert into bar values(?, ?);"
        "insert into bar values(?, ?); select * from bar;",
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        ):
        print(row)
init_db()