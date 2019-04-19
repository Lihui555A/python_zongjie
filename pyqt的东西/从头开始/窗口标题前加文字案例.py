#涉及到信号的中断和重新连接操作
from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
        self.setWindowTitle('第1个窗体')
        self.setWindowTitle('第2个窗体')
    def setup_ui(self):
        self.windowTitleChanged.connect(self.windowtitilechange_cao)
    def windowtitilechange_cao(self,name):
        self.windowTitleChanged.disconnect()  #效果等同于self.blockSignals(True)

        self.setWindowTitle('你好-'+name) #这里会进入一个无限的死循环的过程，需要做的就是在上面断开连接,这样就可以了
        self.windowTitleChanged.connect(self.windowtitilechange_cao) #效果等同于self.blockSignals(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())