from pony.orm import *
from decimal import Decimal

db = Database('mysql', host='localhost',
                user='root',
                passwd='root',
                db='test_db')

db.drop_table('person', with_all_data=True)
db.drop_table('user', with_all_data=True)
db.drop_table('student', with_all_data=True)
db.drop_table('professor', with_all_data=True)
db.drop_table('cart', with_all_data=True)
db.drop_table('product', with_all_data=True)
db.drop_table('tag', with_all_data=True)

class Person(db.Entity):
    _discriminator_ = 1 
    name = Required(str)
    age = Required(int)


class Student(Person):
    _discriminator_ = 3
    gpa = Optional(Decimal)
    mentor = Optional('Professor')


class Professor(Person):
    _discriminator_ = 2
    degree = Required(str)
    students = Set('Student')


class User(db.Entity):
    name = Required(str)
    cart = Optional("Cart") 


class Cart(db.Entity):
    user = Required("User")


class Product(db.Entity):
    tags = Set("Tag")


class Tag(db.Entity):
     products = Set(Product)


sql_debug(True)#显示调试信息 
db.generate_mapping(create_tables=True)


@db_session
def create_persons():
    p1 = Person(name='Person', age=20)
    s = Student(name='Student', age=22, gpa=1.2)
    p2 = Professor(name='Professor', age=12, degree='aaaaaa', students=[s])
    print(p1.id) #这里得不到 id，没提交 
    commit()
    print(p1.id) #这里已经有 id

if __name__ == "__main__":
    create_persons()