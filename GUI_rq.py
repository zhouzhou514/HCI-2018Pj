# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zhouzhou514/Desktop/GUI-DEMO/venv/GUI_rq.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_v as GV
from PyQt5.QtGui import QPixmap



class thiDialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 380, 291, 151))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        self.labelID.setGeometry(QtCore.QRect(110, 0, 500, 500))
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")

        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 271, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(520, 60, 256, 192))
        self.label_face.setObjectName("face")
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        #self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "確認完了\n""申辦！"))
        print("----"+GV.text_g)
        self.label_2.setText(_translate("MainWindow", "專案名: 鑽石成功專案"))
        face = QPixmap('face.jpg')
        self.label_face.setPixmap(face)
        self.labelID.setText(_translate("MainWindow",str(GV.text_g)))

    def setOCR(self):
        self.labelID.setText(str(GV.text_g))



