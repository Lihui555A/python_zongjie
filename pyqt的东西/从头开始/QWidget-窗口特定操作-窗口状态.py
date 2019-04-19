from PyQt5.Qt import QApplication,QWidget,QLabel,Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
        # self.setWindowState(Qt.WindowMaximized)#设置窗口最大化
        # self.setWindowState(Qt.WindowFullScreen)  # 设置窗口全屏，连标题栏也没有了
        # self.setWindowState(Qt.WindowActive)  # 设置窗口活跃状态，总是在最上层
        # self.showFullScreen()#设置窗口全屏
        # self.showMaximized()#设置窗口最大化
        # self.showNormal()#展示窗口普通大小
    def setup_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)#去掉窗口的标题栏
    def mousePressEvent(self,QMouseEvent):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())