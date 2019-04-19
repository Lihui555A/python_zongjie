from PyQt5.Qt import QApplication,QMainWindow,QLabel
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
        self.statusBar()#窗口的状态栏，用到的时候加上这句话就出来了
        self.setStatusTip('当鼠标放到某个设置这个功能的空间上的时候会显示在状态栏的文字')
    def setup_ui(self):
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())