import Board
import copy
from Words import Words

board = Board.Board()
print(board)

words = Words()
stringTrie = words.trie(1)

startChar = board.letters[1][1]
temp = copy.deepcopy(board.letters)
temp[1][1] = '-'

board.dfs(temp, stringTrie, (1,1), startChar, cmdVis = True)