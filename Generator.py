# Tafel erzeugen

import random
import string

class Board:

	def __init__(self, n = 4):    # Dynamic range with "n", in case we decide to alter the size of the board
		lettersString = string.ascii_letters[:26] #'abcdefghijklmnopqrstuvwxyz'
		boardLetters = [['' for i in range(n)] for j in range(n)]
		for i in range(n):
			for j in range(n):
				boardLetters[i][j] = random.choice(lettersString)
		self.letters = boardLetters

	def __str__(self):
		return(str(self.letters))