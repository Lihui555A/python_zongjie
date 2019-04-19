# from PyQt5.Qt import QApplication,QWidget
# import sys
# class Window(QWidget):
#     def __init__(self):
#         print('sjkfjk')
#
# app=QApplication(sys.argv)
# window=Window()
#
# window.show() #这样直接执行会报错，为什么，因为自己创建了一个类继承自QWidget,又定义了自己的构造函数
# #然后自己在实例化对象的时候会自动执行自己类中的构造函数，但是自己类中的构造函数只有一个打印，并没有show方法
# #但是我们继承自QWidget，这个类中应该是有show方法的，那为啥不能用呢，原因是QWidget类中的方法是写在它自己类中的
# #构造函数中，而我们自己创建的类的构造函数把人家的构造函数给顶走了，所以show方法就没有了，所以就报错了
# sys.exit(app.exec_())

