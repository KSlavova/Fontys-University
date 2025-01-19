def average(numbers):# total average
    avg=sum(numbers)/len(numbers)
    return round(avg,2)

def InvalidInput(Num): #checks for invalid or empty input
    if(Num==" " or Num>="A" and Num<="z"):
        inputNum=input("Sorry! Invalid or empty input. Enter input: ")
        return False
    else:
        return True

def input_numbers(): #reads the numbers and adds them into a list
    numList=[]
    inputNum=input("Enter input: ")
    while(inputNum!=""):
        if InvalidInput(inputNum) is True:
           numList.append(float(inputNum))
        inputNum=input("Enter input: ")
    return numList

def average_segment(numbers,start,end):
    avgSeg=[]
    for i in range(start,end,1):
        avgSeg.append(numbers[i])
    return average(avgSeg)



rainfall=input_numbers() 
print("Rainfall Report:")
print(f"Total average: {average(rainfall)}")#prints the total average

for i in range(0,len(rainfall),7): #prints the average per week 
    end=i+7
    while end>len(rainfall):
        end-=1
    print(f"The average per week: {average_segment(rainfall,i,end)}")

for i in range(0,len(rainfall),30): #prints the average per month
    end=i+30
    while end>len(rainfall):
        end-=1
    print(f"The average per month: {average_segment(rainfall,i,end)}")