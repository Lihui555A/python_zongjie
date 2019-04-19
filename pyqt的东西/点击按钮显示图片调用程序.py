from PyQt5 import QtCore, QtGui, QtWidgets
from 点击按钮显示图片 import Ui_Form
from PyQt5 import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, QObject,QThread,pyqtSignal
import sys
sys.path.append('C:\Faster-RCNN-TensorFlow-Python3.5-master')
import demo
class Workthread(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        demo.running()
class myDialog(QtWidgets.QWidget,Ui_Form):#继承自Ui_MainWindow                         #这里改成你画好的界面
    def __init__(self,Dialog):
        super(myDialog, self).__init__()
        self.setupUi(Dialog)
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: black;\n"
                                 "     border-width: 1px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        #设置控制台背景和形状
        Dialog.setStyleSheet('''QWidget#button_widget{       
                background:lightgray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px; }
                
        ''')
        self.pushButton.setStyleSheet(
            '''QPushButton{color:white;background:black;border-radius:5px;}QPushButton:hover{background:gray;}''')
        self.pushButton_2.setStyleSheet(
            '''QPushButton{color:white;background:black;border-radius:5px;}QPushButton:hover{background:gray;}''')
        self.pushButton_3.setStyleSheet(
            '''QPushButton{color:white;background:black;border-radius:5px;}QPushButton:hover{background:gray;}''')
        self.pushButton_4.setStyleSheet(
            '''QPushButton{color:white;background:black;border-radius:5px;}QPushButton:hover{background:gray;}''')
        self.pushButton_5.setStyleSheet(
            '''QPushButton{color:white;background:black;border-radius:5px;}QPushButton:hover{background:gray;}''')

        self.pushButton.clicked.connect(self.openimage)

        self.pushButton_5.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.detect)

        #self.workthread.timer.connect(self.object)
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "",   " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
    def close(self):
        qApp = QtWidgets.QApplication.instance()
        qApp.quit()
    def object(self):
        for i in range(1000000000000):
            print(i)
    def detect(self):
        self.workthread = Workthread()
        self.workthread.start()
        #self.workthread.run()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = myDialog(MainWindow)#注意把类名修改为myDialog

    MainWindow.show()
    sys.exit(app.exec_())