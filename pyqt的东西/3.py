# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
class Ui_Form(object):
    def setupUi(self, Form):     #这个函数接受一个实例化的窗口对象
        Form.resize(500, 616)#在这里这个窗口对象设定了自己的大小
        Form.setWindowIcon(QIcon('bus.png')) #
        self.pushButton = QtWidgets.QPushButton(Form)  #
        self.pushButton.setGeometry(QtCore.QRect(240, 140, 75, 23))

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 290, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
       # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "窗体"))
        self.pushButton.setText(_translate("Form", "按钮"))
        self.label.setText(_translate("Form", "标签"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()   #实例化一个一般窗口
    ui = Ui_Form()  #实例化自己设计的类
    ui.setupUi(Form) #对象调用自己设计的类的方法，参数是传一个实例化的窗口对象
    Form.show()
    sys.exit(app.exec_())

