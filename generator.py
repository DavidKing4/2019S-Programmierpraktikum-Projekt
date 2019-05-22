#Tafel erzeugen
import random
import string

class Board:

	def __init__(self):
		lettersString = string.ascii_letters[:26] #'abcdefghijklmnopqrstuvwxyz'
		boardLetters = [['a' for i in range(4)] for j in range(4)]
		for i in range(4):
			for j in range(4):
				boardLetters[i][j] = random.choice(lettersString)
		self.letters = boardLetters

	def __str__(self):
		return(str(self.letters))