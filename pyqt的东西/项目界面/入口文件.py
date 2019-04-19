from PyQt5.Qt import QApplication,QLabel,QPixmap
from pyqt的东西.项目界面.denglu_pane import Denglu
from pyqt的东西.项目界面.shuxinshibie_pane import Shuxinshibie
from pyqt的东西.项目界面.tuxiangchuli_pane import Tuxiangchuli

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    denglu_jiemian = Denglu()
    shuxinshibie_jiemian = Shuxinshibie()
    tuxiangchuli_jiemian=Tuxiangchuli()
    def shuxinshibie_pane_show():
        shuxinshibie_jiemian.show()
        denglu_jiemian.hide()
    def tuxiangchuli_pane_show():
        tuxiangchuli_jiemian.show()
        denglu_jiemian.hide()
    def denglu_pane_show():
        denglu_jiemian.show()
        shuxinshibie_jiemian.hide()
        tuxiangchuli_jiemian.hide()

    denglu_jiemian.shuxinshibie_pane_show_signal.connect(shuxinshibie_pane_show)
    denglu_jiemian.tuxiangchuli_pane_show_signal.connect(tuxiangchuli_pane_show)
    shuxinshibie_jiemian.denglu_pane_show_signal.connect(denglu_pane_show)
    tuxiangchuli_jiemian.denglu_pane_show_signal.connect(denglu_pane_show)

    denglu_jiemian.show()
    sys.exit(app.exec_())
