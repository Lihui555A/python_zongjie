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
        button.setText('我是按钮')
        button.setEnabled(False)#设置控件是否可用
        print(button.isEnabled())



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())