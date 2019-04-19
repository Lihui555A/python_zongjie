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
        button.setText('开始变大')
        button.clicked.connect(self.start)
        self.button=button
    def start(self):
        if self.button.text()=='开始变大':
            self.button.setText('停止变大')
            self.time_id=self.startTimer(1000)
        else:
            self.button.setText('开始变大')
            self.killTimer(self.time_id)
    def timerEvent(self,event):
        width=self.width()
        width+=5
        height=self.height()
        height+=5
        self.resize(width,height)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())