import random
#listArray=[]
#Amount=int(input("Enter tha amount of numbers you want:"))
#counter=1
#while counter<=Amount:
    #N=random.randint(1,100)
    #listArray.append(N)
    #counter+=1
#print(listArray)
#listArray.clear

Numbers=[]
items=int(input("How manu numbers: "))
for counter in range (0,items,1):
    number=random.randint(1,100)
    Numbers.append(number)
for eachNumber in Numbers:
    print(eachNumber)
Numbers.clear
    