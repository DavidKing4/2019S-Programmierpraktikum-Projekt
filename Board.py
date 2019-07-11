# Spiel Tafel
import copy
import math
from operator import add
from PyQt5 import QtWidgets
import random
import string
import time


class Board:
    # We need to prevent the repetitions

    def __init__(self, n = 4, rand = True, letters = []):    # Dynamic range with "n"

        #lettersString = string.ascii_letters[:26]
        if rand:
            letters = [['' for i in range(n)] for j in range(n)]
            lettersString = string.ascii_letters[:26]    # 'abcdefghijklmnopqrstuvwxyz'
            ran = []
            bran = []
            if n <=5:    # If the elements on the board are fewer than 26 there doesn't have to be any repetitions.

                while len(ran) < n**2:
                     ran.append(random.choice(lettersString))
                     ran = list(set(ran))

                for i in range(n):
                    for j in range(n):
                        letters[i][j] = ran[(n*i)+j]    # random.choice()
            else:
                # If the number of elements greater than 26 there have to be some repetitions
                # but we can reduce the repetitions by creating multiple genuine 26 letter lists
                for i in range((n**2 // 26)+1):
                    while len(ran) < len(lettersString):
                        ran.append(random.choice(lettersString))
                        ran = list(set(ran))
                    # bran.append(lambda: ran[k] for k in range(len(ran)-1))
                    bran += ran

                for imp in range(n):
                    for jan in range(n):
                        letters[imp][jan] = bran[(n*imp)+jan]

        self.letters = letters
        self.size = n

        "The list of the extracted words"
        self.words = []

    def __str__(self):    # up connections counted before down connections in connection array
        return str(self.letters)

    # a -- b -- a
    # | /\ | /\ |
    # a -- n -- t
    # | /\ | /\ |
    # p -- a -- t

    # x 1- x 2- x 3- x
    # 4 56 7 89 A BC D
    # x E- x F- x G- x H
    # I JK L MN O PQ R
    # x S- x TU x V- x
    # W XY Z ab c de f
    # x g- x h- x i- x

    def spcPrint(self, connection = None):    # only functioning on a 4x4 board__
                                              # Primarily for debuging
        if connection is None:   # U -> "is" instead of "=="
            connection = [False for i in range(72)]    # Whole board -> False

        letters = self.letters

        conPos = 0
        for i in range(3):
            for j in range(3):
                print(letters[j][i], end = ' ')
                if connection[conPos]:
                    print('--', end = ' ')
                else:
                    print('   ', end = '')
                conPos += 1

            print(letters[j+1][i], end = '\n')
            for j in range(3):
                if connection[conPos]:
                    print('|', end = ' ')
                else:
                    print('  ', end = '')
                conPos += 1
                if connection[conPos]:
                    print('/', end = '')
                else:
                    print(' ', end = '')
                conPos += 1
                if connection[conPos]:
                    print('\\', end = ' ')
                else:
                    print('  ', end = '')
                conPos += 1

            if connection[conPos]:
                print('|')
            else:
                print(' ')
            conPos += 1
            i += 1
        for j in range(3):
            print(letters[j][i], end = ' ')
            if connection[conPos]:
                print('--', end = ' ')
            else:
                print('   ', end = '')
            conPos += 1
        print(letters[j+1][i])


    # depth first search
    def dfs(self, board, trie, start = (0, 0), prefix = '', cmdVis = False, connection = None, guiVis = False, gui = False, chainList = [], delay = 0): #big boy function
        d = delay
        if cmdVis:
            print(f'prefix = {prefix}')
            self.spcPrint(connection)
            #time.sleep(delay)
            print('Found Words')
            print('-----------')
            for i in self.words:
                print(i)
            print('-----------')

        if cmdVis and connection == None:
            connection = [False for i in range(42)]

        if guiVis:
            for i in chainList:
                gui.blist[i[0]][i[1]].setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #74b9ff ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center;")
                time.sleep(d)

            QtWidgets.qApp.processEvents()

        board = copy.deepcopy(board)

        directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

        if trie.has_key(prefix):    # current word is valid:

            self.words.append(prefix)
            time.sleep(d)
            if cmdVis:
                print(f'ADDED {prefix}')
            if guiVis:
                for i in chainList:

                    gui.blist[i[0]][i[1]].setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #55efc4 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center;")
                    time.sleep(d)
                gui.textEdit.append(f'--> {prefix}')
                time.sleep(d)
                QtWidgets.qApp.processEvents()

        for i in directions:
            newStart = tuple(map(add, i, start))
            x, y = newStart
            if x >= 0 and x < self.size and y >= 0 and y < self.size:
                newPrefix = prefix + board[x][y]
                if guiVis:
                    newChainList = copy.deepcopy(chainList)
                    newChainList.append((newStart[0],newStart[1]))
                else:
                    newChainList = chainList
                if trie.items(newPrefix) != []:    # i not already searched & i a valid space & valid prefix
                    newBoard = copy.deepcopy(board)
                    newBoard[x][y] = '-'

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

                    QtWidgets.qApp.processEvents()
                            
                    self.dfs(newBoard, trie, newStart, newPrefix, cmdVis, newCon, guiVis, gui, newChainList, d)
                    # dfs @i with modified bord & prefix
                    # add word to list if it is at the end of the trie

        gui.blist[start[0]][start[1]].setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        time.sleep(d)
        return