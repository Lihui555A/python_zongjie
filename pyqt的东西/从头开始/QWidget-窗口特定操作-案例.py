from PyQt5.Qt import QApplication,QWidget,QLabel,Qt,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)
    def setup_ui(self):
        button_1=QPushButton(self)
        button_1.setText('最大化')
        button_1.move(100,100)
        button_1.clicked.connect(lambda :self.showMaximized())
        button_2 = QPushButton(self)
        button_2.setText('最小化')
        button_2.move(200, 200)
        button_2.clicked.connect(lambda: self.showNormal())
        button_3 = QPushButton(self)
        button_3.setText('关闭')
        button_3.move(300, 300)
        button_3.clicked.connect(lambda: self.close())
    def mousePressEvent(self, QMouseEvent):
        self.mouse_x = QMouseEvent.globalX()
        self.mouse_y = QMouseEvent.globalY()
        self.x = self.x()  # 鼠标按下时窗口的位置
        self.y = self.y()
    def mouseMoveEvent(self, QMouseEvent):
        self.dis_x = QMouseEvent.globalX() - self.mouse_x
        self.dis_y = QMouseEvent.globalY() - self.mouse_y
        self.move(self.x + self.dis_x, self.y + self.dis_y)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())