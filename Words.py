import pygtrie
import pytrie
import time

class Words:
    """ Lese alle Wörter in eine Liste ein """

    def __init__(self, path='words_new.txt'):  # Wir können später optimisieren
        with open(path) as word_file:
            valid_words = list(word_file.read().split())

        self.list = valid_words

    def __str__(self):
        return str(self.list)

    """Die Länge des längsten Wortes"""

    def long_boi(self):  # Das längste Wort: 'dichlorodiphenyltrichloroethane' mit einer Länge von 31 Buchstaben
        lon = ''
        for i in self.list:
            if len(i) > len(lon):
                lon = i
        return len(lon)

    """ Trei Versuch - PRÄFIX-BASIERT | Funktioniert aber nicht wie ich will """

    def trie(self, trieType = 0):
        # di = {}
        # for k in range(len(self.list)-1):
        #     di[self.list[k]] = k
        if trieType == 0:
            startTime = time.time()
            print(f'pytrie SST start time: {startTime}')
            b = pytrie.SortedStringTrie(zip(self.list,list(range(len(self.list)))))
            print(f'pytrie SST time elapsed: {time.time() - startTime}')
            return(b)

        if trieType == 1:
            startTime = time.time()
            print(f'pytrie ST start time: {startTime}')
            trie = pytrie.StringTrie(zip(self.list,list(range(len(self.list)))))
            print(f'pytrie ST time elapsed: {time.time() - startTime}')
            #print(trie.keys(prefix="aman"))
            return(trie)

        if trieType == 2:
            startTime = time.time()
            print(f'pytrie T start time: {startTime}')
            trie = pytrie.Trie(zip(self.list,list(range(len(self.list)))))
            print(f'pytrie T time elapsed: {time.time() - startTime}')
            print(trie.keys(prefix="aman"))
            return(trie)

        if trieType == 3:
            startTime = time.time()
            print(f'pygtrie CT start time: {startTime}')
            trie = pygtrie.CharTrie(zip(self.list,list(range(len(self.list)))))
            print(f'pygtrie CT time elapsed: {time.time() - startTime}')
            print(trie.keys(prefix="aman"))
            return(trie)

        if trieType == 4: #fast but unusable
            startTime = time.time()
            print(f'pygtrie ST start time: {startTime}')
            trie = pygtrie.StringTrie(zip(self.list,list(range(len(self.list)))))
            print(f'pygtrie ST time elapsed: {time.time() - startTime}')
            print(trie.keys('ute'))
            return(trie)

        if trieType == 5:
            startTime = time.time()
            print(f'dict start time: {startTime}')
            trie = dict(zip(self.list,list(range(len(self.list)))))
            print(f'dict time elapsed: {time.time() - startTime}')
            #print(trie.keys('ute'))
            return(trie)

""" TESTS """

# Trie Test
# w = Words()

# for i in range(6):
#     tr = Words.trie(w, i)
#print(tr.keys(prefix="aman"))
#print(tr.keys(prefix="a"))

# tr = w.trie(1)
# print(tr.items(''))
