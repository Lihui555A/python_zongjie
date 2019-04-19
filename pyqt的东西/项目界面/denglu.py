# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1128, 764)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 540, 231, 191))
        self.pushButton_2.setStyleSheet("QPushButton{border-radius:25px;border: 2px solid gray;font: 18pt \"Agency FB\";}\n"
"QPushButton:hover{border:2px solid red;}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 80, 221, 161))
        self.pushButton_3.setStyleSheet("QPushButton{border-radius:25px;border: 2px solid gray;font: 18pt \"Agency FB\";}\n"
"QPushButton:hover{border:2px solid red;}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 60, 241, 171))
        self.pushButton_4.setStyleSheet("QPushButton{border-radius:25px;border: 2px solid gray;font: 18pt \"Agency FB\";}\n"
"QPushButton:hover{border:2px solid red;}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 530, 241, 181))
        self.pushButton_5.setStyleSheet("QPushButton{border-radius:25px;border: 2px solid gray;font: 18pt \"Agency FB\";}\n"
"QPushButton:hover{border:2px solid red;}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(340, 190, 431, 401))
        self.widget.setStyleSheet("QWidget#widget{border:2px solid gray;border-radius:25px;}")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(240, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 290, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 140, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 200, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(140, 140, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(140, 210, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 271, 61))
        self.label_3.setStyleSheet("font: 36pt \"微软雅黑\";\n"
"font: 24pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(Form.shuxinshibie_pane_show)
        self.pushButton_3.clicked.connect(Form.tuxiangchuli_pane_show)
        self.pushButton_5.clicked.connect(Form.mubiaozhuizong_pane_show)
        self.pushButton_2.clicked.connect(Form.shujuguanli_pane_show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "数据管理"))
        self.pushButton_3.setText(_translate("Form", "图像处理"))
        self.pushButton_4.setText(_translate("Form", "属性识别"))
        self.pushButton_5.setText(_translate("Form", "目标跟踪"))
        self.pushButton.setText(_translate("Form", "取消"))
        self.pushButton_6.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "属性识别管理系统"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

