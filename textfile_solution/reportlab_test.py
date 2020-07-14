from reportlab.pdfgen import canvas
from textfile_solution import PROJECT_PATH
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import Color, magenta, cyan
from reportlab.graphics.barcode import (
    code39, code128, code93, eanbc, qr, usps)
from reportlab.graphics import renderPDF

def write_graph_test():
    #设置绘画开始的位置 
    filename = PROJECT_PATH + '/file_location/reportlab-graph.pdf'
    #定义要生成的 pdf 的名称 
    c=canvas.Canvas(filename)
    #调用函数进行绘画，并将 canvas 对象作为参数传递
    c.drawString(100, 100, 'hello world！')
    #showPage 函数：保存当前页的 canvas
    c.showPage()
    #save 函数：保存文件并关闭 canvas
    c.save()


def write_character_style_test():
    Style=getSampleStyleSheet()
    filename = PROJECT_PATH + '/file_location/reportlab-character_style.pdf'
    # 字体的样式
    bt = Style['Normal']
    # bt.fontName='song'   # 使用的字体
    # 字号 
    bt.fontSize=14
    # 该属性支持自动换行，』CJK『用于中文方式的换行，用于英文中会截断单词，造成
    bt.wordWrap = 'CJK'    
    # 阅读困难，可改为'Normal'
    # 该属性支持第一行开头的空格
    bt.firstLineIndent = 32
    # 该属性用于设置行距
    bt.leading = 20         

    ct=Style['Normal']
    # ct.fontName='song'
    ct.fontSize=12
    # 居中
    ct.alignment=1              
    ct.textColor = colors.red

    t = Paragraph('hello', bt)
    pdf=SimpleDocTemplate(filename)
    pdf.multiBuild([t])


def draw_vector_graph_test():
    filename  = PROJECT_PATH + '/file_location/reportlab-vector_graph.pdf'
    # 设置绘画开始的位置 
    def hello(c):
        #设置描边色 
        c.setStrokeColorRGB(0, 0, 1.0)
        #设置填充色 
        c.setFillColorRGB(1,0,1)
        # draw some lines
        c.line(0.1*inch, 0.1*inch, 0.1*inch, 1.7*inch)
        c.line(0.1*inch, 0.1*inch, 1*inch, 0.1*inch)
        # 画矩形 
        c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=1)
    # 定义要生成的 PDF 文件的名称 
    c=canvas.Canvas(filename)
    # 调用函数进行绘画，并作为参数传递 canvas 对象 
    hello(c)
    # 保存当前页的 canvas
    c.showPage()
    # 保存文件并关闭 canvas
    c.save()


def draw_image_test():
    filename = PROJECT_PATH + '/file_location/reportlab-image.pdf'
    def drawBitmap(c):
        c.drawImage('123.png', 5*mm， 5*mm， 62*mm， 88.6*mm)

    #定义要生成的 PDF 文件的名称 
    c=canvas.Canvas(filename)
    #调用函数生成条形码和二维码，并作为参数传递 canvas 对象 
    drawBitmap(c)
    #保存当前页的 canvas
    c.showPage()
    #保存文件并关闭 canvas
    c.save()


def draw_pie_chart_test():
    class pietests(_DrawingEditorMixin, Drawing):
        def __init__(self, width=400, height=200, *args, **kw):
            Drawing.__init__(self, width, height, *args, **kw)
            self._add(self, Pie(), name='pie', validate=None, desc=None)
            self.pie.sideLabels = 1
            self.pie.labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5']
            self.pie.data = [20, 10, 5, 5, 5]
            self.pie.width = 140
            self.pie.height = 140
            self.pie.y = 35
            self.pie.x = 125
    drawing = pietests()
    # you can do all sorts of things to drawing, lets just save it as pdf and png.
    drawing.save(formats=['pdf', 'png'], outDir='./file_location', fnRoot=None)
    return 0


def draw_qr_or_bar_code_test():
    def createBarCodes(c):
        barcode_value = '0112358'

        barcode39 = code39.Extended39(barcode_value)
        barcode39Std = code39.Standard39(barcode_value, barHeight=20, stop=1)

        barcode93 = code93.Standard93(barcode_value)

        barcode128 = code128.Code128(barcode_value)
        # barcode128Multi = code128.MultiWidthBarcode（barcode_value）

        barcode_usps = usps.POSTNET('50158-9999')

        codes = [barcode39, barcode39Std, barcode93, barcode128, barcode_usps]

        x = 1 * mm
        y = 285 * mm

        for code in codes:
            code.drawOn(c, x, y)
            y = y - 15 * mm

        barcode_eanbc8 = eanbc.Ean8BarcodeWidget(barcode_value)
        d = Drawing(50, 10)
        d.add(barcode_eanbc8)
        renderPDF.draw(d, c, 15, 555)

        barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
        d = Drawing(50, 10)
        d.add(barcode_eanbc13)
        renderPDF.draw(d, c, 15, 465)

        qr_code = qr.QrCodeWidget('http://www.baidu.com')
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(45, 45, transform=[45./width, 0,0,45./height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 15, 405)

    filename = PROJECT_PATH + '/file_location/reportlab-bar_or_qr.pdf'
    # 定义要生成的 PDF 文件的名称 
    c=canvas.Canvas(filename)
    # 调用函数生成条形码和二维码，并作为参数传递 canvas 对象 
    createBarCodes(c)
    # 保存当前页的 canvas
    c.showPage()
    # 保存文件并关闭 canvas
    c.save()


if __name__ == "__main__":
    write_graph_test()
    write_character_style_test()
    draw_vector_graph_test()
    draw_image_test()
    draw_pie_chart_test()
    draw_qr_or_bar_code_test()