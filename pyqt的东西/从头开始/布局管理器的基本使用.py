from PyQt5.Qt import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QTimer
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        lable_1 = QLabel('标签一')
        lable_1.setStyleSheet('background-color:red')
        lable_2 = QLabel('标签二')
        lable_2.setStyleSheet('background-color:green')
        lable_3 = QLabel('标签三')
        lable_3.setStyleSheet('background-color:blue')
        layout_2 = QHBoxLayout()
        layout_2.addWidget(lable_1)
        layout_2.addWidget(lable_2)
        layout_2.addWidget(lable_3)

        lable_1=QLabel('标签一')
        lable_1.setStyleSheet('background-color:red')
        lable_2 = QLabel('标签二')
        lable_2.setStyleSheet('background-color:green')
        lable_3 = QLabel('标签三')
        lable_3.setStyleSheet('background-color:blue')
        layout=QVBoxLayout()
        layout.addWidget(lable_1)
        layout.addLayout(layout_2)
        layout.addWidget(lable_2)
        layout.addWidget(lable_3)
        layout.setSpacing(30) #设置布局管理器内部控件的距离
        layout.setContentsMargins(10,20,30,40) #设置外边距，左上右下
       # layout.replaceWidget('被替换','替换成')  记得把被替换的控件给放到别的控件上，不然会显示不正常
        #如果想把某个控件给释放掉，weight.setparent(None)
        #weight hide()不管控件在不在某个布局上，采用这个方法会从父控件和布局上同时去掉
        self.setLayout(layout)
        self.layout=layout
        timer=QTimer(self)
        timer.timeout.connect(self.start)
        timer.start(100)
    def start(self):
        self.layout.setDirection((self.layout.direction()+1)%4)

        #在布局中的控件之间设置间距可以用layout.inserspaceing()  参数为索引，空间大小
        #在布局中计算索引的时候空白不算数
        #控件之间添加伸缩因子，其实在layout.addweights()括号里除了填写控件之外还有第二个参数，就是设置控件在父控件上所占的比例
        # layout.addWidget(lable_1,2)
        # layout.addLayout(layout_2,3)
        # layout.addWidget(lable_2,1)
        # layout.addWidget(lable_3,5)
        #表示的是把布局分为2+3+1+5=11份，然后各占2份，3份，1份，5份
        #还有一种是在添加控件的过程中添加伸缩因子，
        # layout.addWidget(lable_1,2)
        # layout.addLayout(layout_2,3)
        #layout.addStretch(3)    #这里这句的意思是把整个布局管理器分为2+3+3+1+5=14份，然后呢这个空白部分占3份
        # layout.addWidget(lable_2,1)
        # layout.addWidget(lable_3,5)
        #还有一种情况是
        # layout.addWidget(lable_1)
        # layout.addLayout(layout_2)
        # layout.addStretch()    #这里这句的意思是把整个布局管理器里控件除了自己其他的控件都挤到最小尺寸，剩余的控件都给自己
        # layout.addWidget(lable_2)
        # layout.addWidget(lable_3)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())