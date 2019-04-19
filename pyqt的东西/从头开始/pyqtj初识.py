#-*- coding:utf-8 -*-
from PyQt5.Qt import QObject,QWidget,QAbstractButton,QPushButton

#对于pyqt来说整个的东西就是一个gui库叫做PyQt5，在这个库里包含着许多模块，有常用的也有不常用的，常用的有
# QtWidget,包含的是常用的一些界面的控件
#QtGui包含的基本的图形和字体
#QtCore 包含非界面的一些功能
#不常用的模块有 QtWebKit ,QtTest,QtSql,QtMultimedia,Qt等等模块
#像界面上的按钮，标签，等等控件都是一个类的实例，这些个类都包含在某个上述的模块中，在我们需要某个控件的时候
#比如说用一个按钮   可以这样导包  from PyQt5.QtWidget import QPushButton  表示的意思是从库中的模块中导出类
#当然如果不知道哪个类在哪个模块中，直接可以用from PyQt5.Qt import * 这句话就可以了，因为 Qt模块中包含了所有的类
#也可以从Qt模块中导入某个特定的模块 比如from PyQt5.Qt import QPushButton
#pyqt中所有的控件的类都是来源于祖宗类叫做QObject,然后它的爷爷辈的类叫做QWidget
#查看祖宗类下都有哪些子类
print(QObject.__subclasses__())
print(QWidget.__subclasses__())
print(QAbstractButton.__subclasses__())
#以上三行代码表示了一个继承关系
#QPushButton 继承自 QAbstractButton 继承自 QWidget 继承自 QObject
