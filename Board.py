# Spiel Tafel

import copy
import math
from operator import add
import random
import string
import time

class Board:
    # We need to prevent the repetitions

    def __init__(self, n = 4, rand = True, letters = []):    #Dynamic range with "n", in case we decide to alter the size of the board

        if rand:
            letters = [['' for i in range(n)] for j in range(n)]
            lettersString = string.ascii_letters[:26]    # 'abcdefghijklmnopqrstuvwxyz'
            for i in range(n):
                for j in range(n):
                    letters[i][j] = random.choice(lettersString)

        self.letters = letters
        self.size = n
        self.words = []

    def __str__(self): #up connetions counted before down connections in connection array
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

    def spcPrint(self, connection = None): #__only functioning on a 4x4 board__

        if connection == None:
            connection = [False for i in range(72)]

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
    def dfs(self, board, trie, start = (0,0), prefix = '', cmdVis = False, connection = None):

            if cmdVis:
                print(prefix)
                self.spcPrint(connection)
                time.sleep(.15)
                for i in self.words:
                    print(i)

            if cmdVis and connection == None:
                connection = [False for i in range(42)]

            board = copy.deepcopy(board)

            directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

            if trie.has_key(prefix): #current word is valid:
                self.words.append(prefix)
                if cmdVis:
                    print(f'ADDED {prefix}')


            for i in directions:
                newStart = tuple(map(add, i, start))
                x, y = newStart
                if x >= 0 and x < self.size and y >= 0 and y < self.size:
                    newPrefix = prefix + board[x][y]
                    if trie.items(newPrefix) != []:#i not already searched & i a valid space & valid prefix
                        newBoard = copy.deepcopy(board)
                        newBoard[x][y] = '-'

                        newCon = copy.deepcopy(connection)
                        if cmdVis:
                            if i == (1,0) or i == (-1,0):
                                newCon[13*y + min(start[0], x)] = True
                                print(f'start = {start}')
                                print(f'next = {newStart}')
                            if i == (0,1) or i == (0,-1):
                                newCon[13*min(start[1], y) + 3*(x + 1)] = True
                                print(f'start = {start}')
                                print(f'next = {newStart}')
                            if i == (-1,1) or i == (1,-1):
                                newCon[13*min(start[1], y) + 3*max(start[0], x) + 1] = True
                                print(f'start = {start}')
                                print(f'next = {newStart}')
                            if i == (1,1) or i == (-1,-1):
                                newCon[13*min(start[1], y) + 3*max(start[0], x) + 2] = True
                                print(f'start = {start}')
                                print(f'next = {newStart}')
                                
                        self.dfs(newBoard, trie, newStart, newPrefix, cmdVis, newCon)#dfs @i with modified bord & prefix
                        #add word to list if it is at the end of the trie
            
            return