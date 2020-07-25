'''
@Descripttion: 
@version: 
@Author: crazycosin
@Date: 2020-07-25 18:52:32
@LastEditors: crazycosin
@LastEditTime: 2020-07-25 21:02:35
'''
import sys
from PyQt5.QtWidgets import (
    QAction, QApplication, QWidget, 
    QMainWindow, qApp,
    QLabel, QHBoxLayout,
    QPushButton, QVBoxLayout,
    QGridLayout, QFormLayout,
    QLineEdit, QTextEdit, QSlider,
    QLCDNumber, QMessageBox)
from PyQt5.QtCore import (
    QCoreApplication, Qt, QObject)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from __init__ import PROJECT_PATH
from random import randint


def event_test():
    class Ico(QWidget):
      def __init__(self):
           super().__init__()
           self.initUI()

      def initUI(self):
           self.setGeometry(300, 300, 300, 220)
           self.setWindowTitle('Crazycosin')
           self.setWindowIcon(QIcon('123.ico'))
           qbtn = QPushButton('退出', self)
           qbtn.clicked.connect(QCoreApplication.instance().quit)
           qbtn.resize(70,30)
           qbtn.move(50, 50)
           self.show()
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())


def event_test_2():
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            lcd = QLCDNumber(self)
            sld = QSlider(Qt.Horizontal, self)
            vbox = QVBoxLayout()
            vbox.addWidget(lcd)
            vbox.addWidget(sld)
            self.setLayout(vbox)
            sld.valueChanged.connect(lcd.display)
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('信号和槽')
            self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_test_3():
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('事件处理')
            self.show()

        def keyPressEvent(self, e):
            if e.key() == Qt.Key_Escape:
                self.close()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_test_4():
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUi()

        def initUi(self):
            self.setGeometry(300, 300, 350, 250)
            self.setWindowTitle('书创文化')
            self.lab = QLabel('移动方向', self)
            self.lab.setGeometry(150,100,50,50)
            self.show()

        def keyPressEvent(self, e):
            if e.key() == Qt.Key_Up:
                self.lab.setText('↑')
            elif e.key() == Qt.Key_Down:
                self.lab.setText('↓')
            elif e.key() == Qt.Key_Left:
                self.lab.setText('←')
            else:
                self.lab.setText('→')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_test_5():
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            self.setGeometry(200, 200, 300, 300)
            self.setWindowTitle('书创文化传播')
            bt1 = QPushButton('剪刀',self)
            bt1.setGeometry(30,180,50,50)
            bt2 = QPushButton('石头', self)
            bt2.setGeometry(100,180,50,50)
            bt3 = QPushButton('布',self)
            bt3.setGeometry(170,180,50,50)
            bt1.clicked.connect(self.buttonclicked)
            bt2.clicked.connect(self.buttonclicked)
            bt3.clicked.connect(self.buttonclicked)
            self.show()

        def buttonclicked(self):
            computer = randint(1,3)
            player = 0
            sender = self.sender()
            if sender.text() == '剪刀':
                player = 1
            elif sender.text() == '石头':
                player = 2
            else:
                player = 3
            if player == computer:
                QMessageBox.about(self, '结果', '平手')
            elif player == 1 and computer == 2:
                QMessageBox.about(self, '结果', '智者：石头，我赢了！')
            elif player == 2 and computer == 3:
                QMessageBox.about(self, '结果', '智者：布，我赢了！')
            elif player == 3 and computer == 1:
                QMessageBox.about(self, '结果', '智者：剪刀，我赢了！')
            elif computer == 1 and player == 2:
                QMessageBox.about(self, '结果','智者：剪刀，人类赢了！')
            elif computer == 2 and player == 3:
                QMessageBox.about(self, '结果', '智者：石头，人类赢了！')
            elif computer == 3 and player == 1:
                QMessageBox.about(self, '结果', '智者：布，人类赢了！')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_test_6():
    class Singal(QObject):
      showmouse = pyqtSignal()

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            self.setGeometry(200, 200, 300, 300)
            self.setWindowTitle('书创文化')
            self.s = Singal()
            self.s.showmouse.connect(self.about)

            self.show()
        def about(self):
            QMessageBox.about(self, '警告', '从实招来！你是不是按下鼠标了？')

        def mousePressEvent(self, e):
            self.s.showmouse.emit()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # event_test()
    # event_test_2()
    # event_test_3()
    # event_test_4()
    # event_test_5()
    event_test_6()