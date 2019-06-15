# Spiel Tafel

import copy
import random
import string
from operator import add

class Board:
    # We need to prevent the repetitions

    def __init__(self, n = 4, rand = 1, letters = []):    # Dynamic range with "n", in case we decide to alter the size of the board

        if rand == 1:
            letters = [['' for i in range(n)] for j in range(n)]
            lettersString = string.ascii_letters[:26]    # 'abcdefghijklmnopqrstuvwxyz'
            for i in range(n):
                for j in range(n):
                    letters[i][j] = random.choice(lettersString)

        self.letters = letters
        self.size = n
        self.words = []

    def __str__(self):
        return str(self.letters)

    """ Benachbarte Buchstaben von einem beliebigen Buchstabe """
    def hood(self, row, col):
        # will be optimised

        le_pos = self.letters[row][col]
        hoodies = []
        for i in range(row-1, row+2):
            for j in range(row-1, col+2):
                hoodies.append(self.letters[i][j])
        self.hoodies = hoodies

    #depth first search
    def dfs(self, board, trie, start = (0,0), prefix = ''):

            board = copy.deepcopy(board)
            #print(f'board = {board}')
            #print(f'DFS @ start = {start} with prefix = {prefix}')

            directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

            # if len(trie.items(prefix)) == 1:#end of the trie:
            #     wordList.append(prefix)#add word to wordlist
            #     return wordList

            #else:
            if trie.has_key(prefix): #current word is valid:
                #print(f'added {prefix}')
                self.words.append(prefix)
                #print(self.words)
                #print(len(self.words))

            for i in directions:
                newStart = tuple(map(add, i, start))
                x, y = newStart
                if x >= 0 and x < self.size and y >= 0 and y < self.size:
                    newPrefix = prefix + board[x][y]
                    if trie.items(newPrefix) != []:#i not already searched & i a valid space & valid prefix
                        newBoard = copy.deepcopy(board)
                        newBoard[x][y] = '-'
                        self.dfs(newBoard, trie, newStart, newPrefix)#dfs @i with modified bord & prefix
                        #add word to list if it is at the end of the trie

            return