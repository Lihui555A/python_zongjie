from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=QPushButton(self)
        button.setText('我是按钮')#这样设置的是alt+a快捷键
        button.clicked.connect(lambda:print('点击我了'))
        button.setAutoRepeat(True) #先把自动重复开关打开
        button.setAutoRepeatInterval(1000)# 设置重复间隔
        button.setAutoRepeatDelay(5000)# 设置首次自动重复间隔




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())