# main function
from Board import Board
import copy
from GUI import Boggle
import pytrie
import time
from Words import Words

n = int(input('Board size:'))
board = Board(n)
print(board)

# neue Words
words = Words('words_new.txt')

# neue trie
stringTrie = words.trie()

t = time.time()

for j in range(board.size):
	for i in range(board.size):
		print(f'i = {i}, j = {j}')
		temp = copy.deepcopy(board.letters)
		temp[i][j] = '-'
		startChar = board.letters[i][j]
		board.dfs(temp, stringTrie, (i,j), startChar, cmdVis = False)

print(f'algorithm time = {time.time() - t:.2f}s')

print(len(set(board.words)))
a = list(set(board.words))
a.sort()
w = open('output.txt', 'w')

for i in a:
	w.write(f'{i}\n')
	print(i)

input()


