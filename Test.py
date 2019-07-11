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





b = Board()











w = Words()



board.letters[1][1]



#Board.Board().letters




w.trie(1)














#board[0][0]