import random                      #导入内置模块 
from mongoengine import *
import random

connect('test',
    host='0.0.0.0',
    port=27017)                    #连接数据库对象『test』


class Stu(Document):               #定义 ORM 框架类 Stu
    sid = SequenceField()      
    name = StringField()       
    passwd = StringField()     
    def introduce(self):          #定义函数 introduce()来显示自己的介绍信息 
        print('序号:', self.sid, end=' ') #显示 id
        print('姓名:', self.name, end=' ') #显示姓名 
        print('密码:', self.passwd)#显示密码 
    def set_pw(self, pw):          #定义函数 set_pw()用于修改密码 
        if pw:
            self.passwd = pw     #修改密码 
            self.save() 
         #保存修改的密码 
# …省略部分代码…

def get_str(min, max):
    \"\"\"sumary_line
    随机生成字符串
    Keyword arguments:
    argument -- description
    Return: return_description
    \"\"\"
    
    alpht_list = [chr(65+i) for i in range(26)]
    l = random.randint(min, max)
    s = ''
    for i in range(l):
        s +=random.choice(alpht_list)
    return s

if __name__ == '__main__':
    print('插入一个文档:')
    stu = Stu(name='langchao', passwd='123123')#创建文档类对象实例 stu，设置用户名和密码 
    stu.save()                                  #保存文档 
    stu = Stu.objects(name='lilei').first()     #查询数据并对类进行初始化 
    if stu:
        stu.introduce()                        #显示文档信息 
    print('插入多个文档')                      #显示提示信息 
    for i in range(3):                          #遍历操作 
        Stu(name=get_str(2,4), passwd=get_str(6, 8)).save() #插入 3 个文档 
    stus = Stu.objects()                        #文档类对象实例 stu
    for stu in stus:                            #遍历所有的文档信息 
        stu.introduce()                        #显示所有的遍历文档 
    print('修改一个文档')                        #显示提示信息 
    stu = Stu.objects(name='langchao').first()  #查询某个要操作的文档 
    if stu:
        stu.name='daxie'                       #修改用户名属性 
        stu.save()                             #保存修改 
        stu.set_pw('bbbbbbbb')                 #修改密码属性 
        stu.introduce()                        #显示修改后的结果 
    print('删除一个文档')                        #显示提示信息 
    stu = Stu.objects(name='daxie').first()     #查询某个要操作的文档 
    stu.delete()                                #删除这个文档 
    stus = Stu.objects()
    for stu in stus:                            #遍历所有的文档 
        stu.introduce()                        #显示删除后的结果