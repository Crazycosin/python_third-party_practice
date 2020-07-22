'''
@Descripttion: 
@version: 
@Author: crazycosin
@Date: 2020-07-22 20:24:29
@LastEditors: crazycosin
@LastEditTime: 2020-07-22 21:27:16
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


def pyqt5_test():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('First')
    w.show()
    sys.exit(app.exec_())


class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()                        #用函数 initUI()创建 GUI

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Crazycosin')
        self.setWindowIcon(QIcon('123.ico'))
        self.show()


import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                               QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('这是一个<b>QWidget</b>组件')

        btn = QPushButton('按钮', self)
        btn.setToolTip('这是一个<b>QPushButton</b>组件')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('工具栏')
        self.show()
     

def pyqt5_test_1():
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())


def pyqt5_test_2():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # pyqt5_test()
    # pyqt5_test_1()
    pyqt5_test_2()