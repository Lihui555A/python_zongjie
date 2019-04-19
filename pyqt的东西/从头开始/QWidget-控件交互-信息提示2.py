from PyQt5.Qt import QApplication,QWidget,QLabel,QMainWindow
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
        self.statusBar()
        self.setStatusTip('现在在窗口区域')

    def setup_ui(self):
        lable=QLabel(self)
        lable.setText('我是标签')
        lable.setStatusTip('现在在标签区域')
        lable.setToolTip('这是一个标签') #放在调用这个方法的控件上一会就会出现提示框
        lable.setToolTipDuration(1000)#设置展示时长



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())