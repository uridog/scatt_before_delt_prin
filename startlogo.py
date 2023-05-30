# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from client import get_button_data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, server_socket):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(18, 18, 18);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 450, 161, 41))
        self.pushButton.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
"font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.pushButton.setObjectName("pushButton")
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(320, 390, 161, 41))
        self.signupButton.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
"font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.signupButton.setObjectName("signupButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 721, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/photos/gamelogo.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.signupButton.clicked.connect(self.signuppressed)
        get_button_data(self.signupButton, self.pushButton, server_socket)

    def signuppressed(self):
        print("sign-up pressed")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Log-In"))
        self.signupButton.setText(_translate("MainWindow", "Sign-Up"))
import images