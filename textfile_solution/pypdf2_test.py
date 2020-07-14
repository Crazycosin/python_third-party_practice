from PyPDF2 import PdfFileReader, PdfFileWriter
from textfile_solution import PROJECT_PATH
import PyPDF2


def read_pdf_test():
    readFile = PROJECT_PATH + '/file_location/系统架构设计师考试全程指导.pdf'
    # 获取 PdfFileReader 对象 
    pdfFileReader = PdfFileReader(readFile)
    # 或者 pdfFileReader = PdfFileReader（open(readFile, 'rb')）
    # 获取 PDF 文件的文档信息 
    documentInfo = pdfFileReader.getDocumentInfo()
    print('documentInfo = %s' % documentInfo)
    # 获取页面布局 
    pageLayout = pdfFileReader.getPageLayout()
    print('pageLayout = %s ' % pageLayout)

    # 获取页模式 
    pageMode = pdfFileReader.getPageMode()
    print('pageMode = %s' % pageMode)

    xmpMetadata = pdfFileReader.getXmpMetadata()
    print('xmpMetadata  = %s ' % xmpMetadata)

    # 获取 PDF 文件的页数 
    pageCount = pdfFileReader.getNumPages()

    print('pageCount = %s' % pageCount)
    for index in range(0, pageCount):
        # 返回指定页码的 pageObject
        pageObj = pdfFileReader.getPage(index)
        print('index = %d , pageObj = %s' % (index, type(pageObj)))
        # &lt;class 『PyPDF2.pdf.PageObject'&gt;
        # 获取 pageObject 在 PDF 文档中的页码 
        pageNumber = pdfFileReader.getPageNumber(pageObj)
        print('pageNumber = %s ' % pageNumber)


def create_pdf_test():
    readFile = PROJECT_PATH + '/file_location/系统架构设计师考试全程指导.pdf'
    outFile = PROJECT_PATH + '/file_location/pypdf2-copy.pdf'
    pdfFileWriter = PdfFileWriter()

    # 获取 pdfFileReader 对象 
    pdfFileReader = PdfFileReader(readFile)
    # 或者 pdfFileReader = PdfFileReader（open(readFile, 'rb')）
    numPages = pdfFileReader.getNumPages()

    for index in range(0, numPages):
            pageObj = pdfFileReader.getPage(index)
            # 根据每页返回的 PageObject，写入文件 
            pdfFileWriter.addPage(pageObj)
            pdfFileWriter.write(open(outFile, 'wb'))

    pdfFileWriter.addBlankPage()   #在文件的最后一页写入一个空白页，保存至文件中 
    pdfFileWriter.write(open(outFile,'wb'))


def usageofpageobj_test(inFileList, outFile):
     """
     合并文档 
     :param inFileList: 要合并的文档的列表 
     :param outFile:    合并后的输出文件 
     :return:
     """
     pdfFileWriter = PdfFileWriter()
     for inFile in inFileList:
          # 依次打开要合并的文件 
          pdfReader = PdfFileReader(open(inFile, 'rb'))
          numPages = pdfReader.getNumPages()
          for index in range(0, numPages):
               pageObj = pdfReader.getPage(index)
               pdfFileWriter.addPage(pageObj)

          # 最后统一写入输出文件中 
          pdfFileWriter.write(open(outFile, 'wb'))


def usageofpageobj_split_test():
    readFile = PROJECT_PATH + '/file_location/pypdf2-copy.pdf'
    outFile =  PROJECT_PATH + '/file_location/pypdf2-split.pdf'
    pdfFileWriter = PdfFileWriter()

    # 获取 pdfFileReader 对象 
    pdfFileReader = PdfFileReader(readFile)
    # 或者 pdfFileReader = PdfFileReader（open(readFile, 'rb')）
    # 文档总页数 
    numPages = pdfFileReader.getNumPages()
    if numPages > 5:
        # 将第 5 页之后的页面输出到一个新的文件中，即分割文档 
        for index in range(5, numPages):
            pageObj = pdfFileReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
        # 添加完之后一起保存至文件中 
        pdfFileWriter.write(open(outFile, 'wb'))


def merge_three_pdfs():
    pdff1 = open("./file_location/pypdf2-copy.pdf", "rb")
    pr = PyPDF2.PdfFileReader(pdff1)
    print(pr.numPages)

    pdff2 = open("./file_location/pypdf2-out.pdf", "rb")
    pr2 = PyPDF2.PdfFileReader(pdff2)

    pdf3 = open("./file_location/pypdf2-split.pdf", "rb")
    pr3 = PyPDF2.PdfFileReader(pdf3)

    pdfw = PyPDF2.PdfFileWriter()
    pageobj = pr.getPage(0)
    pdfw.addPage(pageobj)

    for pageNum in range(pr2.numPages):
        pageobj2 = pr2.getPage(pageNum)
        pdfw.addPage(pageobj2)

    pageobj3 = pr3.getPage(0)
    pdfw.addPage(pageobj3)

    pdfout = open("aaa.pdf", "wb")
    pdfw.write(pdfout)
    pdfout.close()
    pdff1.close()
    pdff2.close()
    pdf3.close()


if __name__ == "__main__":
    read_pdf_test()
    create_pdf_test()
    inFileList = [
        PROJECT_PATH + '/file_location/pypdf2-copy.pdf',
        PROJECT_PATH + '/file_location/pypdf2-copy.pdf',
    ]
    outFile = PROJECT_PATH + '/file_location/pypdf2-out.pdf'
    usageofpageobj_test(inFileList, outFile)
    usageofpageobj_split_test()
