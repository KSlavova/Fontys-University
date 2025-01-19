import random
array=[]
Sum=0
counter=1
while counter<=5:
    N=random.randint(1,100)
    array.append(N)
    counter+=1

addition=0
for eachNum in array:
    addition+=eachNum

print(addition)
print(array)
array.clear
