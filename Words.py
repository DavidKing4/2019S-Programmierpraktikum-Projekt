from pytrie import SortedStringTrie as baum


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

    def trie(self):
        di = {}
        for k in range(len(self.list)-1):
            di[self.list[k]] = k

        return baum(di)


""" TESTS """

# Trie Test
w = Words()
tr = Words.trie(w)
tr.keys(prefix="aman")


