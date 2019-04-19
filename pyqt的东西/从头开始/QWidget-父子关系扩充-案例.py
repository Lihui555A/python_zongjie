from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        for i in range(20):
            label=QLabel(self)
            label.setText('label_'+str(i))
            label.move(20*i,20*i)

    def mousePressEvent(self, QMouseEvent):#这里有必要解释一下，当我们在界面上点击标签控件的时候，会触发标签控件的鼠标点击事件，
        # 但是默认情况下标签控件的鼠标点击事件是不做任何事情，如果想做需要我们自己去定义，但是因为标签控件有
        # 父控件，标签控件没做的事会继承给父控件的鼠标点击事件，而在这里我们给父控件的鼠标点击事件做了处理，就有了这样处理的结果
        x=QMouseEvent.x()
        y=QMouseEvent.y()
        widget=self.childAt(x,y)
        if widget!=None:
            widget.setStyleSheet('background-color:yellow')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())