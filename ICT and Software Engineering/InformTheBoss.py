def error(c): #c is the entered command
    message="Error. This is not a valid command."
    return message

flowerD={}

#empty lists in the dictionary
flowerD["flowers"]=[]
flowerD["prices"]=[]

counter=0 #counts the bunches of flowers
command=input("Enter command: ") #s for sold and i for information

while(command=="s"):
    flower=input("Enter the name of the flower: ") 
    flowerD["flowers"].append(flower)
    price=float(input("Enter the price: "))
    flowerD["prices"].append(price)
    counter+=1
    command=input("Enter command: ")
    if(command=="i"):
         avg=sum(flowerD["prices"])/len(flowerD["prices"]) #gets the average value of the prices 
         Max=max(flowerD["prices"]) #gets the max value of the list
         Min=min(flowerD["prices"]) #gets the min value of the list
         print ("Information")
         print(f"Bunches of flowers sold: {counter}")
         print(f"The value of the most expensive bunch sold: {Max}")
         print(f"The value of the least expensive bunch sold: {Min}")
         print(f"Average value of the bunches sold: {round(avg,2)}")
         command=input("Enter command: ")
else:
    message=error(command)
    print(message)
