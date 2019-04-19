from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QLineEdit
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setup_ui()
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.label.setVisible(False)
        self.button.setEnabled(False)
    def setup_ui(self):
        self.label=QLabel(self)
        self.label.move(100,100)
        self.button=QPushButton(self)
        self.button.setText('我是按钮')
        self.button.move(200,200)
        self.button.clicked.connect(self.check)
        self.lineedit=QLineEdit(self)
        self.lineedit.move(300,300)
        self.lineedit.textChanged.connect(self.yes_or_no)
    def yes_or_no(self):
        if self.lineedit.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
    def check(self):
        if self.lineedit.text()=="sz":
            self.label.setVisible(True)
            self.label.setText('登录成功')
            self.label.adjustSize()
        else:
            self.label.setVisible(True)
            self.label.setText('登录失败')
            self.label.adjustSize()



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())