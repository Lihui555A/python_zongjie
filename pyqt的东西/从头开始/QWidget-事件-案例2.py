from PyQt5.Qt import QApplication,QWidget,QLabel,QKeyEvent,Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        label=Lable(self)
        label.resize(200,200)
        label.setStyleSheet('background-color:red')
        label.move(100,100)
        label.grabKeyboard()#这里记得确定捕获键盘输入事件的对象，这个

class Lable(QLabel):
    def keyPressEvent(self, Event):  #Event是个事件对象，是QKeyEvent类的对象，这个类中有一些方法
        print('jjj')
        if Event.key()==Qt.Key_Tab:  #用来捕获用户具体按得是那个普通键
            print('用户点击了TAB')
        if Event.modifiers()==Qt.ControlModifier|Qt.ShiftModifier and Event.key()==Qt.Key_S: #用来捕获用户具体按的是那个特殊键
            print('用户点击啦control shift s键')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())