# -*- coding: utf-8 -*-
import sys
import time

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, Client):
        self.client = Client

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.game_table = QtWidgets.QTableWidget(self.centralwidget)
        self.game_table.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.game_table.setStyleSheet(";background-color:rgb(255, 255, 255);\n"
                                      "border:1px solid red\n"
                                      ";gridline-color: rgb(170, 85, 255);\n"
                                      "text-color:rgb(255, 85, 127)")
        self.game_table.setAlternatingRowColors(True)
        self.game_table.setObjectName("game_table")
        self.game_table.setColumnCount(7)
        self.game_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setItem(1, 1, item)
        self.game_table.horizontalHeader().setStretchLastSection(False)
        self.game_table.verticalHeader().setCascadingSectionResizes(False)
        self.game_table.verticalHeader().setStretchLastSection(False)
        self.round_starting = QtWidgets.QLabel(self.centralwidget)
        self.round_starting.setGeometry(QtCore.QRect(100, 390, 321, 51))
        self.round_starting.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.round_starting.setObjectName("round_starting")
        self.round_time = QtWidgets.QLabel(self.centralwidget)
        self.round_time.setGeometry(QtCore.QRect(160, 470, 461, 81))
        self.round_time.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.round_time.setObjectName("round_time")
        self.continue_button = QtWidgets.QPushButton(self.centralwidget)
        self.continue_button.setGeometry(QtCore.QRect(260, 290, 311, 91))
        self.continue_button.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.continue_button.setObjectName("continue_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 400, 31, 41))
        self.label_2.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.label_2.setObjectName("label_2")
        self.two = QtWidgets.QLabel(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(460, 400, 31, 41))
        self.two.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.two.setObjectName("two")
        self.one = QtWidgets.QLabel(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(490, 400, 31, 41))
        self.one.setStyleSheet("font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.one.setObjectName("one")
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
        self.check_for_button(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.game_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", " "))
        item = self.game_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", " "))
        item = self.game_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", " "))
        item = self.game_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "country"))
        item = self.game_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "city"))
        item = self.game_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "boy name"))
        item = self.game_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "movie"))
        item = self.game_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "household-item"))
        item = self.game_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "fruit and veggies"))
        item = self.game_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "animal"))
        __sortingEnabled = self.game_table.isSortingEnabled()
        self.game_table.setSortingEnabled(False)
        self.game_table.setSortingEnabled(__sortingEnabled)
        self.round_starting.setText(_translate("MainWindow", "round starting in "))
        self.round_starting.hide()
        self.label_2.setText(_translate("MainWindow", "3"))
        self.label_2.hide()
        self.two.setText(_translate("MainWindow", "2"))
        self.two.hide()
        self.one.setText(_translate("MainWindow", "1"))
        self.one.hide()
        self.round_time.setText(_translate("MainWindow", "round timer 30 seconds"))
        self.round_time.hide()

    def check_for_button(self, MainWindow):
        self.continue_button.clicked.connect(lambda: self.continue_pressed(MainWindow))

    def continue_pressed(self, MainWindow):
        print("continuepressed")
        self.client.screen_state = 2
        MainWindow.close()

    def insert_value(self, category, round_num, word):
        _translate = QtCore.QCoreApplication.translate
        item = self.game_table.item(round_num - 1, category)
        item.setText(_translate("MainWindow", word))

    def start_round(self):
        self.round_starting.show()
        time.sleep(1)
        self.one.show()
        time.sleep(1)
        self.two.show()
        time.sleep(1)
        self.label_2.show()
        time.sleep(1)
        self.round_starting.hide()
        self.one.hide()
        self.two.hide()
        self.label_2.hide()

    def set_letter(self, round_num, letter):
        _translate = QtCore.QCoreApplication.translate
        item = self.game_table.verticalHeaderItem(round_num - 1)
        item.setText(_translate("MainWindow", letter))


def show_game(window):
    app2 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app2.exec_())
