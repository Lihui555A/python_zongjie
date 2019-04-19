from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)

        self.setup_ui()

        self.del_func2()
    def setup_ui(self):
        lable_1=QLabel(self)
        lable_1.destroyed.connect(self.del_func2)
        lable_1.resize(100,100)
        lable_1.setStyleSheet('background-color:red')
        lable_2=QLabel(lable_1)
        lable_2.resize(50,50)
        lable_2.setStyleSheet('background-color:green')
        lable_2.destroyed.connect(lambda :print('对象二被销毁'))
        lable_3=QLabel(lable_2)
        lable_3.resize(50, 50)
        lable_3.setStyleSheet('background-color:yellow')
        lable_3.destroyed.connect(lambda: print('对象三被销毁'))
        #del lable_1  #在执行这句话之前label_3是放在label_2上的，label_2是放在label_1上的，所以正常情况下删除lable-1会把其他两
        # 个子对象一块给删除了，但是这个del删除时干不了这个事情的
        lable_1.deleteLater() #这句话是可以的一下子都删除的，但是这句话是放在最后执行的
        print(lable_2)
    def del_func2(self):
        print('对象一被销毁')



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())