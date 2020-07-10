# - * - coding: utf-8 - * -
import pymysql

# 打开数据库连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='test_db',
    port=3306,
    charset='utf8',
)

# 创建游标对象
cursor = db.cursor()

# execute执行sql语句
sql = """
    show variables like '%%log%%';
    """
cursor.execute(sql)
# 获取单条记录
data = cursor.fetchone()

# 事务机制
try:
    cursor.execute(sql)
    # 向数据库提交
    db.commit()
except:
    # 错误时回滚数据
    db.rollback()

# 关闭游标
cursor.close()

# 关闭连接
db.close()