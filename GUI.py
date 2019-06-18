import Board as b
import copy
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

import sip

import time
from PyQt5 import QtCore, QtWidgets

import copy
import math
from operator import add
import random
import string
import time




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
        self.pushButton_30 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_30.setGeometry(QtCore.QRect(1, 478, 100, 100))
        self.pushButton_30.setObjectName("pushButton")
        self.pushButton_20 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_20.setGeometry(QtCore.QRect(1, 350, 100, 100))
        self.pushButton_20.setObjectName("pushButton_2")
        self.pushButton_00 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_00.setGeometry(QtCore.QRect(1, 94, 100, 100))
        self.pushButton_00.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1, 222, 100, 100))
        self.pushButton_10.setObjectName("pushButton_4")
        self.pushButton_02 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_02.setGeometry(QtCore.QRect(304, 94, 100, 100))
        self.pushButton_02.setObjectName("pushButton_5")
        self.pushButton_01 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_01.setGeometry(QtCore.QRect(152, 94, 100, 100))
        self.pushButton_01.setObjectName("pushButton_6")
        self.pushButton_03 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_03.setGeometry(QtCore.QRect(455, 94, 100, 100))
        self.pushButton_03.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_11.setGeometry(QtCore.QRect(152, 222, 100, 100))
        self.pushButton_11.setObjectName("pushButton_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_12.setGeometry(QtCore.QRect(304, 222, 100, 100))
        self.pushButton_12.setObjectName("pushButton_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_13.setGeometry(QtCore.QRect(455, 222, 100, 100))
        self.pushButton_13.setObjectName("pushButton_10")
        self.pushButton_21 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_21.setGeometry(QtCore.QRect(152, 350, 100, 100))
        self.pushButton_21.setObjectName("pushButton_11")
        self.pushButton_22 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_22.setGeometry(QtCore.QRect(304, 350, 100, 100))
        self.pushButton_22.setObjectName("pushButton_12")
        self.pushButton_23 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_23.setGeometry(QtCore.QRect(455, 350, 100, 100))
        self.pushButton_23.setObjectName("pushButton_13")
        self.pushButton_31 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_31.setGeometry(QtCore.QRect(152, 478, 100, 100))
        self.pushButton_31.setObjectName("pushButton_14")
        self.pushButton_32 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_32.setGeometry(QtCore.QRect(304, 478, 100, 100))
        self.pushButton_32.setObjectName("pushButton_15")
        self.pushButton_33 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_33.setGeometry(QtCore.QRect(455, 478, 100, 100))
        self.pushButton_33.setObjectName("pushButton_16")

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
        self.pushButton_bo4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_bo4.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_bo4, 1, 1, 1, 1)
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
        self.board = b.Board()
        self.words = Words()
        self.size = 4

        # Button List

    """ BUTTON NAMES """
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOOGLE"))
        self.pushButton_30.setText(_translate("MainWindow", self.board.letters[3][0]))
        self.pushButton_20.setText(_translate("MainWindow", self.board.letters[2][0]))
        self.pushButton_00.setText(_translate("MainWindow", self.board.letters[0][0]))
        self.pushButton_10.setText(_translate("MainWindow", self.board.letters[1][0]))
        self.pushButton_02.setText(_translate("MainWindow", self.board.letters[0][2]))
        self.pushButton_01.setText(_translate("MainWindow", self.board.letters[0][1]))
        self.pushButton_03.setText(_translate("MainWindow", self.board.letters[0][3]))
        self.pushButton_11.setText(_translate("MainWindow", self.board.letters[1][1]))
        self.pushButton_12.setText(_translate("MainWindow", self.board.letters[1][2]))
        self.pushButton_13.setText(_translate("MainWindow", self.board.letters[1][3]))
        self.pushButton_21.setText(_translate("MainWindow", self.board.letters[2][1]))
        self.pushButton_22.setText(_translate("MainWindow", self.board.letters[2][2]))
        self.pushButton_23.setText(_translate("MainWindow", self.board.letters[2][3]))
        self.pushButton_31.setText(_translate("MainWindow", self.board.letters[3][1]))
        self.pushButton_32.setText(_translate("MainWindow", self.board.letters[3][2]))
        self.pushButton_33.setText(_translate("MainWindow", self.board.letters[3][3]))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_bo4.setText(_translate("MainWindow", "Exit"))
        self.pushButton_17.setText(_translate("MainWindow", "Run"))
        self.pushButton_18.setText(_translate("MainWindow", "Print"))
        self.pushButton_19.setText(_translate("MainWindow", "New Board"))

        """ BUTTON-FUNCTION CONNECTIONS """
        self.pushButton_17.clicked.connect(lambda: self.newdfs(self.board, (0,0), self.words.trie(1), ""))
        self.pushButton_18.clicked.connect(self.btn_click)
        self.pushButton_19.clicked.connect(self.btn_click)
        self.pushButton_bo4.clicked.connect(self.btn_click)



        # Button List

        self.blist = [[self.pushButton_00, self.pushButton_01, self.pushButton_02, self.pushButton_03],
                      [self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13],
                      [self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23],
                      [self.pushButton_30, self.pushButton_31, self.pushButton_32, self.pushButton_33]]


    """ BUTTON FUNCTIONS """

    def run(self):
        stringTrie = self.words.trie(1)
        startChar = self.board.letters[0][0]
        temp = copy.deepcopy(self.board.letters)
        for i in range(len(self.board.letters) - 1):
            for j in range(len(self.board.letters) - 1):
                self.blist[1].setStyleSheet("background-color: red")
                time.sleep(.15)

                self.board.dfs(temp, stringTrie, (3, 0), cmdVis=True)

    def dfs_gui(self):
        board = self.board
        trie = self.words.trie(1)
        temp = copy.deepcopy(self.board.letters)
        pass

    def btn_click(self):
        sender = self.MainWindow.sender()
        if sender.text() == 'Print':
            print(self.board.letters)

        elif sender.text() == 'New Board':
            self.board = b.Board()
            d = self.MainWindow.children()
            e = reversed(d)

            for g in e:
                g.deleteLater()

            self.MainWindow.deleteLater()



        elif sender.text() == 'Exit':
            self.textEdit.setText("Exit Button doesn't work yet")

    def newdfs(self, board, start, trie, prefix):
        self.blist[start[0]][start[1]].setStyleSheet("background-color: #03A9F4")

        indic = [-1, 0, 1]

        # Position of the origin letter
        pos = board.letters[start[0]][start[1]]
        prow = start[0]
        pcol = start[1]


        print(pos)

        neigh = []

        # Neighboors of the origin letter
        for i in indic:
            for j in indic:
                x = prow + i
                y = pcol +j
                if 0 <= x < 4 and 0 <= y < 4 and ([x,y]!=[prow,pcol]):
                    neigh.append([x,y])
                    self.blist[x][y].setStyleSheet("background-color:#BDBDBD")

        print(neigh)

        if trie.has_key(prefix):
            self.words.append(prefix)
            self.textEdit.setText(prefix)
            












    # depth first search
    def dfsgui(self, board):

        # board = self.board
        trie = self.words.trie(1)
        temp = copy.deepcopy(self.board.letters)
        start = (0,0)
        prefix = ''
        cmdVis = False
        connection = None

        self.blist[start[0]][start[1]].setStyleSheet("background-color: blue")



        if cmdVis:
            print(f'prefix = {prefix}')
            self.spcPrint(connection)
            time.sleep(.15)
            print('Found Words')
            print('-----------')
            for i in self.words:
                self.textEdit.setText(i)
            print('-----------')

        if cmdVis and connection == None:
            connection = [False for i in range(42)]

        board = copy.deepcopy(board)

        directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        if trie.has_key(prefix):  # current word is valid:
            self.words.append(prefix)
            if cmdVis:
                print(f'ADDED {prefix}')


        for i in directions:
            newStart = tuple(map(add, i, start))
            x, y = newStart
            if x >= 0 and x < self.size and y >= 0 and y < self.size:
                newPrefix = prefix + board.letters[x][y]
                if trie.items(newPrefix) != []:  # i not already searched & i a valid space & valid prefix
                    newBoard = copy.deepcopy(board)
                    newBoard.letters[x][y] = '-'

                    newCon = copy.deepcopy(connection)
                    if cmdVis:
                        if i == (1, 0) or i == (-1, 0):
                            newCon[13 * y + min(start[0], x)] = True
                            print(f'start = {start}')
                            print(f'next = {newStart}')
                        if i == (0, 1) or i == (0, -1):
                            newCon[13 * min(start[1], y) + 3 * (x + 1)] = True
                            print(f'start = {start}')
                            print(f'next = {newStart}')
                        if i == (-1, 1) or i == (1, -1):
                            newCon[13 * min(start[1], y) + 3 * max(start[0], x) + 1] = True
                            print(f'start = {start}')
                            print(f'next = {newStart}')
                        if i == (1, 1) or i == (-1, -1):
                            newCon[13 * min(start[1], y) + 3 * max(start[0], x) + 2] = True
                            print(f'start = {start}')
                            print(f'next = {newStart}')

                    self.dfsgui(newBoard)
                    # newBoard, trie, newStart, newPrefix, cmdVis, newCon
                    # dfs @i with modified bord & prefix
                    # add word to list if it is at the end of the trie

        return

    # board.dfs(temp, stringTrie, (1,1), startChar, cmdVis = True)
    # def dfs2(self, board, trie, ):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Boggle()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())