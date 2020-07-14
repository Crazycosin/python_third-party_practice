import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from textfile_solution import PROJECT_PATH
import random
from urllib.request import urlopen, Request

#  解析 PDF 文本，保存到文本文件中 
def parse_local_pdf_test():
    filename = PROJECT_PATH + '/file_location/系统架构设计师考试全程指导.pdf'
    # 以二进制读模式打开 
    fp = open(filename, 'rb') 
    # 用文件对象来创建一个 PDF 文档分析器 
    praser = PDFParser(fp)
    # 创建一个 PDF 文档 
    doc = PDFDocument()
    # 连接分析器与文档对象 
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码 
    # 如果没有密码，就创建一个空的字符串 
    doc.initialize()

    # 检测文档是否提供转换方法，不提供就忽略 
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建 PDF 资源管理器来管理共享资源 
        rsrcmgr = PDFResourceManager()
        # 创建一个 PDF 设备对象 
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        #创建一个 PDF 解释器对象 
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        #遍历列表，每次处理一页的内容 
        for page in doc.get_pages(): #获取 page 列表 
            interpreter.process_page(page)
            # 接受该页面的 LTPage 对象 
            layout = device.get_result()
            # 这里 layout 是一个 LTPage 对象，里面存放着这个 page 解析出的各种对象，一般包括 
            #LTTextBox、LTFigure、LTImage、LTTextBoxHorizontal 等，要获取文本就需要获得对 
            #象的 text 属性 
            for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        with open(r'./file_location/123.txt', 'a') as f:
                                results = x.get_text()
                                print(results)
                                f.write(results + '\n')


def parse_online_pdf_test(url):
    #  解析 PDF 文本，保存到文本文件中 
    user_agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36']
    # fp = open（_path， 『rb』）  # rb 以二进制读模式打开本地 PDF 文件 
    # 随机从 user_agent 列表中抽取一个元素 
    request = Request(url=url, headers={'User-Agent': random.choice(user_agent)})
    # 打开在线 PDF 文档
    fp = urlopen(request)  

    # 用文件对象来创建一个 PDF 文档分析器 
    praser_pdf = PDFParser(fp)

    # 创建一个 PDF 文档 
    doc = PDFDocument()

    # 连接分析器与文档对象 
    praser_pdf.set_document(doc)
    doc.set_parser(praser_pdf)

    # 提供初始化密码 doc.initialize（「123456」）
    # 如果没有密码，就创建一个空的字符串 
    doc.initialize()

    #检测文档是否提供转换方法，不提供就忽略 
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #创建 PDF 资源管理器来管理共享资源 
        rsrcmgr = PDFResourceManager()

        #创建一个 PDF 参数分析器 
        laparams = LAParams()

        #创建聚合器 
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)

        #创建一个 PDF 页面解释器对象 
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        #遍历列表，每次处理一页的内容 
        #获取 page 列表 
        for page in doc.get_pages():
            #使用页面解释器来读取 
            interpreter.process_page(page)

            #使用聚合器获取内容 
            layout = device.get_result()

            #这里 layout 是一个 LTPage 对象，里面存放着这个 page 解析出的各种对象，一般包括 
            #LTTextBox、LTFigure、LTImage、LTTextBoxHorizontal 等，要获取文本就需要获得 
            #对象的 text 属性，
            for out in layout:
                    # 判断是否含有 get_text()方法 
                    # if hasattr（out，「get_text」）:
                    if isinstance(out, LTTextBoxHorizontal):
                        results = out.get_text()
                        print('results: ' + results)


if __name__ == '__main__':
     parse_local_pdf_test()
     url = 'https://github.com/Crazycosin/python_third-party_practice \
            /blob/master/textfile_solution/file_location/系统架构设计师考试全程指导.pdf'
     parse_online_pdf_test(url)