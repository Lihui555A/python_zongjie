#-*- coding:utf-8 -*-
import sys
args=sys.argv
print(args)#直接终端运行这个python C:/Users/36554/Desktop/python总结/pyqt的东西/从头开始/sys介绍.py命令的话出来的是这个文件的全路径
#如果在终端输入python C:/Users/36554/Desktop/python总结/pyqt的东西/从头开始/sys介绍.py 1, 2这个命令的话，会打印出
#['C:/Users/36554/Desktop/python总结/pyqt的东西/从头开始/sys介绍.py', '1,', '2']，也就是说这个sys的作用就是为了在终端运行的时候能够传递参数