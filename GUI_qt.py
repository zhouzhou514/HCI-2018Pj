# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zhouzhou514/Desktop/GUI-DEMO/venv/GUI_qt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import global_v as GV


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.age=GV.age_g
        self.gender=GV.gender_g
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 440, 471, 101))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.input_gender = QtWidgets.QLineEdit(self.centralwidget)
        self.input_gender.setGeometry(QtCore.QRect(630, 99, 121, 31))
        self.input_gender.setObjectName("input_gender")
        self.input_age = QtWidgets.QLineEdit(self.centralwidget)
        self.input_age.setGeometry(QtCore.QRect(630, 149, 121, 31))
        self.input_age.setObjectName("input_age")
        self.input_job = QtWidgets.QLineEdit(self.centralwidget)
        self.input_job.setGeometry(QtCore.QRect(630, 199, 121, 31))
        self.input_job.setObjectName("input_job")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(80, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(80, 170, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")

        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(220, 80, 391, 291))
        self.label_face.setObjectName("face")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "按我享受好康！"))
        self.input_gender.setPlaceholderText(_translate("MainWindow", "更正性別"))
        self.input_age.setPlaceholderText(_translate("MainWindow", "更正年齡"))
        self.input_job.setPlaceholderText(_translate("MainWindow", "更正職業"))
        self.label.setText(_translate("MainWindow", "檢測到潛在客戶"))
        self.label_gender.setText(_translate("MainWindow", "性別: "+GV.gender_g))
        self.label_age.setText(_translate("MainWindow", "年齡: "+GV.age_g))
        face = QPixmap('face.jpg')
        self.label_face.setPixmap(face)

    def start(self):
        Tage = self.input_age.text()
        Tgender = self.input_gender.text()
        if Tage!='':
            GV.age_g=Tage
        if Tgender!='':
            GV.gender_g=Tgender
        GV.job_g = self.input_job.text()
        self.slavewindow.show()
        self.close()

