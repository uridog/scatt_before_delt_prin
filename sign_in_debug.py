# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_signUpWindow(object):
    def setupUi(self, signUpWindow):
        signUpWindow.setObjectName("signUpWindow")
        signUpWindow.resize(800, 600)
        signUpWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(signUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gamelogo = QtWidgets.QLabel(self.centralwidget)
        self.gamelogo.setGeometry(QtCore.QRect(40, 0, 721, 371))
        self.gamelogo.setObjectName("gamelogo")
        self.firstname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.firstname_text.setGeometry(QtCore.QRect(40, 380, 211, 71))
        self.firstname_text.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                          "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                          "")
        self.firstname_text.setObjectName("firstname_text")
        self.lastname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.lastname_text.setGeometry(QtCore.QRect(40, 470, 211, 71))
        self.lastname_text.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                         "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                         "")
        self.lastname_text.setObjectName("lastname_text")
        self.username_text = QtWidgets.QTextEdit(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(260, 380, 201, 71))
        self.username_text.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                         "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                         "")
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QTextEdit(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(260, 470, 201, 71))
        self.password_text.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                         "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                         "")
        self.password_text.setObjectName("password_text")
        self.robot_box = QtWidgets.QCheckBox(self.centralwidget)
        self.robot_box.setGeometry(QtCore.QRect(480, 440, 151, 17))
        self.robot_box.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.robot_box.setObjectName("robot_box")
        self.username_taken = QtWidgets.QLabel(self.centralwidget)
        self.username_taken.setGeometry(QtCore.QRect(480, 380, 151, 21))
        self.username_taken.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.username_taken.setObjectName("username_taken")
        self.password_error = QtWidgets.QLabel(self.centralwidget)
        self.password_error.setGeometry(QtCore.QRect(480, 410, 151, 21))
        self.password_error.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.password_error.setObjectName("password_error")
        self.pass_error_len = QtWidgets.QLabel(self.centralwidget)
        self.pass_error_len.setGeometry(QtCore.QRect(640, 380, 161, 21))
        self.pass_error_len.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pass_error_len.setObjectName("pass_error_len")
        self.pass_error_num = QtWidgets.QLabel(self.centralwidget)
        self.pass_error_num.setGeometry(QtCore.QRect(640, 410, 161, 21))
        self.pass_error_num.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pass_error_num.setObjectName("pass_error_num")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(480, 470, 151, 71))
        self.signin_button.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                         "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.signin_button.setObjectName("signin_button")
        signUpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signUpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        signUpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signUpWindow)
        self.statusbar.setObjectName("statusbar")
        signUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(signUpWindow)
        QtCore.QMetaObject.connectSlotsByName(signUpWindow)

    def retranslateUi(self, signUpWindow):
        _translate = QtCore.QCoreApplication.translate
        signUpWindow.setWindowTitle(_translate("signUpWindow", "MainWindow"))
        self.gamelogo.setText(
            _translate("signUpWindow", "<html><head/><body><p><img src=\":/photos2/logo3.png\"/></p></body></html>"))
        self.firstname_text.setHtml(_translate("signUpWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">first name</span></p></body></html>"))
        self.lastname_text.setHtml(_translate("signUpWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">last name</span></p></body></html>"))
        self.username_text.setHtml(_translate("signUpWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">username</span></p></body></html>"))
        self.password_text.setHtml(_translate("signUpWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">password</span></p></body></html>"))
        self.robot_box.setText(_translate("signUpWindow", "I am not a robot"))
        self.username_taken.setText(_translate("signUpWindow", "username taken"))
        self.password_error.setText(_translate("signUpWindow", "password not by rules"))
        self.pass_error_len.setText(_translate("signUpWindow", "password 8-16 letters long"))
        self.pass_error_num.setText(_translate("signUpWindow", "password must contain a number"))
        self.signin_button.setText(_translate("signUpWindow", "sign-in"))


import photos2
def show_debug():
    print("1")
    print(sys.argv)
    try:
        app1 = QtWidgets.QApplication(sys.argv)
    except:
        app1 = QtWidgets.QApplication(sys.argv)

    print("2")
    signUpWindow1 = QtWidgets.QMainWindow()
    print("3")
    ui1 = Ui_signUpWindow()
    print("4")
    ui1.setupUi(signUpWindow1)
    print("5")
    signUpWindow1.show()
    print("6")
    sys.exit(app1.exec_())
if __name__ == "__main__":

    show_debug()
    # app = QtWidgets.QApplication(sys.argv)
    # signUpWindow = QtWidgets.QMainWindow()
    # ui = Ui_signUpWindow()
    # ui.setupUi(signUpWindow)
    # signUpWindow.show()
    # sys.exit(app.exec_())


