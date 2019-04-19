from PyQt5.Qt import QApplication,QWidget,QLabel,QProgressBar,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        pro=progressbar(self)
        pro.move(100,200)
        pro.resize(300,10)
        self.pro=pro
        button=QPushButton('开始',self)
        button.move(120,220)
        self.button=button
        self.button.clicked.connect(self.start_stop)
    def start_stop(self):
        if self.button.text()=='开始':
            self.button.setText('停止')
            self.pro.start()
        else:
            self.button.setText('开始')
            self.pro.stop()
class progressbar(QProgressBar):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.num=0
    def start(self):
        self.time_id=self.startTimer(100)
    def timerEvent(self, QTimerEvent):
        self.num+=1
        self.setValue(self.num)
    def stop(self):
        self.killTimer(self.time_id)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())