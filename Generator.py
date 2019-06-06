# Tafel erzeugen

import random
import string

class Board:
    # We need to prevent the repetitions

    def __init__(self, n = 4):    # Dynamic range with "n", in case we decide to alter the size of the board
        lettersString = string.ascii_letters[:26]    # 'abcdefghijklmnopqrstuvwxyz'
        boardLetters = [['' for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                boardLetters[i][j] = random.choice(lettersString)
        self.letters = boardLetters

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



