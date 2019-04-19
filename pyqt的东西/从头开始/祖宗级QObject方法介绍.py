#-*- coding:utf-8 -*-
from PyQt5.Qt import QApplication,QWidget,QLabel,QObject
import sys
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        self.Qobject_methods()
    def Qobject_methods(self):
        obj=QObject()
        #可以设置对象名称
        obj.setObjectName('notice')
        print(obj.objectName())
        #可以设置对象的某些属性
        obj.setProperty("notice_level",'error')
        obj.setProperty("notice_leve2", 'warning')
        print(obj.property('notice_level'))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())