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
        button.setFlat(True)  #这句话会把窗口的边框和背景颜色去掉
        button_2 = QPushButton(self)
        button_2.setText('我是按钮二')
        button_2.move(100,100)
        button_2.setDefault(True)#打开窗口直接默认被选中



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())