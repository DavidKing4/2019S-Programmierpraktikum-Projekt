import Generator
from Words import Words

b = Generator.Board()
print(b)

print(Generator.Board(n=6))

print(Words('words_new.txt').list[0])


bo = Generator.Board()
bo.letters

# manuel hoodies
bo.letters[2][1]    # main man
bo.letters[2][0]
bo.letters[2][2]

bo.letters[1][0]
bo.letters[1][1]
bo.letters[1][2]

bo.letters[3][0]
bo.letters[3][1]
bo.letters[3][2]




try:
    a = bo.letters[-1][0]
except:
    a = None

l = []
for i in range(1,4):
    for j in range(1,4):
        l.append((i,j))

bo.letters[l[1][1]][l[1][0]

bo.hood(1,1)
