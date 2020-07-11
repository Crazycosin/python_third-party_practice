from docx import Document
from textfile_solution import PROJECT_PATH
from docx import Document
from PIL import Image，ImageDraw
from io import BytesIO


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
        im = Image.new('RGB', (img_size，img_size),'white')
        draw_obj = ImageDraw.Draw(im)
        draw_obj.ellipse((0, 0, img_size-1, img_size-1), fill=255-x)#画圆 
        fake_buf_file = BytesIO()             #用 BytesIO 将图片保存在内存里，减少磁盘操作 
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


if __name__ == "__main__":
    create_doc()
    insert_graph_doc()