#main function
from Board import Board
import copy
import pytrie
import time
from Words import Words

#neue Tafel
n = int(input('Board size:'))
board = Board(n)
print(board)

#neue Words
words = Words('words_new.txt')

#neue trie
stringTrie = words.trie(1)

t = time.time()
#DFS through boards, checking validity throughout
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

testBoard = Board(4,0,[['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']])
connections = [False for i in range(42)]
# connections[0] = True
# connections[1] = True
# connections[2] = True
# connections[13] = True
# connections[14] = True
# connections[15] = True
# connections[26] = True
# connections[27] = True
#connections[31] = True
#testBoard.spcPrint(connections)