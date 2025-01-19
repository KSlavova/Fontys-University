word="school"
wordList=list(word)
#print(wordList)
#wordList.clear()
letter=input("Give me a letter: ")
lowerLetter=letter.lower()
if lowerLetter in wordList:
    print("The letter " + lowerLetter + " is in my word!")
else:
    print("The letter " + lowerLetter + " is NOT in my word!")