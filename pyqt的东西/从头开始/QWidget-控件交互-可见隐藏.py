from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        self.setWindowTitle('被编辑[*]')
        self.setWindowModified(True)#设置窗口编辑状态
        print(self.isWindowModified())#判断窗口是否处于被编辑状态
        print(self.isActiveWindow())#判断窗口是否处于活跃状态

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.setVisible(True)#其实窗口和控件的显示都是调用这个setVisible方法，
    # 然后这个方法会调用控件的painevent方法进行绘制，window.show只不过是setVisible方法的马甲，与之相反的马甲是hide()方法
    #判断是否相对于父控件隐藏isHidden(),判断是否可见isVisible(）
    sys.exit(app.exec_())