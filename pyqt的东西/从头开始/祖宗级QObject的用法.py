#-*- coding:utf-8 -*-
from PyQt5.Qt import QWidget,QApplication,QObject,QLabel,qApp,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setup_ui()
        self.setWindowTitle('祖宗级QObject的用法')
        self.resize(500,500)
    def setup_ui(self):
        self.QObject_method()
        self.Use_QObject()

    def Use_QObject(self):
        with open('QObject.qss','r')as f:
            qApp.setStyleSheet(f.read()) #会根据qss样式表的要求去改变样式

    def QObject_method(self):

        label_1=QLabel(self)
        label_1.setObjectName('lable_1')
        label_1.setText('我是第一个标签')
        label_1.move(100,100)
        label_1.setStyleSheet('font-size:20px;color:red') #设置样式表
        label_2 = QLabel(self)
        label_2.setObjectName('lable_2')
        label_2.setText('我是第二个标签')
        label_2.move(200,200)
        label_3 = QLabel(self)
        label_3.setObjectName('lable_3')
        label_3.setText('我是第三个标签')
        label_3.move(300,300)

        button_1=QPushButton(self)
        button_1.setText('我是按钮一')
        button_1.setObjectName('button-1')
        button_1.move(120,120)
        button_2 = QPushButton(self)
        button_2.setText('我是按钮二')
        button_2.move(220, 220)
        button_2.setObjectName('button-2')
        button_3 = QPushButton(self)
        button_3.setText('我是按钮三')
        button_3.setObjectName('button-3')
        button_3.move(320,320)

        label_4 = QLabel(self)
        label_4.setObjectName('notice')
        label_4.setText('我是第四个标签')
        label_4.move(100, 200)
        label_4.setProperty('notice_level','error')
        label_5 = QLabel(self)
        label_5.setObjectName('notice')
        label_5.setText('我是第五个标签')
        label_5.move(100, 300)
        label_5.setProperty('notice_level', 'warning')
        label_6 = QLabel(self)
        label_6.setObjectName('notice')
        label_6.setText('我是第六个标签')
        label_6.move(100, 400)
        label_6.setProperty('notice_level', 'danger')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

