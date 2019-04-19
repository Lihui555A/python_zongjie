from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,QMenu,QIcon,QAction
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=QPushButton(self)
        button.setText('点我出菜单')

        menu=QMenu()
        action_1=QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'),'动作一',menu)
        action_1.triggered.connect(lambda :print('我是菜单的第一个动作'))
        action_2 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '动作二', menu)
        action_2.triggered.connect(lambda: print('我是菜单的第二个动作'))
        action_3 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '动作三', menu)
        action_3.triggered.connect(lambda: print('我是菜单的第三个动作'))
        menu.addAction(action_1)
        menu.addAction(action_2)
        menu.addSeparator()#添加分割线
        menu.addAction(action_3)

        #添加子菜单

        menu2=QMenu('我是子菜单',menu)
        action_4 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '动作四', menu2)
        menu2.addAction(action_4)
        menu.addMenu(menu2)

        button.setMenu(menu)


        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())