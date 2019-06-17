import Board
import copy
from Words import Words

board = Board.Board()
print(board)
board.spcPrint()
words = Words()
stringTrie = words.trie(1)

startChar = board.letters[1][1]
temp = copy.deepcopy(board.letters)
temp[1][1] = '-'

board.dfs(temp, stringTrie, (1,1), startChar, cmdVis = True)

"""Let's do it!"""
for i in range(len(board.letters)-1):
    for j in range(len(board.letters)-1):
        board.dfs(temp, stringTrie, (i,j), cmdVis = True )



set(board.words)

board.letters




board.letters[1][1]