from PyQt5.Qt import QApplication,QWidget,QLabel,QToolButton,QIcon,QAction,Qt,QMenu
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        button=Toolbutton(self)
        button.setAutoRaise(True)
        button.setText('nihao')
        button.setIcon(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'))
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        menu = QMenu(button)
        action_1 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作一', menu)
        action_2 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作二', menu)
        action_3 = QAction(QIcon(r'C:\Users\36554\Desktop\python总结\pyqt的东西\QT小图标\actions\add.png'), '我是动作三', menu)
        menu_2 = QMenu("子菜单", menu)
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
        button.setMenu(menu)  #这里需要注意的是这里的setmenu方法和pushbutton里的setmenu方法不同，这里的按下按钮一会之后才能出来菜单

        #设置菜单弹出方式
        button.setPopupMode(QToolButton.MenuButtonPopup) #这个是按钮的右边有一个向下的箭头，点击箭头然后出现这个菜单
        button.setPopupMode(QToolButton.InstantPopup) #点击按钮马上显示菜单
        button.setPopupMode(QToolButton.DelayedPopup)#默认是这个，点住按钮一会之后出现菜单、
class Toolbutton(QToolButton):  #自己重写的方法，鼠标进入后触发
    def enterEvent(self, QEvent):
        self.showMenu()


        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())