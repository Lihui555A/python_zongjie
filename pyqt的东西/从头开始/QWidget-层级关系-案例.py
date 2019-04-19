from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        label_1=Lable(self)
        label_1.resize(50,50)
        label_1.setStyleSheet('background-color:red')
        label_1.move(50,50)

        label_2 = Lable(self)
        label_2.resize(50, 50)
        label_2.setStyleSheet('background-color:black') #默认情况下后添加的控件在最上层
        label_2.move(90, 90)
        label_1.raise_()#把label_1放到上面
        label_1.lower()  # 把label_1放到下面
        label_1.stackUnder(label_2)#把lable_1放到lable_2下面
class Lable(QLabel):
    def mousePressEvent(self,QMouseEvent):
        self.raise_()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())