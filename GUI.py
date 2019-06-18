import Board
import copy
import multiprocessing
import time
from Words import Words
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QTextEdit, QLabel, QRadioButton, QCheckBox, QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
import os

class Boggle(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.MainWindow = MainWindow

        """ BUTTONS """
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(50, 0, 556, 672))
        self.gridWidget.setObjectName("gridWidget")
        self.pushButton = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton.setGeometry(QtCore.QRect(1, 478, 100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1, 350, 100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1, 94, 100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1, 222, 100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(304, 94, 100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(152, 94, 100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(455, 94, 100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(152, 222, 100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(304, 222, 100, 100))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_10.setGeometry(QtCore.QRect(455, 222, 100, 100))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_11.setGeometry(QtCore.QRect(152, 350, 100, 100))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_12.setGeometry(QtCore.QRect(304, 350, 100, 100))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_13.setGeometry(QtCore.QRect(455, 350, 100, 100))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_14.setGeometry(QtCore.QRect(152, 478, 100, 100))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_15.setGeometry(QtCore.QRect(304, 478, 100, 100))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_16.setGeometry(QtCore.QRect(455, 478, 100, 100))
        self.pushButton_16.setObjectName("pushButton_16")

        self.label = QtWidgets.QLabel(self.gridWidget)
        self.label.setGeometry(QtCore.QRect(-206, 5, 321, 51))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(693, 6, 301, 571))
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 600, 991, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 1, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 0, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """ BOARD SETTINGS """
    def __init__(self):
        """ Board """
        self.board = Board.Board()
        self.words = Words()

    """ BUTTON NAMES """
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOOGLE"))
        self.pushButton.setText(_translate("MainWindow", self.board.letters[3][0]))
        self.pushButton_2.setText(_translate("MainWindow", self.board.letters[2][0]))
        self.pushButton_3.setText(_translate("MainWindow", self.board.letters[0][0]))
        self.pushButton_4.setText(_translate("MainWindow", self.board.letters[1][0]))
        self.pushButton_5.setText(_translate("MainWindow", self.board.letters[0][2]))
        self.pushButton_6.setText(_translate("MainWindow", self.board.letters[0][1]))
        self.pushButton_7.setText(_translate("MainWindow", self.board.letters[0][3]))
        self.pushButton_8.setText(_translate("MainWindow", self.board.letters[1][1]))
        self.pushButton_9.setText(_translate("MainWindow", self.board.letters[1][2]))
        self.pushButton_10.setText(_translate("MainWindow", self.board.letters[1][3]))
        self.pushButton_11.setText(_translate("MainWindow", self.board.letters[2][1]))
        self.pushButton_12.setText(_translate("MainWindow", self.board.letters[2][2]))
        self.pushButton_13.setText(_translate("MainWindow", self.board.letters[2][3]))
        self.pushButton_14.setText(_translate("MainWindow", self.board.letters[3][1]))
        self.pushButton_15.setText(_translate("MainWindow", self.board.letters[3][2]))
        self.pushButton_16.setText(_translate("MainWindow", self.board.letters[3][3]))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_20.setText(_translate("MainWindow", "Exit"))
        self.pushButton_17.setText(_translate("MainWindow", "Run"))
        self.pushButton_18.setText(_translate("MainWindow", "Print"))
        self.pushButton_19.setText(_translate("MainWindow", "Abort"))

        """ BUTTON-FUNCTION CONNECTIONS """
        self.pushButton_17.clicked.connect(self.run)
        self.pushButton_18.clicked.connect(self.btn_click)
        self.pushButton_19.clicked.connect(self.btn_click)
        self.pushButton_20.clicked.connect(self.btn_click)

    """ BUTTON FUNCTIONS """

    def btn_click(self):
        sender = self.MainWindow.sender()
        if sender.text() == 'Print':
            print(self.board.letters)
        """
        elif sender.text() == 'Abort':
            p = multiprocessing.Process(target=self.run())
            p.terminate()
        elif sender.text() == 'Exit':
            sys.exit()"""

    def run(self):
        stringTrie = self.words.trie(1)
        startChar = self.board.letters[0][0]
        temp = copy.deepcopy(self.board.letters)
        for i in range(len(self.board.letters) - 1):
            for j in range(len(self.board.letters) - 1):
                print(self.board.dfs(temp, stringTrie, (i, j), cmdVis=True))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Boggle()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())