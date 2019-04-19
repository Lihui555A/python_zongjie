from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QObject
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        wid=QWidget()
        obj=QObject()
        label=QLabel()
        button=QPushButton()
        list1=[wid,obj,label,button]
        for i in list1:
            #print(i.isWidgetType())#判断是否是控件
            print(i.inherits('QWidget'))#判断某个对象是否继承自某个类，包括间接继承和直接继承括号中是父类名的字符串




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())