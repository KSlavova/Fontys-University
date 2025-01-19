answer="J"
while(answer!="N"):
    N=int(input("Enter a number lower than 10: "))
    S=N+1
    if(S<10 and S!=10):
        print("I win!")
    if(S==10):
        print("You win!")
    if(S>10): 
        print("Sorry! Your number is not lower than 10.")
    print("Do you want to play another game?")
    answer=input("Answer: ")
    if(answer=="J"):
        print("Lets play another game!")
    else:
        print("You exited the game.")
