# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '自己做的音乐播放器.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1056, 864)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_8.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_7, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))

        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 2, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 104))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 92))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.toolButton = QtWidgets.QToolButton(self.widget_5)
        self.toolButton.setMinimumSize(QtCore.QSize(0, 95))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/100.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(133, 72))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_6.addWidget(self.toolButton, 0, 2, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.widget_5)
        self.toolButton_4.setMinimumSize(QtCore.QSize(0, 95))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(133, 72))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_6.addWidget(self.toolButton_4, 0, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget_5)
        self.toolButton_2.setMinimumSize(QtCore.QSize(0, 95))
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(133, 72))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_6.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_5)
        self.toolButton_3.setMinimumSize(QtCore.QSize(0, 95))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(133, 72))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_6.addWidget(self.toolButton_3, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.widget_5, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 96))
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_7.addWidget(self.pushButton_20, 2, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_7.addWidget(self.pushButton_16, 1, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_7.addWidget(self.pushButton_17, 4, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_7.addWidget(self.pushButton_19, 3, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_7.addWidget(self.pushButton_18, 5, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_7.addWidget(self.pushButton_21, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_6, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(334, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 63))
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_8)
        self.toolButton_5.setIcon(icon)
        self.toolButton_5.setIconSize(QtCore.QSize(143, 81))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_9.addWidget(self.toolButton_5, 0, 0, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.widget_8)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(143, 81))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_9.addWidget(self.toolButton_6, 0, 1, 1, 1)
        self.toolButton_7 = QtWidgets.QToolButton(self.widget_8)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(143, 81))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setObjectName("toolButton_7")
        self.gridLayout_9.addWidget(self.toolButton_7, 1, 0, 1, 1)
        self.toolButton_8 = QtWidgets.QToolButton(self.widget_8)
        self.toolButton_8.setIcon(icon)
        self.toolButton_8.setIconSize(QtCore.QSize(143, 81))
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_8.setObjectName("toolButton_8")
        self.gridLayout_9.addWidget(self.toolButton_8, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget_8, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_4, 1, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_10.addWidget(self.pushButton_22, 0, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_10.addWidget(self.pushButton_23, 0, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_10.addWidget(self.pushButton_24, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(256, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayout_5.addWidget(self.widget_9, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 11, 0, 1, 3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 12, 0, 1, 3)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 3, 0, 1, 3)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 10, 0, 1, 3)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 9, 0, 1, 3)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 1, 0, 1, 3)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_3.addWidget(self.pushButton_13, 4, 0, 1, 3)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 2, 0, 1, 3)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 8, 0, 1, 3)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_3.addWidget(self.pushButton_14, 6, 0, 1, 3)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_3.addWidget(self.pushButton_15, 5, 0, 1, 3)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 7, 0, 1, 3)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 8)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "搜索   "))
        self.toolButton.setText(_translate("Form", "你说中部"))
        self.toolButton_4.setText(_translate("Form", "你妹妹的"))
        self.toolButton_2.setText(_translate("Form", "我不知道"))
        self.toolButton_3.setText(_translate("Form", "我觉得可"))
        self.label_2.setText(_translate("Form", "  今日推荐"))
        self.pushButton_20.setText(_translate("Form", "多费劲顺丰加    打飞机   打飞机老司机   京东方肯德基"))
        self.pushButton_16.setText(_translate("Form", "哈        给谁看     合肥市考核分时间段   好几十附近 "))
        self.pushButton_17.setText(_translate("Form", "副书记分类就      的加减法       见附件  夹打开分类及"))
        self.pushButton_19.setText(_translate("Form", "分手就分手框里     技术附件       粉红色的尽快发货"))
        self.pushButton_18.setText(_translate("Form", "福建省会计法      地方                 烦上加烦"))
        self.pushButton_21.setText(_translate("Form", "呵呵呵 不知道该怎么  的加减法抗裂砂浆    是咖啡机     大"))
        self.label_4.setText(_translate("Form", "热门歌单"))
        self.label_3.setText(_translate("Form", "最新歌曲"))
        self.toolButton_5.setText(_translate("Form", "福建省开了房间激地方"))
        self.toolButton_6.setText(_translate("Form", "电风扇水电费发顺丰地方"))
        self.toolButton_7.setText(_translate("Form", "所发生的防守打法"))
        self.toolButton_8.setText(_translate("Form", "发送到发送到发送到他也"))
        self.pushButton_22.setText(_translate("Form", "PushButton"))
        self.pushButton_23.setText(_translate("Form", "PushButton"))
        self.pushButton_24.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))
        self.pushButton_11.setText(_translate("Form", "PushButton"))
        self.pushButton_13.setText(_translate("Form", "PushButton"))
        self.pushButton_12.setText(_translate("Form", "PushButton"))
        self.pushButton_10.setText(_translate("Form", "PushButton"))
        self.pushButton_14.setText(_translate("Form", "PushButton"))
        self.pushButton_15.setText(_translate("Form", "PushButton"))
        self.pushButton_9.setText(_translate("Form", "PushButton"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

