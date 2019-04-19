import sys
from PyQt5.QtWidgets import QWidget, QToolTip,QPushButton, QApplication
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()  #括号中的self表示的是当前类的对象，Exampel表示的是当前的类名，这句话的意思就是让当前类去继承父类的初始化方法

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
