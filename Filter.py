from Words import Words

newWords = []

for i in Words().list:
	if len(i) >= 3:
		newWords.append(i)

file = open('words_new.txt','w')

for i in newWords:
	file.write(i + '\n')

