from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QIcon,QSize
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
        icon=QIcon(R'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\call-start.png')
        button.setIcon(icon)  #设置图标样式
        size=QSize(50,50) #设置图标大小
        button.setIconSize(size)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())