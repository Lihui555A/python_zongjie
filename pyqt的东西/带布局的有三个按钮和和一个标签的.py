# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '带布局的有三个按钮和和一个标签的.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(686, 568) #这里有一个传进去的窗口组件，类是自己建立的

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 50, 271, 131))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 230, 239, 80))

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)

        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 80, 54, 12))

        self.label.setObjectName("label")

        self.retranslateUi(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "标签"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

