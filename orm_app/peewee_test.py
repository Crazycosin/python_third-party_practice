from datetime import date, datetime
from peewee import *

db = SqliteDatabase('people.db')

# 模型定义
class Person(Model):
      name = CharField()
      birthday = DateField()
      is_relative = BooleanField()

      class Meta:
            database = db #这个模型使用了「people.db」数据库 

class Pet(Model):
      owner = ForeignKeyField(Person, related_name='pets')
      name = CharField()
      animal_type = CharField()

      class Meta:
            database = db #这个模型使用了「people.db」数据库 

def create_db():
    # 连接数据库
    db.connect()
    # 创建 Person 和 Pet 表
    db.create_tables([Person, Pet])

    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
    uncle_bob.save()

    # 连接数据库关闭
    db.close()

def operate_db():
    uncle_bob = Person(name='Bo', birthday=date(1960, 1,15), is_relative=True)
    uncle_bob.save()
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
    grandma.name = 'Grandma L.'
    grandma.save()  #更新数据库中 grandma 的名字 

    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
    herb_mittens.delete_instance() #删除 
    herb_fido.owner = uncle_bob
    herb_fido.save()
    bob_fido = herb_fido


def query_db():
    #获取单个数据记录 
    grandma = Person.select().where(Person.name == 'Grandma L.').get()
    # 同上
    grandma = Person.get(Person.name == 'Grandma L.')
    #获取数据列表 
    for person in Person.select():
        print('人名:', person.name, person.is_relative)
    query = Pet.select().where(Pet.animal_type == 'cat')
    for pet in query:
        print('宠物名:', pet.name, '主人名:', pet.owner.name)

    #连接查询 
    query = (Pet.select(Pet, Person)
          .join(Person)
          .where(Pet.animal_type == 'cat'))
    for pet in query:
        print(pet.name, pet.owner.name)

    # 获取 Bob 拥有的所有宠物 
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
        print(pet.name)

    # 同上
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
    for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
        print(pet.name)

    # 按日期排序 
    for person in Person.select().order_by(Person.birthday.desc()):
        print(person.name, person.birthday)
    # -------------------------------------------------------------------------------
    for person in Person.select():
        print(person.name, person.pets.count(), 'pets')
        for pet in person.pets:
               print(' ', pet.name, pet.animal_type)

    # --------------------------------------------------------------------------------
    #查询条件 
    d1940 = date(1940, 1, 1)
    d1960 = date(1960, 1, 1)

    # 查询 1960 年之后出生和 1940 年之前出生的人 
    query = (Person.select()
         .where((Person.birthday < d1940) | (Person.birthday < d1960)))
    for person in query:
        print(person.name, person.birthday)
    # 查询生日在 1940 年与 1960 年之间的人 
    query = (Person
        .select()
        .where((Person.birthday < d1940) & (Person.birthday < d1960)))
    for person in query:
        print(person.name, person.birthday)
    # ------------------------------------------------------
    # 查询以 g 开头的人名 
    expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g' )
    for person in Person.select().where(expression):
        print(person.name)

    # 连接数据库
    db.close()

mysql_db = MySQLDatabase('test_db', host='127.0.0.1', port=3306, user='root', passwd='root')
mysql_db.connect()

class BaseModel(Model):
     class Meta:
          database = mysql_db

class User(BaseModel):
     username = CharField(unique=True)

class Tweet(BaseModel):
     user = ForeignKeyField(User, related_name='tweets')
     message = TextField()
     created_date = DateTimeField(default=datetime.now)
     is_published = BooleanField(default=True)


if __name__ == "__main__":
    # create_db()
    # operate_db()
    # query_db()
    # mysql创建表 
    User.create_table()  #创建 User 表 
    Tweet.create_table()  #创建 Tweet 表