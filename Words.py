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

    '''creates a trie structure'''
    def trie(self):
        startTime = time.time()
        print(f'pytrie ST start')
        trie = pytrie.StringTrie(zip(self.list,list(range(len(self.list)))))
        print(f'pytrie ST time elapsed: {time.time() - startTime:.2f}s')
        return(trie)