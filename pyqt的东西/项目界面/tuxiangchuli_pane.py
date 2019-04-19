from PyQt5.Qt import *
from pyqt的东西.项目界面.tuxiangchuli import Ui_Form
#from pyqt的东西.项目界面.denglu_pane import Denglu
class Tuxiangchuli(QWidget,Ui_Form):
    denglu_pane_show_signal=pyqtSignal()
    def __init__(self):
        super(Tuxiangchuli, self).__init__()
        self.setupUi(self)
    def denglu_pane_show(self):
        self.denglu_pane_show_signal.emit()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    denglu_jiemian = Tuxiangchuli()
    denglu_jiemian.show()
    sys.exit(app.exec_())