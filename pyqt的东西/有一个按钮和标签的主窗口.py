# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '有一个按钮和标签的主窗口.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 600)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)  #实例化一个中心窗口控件
        # self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #实例化一个中按钮放在这个中心窗口控件上
        self.pushButton.setGeometry(QtCore.QRect(200, 160, 75, 23))  #按钮的绝对位置
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)  #实例化一个标签放在这个中心窗口控件上
        self.label.setGeometry(QtCore.QRect(210, 280, 54, 12))  #标签的大小以及位置
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)       #把这个中心窗口控件放在主窗口上
        self.menubar = QtWidgets.QMenuBar(MainWindow)         #实例化一个菜单栏控件放在主窗口上
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))   #设置菜单栏的位置和大小
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)                 #把这个菜单栏放在主窗口上
        self.statusbar = QtWidgets.QStatusBar(MainWindow)     #实例化一个状态栏控件在主窗口上
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)                #把状态栏放在主窗口上

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "哈哈"))
        self.label.setText(_translate("MainWindow", "呵呵呵"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

