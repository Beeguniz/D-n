# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercises12.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1008)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1911, 1011))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 961, 1011))
        self.widget_2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget_2.setObjectName("widget_2")
        self.q1 = QtWidgets.QLabel(self.widget_2)
        self.q1.setGeometry(QtCore.QRect(150, 170, 731, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q1.setFont(font)
        self.q1.setMouseTracking(False)
        self.q1.setTabletTracking(False)
        self.q1.setAcceptDrops(False)
        self.q1.setAutoFillBackground(False)
        self.q1.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1.setScaledContents(False)
        self.q1.setWordWrap(True)
        self.q1.setObjectName("q1")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.ans12_1_1 = QtWidgets.QComboBox(self.widget_2)
        self.ans12_1_1.setGeometry(QtCore.QRect(310, 190, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_1_1.setFont(font)
        self.ans12_1_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_1_1.setObjectName("ans12_1_1")
        self.ans12_1_1.addItem("")
        self.ans12_1_1.addItem("")
        self.ans12_1_1.addItem("")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(50, 500, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.q2 = QtWidgets.QLabel(self.widget_2)
        self.q2.setGeometry(QtCore.QRect(190, 460, 661, 141))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q2.setFont(font)
        self.q2.setMouseTracking(False)
        self.q2.setTabletTracking(False)
        self.q2.setAcceptDrops(False)
        self.q2.setAutoFillBackground(False)
        self.q2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q2.setScaledContents(False)
        self.q2.setWordWrap(True)
        self.q2.setObjectName("q2")
        self.ans12_2 = QtWidgets.QComboBox(self.widget_2)
        self.ans12_2.setGeometry(QtCore.QRect(420, 480, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_2.setFont(font)
        self.ans12_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_2.setObjectName("ans12_2")
        self.ans12_2.addItem("")
        self.ans12_2.addItem("")
        self.ans12_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(50, 790, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.check12_1 = QtWidgets.QPushButton(self.widget_2)
        self.check12_1.setGeometry(QtCore.QRect(420, 340, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check12_1.setFont(font)
        self.check12_1.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check12_1.setObjectName("check12_1")
        self.check12_2 = QtWidgets.QPushButton(self.widget_2)
        self.check12_2.setGeometry(QtCore.QRect(430, 640, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check12_2.setFont(font)
        self.check12_2.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check12_2.setObjectName("check12_2")
        self.q2_2 = QtWidgets.QLabel(self.widget_2)
        self.q2_2.setGeometry(QtCore.QRect(180, 760, 661, 141))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.q2_2.setFont(font)
        self.q2_2.setMouseTracking(False)
        self.q2_2.setTabletTracking(False)
        self.q2_2.setAcceptDrops(False)
        self.q2_2.setAutoFillBackground(False)
        self.q2_2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q2_2.setScaledContents(False)
        self.q2_2.setWordWrap(True)
        self.q2_2.setObjectName("q2_2")
        self.ans12_3 = QtWidgets.QComboBox(self.widget_2)
        self.ans12_3.setGeometry(QtCore.QRect(480, 780, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_3.setFont(font)
        self.ans12_3.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_3.setObjectName("ans12_3")
        self.ans12_3.addItem("")
        self.ans12_3.addItem("")
        self.ans12_3.addItem("")
        self.check12_3 = QtWidgets.QPushButton(self.widget_2)
        self.check12_3.setGeometry(QtCore.QRect(430, 920, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check12_3.setFont(font)
        self.check12_3.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check12_3.setObjectName("check12_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(270, 30, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 20px;\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.back_gr12 = QtWidgets.QPushButton(self.widget_2)
        self.back_gr12.setGeometry(QtCore.QRect(20, 940, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_gr12.setFont(font)
        self.back_gr12.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.back_gr12.setObjectName("back_gr12")
        self.ans12_1_2 = QtWidgets.QComboBox(self.widget_2)
        self.ans12_1_2.setGeometry(QtCore.QRect(710, 190, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_1_2.setFont(font)
        self.ans12_1_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_1_2.setObjectName("ans12_1_2")
        self.ans12_1_2.addItem("")
        self.ans12_1_2.addItem("")
        self.ans12_1_2.addItem("")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(960, -10, 941, 1011))
        self.widget_3.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:0, y2:1, stop:0 rgba(189, 182, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(70, 340, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.q1_2 = QtWidgets.QLabel(self.widget_3)
        self.q1_2.setGeometry(QtCore.QRect(170, 290, 711, 141))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.q1_2.setFont(font)
        self.q1_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q1_2.setMouseTracking(True)
        self.q1_2.setTabletTracking(False)
        self.q1_2.setAcceptDrops(False)
        self.q1_2.setAutoFillBackground(False)
        self.q1_2.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.q1_2.setScaledContents(False)
        self.q1_2.setWordWrap(True)
        self.q1_2.setObjectName("q1_2")
        self.ans12_4_1 = QtWidgets.QComboBox(self.widget_3)
        self.ans12_4_1.setGeometry(QtCore.QRect(330, 310, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_4_1.setFont(font)
        self.ans12_4_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_4_1.setObjectName("ans12_4_1")
        self.ans12_4_1.addItem("")
        self.ans12_4_1.addItem("")
        self.ans12_4_1.addItem("")
        self.ans12_4_2 = QtWidgets.QComboBox(self.widget_3)
        self.ans12_4_2.setGeometry(QtCore.QRect(740, 310, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_4_2.setFont(font)
        self.ans12_4_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_4_2.setObjectName("ans12_4_2")
        self.ans12_4_2.addItem("")
        self.ans12_4_2.addItem("")
        self.ans12_4_2.addItem("")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(70, 620, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.check12_4 = QtWidgets.QPushButton(self.widget_3)
        self.check12_4.setGeometry(QtCore.QRect(430, 440, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check12_4.setFont(font)
        self.check12_4.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check12_4.setObjectName("check12_4")
        self.q1_3 = QtWidgets.QLabel(self.widget_3)
        self.q1_3.setGeometry(QtCore.QRect(160, 600, 731, 181))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.q1_3.setFont(font)
        self.q1_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q1_3.setMouseTracking(True)
        self.q1_3.setTabletTracking(False)
        self.q1_3.setAcceptDrops(False)
        self.q1_3.setAutoFillBackground(False)
        self.q1_3.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.q1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.q1_3.setScaledContents(False)
        self.q1_3.setWordWrap(True)
        self.q1_3.setIndent(10)
        self.q1_3.setOpenExternalLinks(False)
        self.q1_3.setObjectName("q1_3")
        self.ans12_5_1 = QtWidgets.QComboBox(self.widget_3)
        self.ans12_5_1.setGeometry(QtCore.QRect(380, 640, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_5_1.setFont(font)
        self.ans12_5_1.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_5_1.setObjectName("ans12_5_1")
        self.ans12_5_1.addItem("")
        self.ans12_5_1.addItem("")
        self.ans12_5_1.addItem("")
        self.check12_5 = QtWidgets.QPushButton(self.widget_3)
        self.check12_5.setGeometry(QtCore.QRect(440, 820, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check12_5.setFont(font)
        self.check12_5.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(170, 255, 255);\n"
"}")
        self.check12_5.setObjectName("check12_5")
        self.ans12_5_2 = QtWidgets.QComboBox(self.widget_3)
        self.ans12_5_2.setGeometry(QtCore.QRect(750, 640, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ans12_5_2.setFont(font)
        self.ans12_5_2.setStyleSheet("border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border: 2px solid black;\n"
"padding: 15px;\n"
"background-color: rgb(255, 255, 255);")
        self.ans12_5_2.setObjectName("ans12_5_2")
        self.ans12_5_2.addItem("")
        self.ans12_5_2.addItem("")
        self.ans12_5_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.check12_1.clicked.connect(self.check_answer12_1)
        self.check12_2.clicked.connect(self.check_answer12_2)
        self.check12_3.clicked.connect(self.check_answer12_3)
        self.check12_4.clicked.connect(self.check_answer12_4)
        self.check12_5.clicked.connect(self.check_answer12_5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.q1.setText(_translate("MainWindow", "あした　　　　　こくさいこうえん           おまつりが　あります。"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.ans12_1_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_1_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_1_1.setItemText(2, _translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.q2.setText(_translate("MainWindow", "月よう日            たいこコンサートが　あります。"))
        self.ans12_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_2.setItemText(2, _translate("MainWindow", "で"))
        self.label_5.setText(_translate("MainWindow", "3"))
        self.check12_1.setText(_translate("MainWindow", "Check"))
        self.check12_2.setText(_translate("MainWindow", "Check"))
        self.q2_2.setText(_translate("MainWindow", "つくえの　うえ             ほんが　あります。"))
        self.ans12_3.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_3.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_3.setItemText(2, _translate("MainWindow", "で"))
        self.check12_3.setText(_translate("MainWindow", "Check"))
        self.label.setText(_translate("MainWindow", "Question 1. Choose the correct word:"))
        self.back_gr12.setText(_translate("MainWindow", "Back"))
        self.ans12_1_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_1_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_1_2.setItemText(2, _translate("MainWindow", "で"))
        self.label_6.setText(_translate("MainWindow", "4"))
        self.q1_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; color:#717171; background-color:#fffdf7;\">テーブルの うえ           バナナ</span><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; font-weight:400; color:#717171; background-color:#fffdf7;\"/><span style=\" font-family:\'Noto Sans JP\',\'ヒラギノ角ゴ Pro W3\',\'Hiragino Kaku Gothic Pro\',\'メイリオ\',\'Meiryo\',\'ＭＳ Ｐゴシック\',\'sans-serif\'; font-size:20px; color:#717171; background-color:#fffdf7;\">あります。</span></p><p><br/><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; color:#717171;\"/><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; font-weight:400; color:#717171;\"/><a name=\"ui-id-4-button\"/><a href=\"https://a1.marugotoweb.jp/en/grammar_topic6_11.php#nogo\"><span style=\" font-family:\'Verdana\',\'Arial\',\'sans-serif\'; font-size:20px; font-weight:400; color:#666666; background-color:#fffdf7; vertical-align:middle;\"><br/></span></a><span style=\" font-family:\'Noto Sans JP\'; font-size:18px; font-weight:400; color:#717171;\"/><a name=\"ui-id-4-button\"/><a href=\"https://a1.marugotoweb.jp/en/grammar_topic6_11.php#nogo\"><span style=\" font-family:\'Verdana\',\'Arial\',\'sans-serif\'; font-size:20px; font-weight:400; color:#666666; background-color:#fffdf7; vertical-align:middle;\"><br/></span></a></p></body></html>"))
        self.q1_2.setText(_translate("MainWindow", "２３日            わたしの　いえ                   パーティーが　あります。"))
        self.ans12_4_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_4_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_4_1.setItemText(2, _translate("MainWindow", "x"))
        self.ans12_4_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_4_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_4_2.setItemText(2, _translate("MainWindow", "で"))
        self.label_7.setText(_translate("MainWindow", "5"))
        self.check12_4.setText(_translate("MainWindow", "Check"))
        self.q1_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.q1_3.setText(_translate("MainWindow", "らいしゅう             えいがを　見                いきませんか。"))
        self.ans12_5_1.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_5_1.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_5_1.setItemText(2, _translate("MainWindow", "x"))
        self.check12_5.setText(_translate("MainWindow", "Check"))
        self.ans12_5_2.setItemText(0, _translate("MainWindow", "?"))
        self.ans12_5_2.setItemText(1, _translate("MainWindow", "に"))
        self.ans12_5_2.setItemText(2, _translate("MainWindow", "x"))

    def check_answer12_1(self):
        selected_answer12_1_1 = self.ans12_1_1.currentText()
        selected_answer12_1_2 = self.ans12_1_2.currentText()
        if selected_answer12_1_1 == 'X' and selected_answer12_1_2 == 'で':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer12_2(self):
        selected_answer12_2 = self.ans12_2.currentText()
        if selected_answer12_2 == 'に':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()

    def check_answer12_3(self):
        selected_answer12_3 = self.ans12_3.currentText()
        if selected_answer12_3 == 'に':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer12_4(self):
        selected_answer12_4_1 = self.ans12_4_1.currentText()
        selected_answer12_4_2 = self.ans12_4_2.currentText()
        if selected_answer12_4_1 == 'に' and selected_answer12_4_2 =='で':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()
    def check_answer12_5(self):
        selected_answer12_5_1 = self.ans12_5_1.currentText()
        selected_answer12_5_2 = self.ans12_5_2.currentText()
        if selected_answer12_5_1 == 'X' and selected_answer12_5_2 =='に':
                msg = QMessageBox()
                msg.setText("You are Correct!!!")
                msg.exec_()
        else:
                msg = QMessageBox()
                msg.setText("Incorrect!!! Try again.")
                msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
