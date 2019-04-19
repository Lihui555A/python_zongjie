from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QCheckBox,QRadioButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(100,100)
        chekbox=QCheckBox(self)
        chekbox.setText('我是多选按钮')
        chekbox.move(200,200)
        radiobutton=QRadioButton(self)
        radiobutton.setText('我是单选按钮')
        radiobutton.move(300,300)


        button.setDown(True)#设置按钮被按下
        print(button.isDown())#判断是否按钮被按下
        print(button.isCheckable())#判断控件是否可以被选中
        button.setCheckable(True)#设置按钮能够被选中
        print(button.isChecked())#判断控件是否被选中了
        radiobutton.setChecked(True)#把控件选中
        button_2=QPushButton(self)
        button_2.setText('改变状态')
        button_2.move(400,400)
        button_2.clicked.connect(self.change)
        self.button=button
        self.radiobutton=radiobutton
        self.checkbutton=chekbox
    def change(self):
        self.button.toggle()
        self.radiobutton.toggle()
        self.checkbutton.toggle() #这个方法是用来改变状态的


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())