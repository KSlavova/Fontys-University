word="environment"
wordList=list(word)
if(len(wordList.index()))<=10:
    for i in range(1,10,1):
        print("*", end=" ")
#elif(len(wordList.index()>10)):
    for j in range(10,len(wordList)+1,1):
        print("*", end="  ")
print()
for n in range(1,len(wordList)+1,1):
    print(n, end=" ")