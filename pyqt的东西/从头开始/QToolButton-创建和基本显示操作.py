from PyQt5.Qt import QApplication,QWidget,QLabel,QToolButton,QIcon,Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=QToolButton(self)
        button.setIcon(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\address-book-new.png'))
        button.setText('我是工具按钮')
        button.setToolTip('这是工具菜单中的按钮，一般只显示图标')#同时设置文字和图标，默认只显示图标

        button.setToolButtonStyle(Qt.ToolButtonIconOnly)#紧显示图标
        button.setToolButtonStyle(Qt.ToolButtonTextOnly)  # 仅仅显示文字
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文字在图标旁边
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文字在图标下方


        button.setArrowType(Qt.NoArrow)#设置箭头的方向
        button.setArrowType(Qt.UpArrow)
        button.setArrowType(Qt.DownArrow)
        button.setArrowType(Qt.LeftArrow)
        button.setArrowType(Qt.RightArrow)

        button.setAutoRaise(True) #设置自动提升


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())