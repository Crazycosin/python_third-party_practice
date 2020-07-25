'''
@Descripttion: 
@version: 
@Author: crazycosin
@Date: 2020-07-25 18:35:58
@LastEditors: crazycosin
@LastEditTime: 2020-07-25 18:51:20
'''
import sys
from PyQt5.QtWidgets import (
    QAction, QApplication, QWidget, 
    QMainWindow, qApp,
    QLabel, QHBoxLayout,
    QPushButton, QVBoxLayout,
    QGridLayout, QFormLayout,
    QLineEdit, QTextEdit)
from PyQt5.QtGui import QIcon
from __init__ import PROJECT_PATH


def widget_test():
    class Example(QWidget):
      def __init__(self):
           super().__init__()
           self.initUI()

      def initUI(self):
           lbl1 = QLabel('第 1 行文本', self)
           lbl1.move(15, 10)
           lbl2 = QLabel('第 2 行文本', self)
           lbl2.move(35, 40)
           lbl3 = QLabel('第 3 行文本', self)
           lbl3.move(55, 70)
           self.setGeometry(300, 300, 250, 150)
           self.setWindowTitle('Absolute')
           self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def widget_test_2():
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            okButton = QPushButton('确定')
            cancelButton = QPushButton('取消')
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(okButton)
            hbox.addWidget(cancelButton)
            vbox = QVBoxLayout()
            vbox.addStretch(1)
            vbox.addLayout(hbox)
            self.setLayout(vbox)
            self.setGeometry(300, 300, 300, 150)
            self.setWindowTitle('按钮布局')
            self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def widget_test_3():
    class Example(QWidget):
      def __init__(self):
           super().__init__()
           self.initUI()

      def initUI(self):
           grid = QGridLayout()
           self.setLayout(grid)
           names = ['删除', '后退', '', '关闭',
                     '7', '8', '9', '除',
                     '4', '5', '6', '乘',
                     '1', '2', '3', '减',
                     '0', '.', '=', '加']

           positions = [(i, j) for i in range(5) for j in range(4)]
           for position, name in zip(positions, names):
                if name == '':
                     continue
                button = QPushButton(name)
                grid.addWidget(button, *position)
           self.move(300, 150)
           self.setWindowTitle('模拟计算器')
           self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def widget_test_4():
    class Example(QWidget):
      def __init__(self):
           super().__init__()
           self.Init_UI()

      def Init_UI(self):
           self.setGeometry(300,300,300,200)
           self.setWindowTitle('留言板系统')
           formlayout = QFormLayout()
           nameLabel = QLabel('标题')
           nameLineEdit = QLineEdit('')
           introductionLabel = QLabel('内容')
           introductionLineEdit = QTextEdit('')
           formlayout.addRow(nameLabel, nameLineEdit)
           formlayout.addRow(introductionLabel, introductionLineEdit)
           self.setLayout(formlayout)
           self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # widget_test()
    # widget_test_2()
    # widget_test_3()
    widget_test_4()