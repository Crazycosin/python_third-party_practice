import xlsxwriter  #导入模板 
from textfile_solution import PROJECT_PATH

def create_excel_test():
    filename = PROJECT_PATH + '/file_location/xlsxwriter-hello.xlsx'
    # 创建一个名为 hello.xlsx 的 workbook
    workbook = xlsxwriter.Workbook(filename)
    # 创建一个默认工作簿
    worksheet = workbook.add_worksheet()
    # 工作簿也支持命名，
    # 如 workbook.add_worksheet('hello')
    # 使用工作簿在 A1 中写入 Hello world
    worksheet.write('A1', 'Hello world')
    workbook.close()  # 关闭工作簿


def insert_multiple_data_test():
    """sumary_line
    批量插入数据
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    filename = PROJECT_PATH + '/file_location/xlsxwriter-Expenses01.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # 需要写入的数据 
    expenses = (['Rent', 1000],
               ['Gas', 100],
               ['Food', 300],
               ['Gym', 50],
    )

    # 行与列的初始位置 
    row = 0
    col = 0

    for item, cost in (expenses):
        # 在第一列写入 item
        worksheet.write(row, col, item)
        # 在第二列写入 cost
        worksheet.write(row, col + 1, cost)  
        row + 1  # 每次循环行数发生改变 

    worksheet.write(row, 0, 'Total')
    # 写入公式
    worksheet.write(row, 1, '=SUM(B1:B4)')  
    

def set_excel_style_test():
    # 创建文件及 sheet
    filename = PROJECT_PATH + '/file_location/xlsxwriter-Expenses03.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    # 设置粗体，默认是 False
    bold = workbook.add_format({'bold': True})
    # 定义数字格式 
    money = workbook.add_format({'num_format': '$#,##0'})
    # 自定义粗体格式 
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)
    # 写入表中的数据 
    expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],)

    # 从标题下面的第一个单元格开始 
    row = 1
    col = 0

    # 迭代数据并逐行地写入 
    for item, cost in (expenses):
        # 用默认格式写入
        worksheet.write(row, col, item)
        # 用自定义 money 格式写入
        worksheet.write(row, col + 1, cost, money)   
        row += 1

    # 用公式计算总数 
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 1, '=SUM(B2:B5)', money)

    workbook.close()


def insert_images_excel_test():
    # 创建一个新 Excel 文件并添加工作表 
    filename = PROJECT_PATH + '/file_location/xlsxwriter-images.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # 展开第一列，使正文更清楚 
    worksheet.set_column('A:A', 20)

    #  添加粗体格式用于突出显示单元格 
    bold = workbook.add_format({'bold': True})

    # 写一些简单的文字 
    worksheet.write('A1', 'Hello')
    # 设置文本与格式 
    worksheet.write('A2', 'World', bold)

    # 写入一些数字 
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)
    # 插入图像 
    worksheet.insert_image('B5', '123.png')
    workbook.close()


def insert_chart_excel_test():
    filename = PROJECT_PATH + '/file_location/xlsxwriter-chart.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # 新建图表对象 
    chart = workbook.add_chart({'type': 'column'})

# 向Excel 文件中写入数据，在建立图表时要用到 
    data = [
     [1, 2, 3, 4, 5],
     [2, 4, 6, 8, 10],
     [3, 6, 9, 12, 15],
    ]

    worksheet.write_column('A1', data[0])
    worksheet.write_column('B1', data[1])
    worksheet.write_column('C1', data[2])

    # 向图表中添加数据 
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
    chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

    # 将图标插入表单中 
    worksheet.insert_chart('A7', chart)

    workbook.close()


def insert_chart_excel_test_1():
    filename = PROJECT_PATH + '/file_location/xlsxwriter-chart_scatter.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    # 添加图表引用表格中的数据 
    headings = ['Number', 'Batch 1', 'Batch 2']
    data = [
        [2, 3, 4, 5, 6, 7],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
    ]

    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])

    # 创建一个散点图 
    chart1 = workbook.add_chart({'type': 'scatter'})

    #配置第一个系列的散点 
    chart1.add_series({
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
    })

    #配置第二个系列的散点，注意，使用替代语法来定义范围 
    chart1.add_series({
        'name':       ['Sheet1', 0, 2],
        'categories': ['Sheet1', 1, 0, 6, 0],
        'values':     ['Sheet1', 1, 2, 6, 2],
    })

    #添加图表标题和轴标签 
    chart1.set_title ({'name': 'Results of sample analysis'})
    chart1.set_x_axis({'name': 'Test number'})
    chart1.set_y_axis({'name': 'Sample length (mm)'})

    #设置 Excel 图表样式 
    chart1.set_style(11)

    #将图表插入工作表（带偏移量）中 
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()


def insert_chart_excel_test_2():
    # 新建一个 Excel 文件，命名为 chart-pie_line.xlsx
    filename = PROJECT_PATH + '/file_location/chart-pie_line.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    # 添加一个 Sheet，不写名字，默认为 Sheet1
    worksheet = workbook.add_worksheet()
    # 准备数据 
    headings=['姓名', '数学', '语文']
    data=[['C 罗张', 78, 60], ['糖人李', 98, 89], ['梅西徐', 88, 100]]
    # 样式
    head_style = workbook.add_format({'bold':True, 'bg_color': 'yellow', 'align': 'center', 'font':13})
    # 写数据 
    worksheet.write_row('A1',headings, head_style)
    for i in range(0, len(data)):
        worksheet.write_row('A{}'.format(i+2), data[i])
    # 添加柱状图 
    chart1 = workbook.add_chart({'type':'column'})
    chart1.add_series({
        'name': '=Sheet1！$B$1',#图例项 
        'categories': '=Sheet1！$A$2:$A$4', 
        'values': '=Sheet1！$B$2:$B$4'
    })
    chart1.add_series({
        'name':'=Sheet1！$C$1',
        'categories':'=Sheet1！$A$2:$A$4',
        'values':'=Sheet1！$C$2:$C$4'
    })
    # 添加柱状图标题 
    chart1.set_title({'name':'柱状图'})
    # &lt;em&gt;y&lt;/em&gt; 轴名称 
    chart1.set_y_axis({'name':'分数'})
    # &lt;em&gt;x&lt;/em&gt; 轴名称 
    chart1.set_x_axis({'name':'人名'})
    #图表样式 
    chart1.set_style(11)

    #添加柱状图叠图子类型 
    chart2 = workbook.add_chart({'type':'column','subtype':'stacked'})
    chart2.add_series({
        'name':'=Sheet1！$B$1',
        'categories':'=Sheet1！$A$2:$a$4',
        'values':'=Sheet1！$B$2:$B$4'
    })
    chart2.add_series({
        'name':'=Sheet1！$C$1',
        'categories':'=Sheet1！$A$2:$a$4',
        'values':'=Sheet1！$C$2:$C$4'
    })
    chart2.set_title({'name':'叠图子类型'})
    chart2.set_x_axis({'name':'姓名'})
    chart2.set_y_axis({'name':'成绩'})
    chart2.set_style(12)

    #添加饼图 
    chart3 = workbook.add_chart({'type':'pie'})
    chart3.add_series({
        #「name」:「饼形图」，
        'categories': '=Sheet1！$A$2:$A$4',
        'values': '=Sheet1！$B$2:$B$4',
        #定义各饼块的颜色 
        'points': [
            {'fill': {'color': 'yellow'}},
            {'fill': {'color': 'blue'}},
            {'fill': {'color': 'red'}}
        ]
        })
    chart3.set_title({'name': '饼图成绩单'})
    chart3.set_style(3)

    #插入图表 
    worksheet.insert_chart('B7',chart1)
    worksheet.insert_chart('B25', chart2)
    worksheet.insert_chart('J2',chart3)

    #关闭 Excel 文件 
    workbook.close()

if __name__ == "__main__":
    create_excel_test()
    insert_multiple_data_test()
    set_excel_style_test()
    insert_images_excel_test()
    insert_chart_excel_test()
    insert_chart_excel_test_1()
    insert_chart_excel_test_2()