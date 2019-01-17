import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog
from GUI_qt import *
from GUI_nd import *
from GUI_rq import *
import global_v as GV


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.slavewindow = secWindow()
        self.pushButton.clicked.connect(self.start)


class secWindow(QDialog, secDialog):
    def __init__(self, parent=None):
        super(secWindow, self).__init__(parent)
        self.setupUi(self)
        self.slavewindow = thiDialog()
        self.pushButton.clicked.connect(self.start)

class thiDialog(QWidget, thiDialog):
    def __init__(self, parent=None):
        super(thiDialog, self).__init__(parent)
        self.setupUi(self)

def FirstUi():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec())
