# django 常用指令


## 1.新建一个django项目
```shell
django-admin.py startproject project-name

# windows
django-admin startproject project-name
```

## 2.新建一个django应用
```shell
python manage.py startapp app-name

# 或者
django-admin.py startapp app-name
```

## 3.同步数据库
```shell
python manage.py syncdb

# django version 1.7.1 over
python manage.py makemigrations
python manage.py migrate
```

## 4.使用开发服务器
```shell
# 监听所有可用ip，访问端口为8001
python manage.py runserver 0.0.0.0 8001
```

## 5.清空数据库
```shell
python manage.py flush
```

## 6.创建超级管理员
```shell
python manage.py createsuperuser
# 按照提示输入用户名以及密码
# 修改用户密码
python manage.py changepassword username
```

## 7.导出数据与导入数据
```shell
# 导出数据
python manage.py dumpdata appname > appname.json
# 导入数据
python manage.py loaddata appname.json
```

## 8.启动django项目的终端并打开命令行操作界面
```shell
python manage.py shell
```

## 9.显示数据库的基本信息
```shell
python manage.py dbshell
```