# - * - coding: utf-8 - * -
import MySQLdb


conn = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='test_db',
    charset='utf8'
)

# 创建游标
cur = conn.cursor()

# 执行sql语句
sql = """
    show variables like '%%log%%';
"""
cur.execute(sql)
data  = cur.fetchall()
print(data)
# 关闭游标
cur.close()

# 提交事务
conn.commit()

# 关闭数据库连接
conn.close()