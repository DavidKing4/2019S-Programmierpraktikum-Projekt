from Board import *
import copy
from NEWGUI import BOGGLE
from PyQt5 import QtWidgets
import sys
from Words import Words



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = BOGGLE()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

print('hi')
Board.dfs(BOGGLE.board, BOGGLE.trie, start = (1, 1), prefix = '', cmdVis = False, connection = None, guiVis = True, gui = BOGGLE, chainList = [(1,1)])




startChar = board.letters[1][1]
temp = copy.deepcopy(board.letters)
temp[1][1] = '-'

board.dfs(temp, stringTrie, (1,1), startChar, cmdVis = False)

"""Let's do it!"""
# for i in range(len(board.letters)-1):
#     for j in range(len(board.letters)-1):
#         print(board.dfs(temp, stringTrie, (i,j), cmdVis = True ))

len(board.letters)




set(board.words)


board.words

board.letters




b=Board()
Board.dfs(b, trie=w.trie, board= b.letters )











w = Words()



board.letters[1][1]



#Board.Board().letters




w.trie()







import numpy as np
from numpy import reshape
lid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t"]
a = []
for i in range(0,len(lid), 4):
    a.append(lid[i:i+4])
a
#board[0][0]

def i_list(el, li):
    out = None
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if el == li[i][j]:
                out= (i, j)
    return out
lid[-2]
i_list("i", a)








from operator import add
a = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

b = (3,2)

c= []
for i in a:
    c.append(tuple(map(add, i, b)))


a

a[-1:]




