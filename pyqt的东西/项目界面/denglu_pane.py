from PyQt5.Qt import *
from pyqt的东西.项目界面.denglu import Ui_Form

class Denglu(QWidget,Ui_Form):
    shuxinshibie_pane_show_signal=pyqtSignal()
    tuxiangchuli_pane_show_signal=pyqtSignal()
    def __init__(self):
        super(Denglu, self).__init__()
        self.setupUi(self)
    def shuxinshibie_pane_show(self):
        self.shuxinshibie_pane_show_signal.emit()
    def tuxiangchuli_pane_show(self):
        self.tuxiangchuli_pane_show_signal.emit()
    def mubiaozhuizong_pane_show(self):
        pass
    def shujuguanli_pane_show(self):
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    denglu_jiemian = Denglu()
    denglu_jiemian.show()
    sys.exit(app.exec_())