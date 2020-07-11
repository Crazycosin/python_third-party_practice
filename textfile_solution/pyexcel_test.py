# - * - coding: utf-8 - * -
import pyexcel
from textfile_solution import PROJECT_PATH

def load_and_export_csv_test():
    sheet = pyexcel.get_sheet(file_name=PROJECT_PATH+"//file_location//data.csv")
    print(sheet)

    with open('./file_location/tab_example.csv', 'w') as f:
        unused = f.write('I\tam\ttab\tseparated\tcsv\n')  # for passing doctest
        unused = f.write('You\tneed\tdelimiter\tparameter\n')  # unused is added
    sheet = pyexcel.get_sheet(file_name=PROJECT_PATH+"//file_location//tab_example.csv", delimiter='\t')
    print(sheet)


def read_data_test():
    # 读取的文件「example.xlsm」
    spreadsheet = ppyexcele.get_sheet(file_name=PROJECT_PATH+"//file_location//tab_example.csv")
    # 遍历每一行 
    for r in spreadsheet.row_range():
        # 遍历每一列 
        for c in spreadsheet.column_range():
            print(spreadsheet.cell_value(r, c))


def read_data_test1():
    spreadsheet = pyexcel.get_sheet(file_name=PROJECT_PATH+"//file_location//tab_example.csv")
    for value in spreadsheet.columns():
        print(value)


def read_data_test2():
    book = pyexcel.get_book(file_name=PROJECT_PATH+"//file_location//multiple-sheets-example.xlsx")

     # 默认的迭代器为 Boo 实例 
    for sheet in book:
          # 每张表都有名字 
        print('sheet: %s' %sheet.name)
          # 一旦拥有了一个表实例，
          #就可以将其视为一个读取器实例，可以按照期望的方式迭代它的成员 
        for row in sheet:
            print(row)


def export_sheets_test():
    data = {
          "Sheet 1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
          "Sheet 2": [['X', 'Y', 'Z'], [1, 2, 3], [4, 5, 6]],
          "Sheet 3": [['O', 'P', 'Q'], [3, 2, 1], [4, 3, 2]]
    }
    ppyexcele.save_book_as(bookdict=data, dest_file_name=PROJECT_PATH+"//file_location//multiple-sheets1.xls")

def read_multiple_data_test():
    sheet = pe.get_sheet(file_name=PROJECT_PATH+"//file_location//multiple-sheets1.xls", 
                        name_columns_by_row=0)
    print(json.dumps(sheet.to_dict()))
    #获取列标题 
    print(sheet.colnames)
    #在一维数组中获取内容 
    data = list(sheet.enumerate())
    print(data)
    #逆序获取一维数组中的内容 
    data = list(sheet.reverse())
    print(data)

    #在一维数组中获取内容，但垂直地迭代 
    data = list(sheet.vertical())
    print(data)
    #获取一维数组中的内容，以相反的顺序垂直迭代 
    data = list(sheet.rvertical())
    print(data)

    #获取二维数组的数据 
    data = list(sheet.rows())
    print(data)

    #以相反的顺序获取二维数组的行 
    data = list(sheet.rrows())
    print(data)

    #获取二维数组的列 
    data = list(sheet.columns())
    print(data)

    #以相反的顺序获取一个二维数组的列 
    data = list(sheet.rcolumns())
    print(data)

    #可以把结果写入一个文件中 
    sheet.save_as('./file_location/example_series.xls')


def export_data_to_db():
    engine = create_engine('sqlite:///birth.db')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)

    class BirthRegister（Base）:
        __tablename__ = 'birth'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        weight = Column(Float)
        birth = Column(Date)

    Base.metadata.create_all（engine）

    # 创建数据 
    data = [
        ['name', 'weight', 'birth'],
        ['Adam', 3.4, datetime.date(2017, 2, 3)],
        ['Smith', 4.2, datetime.date(2014, 11, 12)]
    ]
    pyexcel.save_as(array=data,
                dest_file_name='birth.xls')

    # 导入 Excel 文件中 
    session = Session()  # obtain a sql session
    pyexcel.save_as(file_name='birth.xls',
                    name_columns_by_row=0,
                    dest_session=session,
                    dest_table=BirthRegister)

    # 验证结果 
    sheet = pyexcel.get_sheet(session=session, table=BirthRegister)
    print(sheet)
    session.close()


if __name__ == "__main__":
    load_and_export_csv_test()
    read_data_test()