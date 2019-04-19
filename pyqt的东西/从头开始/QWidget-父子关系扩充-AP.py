from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        lable_1=Label(self)
        lable_1.move(100,100)
        lable_1.setText('标签一')
        lable_2 = Label(self)
        lable_2.move(200, 200)
        lable_2.setText('标签二')
        lable_3 = Label(self)
        lable_3.move(300, 300)
        lable_3.setText('标签三')

        print(self.childAt(100,100))#查看父控件上100,100的位置上有没有子控件
        print(lable_1.parentWidget())#查看lable_1的父控件是谁
        print(self.childrenRect())#查看父控件上的所有的子控件围成的矩形
class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.setStyleSheet('background-color:red')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())