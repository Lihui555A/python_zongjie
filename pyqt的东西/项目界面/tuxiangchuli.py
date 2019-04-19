# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tuxiangchuli.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1153, 891)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 0, 321, 91))
        self.label.setStyleSheet("font: 28pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(50, 70, 1031, 751))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 1031, 699))
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(360, 20, 291, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(0, 90, 1031, 211))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 20, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.page)
        self.progressBar.setGeometry(QtCore.QRect(10, 330, 1011, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(50, 370, 311, 291))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page)
        self.textEdit_2.setGeometry(QtCore.QRect(650, 370, 311, 301))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 400, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 530, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(450, 470, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(150, 670, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(780, 680, 71, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 610, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 1031, 699))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        self.pushButton_3.clicked.connect(Form.denglu_pane_show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图像处理"))
        self.pushButton.setText(_translate("Form", "打开文件"))
        self.comboBox.setCurrentText(_translate("Form", "选择增强方法"))
        self.comboBox.setItemText(0, _translate("Form", "选择增强方法"))
        self.pushButton_2.setText(_translate("Form", "保存"))
        self.pushButton_4.setText(_translate("Form", "上一张"))
        self.pushButton_5.setText(_translate("Form", "下一张"))
        self.label_2.setText(_translate("Form", "共处理%s张图片"))
        self.label_3.setText(_translate("Form", "原图"))
        self.label_4.setText(_translate("Form", "增强后图片"))
        self.pushButton_3.setText(_translate("Form", "返回"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "图像增强"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "图像融合"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

