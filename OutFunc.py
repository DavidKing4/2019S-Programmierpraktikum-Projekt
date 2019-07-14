import copy
import time
import threading
from operator import add

def i_list(el, li):
    out = None
    for i in range(len(li)):
        for j in range(len(li[i])):
            if el == li[i][j]:
                out = (i, j)
    return out

def listi_list(el, li):
    out = []
    for i in range(len(li) ):
        for j in range(len(li[i]) ):
            if li[i][j] == el:
                out.append((i,j))
    return out

def foundWordlist(word, board): 
    found = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == word[0]:
                newWord = word[1:]
                newBoard = copy.deepcopy(board)
                newBoard[i][j] = '-'
                pathList = [(i, j)]
                found.append(search(word = newWord, board = newBoard, start = (i, j), path = [(i,j)], pathList = []))
    if found != [] and found[0] != [] and type(found[0][0]) == tuple:
        found = [found]
    return found
            
def search(word, board, start, path = [], pathList = []):

    if len(word) == 0:
        return path

    directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    n = len(board)

    for i in directions:
        newStart = tuple(map(add, i, start))
        x, y = newStart
        if x >= 0 and x < n and y >= 0 and y < n:
            if board[x][y] == word[0]:
                newWord = word[1:]
                newBoard = copy.deepcopy(board)
                newBoard[x][y] = '-'
                path.append((x, y))
                temp = search(word = newWord, board = newBoard, start = newStart, path = path, pathList = pathList)
                if temp != [] and type(temp[0]) == tuple:
                    pathList.append(temp)
        else:
            newWord = word
            newBoard = newBoard = copy.deepcopy(board)
    return pathList


                


def formatTime(x):
    minutes, seconds_rem = divmod(x, 60)
    return str(minutes)+":"+str(seconds_rem)
def formatSec(x):
    seconds_rem = x
    return str(seconds_rem)

class RestartableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        self._args, self._kwargs = args, kwargs
        super().__init__(*args, **kwargs)
    def clone(self):
        return RestartableThread(*args, **kwargs)