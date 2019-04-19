# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.resize(600, 400)
        self.setWindowTitle("label显示图片")
        self.label = QLabel(self)
        self.label.setText("   显示图片")
        self.label.setFixedSize(300, 200)
        self.label.move(160, 160)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        #D:\anacanda\Anaconda3\Lib\site - packages\PyQt5\Qt\plugins\platforms
        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())





# from PyQt5 import QtWidgets, QtGui
# import sys
# from first import Ui_Form   # 导入生成first.py里生成的类
# from PyQt5.QtWidgets import QFileDialog
# class mywindow(QtWidgets.QWidget,Ui_Form):
#     def __init__(self):
#         super(mywindow,self).__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.openimage)
#         #定义槽函数
#     def openimage(self):
#    # 打开文件路径
#    #设置文件扩展名过滤,注意用双分号间隔
#         imgName,imgType= QFileDialog.getOpenFileName(self,
#                                     "打开图片",
#                                     "",
#                                     " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
#
#         print(imgName,imgType)
#         #利用qlabel显示图片
#         png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
#         self.label.setPixmap(png)
# app = QtWidgets.QApplication(sys.argv)
# window = mywindow()
# window.show()
# sys.exit(app.exec_())
