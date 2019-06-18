import Board as b
import copy
from Words import Words

board = b.Board()
print(board)
board.spcPrint()
words = Words()
stringTrie = words.trie(1)

board.letters[0][0]


startChar = board.letters[1][1]
temp = copy.deepcopy(board.letters)
temp[1][1] = '-'

board.dfs(temp, stringTrie, (1,1), startChar, cmdVis = True)

"""Let's do it!"""
for i in range(len(board.letters)-1):
    for j in range(len(board.letters)-1):
        print(board.dfs(temp, stringTrie, (i,j), cmdVis = True ))

len(board.letters)




set(board.words)


board.words

board.letters


















w = Words()



board.letters[1][1]



Board.Board().letters




w.trie(1)














board[0][0]