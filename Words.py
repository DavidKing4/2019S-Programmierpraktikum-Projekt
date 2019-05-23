import pytrie as py
import os

# working directory
os.getcwd()

# Um "working directory" zu ändern | An dieser Stelle müssen wir eine Lösung finden direkt die Datei im Github-Ordner zu addressieren.
os.chdir("C:/Users/Utku Bilen Demir/Desktop/e4Ke2/Math/Programmieren/ProProjekt/2019S-Programmierpraktikum-Projekt")


class Words:
    
    " Lese alle Wörter in eine Liste ein "
    def __init__(self):    # Brauchen wir das wirklich als Funktion schreiben? Wir können später optimisieren
        with open('words_alpha.txt') as word_file:
            valid_words = list(word_file.read().split())
    
        self.list = valid_words
    def __str__(self):
        return str(self.list)
    
    

    
    
    """ Die Länge des längsten Wortes """
    def long_boi(self):    # Das längste Wort in unserer Liste: 'dichlorodiphenyltrichloroethane' mit einer Länge von 31 Buchstaben
        lon = ''   
        for i in self.list:
            if len(i) > len(lon):
                lon= i
        return(len(lon))
    
    """ Trei Versuch - PRAEFIX-BASIERT | Es hat nicht funktioniert aber ich versuch spaeter weiter """
    def trei(self, pre):
        tr = py.StringTrie()    # Ein leeres Baeumchen
        for i in self:    # Unsere Liste wird ins Trei eingetragen
            tr[i] = i
        return tr.values(pre)    # Passende Erweiterungen werden ausgegeben.
        
            
        
        




""" TESTS """

Words.trei(w,'a')



Words.long_boi(w)

w = Words()
print(w)

w.list[300000]

w.list[len(w.list)-1]


for i in wlist:
    if i[1] == 'a':
        return i
    
    
    
    
lon = ''   
for i in w.list:
    if len(i) > len(lon):
        lon= i
        
        
        
        
lon


py.Trie(w.list)


py.Trie()
