from Board import *
import copy
from operator import add
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from Words import Words


class BOGGLE(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 750)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(560, 20, 321, 500))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 530, 681, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 570, 861, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(720, 530, 161, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 500, 500))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        """BUTTONS"""
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)


        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_13, 1, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_20, 2, 0, 1, 1)
        self.pushButton_01 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_01, 0, 1, 1, 1)
        self.pushButton_00 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_00.setFont(font)
        self.pushButton_00.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_00, 0, 0, 1, 1)
        self.pushButton_03 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_03, 0, 3, 1, 1)
        self.pushButton_02 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_02, 0, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_22, 2, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_23, 2, 3, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_31, 3, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_30, 3, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_21, 2, 1, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_32, 3, 2, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_33, 3, 3, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(20, 620, 861, 62))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        self.frame1.setFont(font)
        self.frame1.setObjectName("frame1")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 0, 200, 62))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_18.setEnabled(True)
        self.pushButton_18.setGeometry(QtCore.QRect(217, 0, 200, 62))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_19.setEnabled(True)
        self.pushButton_19.setGeometry(QtCore.QRect(433, 0, 200, 62))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_200 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_200.setEnabled(True)
        self.pushButton_200.setGeometry(QtCore.QRect(650, 0, 200, 62))
        self.pushButton_200.setObjectName("pushButton_20")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuGrid = QtWidgets.QMenu(self.menuOptions)
        self.menuGrid.setObjectName("menuGrid")
        self.menuGame_Mode = QtWidgets.QMenu(self.menuOptions)
        self.menuGame_Mode.setObjectName("menuGame_Mode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSolve = QtWidgets.QAction(MainWindow)
        self.actionSolve.setObjectName("actionSolve")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.action4x4 = QtWidgets.QAction(MainWindow)
        self.action4x4.setObjectName("action4x4")
        self.action6x6 = QtWidgets.QAction(MainWindow)
        self.action6x6.setObjectName("action6x6")
        self.action12x12 = QtWidgets.QAction(MainWindow)
        self.action12x12.setObjectName("action12x12")
        self.actionSolver = QtWidgets.QAction(MainWindow)
        self.actionSolver.setObjectName("actionSolver")
        self.action1_Player = QtWidgets.QAction(MainWindow)
        self.action1_Player.setObjectName("action1_Player")
        self.action2_Players = QtWidgets.QAction(MainWindow)
        self.action2_Players.setObjectName("action2_Players")
        self.menuFile.addAction(self.actionSolve)
        self.menuFile.addAction(self.actionNew_Game)
        self.menuFile.addAction(self.actionExit)
        self.menuGrid.addSeparator()
        self.menuGrid.addAction(self.action4x4)
        self.menuGrid.addAction(self.action6x6)
        self.menuGrid.addAction(self.action12x12)
        self.menuGame_Mode.addSeparator()
        self.menuGame_Mode.addAction(self.actionSolver)
        self.menuGame_Mode.addAction(self.action1_Player)
        self.menuGame_Mode.addAction(self.action2_Players)
        self.menuOptions.addAction(self.menuGrid.menuAction())
        self.menuOptions.addAction(self.menuGame_Mode.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """ BOARD SETTINGS """
    def __init__(self, board = None, size = 4, trie = None, words = None):
        """ Board """
        if board == None:
            self.board = Board()
        if words == None:
            self.words = Words()
        if trie == None:
           self.trie = self.words.trie()
        self.wordList = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_13.setText(_translate("MainWindow", self.board.letters[1][3]))
        self.pushButton_20.setText(_translate("MainWindow", self.board.letters[2][0]))
        self.pushButton_01.setText(_translate("MainWindow", self.board.letters[0][1]))
        self.pushButton_00.setText(_translate("MainWindow", self.board.letters[0][0]))
        self.pushButton_03.setText(_translate("MainWindow", self.board.letters[0][3]))
        self.pushButton_02.setText(_translate("MainWindow", self.board.letters[0][2]))
        self.pushButton_11.setText(_translate("MainWindow", self.board.letters[1][1]))
        self.pushButton_10.setText(_translate("MainWindow", self.board.letters[1][0]))
        self.pushButton_12.setText(_translate("MainWindow", self.board.letters[1][2]))
        self.pushButton_22.setText(_translate("MainWindow", self.board.letters[2][2]))
        self.pushButton_23.setText(_translate("MainWindow", self.board.letters[2][3]))
        self.pushButton_31.setText(_translate("MainWindow", self.board.letters[3][1]))
        self.pushButton_30.setText(_translate("MainWindow", self.board.letters[3][0]))
        self.pushButton_21.setText(_translate("MainWindow", self.board.letters[2][1]))
        self.pushButton_32.setText(_translate("MainWindow", self.board.letters[3][2]))
        self.pushButton_33.setText(_translate("MainWindow", self.board.letters[3][3]))
        self.pushButton_17.setText(_translate("MainWindow", "Solve"))
        self.pushButton_18.setText(_translate("MainWindow", "New Board"))
        self.pushButton_19.setText(_translate("MainWindow", "Print"))
        self.pushButton_200.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "Game"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuGrid.setTitle(_translate("MainWindow", "Grid"))
        self.menuGame_Mode.setTitle(_translate("MainWindow", "Game Mode"))
        self.actionSolve.setText(_translate("MainWindow", "Solve"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.action4x4.setText(_translate("MainWindow", "4x4"))
        self.action6x6.setText(_translate("MainWindow", "6x6"))
        self.action12x12.setText(_translate("MainWindow", "12x12"))
        self.actionSolver.setText(_translate("MainWindow", "Solver"))
        self.action1_Player.setText(_translate("MainWindow", "1 Player"))
        self.action2_Players.setText(_translate("MainWindow", "2 Players"))

        """ BUTTON-FUNCTION CONNECTIONS """
        self.pushButton_17.clicked.connect(lambda: self.dfsguiprep())
        self.pushButton_13.clicked.connect(lambda: self.dfsguisingle((1, 3)))
        self.pushButton_00.clicked.connect(lambda: self.dfsguisingle((0,0)))
        self.pushButton_01.clicked.connect(lambda: self.dfsguisingle((0,1)))
        self.pushButton_02.clicked.connect(lambda: self.dfsguisingle((0,2)))
        self.pushButton_03.clicked.connect(lambda: self.dfsguisingle((0,3)))
        self.pushButton_10.clicked.connect(lambda: self.dfsguisingle((1,0)))
        self.pushButton_11.clicked.connect(lambda: self.dfsguisingle((1, 1)))
        self.pushButton_12.clicked.connect(lambda: self.dfsguisingle((1, 2)))
        self.pushButton_20.clicked.connect(lambda: self.dfsguisingle((2,0)))
        self.pushButton_21.clicked.connect(lambda: self.dfsguisingle((2,1)))
        self.pushButton_22.clicked.connect(lambda: self.dfsguisingle((2,2)))
        self.pushButton_23.clicked.connect(lambda: self.dfsguisingle((2,3)))
        self.pushButton_30.clicked.connect(lambda: self.dfsguisingle((3,0)))
        self.pushButton_31.clicked.connect(lambda: self.dfsguisingle((3,1)))
        self.pushButton_32.clicked.connect(lambda: self.dfsguisingle((3,2)))
        self.pushButton_33.clicked.connect(lambda: self.dfsguisingle((3,3)))

        """ Button List """

        self.blist = [[self.pushButton_00, self.pushButton_01, self.pushButton_02, self.pushButton_03],
                      [self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13],
                      [self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23],
                      [self.pushButton_30, self.pushButton_31, self.pushButton_32, self.pushButton_33]]

    """ BUTTON FUNCTIONS """



    def dfsguisingle(self, bs):

        stringTrie = self.trie
        startChar = self.board.letters[bs[0]][bs[1]]
        temp = copy.deepcopy(self.board.letters)
        temp[bs[0]][bs[1]] = '-'

        Board.dfs(self.board, temp, stringTrie, (bs[0], bs[1]), startChar, False, None, True, self, [(bs[0], bs[1])])

    def dfsguiprep(self):

        count = 0
        limit = 100
        n = 4

        stringTrie = self.trie
        for i in range(n):
            for j in range(n):

                QtWidgets.qApp.processEvents()
                startChar = self.board.letters[i][j]
                temp = copy.deepcopy(self.board.letters)
                temp[i][j] = '-'

                Board.dfs(self.board, temp, stringTrie, (i,j), startChar, False, None, True, self, [(i,j)])

                count += 100 / n**2
                self.progressBar.setValue(count)

    # depth first search
    # def dfsgui(self, board, trie, start = (0, 0), prefix = '', chainList = [], cmdVis = False, connection = None):

    #     QtWidgets.qApp.processEvents()

    #     if cmdVis:
    #         print(f'prefix = {prefix}')
    #         print(board)
    #         self.board.spcPrint(connection)
    #         #time.sleep(.15)
    #         print('Found Words')
    #         print('-----------')
    #         # for i in self.wordList:
    #         #     self.textEdit.setText(i)
    #         #     print(i)
    #         wlist = set(self.wordList)
    #         self.textEdit.clear()
    #         for i in wlist:
    #             self.textEdit.append(i)
    #             print(i)
    #         print('-----------')

    #     for i in chainList:
    #         self.blist[i[0]][i[1]].setStyleSheet("background-color: #03A9F4")

    #     if cmdVis and connection == None:
    #         connection = [False for i in range(42)]

    #     board = copy.deepcopy(board)

    #     directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

    #     if trie.has_key(prefix):  # current word is valid:
    #         self.wordList.append(prefix)
    #         for i in chainList:
    #             self.blist[i[0]][i[1]].setStyleSheet("background-color: #00cc00")
    #         if cmdVis:
    #             print(f'ADDED {prefix}')
    #             print(chainList)
    #         self.textEdit.append(f'--> {prefix}')
    #         QtWidgets.qApp.processEvents()
    #         #time.sleep(.5)
    #         #input()

    #     QtWidgets.qApp.processEvents()

    #     for i in directions:
    #         newStart = tuple(map(add, i, start))
    #         x, y = newStart
    #         if x >= 0 and x < self.size and y >= 0 and y < self.size:
    #             newPrefix = prefix + board[x][y]
    #             newChainList = copy.deepcopy(chainList)
    #             newChainList.append((newStart[0],newStart[1]))
    #             if trie.items(newPrefix) != []:  # i not already searched & i a valid space & valid prefix
    #                 newBoard = copy.deepcopy(board)
    #                 newBoard[x][y] = '-'

    #                 newCon = copy.deepcopy(connection)
    #                 if cmdVis:
    #                     if i == (1, 0) or i == (-1, 0):
    #                         newCon[13 * y + min(start[0], x)] = True
    #                         print(f'start = {start}')
    #                         print(f'next = {newStart}')
    #                     if i == (0, 1) or i == (0, -1):
    #                         newCon[13 * min(start[1], y) + 3 * (x + 1)] = True
    #                         print(f'start = {start}')
    #                         print(f'next = {newStart}')
    #                     if i == (-1, 1) or i == (1, -1):
    #                         newCon[13 * min(start[1], y) + 3 * max(start[0], x) + 1] = True
    #                         print(f'start = {start}')
    #                         print(f'next = {newStart}')
    #                     if i == (1, 1) or i == (-1, -1):
    #                         newCon[13 * min(start[1], y) + 3 * max(start[0], x) + 2] = True
    #                         print(f'start = {start}')
    #                         print(f'next = {newStart}')
    #                 QtWidgets.qApp.processEvents()

    #                 self.dfsgui(newBoard, trie, newStart, newPrefix, newChainList, cmdVis, newCon)
    #                 # newBoard, trie, newStart, newPrefix, cmdVis, newCon
    #                 # dfs @i with modified bord & prefix
    #                 # add word to list if it is at the end of the trie

    #     self.blist[start[0]][start[1]].setStyleSheet("background-color: None")
    #     return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Breeze')
    MainWindow = QtWidgets.QMainWindow()
    ui = BOGGLE()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())