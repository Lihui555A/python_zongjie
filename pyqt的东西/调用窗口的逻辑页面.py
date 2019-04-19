from PyQt5 import QtCore, QtGui, QtWidgets
from 打算好好做的音乐播放器 import Ui_MainWindow
from PyQt5 import Qt
import sys
class myDialog(Ui_MainWindow):#继承自Ui_MainWindow                         #这里改成你画好的界面
    def __init__(self,Dialog): #自己初始化的时候需要传进去一个窗体
        super().setupUi(Dialog) #这句话就是在调用你刚才画的那个窗口呢
        self.left_close.setFixedSize(20, 20)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(20, 20)  # 设置按钮大小
        self.left_mini.setFixedSize(20, 20)  # 设置最小化按钮大小
        #给左侧上面的按钮上颜色以及划过之后的反应
        self.left_close.setStyleSheet( '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet( '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet( '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        #给左侧的按钮去边框和换文字颜色
        #这里需要记住的是设置风格只要写了一次，就在原来的基础上改，不要在另写了
        self.left_widget.setStyleSheet('''     
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                           }
        ''')
        # # 设置左侧边框的左上角有左下角的角
        # self.left_widget.setStyleSheet('''
        #          ''')
        #对右侧的输入框进行圆角调整
        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        #对右侧主体的的背景颜色和边框圆角做调整，还有右侧的标签字体做调整
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        #右侧热门推荐，今日歌单去toolbutton按钮去边框
        self.right_recommend_widge.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        #右侧播放列表，其实就是对pushbutton做调整
        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:60px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        #进度条和播放控制按钮去边框
        self.progressBar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')

        self.widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
            }QPushButton:hover{
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        Dialog.setWindowOpacity(0.9)  # 设置窗口透明度 这里记着设置的是你的主窗体
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #把间隙去掉
        self.gridLayout_2.setSpacing(0)

        #隐藏边框
        Dialog.setWindowFlags(Qt.Qt.FramelessWindowHint)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)#注意把类名修改为myDialog

    MainWindow.show()
    sys.exit(app.exec_())

