#-*- coding:utf-8 -*-
from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        label=Label(self,'100')
        self.label=label
        button=QPushButton(self)
        button.setText('开始倒计时')
        button.clicked.connect(self.open_or_stop)
        self.button=button
    def open_or_stop(self):
        if self.button.text()=='开始倒计时':
            self.label.start()
            self.button.setText('停止倒计时')
        else:
            self.label.stop()
            self.button.setText('开始倒计时')
class Label(QLabel):
    def __init__(self,window,value):
        super(Label,self).__init__(window)
        self.setText(value)
        self.move(250, 250)
        self.setStyleSheet('font-size:50px')
          # 标签控件中有这个startTimer(1000)方法，其中1000代表是1秒，每隔一秒会调用label类中
        # 的timerEvent方法，然后在label类中重写这个方法就可以了
    def timerEvent(self,event):
        newtext=int(self.text())
        newtext-=1
        self.setText(str(newtext))
    def start(self):
        self.time_id = self.startTimer(1000)
        print(self.time_id)
    def stop(self):
        self.killTimer(self.time_id)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())