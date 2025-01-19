listOfNum=[]
avg=0
Sum=0
counter=0
N=int(input("Enter a whole number: "))
listOfNum.append(N)
while N!=0:
     N=int(input("Enter a whole number: "))
     listOfNum.append(N)
     counter+=1
#avg=sum(listOfNum)/(len(listOfNum)-1)
for eachNum in listOfNum:
     Sum+=eachNum

avg=Sum/counter
print(listOfNum)
print(avg)
listOfNum.clear