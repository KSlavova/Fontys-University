from random import choice

def firstLine(line,word):  #prints the empty word with the first and last letters
    for counter in range(0,len(word),1):
       line.append("_")
    line[0]=word[0] #sets the first letter
    end=len(word)-1
    line[end]=word[end] #sets the last letter
    return line

def AddLetters(guessLetter,emptyWord,word): #fills the empty spaces
    for letter in word:
        if(letter==guessLetter):
            ind=word.index(letter)
            emptyWord[ind]=letter
    return emptyWord

def Print(word):    #prints the updated word
    for element in word:
        print(element, end=" ")
    print()

wordsList=["dog","rainbow", "cat", "fish","mouse","ocean"]
hintsList=["A friendly animal that barks.",
"A colorful arc that appears in the sky after rain.", 
"A small animal that says 'meow'.",
"A small animal that swims in water.",
"A small animal that loves cheese.",
"A large body of water."]

balloons=2 #attempts you have
emptyWord=[]
usedLetters=[]

print("Welcome to the Balloon Game!")
print("You have two balloons. Good luck!")

word=choice(wordsList) #chooses random word from the wordList
ind=wordsList.index(word) #gets the index of the word that equals to the index of the hint
print(hintsList[ind])

Print(firstLine(emptyWord,word))
while balloons>=1 and "_" in emptyWord:  
    guess=input("Enter a letter: ").lower() #so you can enter capital letters too
    if guess>="a" and guess<="z" and len(guess)==1: #checks for correct input
        if guess not in usedLetters:
            if guess not in word:
                print("Sorry! This letter is not in the word.")
                balloons-=1
                usedLetters.append(guess)
            else:
                updatedWord=AddLetters(guess,emptyWord,word)
                Print(updatedWord)
                balloons+=1
                usedLetters.append(guess)
        else:
            print("You've already used this letter.")
    else:
        print("Sorry! This is not a correct input!")

if balloons>0:
    print("You win!")
else:
    print("You lost!")