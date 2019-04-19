
#查看某个类继承自哪个直接父类用print(QWidget.__bases__)这句话就可以了，QWidget是想要查询的类名
#查看所有的某各类的家谱类，用 print(QWidget.mro())
from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.move(100,100)
        self.label=QLabel(self)
        self.label.move(20,20)
        self.label.resize(50,20)
        self.label.setStyleSheet('background-color:red')
    #     self.setup_ui()
    # def setup_ui(self):
    #     print(self.x()) #如果是父控件，则表示框架左上角距离屏幕左上角的位置，
    #     print(self.label.x())#如果不是父控件则表示自己的左上角距离父控件左上角的位置
    #
    #     print(self.pos()) #x()和y()的组合
    #     print(self.label.pos())
    #
    #     print(self.width())#客户区宽度
    #     print(self.label.width())
    #
    #
    #
    #     print(self.size())#客户区宽和高
    #     print(self.label.size())
    #
    #
    #     print(self.geometry()) #控件客户区左上角相对于父控件的左上角的位置，和客户区的大小,这些控件都是要看是不是顶层窗口控件的如果是顶层窗口控件
    #     # 位置指的一般都是客户区左上角距离屏幕左上角的距离，如果是子控件表示都是子控件左上角相对于父控件的客户区的左上角的距离
    #     print(self.label.geometry())
    #     # print(self.geometry().width())
    #     # print(self.geometry().height())
    #     print(self.frameGeometry()) #整个框架的左上角相对于父控件的左上角的位置，和整个控件（算框架）的大小



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    print(window.pos())
    print(window.geometry())
    print(window.label.pos())
    print(window.label.geometry())
    sys.exit(app.exec_())