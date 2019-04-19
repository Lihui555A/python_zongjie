# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)  #给传进去的主窗口重新定义大小
        self.centralwidget = QtWidgets.QWidget(MainWindow) #弄一个窗口控件作为中心控件
        MainWindow.setCentralWidget(self.centralwidget) #把这个中心控件放在主窗口上
        self.menubar = QtWidgets.QMenuBar(MainWindow) # 实例化一个菜单栏控件这个是往主窗口上放的
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23)) #把菜单栏放在一个绝对位置上
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar) #   #把菜单栏对象放在主窗口上
        self.statusbar = QtWidgets.QStatusBar(MainWindow) #实例化一个状态栏控件
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar) #把状态栏控件放在主窗口上

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

