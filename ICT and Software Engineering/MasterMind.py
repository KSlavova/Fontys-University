from random import randint

def CodeGenerator(List):   #generates random code
    for i in range(0,4,1):
        code=randint(1,6)
        secretCode.append(code)
    return List

def ConvertToInt(emptyList, List): #to convert the digits in the list into integers
    for elem in List:
        emptyList.append(int(elem))
    return emptyList

def Checking(counterRight,counterWrong,userList,List): #searches if there are correct guesses
    copyList=List.copy() 
    for i in range(0,4,1):  #checks for correct guesses on correct places
     if userList[i]==List[i]:
        counterRight+=1
        copyList.remove(List[i]) #removes the full matches 

    for i in range(0,4,1):   #checks for correct digits in wrong places
         if userList[i] in copyList: #checks if the digit is in the list with removed matches
            counterWrong+=1
    return counterRight, counterWrong

def InputNotValid(guess): #checks for invalid input
    for digit in guess:
        if len(guess)!=4 or digit>="A" and digit<="z": 
            return False
    for digit in guess:
        if int(digit)<1 or int(digit)>6:
            return False
    return True

command="yes"
while command!="no":
    attempts=12 
    secretCode=[]
    code=CodeGenerator(secretCode)
    print(code) 
    rightPlace=0
    while(attempts>0 and rightPlace<4):
        emptyList=[] #to convert the digits in the list into integers
        guess=input("Enter 4 digits between 1-6: ")

        while InputNotValid(guess)==False:
            guess=input("This input is not correct!Enter 4 digits between 1-6: ")
        
        guessList=ConvertToInt(emptyList,guess)  #converts the digits to int

        rightPlace,wrongPlace=Checking(0,0,guessList,code)  
        print(f"Guessed digits:{rightPlace}, right digits in wrong place:{wrongPlace}")

        if(rightPlace==4):
            print("You win!")
        else:
            attempts-=1
            print(f"You have:{attempts}")
        if(attempts==0):
            print("You lost!") 

    code.clear() #empties the list 
    command=input("Do you want to play again: ")