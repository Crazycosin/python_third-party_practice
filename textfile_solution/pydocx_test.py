from docx import Document
from textfile_solution import PROJECT_PATH
from docx import Document
from PIL import Image, ImageDraw
from io import BytesIO
import psutil


def create_doc():
    document = Document()
    document.add_paragraph('Hello,Word!')
    filename = PROJECT_PATH + '/file_location/demo.docx'
    document.save(filename)


def insert_graph_doc():
    document = Document()                        #新建文档 
    p = document.add_paragraph()                 #添加一个段落 
    r = p.add_run()                              #添加一个游程 
    img_size = 20
    for x in range(20):
        im = Image.new('RGB', (img_size, img_size), 'white')
        draw_obj = ImageDraw.Draw(im)
        draw_obj.ellipse((0, 0, img_size-1, img_size-1), fill=255-x)#画圆 
        fake_buf_file = BytesIO()          #用 BytesIO 将图片保存在内存里，减少磁盘操作 
        im.save(fake_buf_file, 'png')
        r.add_picture(fake_buf_file)            #在当前游程中插入图片 
        fake_buf_file.close()
        filename = PROJECT_PATH + '/file_location/demo.docx'
        document.save(filename)


def create_structure_doc():
    doc = Document()
    doc.add_paragraph(u'Python 为什么这么受欢迎？', 'Title')
    doc.add_paragraph(u'作者','Subtitle')
    doc.add_paragraph(u'摘要：本文阐明了 Python 的优势...','Body Text 2')
    doc.add_paragraph(u'简单', 'Heading 1')
    doc.add_paragraph(u'易学')
    doc.add_paragraph(u'易用', 'Heading 2')
    doc.add_paragraph(u'功能强')
    p = doc.add_paragraph(u'贴合小年轻')
    p.style = 'Heading 2'
    doc.save('demo.docx')


def style_doc():
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    doc = Document()
    styles = doc.styles
    print("\n".join([s.name for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH]))


def read_doc_test():
    from docx import Document
    import sys
    path = PROJECT_PATH + "/file_location/demo.docx"
    document = Document(path)
    for p in document.paragraphs:
        print(len(p.text))
        print(p.style.name)
        print(p.text)


def create_cell_doc_test():
    #获取当前计算机的配置 
    vmem = psutil.virtual_memory()
    vmem_dict = vmem._asdict()

    trow = 2
    tcol = len(vmem_dict.keys())
    #产生表格 

    document = Document()
    path = PROJECT_PATH + "/file_location/table.docx"
    table = document.add_table(rows=trow,cols=tcol,style = 'Table Grid')
    for col, info in enumerate(vmem_dict.keys()):
        table.cell(0,col).text = info
        if info == 'percent':
            table.cell(1,col).text = str(vmem_dict[info])+ '%'
        else:
            table.cell(1,col).text = str(vmem_dict[info]/(1024*1024)) + 'MB'
    document.save(path)


def operate_cell_doc_test():
    document = Document()
    table = document.add_table(rows=9, cols=10, style = 'Table Grid')
    cell_1 = table.cell(1,2)
    cell_2 = table.cell(4,6)
    cell_1.merge(cell_2)
    path = PROJECT_PATH + "/file_location/table-1.docx"
    path_2 = PROJECT_PATH + "/file_location/table-2.docx"
    document.save(path)

    document = Document(path)
    table = document.tables[0]
    for row,obj_row in enumerate(table.rows):
        for col,cell in enumerate(obj_row.cells):
            cell.text = cell.text + "%d,%d " % (row,col)
    document.save(path_2)


def operate_cell_doc_1_test():
    document = Document()
    path = PROJECT_PATH + "/file_location/table-step.docx"
    for row in range(9):
        t = document.add_table(rows=1, cols=1, style='Table Grid')
        t.autofit = False  # 很重要，必须设置 
        w = float(row) / 2.0
        t.columns[0].width = Inches(w)

    document.save('table-step.docx')


if __name__ == "__main__":
    create_doc()
    insert_graph_doc()