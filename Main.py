# main function
from Board import Board
import pytrie
import time
from Words import Words

# neue Tafel
 # n = int(input('Board size:'))
 # board = Board(n)
 # print(board)
board = Board(n=6)
print(board.letters)

# neue Words
words = Words('words_new.txt')

# neue trie
stringTrie = words.trie(1)

t = time.time()
# DFS through boards, checking validity throughout
for i in range(board.size):
    for j in range(board.size):
        print(f'i = {i}, j = {j}')
        temp = list(board.letters)
        board.dfs(temp, stringTrie, (i,j))

print(f'algorithm time = {time.time() - t}')

print(len(set(board.words)))
a = list(set(board.words))
a.sort()
w = open('output.txt', 'w')

for i in a:
    w.write(f'{i}\n')

