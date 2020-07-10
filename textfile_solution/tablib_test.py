# - * - coding: utf-8 - * -
import tablib


def create_data():
    data = tablib.Dataset()

    # 添加行
    # 名称的集合
    names = ["Kenneth Reitz", "Bessie Monke"]
    for name in names:
        # 分割名称
        fname, lname = name.split()
        # 将名称添加到数据集中
        data.append([fname, lname])
    print(data.dict)

    # 添加标题
    data.headers = ['First Name', 'Last Name']
    print(data.dict)

    # 添加列
    data.append_col([22, 20], header='Age')
    print(data.dict)

    # 导出数据 返回对应格式的数据流
    data.export('csv')
    # 写到文件中
    with open('./file_location/data.csv', 'w') as f:
        f.write(data.csv)
    data.export('json')
    data.export('yaml')
    data.export('xls')

    # 导入数据
    imported_data = tablib.Dataset().load(open('./file_location/data.csv').read())
    print(imported_data.dict)


def operate_test():
    names = ["Kenneth Reitz", "Bessie Monke"]
    data = tablib.Dataset()
    data.headers = ("First Name", "Last Name")
    for name in names:
        fname, lname = name.split()
        data.append((fname, lname))
    data.append_col((22, 20), header='Age')
    # 显示某条信息
    print(data[0])
    # 显示某列的值
    print(data['First Name'])
    # 使用索引访问列
    print(data.headers)
    print(data.get_col(1))
    # 计算平均年龄
    ages = data["Age"]
    print(float(sum(ages)) / len(ages))


def delete_test():
    headers = ('area', 'user', 'recharge')
    data = [
        ('1', 'Rooney', 20),
        ('2', 'John', 30),
    ]
    data = tablib.Dataset(*data, headers=headers)

    # 可以通过下面这些方式得到各种格式的数据
    print(data.csv)
    print(data.xls)
    print(data.json)
    print(data.yaml)
    print(data.tsv)

    # 增加行
    data.append(['3', 'Keven', 18])
    # 增加列
    data.append_col((22, 20, 13), header='Age')
    print(data.csv)

    # 删除行
    del data[1:3]
    # 删除列
    del data['Age']
    print(data.csv)


def data_sets_test():
    import tablib
    import os

    # 创建数据集，方法 1
    dataset1 = tablib.Dataset()
    header1 = ('ID', 'Name', 'Tel', 'Age')
    dataset1.headers = header1
    dataset1.append((1, 'zhangsan', 13711111111, 16))
    dataset1.append((2, 'lisi', 13811111111, 18))
    dataset1.append((3, 'wangwu', 13911111111, 20))
    dataset1.append((4, 'zhaoliu', 15811111111, 25))
    print('dataset1:', os.linesep, dataset1, os.linesep)

    # 创建数据集，方法 2
    header2 = ('ID', 'Name', 'Tel', 'Age')
    data2 = [
        [1,"zhangsan", 13711111111, 16],
    [2, "lisi",  13811111111, 18],
    [3, "wangwu", 13911111111, 20],
    [4, "zhaoliu", 15811111111, 25]
    ]
    dataset2 = tablib.Dataset(*data2, headers=header2)
    print('dataset2: ', os.linesep, dataset2, os.linesep)

    # 增加行
    dataset1.append([5, 'sunqi', 15911111111, 30])  # 添加到最后一行的下面
    dataset1.insert(0, [0, 'liuyi', 18211111111, 35])  # 在指定位置添加行
    print("增加行后的dataset1: ", os.linesep, dataset1, os.linesep)

    # 删除行
    dataset1.pop()  # 删除最后一行
    dataset1.lpop()  # 删除第一行
    del dataset1[0:2]  # 删除第[0,2)行数据
    print("删除行后的dataset1:", os.linesep, dataset1, os.linesep)

    # 增加列
    # 现在 dataset1 就剩两行数据了
    dataset1.append_col(("beijing", "shenzhen"), header="city")     #增加列到最后一列
    dataset1.insert_col(2, ("male", "female"),header="sex")        #在指定位置添加列
    print("增加列后的dataset1: ", os.linesep, dataset1, os.linesep)

    # 删除列
    del dataset1["Tel"]
    print("删除列后的dataset1: ", os.linesep, dataset1, os.linesep)

    # 获取各种格式的数据
    print("yaml format: ", os.linesep, dataset1.yaml, os.linesep)
    print("csv format: ",  os.linesep, dataset1.csv, os.linesep)
    print("tsv format: ",  os.linesep, dataset1.tsv,  os.linesep)

    # 导出到 Excel 表格中
    dataset1.title = "dataset1"  # 设置 Excel 中表单的名称
    dataset2.title = "dataset2"
    myfile = open("./file_location/mydata.xls","wb")
    myfile.write(dataset1.xls)
    myfile.close()

    # 如果有多个 sheet 表单，使用 DataBook 就可以了
    myDataBook = tablib.Databook((dataset1, dataset2))
    myfile = open(myfile.name, "wb")
    myfile.write(myDataBook.xls)
    myfile.close()


def filter_test():
    students = tablib.Dataset()
    students.headers = ['first', 'last']
    students.rpush(['Kenneth', 'Reitz'], tags=['male', 'technical'])
    students.rpush(['Bessie', 'Monke'], tags=['female', 'creative'])
    print(students.filter(['male']).yaml)


def sparator_test():
    """
    分离表格中的数据
    :return:
    """
    daniel_tests = [
        ('11/24/09', 'Math 101 Mid-term Exam', 56.),
        ('05/24/10', 'Math 101 Final Exam', 62.)
    ]

    suzie_tests = [
        ('11/24/09', 'Math 101 Mid-term Exam', 56.),
        ('05/24/10', 'Math 101 Final Exam', 62.)
    ]
    tests = tablib.Dataset()
    tests.headers = ["Date", "Test Name", "Grade"]

    # Daniel 的数据
    tests.append_separator("Daniel的得分")

    for test_row in daniel_tests:
        tests.append(test_row)

    # Susie 的数据
    tests.append_separator("Susie的得分")

    for test_row in suzie_tests:
        tests.append(test_row)

    # 写入 Excel 表格
    with open('./file_location/grades.xls', 'wb') as f:
        f.write(tests.export('xls'))

if __name__ == "__main__":
    create_data()
    operate_test()
    delete_test()
    data_sets_test()
    filter_test()
    sparator_test()