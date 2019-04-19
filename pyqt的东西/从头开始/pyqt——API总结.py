#-*- coding:utf-8 -*-
from PyQt5.Qt import *


#查看祖宗类下都有哪些子类
# print(QObject.__subclasses__())
# print(QWidget.__subclasses__())
# print(QAbstractButton.__subclasses__())


#查看某个类的父类
# mros=QObject.mro()
# for i in mros:
#     print i

#将某一控件对象设置为另一个控件对象的父控件
obj=QObject()
obj_1=QObject()
obj.setParent(obj_1)
#现在这种情况是obj_1是obj的父对象


#获取某个子控件的父对象
#print (obj.parent())


#从某个父控件中查找子控件
#print (obj_1.children())  #获取直接子对象



#print (obj_1.findChild(QObject,'对象名','查找方式'))
# #从父控件中查找指定类型的一个子控件，如果相同类别的子控件比较多，可以设置每个控件的对象名，然后将对象名传到前面的参数中



#print (obj_1.findChildren(QObject,'对象名','查找方式'))
# #从父控件中查找指定类型的多个子控件，
#Qt.FindChildrenRecursively  #递归查找，默认选项
#Qt.FindDirectChildrenOnly   #只查找一级子对象

#对象释放信号
#obj.destroyed.connect(‘槽函数’)


#零时阻断链接
#obj.blockSignals(True)#括号里参数是bool类型的，

#查看控件对象的某个信号链接了几个槽函数
#print (obj.receivers(button.clicked)) #括号里的参数指的是具体的信号的名称

#判断控件类型
#print obj.isWidgetType()  #判断是不是控件
#print obj.inherits('QObject')  #判断某个对象是否继承自某个类型，包括直接继承和间接继承

#控件对象删除
obj.deleteLater()