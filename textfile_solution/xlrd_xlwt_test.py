from textfile_solution import PROJECT_PATH
import xlrd
import xlwt
from datetime import datetime


def xlrd_test():
    # 打开 Excel
    filename = PROJECT_PATH + '/file_location/xlrd_test.xlsx'
    data = xlrd.open_workbook(filename)
    # 查看文件中包含 sheet 的名称 
    data.sheet_names()
    # 得到第一个工作表 
    table = data.sheets()[0]
    table = data.sheet_by_index(0)
    table = data.sheet_by_name(u'Sheet1')
    # 获取行数和列数 
    nrows = table.nrows
    ncols = table.ncols
    print(nrows)
    print(ncols)
    # 遍历行，得到索引的列表 
    for rownum in range(table.nrows):
        print(table.row_values(rownum))
    # 分别使用行与列索引 
    cell_A1 = table.row(0)[0].value
    cell_A2 = table.col(1)[0].value
    print(cell_A1)
    print(cell_A2)


def xlwt_test():
    filename = PROJECT_PATH + '/file_location/xlwt_test.xlsx'
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
     num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')# 当前日期 

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')# sheet 的名字 

    ws.write(0, 0, 1234.56, style0)# 第 1 个单元格的内容 
    ws.write(1, 0, datetime.now(), style1)# 第 2 个单元格的内容 
    ws.write(2, 0, 1) # 第 3 个单元格的内容 
    ws.write(2, 1, 1) # 第 4 个单元格的内容 
    ws.write(2, 2, xlwt.Formula('A3+B3'))# 第 5 个单元格的内容 
    wb.save(filename)


if __name__ == "__main__":
    xlrd_test()
    xlwt_test()