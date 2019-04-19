from PyQt5.Qt import *
from pyqt的东西.项目界面.shuxinshibie import Ui_Form

class Shuxinshibie(QWidget,Ui_Form):
    denglu_pane_show_signal=pyqtSignal()
    def __init__(self):
        super(Shuxinshibie, self).__init__()
        self.setupUi(self)
    def denglu_pane_show(self):
        self.denglu_pane_show_signal.emit()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    denglu_jiemian = Shuxinshibie()
    denglu_jiemian.show()
    sys.exit(app.exec_())