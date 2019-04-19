from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        label_1=QLabel(self)
        label_1.setText('我是标签一')
        label_1.move(100,100)
        label_2 = QLabel(self)
        label_2.setText('我是标签二')
        label_2.move(200, 200)
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(300,300)
        self.lable_color()
        self.button_color()
    def lable_color(self):
        for i in self.children():
            if i.inherits('QLabel'):
                i.setStyleSheet('background-color:red;color:white')
    def button_color(self):
        for i in self.findChildren(QPushButton):
            i.setStyleSheet('background-color:black;color:white')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())