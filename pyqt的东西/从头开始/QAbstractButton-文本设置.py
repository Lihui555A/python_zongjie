from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        self.button=QPushButton(self)
        self.button.setText('1')
        self.button.clicked.connect(self.chage_button_text)
    def chage_button_text(self):
        text=self.button.text()
        newtext=int(text)+1
        self.button.setText(str(newtext))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())