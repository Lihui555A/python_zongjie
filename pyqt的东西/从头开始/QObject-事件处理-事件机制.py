#-*- coding:utf-8 -*-
from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QObject,QEvent
import sys
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=Button(self)
        button.setText('我是按钮')
        button.move(100,100)
        button.clicked.connect(self.button_click_fun)
        #下面介绍pyqt点击按钮后是怎么样连接上槽函数的，当用户点击按钮的时候，会产生事件消息，最先接收
        # 这个事件消息的是操作系统，然后操作系统会把这个事件消息发送给应用程序的消息队列，因为应用程序是开着的，
        #所以一直处于监听事件消息的状态，一旦接收到新的事件消息，就会把这个事件消息包装成一个事件对象，然后
        #把这个事件对象发送给QApplication的notify方法，然后notify方法会把这个接收者（被点击的控件）和消息对象
        #（怎么点击的单击，还是双击等等）进行特定的分发，分发给事件接收者的event方法，这里的事件接受者是这个按钮，也就是按钮中的event方法
    def button_click_fun(self):
        print('点我了') #
class App(QApplication):
    def notify(self,recevier,event): #括号里的参数一个是事件的接收者，一个是事件本身
        if recevier.inherits('QPushButton')and event.type()==QEvent.MouseButtonPress:
            print(recevier,event)

        return super(App,self).notify(recevier,event)  #这里调用父类的方法，括号里的参数一个是事件的接收者，一个是事件本
        # 身，然后这个函数根据这两个参数会返回一个
class Button(QPushButton):
    def event(self, event):
        if  event.type()==QEvent.MouseButtonPress:
            print('鼠标被点击了')
        return super(Button,self).event(event) #其实在原来的这个按钮类的所有事件中，其中当你点击了按钮之
        # 后会调用这个按钮类的MousePressEvent方法，这个方法原来是用来给你连接的槽函数发射信号的，现在我们在下面重写一下他
    def mousePressEvent(self, QMouseEvent):
        print('点击我把，我会把原来的信号与槽断开')
        return super(Button,self).mousePressEvent(QMouseEvent) #有了这句话就就不会中断了
if __name__ == '__main__':
    app=App(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())