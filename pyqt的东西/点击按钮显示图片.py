# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '点击按钮显示图片.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1165, 772)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(32, 32, 32, 23)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.button_widget = QtWidgets.QWidget(Form)
        self.button_widget.setObjectName("button_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.button_widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.button_widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 6, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 5, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 2)
        self.gridLayout.setColumnStretch(7, 1)
        self.gridLayout.setColumnStretch(8, 2)
        self.verticalLayout.addWidget(self.button_widget)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "多图模式"))
        self.pushButton.setText(_translate("Form", "单图模式"))
        self.pushButton_3.setText(_translate("Form", "启动识别"))
        self.pushButton_5.setText(_translate("Form", "返回"))
        self.pushButton_4.setText(_translate("Form", "查看结果"))
        self.pushButton_6.setText(_translate("Form", "下一张"))
        self.pushButton_7.setText(_translate("Form", "上一张"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

