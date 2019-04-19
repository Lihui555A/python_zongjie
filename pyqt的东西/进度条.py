# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # @Time    : 18-8-29 下午11:00
# # @Author  : Tanclin
# # @File    : demo.py
#
# from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
# from PyQt5.QtCore import QBasicTimer #定时器
# from PyQt5.QtGui import QIcon #设置图标
# import sys
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.btn.clicked.connect(self.Action)
#     def initUI(self):
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(50,50,200,25)
#         self.btn = QPushButton("运行 or 停止",self)
#         self.btn.move(105,90)
#         self.timer = QBasicTimer()
#         self.step = 0
#         self.setGeometry(300,300,300,180)
#         self.setWindowTitle("Demo for Lin")
#         self.show()
#     def timerEvent(self, *args, **kwargs):
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText("完成")
#             return
#         self.step = self.step+1
#         #重置、刷新进度条
#         self.pbar.setValue(self.step)
#     def Action(self):   #槽函数
#         #判断进度条是否已经激活，处于执行状态
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText("运行")
#         else:
#             #激活进度条开始执行
#             self.timer.start(100,self)
#             self.btn.setText("停止")
# if __name__=='__main__':
#     #构建Qt的应用对象
#     app = QApplication(sys.argv)
#     ex = Example()
#     #开始运行程序
#     sys.exit(app.exec_())
list=[5,2,3,4]
for i in reversed(list):
    print(i)