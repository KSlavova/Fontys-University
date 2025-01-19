import random
answer="yes" #answer to the question: "Do you want to play again?"
bestScore=[]
while (answer!="no"):
    randomNumber=random.randint(1,100)
    guess=int(input("Enter your guess here: "))
    while (guess<1 or guess>100):
        print("Sorry! Your number is not between 1 and 100.")
        guess=int(input("Enter your guess here: "))
    attempts=1
    while (guess!=randomNumber):
        if(guess>randomNumber):
            print("Too high!")
            guess=int(input("Enter your guess here: "))
            while (guess<1 or guess>100):
                print("Sorry! Your number is not between 1 and 100.") 
                guess=int(input("Enter your guess here: "))
            attempts+=1
        elif(guess<randomNumber):
            print("Too low!")
            guess=int(input("Enter your guess here: "))
            while (guess<1 or guess>100):
                print("Sorry! Your number is not between 1 and 100.")
                guess=int(input("Enter your guess here: "))
            attempts+=1
    bestScore.append(attempts)
    print(f"Congratulations! You guessed the number! Here are your attempts: {str(attempts)}")
    print(f"Here is your best score:  {str(min(bestScore))}")
    answer=input("Do you want to play again: ")
print("You exited the game.")