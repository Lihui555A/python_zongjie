from PyQt5.Qt import QApplication, QWidget, QLabel, QLineEdit, Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体')  # self代表的对象本身
        self.resize(500, 500)
        self.setup_ui()
    def setup_ui(self):
        self.linedit_1 = QLineEdit(self)
        self.linedit_1.move(100, 100)

        self.linedit_2 = QLineEdit(self)
        self.linedit_2.move(150, 150)
        self.linedit_2.setFocus()  # 正常情况下焦点是在linedit_1上的，但是linedit_2设置焦点后会在自己身上
        self.linedit_2.clearFocus()  # 去除焦点
        self.linedit_3 = QLineEdit(self)
        self.linedit_3.move(250, 250)
        self.setTabOrder(self.linedit_1, self.linedit_3)#设置父窗口上控件获取焦点的顺序，linedit_1完了是linedit_3

    def mousePressEvent(self, QMouseEvent):
        print(self.focusWidget()) #打印出当前界面上获取焦点的控件
        self.focusNextChild()#使得下一控件获取焦点

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())