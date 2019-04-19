from PyQt5.Qt import QApplication,QWidget,QLabel
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        pass
    def mousePressEvent(self, QMouseEvent):
        self.mouse_x=QMouseEvent.globalX()
        self.mouse_y = QMouseEvent.globalY()
        self.x = self.x()#鼠标按下时窗口的位置
        self.y = self.y()
        print(QMouseEvent.globalX(),QMouseEvent.globalY())  #打印鼠标的全局位置
    def mouseMoveEvent(self, QMouseEvent):
        self.dis_x=QMouseEvent.globalX()-self.mouse_x
        self.dis_y = QMouseEvent.globalY() -self.mouse_y
        self.move(self.x+self.dis_x,self.y+self.dis_y)

        #self.move(self.mouse_x,self.mouse_y)
    def mouseReleaseEvent(self,QMouseEvent):
        print('鼠标释放')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())