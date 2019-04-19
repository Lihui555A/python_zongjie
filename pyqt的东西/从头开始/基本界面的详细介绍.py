#-*- coding:utf-8 -*-
from PyQt5.Qt import QApplication,QLabel,QWidget,qApp
import sys
app=QApplication(sys.argv)#创建一个应用程序对象，这个程序在终端命令下运行的时候可以传多余的参数，那如果想看这些参数怎么办
#需要用到下面这句话
#print(app.arguments()) 这样的话在终端用命令python C:/Users/36554/Desktop/python总结/pyqt的东西/从头开始/基本界面的详细介绍.py 1,2,3,4执行这个程序的时候界面会出来，然后也会打印出['C:/Users/36554/Desktop/python总结/pyqt的东西/从头开始/基本界面的详细介绍.py', '1,2,3,4']
#print(qApp.arguments()) 这句话也可以打印出命令传的参数
window=QWidget()  #创建一个控件，没有父控件的话，这个空间就是顶层窗口控件，系统会自动的给窗口加
# 一些修饰（标题栏，）窗口控件具备一些特性（设置标题，图标），默认情况下这个控件不会被展示只有手动的调用show(）才可以
window.setWindowTitle('第一个窗口')
window.resize(500,500)
window.move(400,200)
label=QLabel(window)  #label是子控件，放在父控件window上，window只要展示，那么label就会展示，同时window关闭，label也会消失
label.setText('Hello World')
label.move(200,100)
window.show()
sys.exit(app.exec_())#app.exec_()表示程序进入监听状态的消息循环监听用户的操作，只有关闭窗口的时候这个消息循环才停止
#sys.exit表示的是检查程序是否是正常退出的