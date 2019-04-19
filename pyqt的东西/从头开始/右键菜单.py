from PyQt5.Qt import QApplication,QWidget,QLabel,QMenu,QAction,QIcon
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):

        pass
    def contextMenuEvent(self, QContextMenuEvent):
        menu=QMenu(self)
        action_1=QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'),'我是动作一',menu)
        action_2 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作二', menu)
        action_3 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作三', menu)
        menu_2 = QMenu("子菜单",menu)
        action_4 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作四', menu_2)
        action_5 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作五', menu_2)
        action_6 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作六', menu_2)
        menu_2.addAction(action_4)
        menu_2.addAction(action_5)
        menu_2.addAction(action_6)

        menu.addAction(action_1)
        menu.addMenu(menu_2)
        menu.addAction(action_2)
        menu.addSeparator()
        menu.addAction(action_3)
        menu.exec_(QContextMenuEvent.globalPos()) #注意这里的菜单展示功能是这句话，括号里的参数是鼠标右键点击时的鼠标的位置

       # globalpos=self.mapToGlobal(point())  这句话的意思是把窗口上的局部坐标隐射成全局性的坐标

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())