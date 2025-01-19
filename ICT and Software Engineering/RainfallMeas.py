def average(numbers):# total average
    avg=sum(numbers)/len(numbers)
    return round(avg,2)

def input_numbers(): #reads the numbers and adds them into a list
    numList=[]
    inputNum=input("Enter input: ")
    while(inputNum!=""):
        numList.append(float(inputNum))
        inputNum=input("Enter input: ")
    return numList

def average_segment(numbers,start, end): #calculates the average of a segment 
    #Sum=0                                
    #for i in range(start, end+1, 1):    #version without implementation
        #Sum+=numbers[i]
    #avg=Sum/7
    seg=numbers[start:end+1] #the searched segment
    return average(seg)  #implementing the average in the average_segment


rainfall=input_numbers() 
if len(rainfall)>=7:
    weekDays=7
    for counter in range(0,len(rainfall),1):
        s=counter*weekDays
        e=s+weekDays
        print(f"Average for a week: {average_segment(rainfall,s,e)}") 
    
#to do...

if len(rainfall)>=30:
    print(f"Average for a month: {average_segment(rainfall,s,e)}")


#print(rainfall)
print("Rainfall Report:")
print(f"Total average: {average(rainfall)}")#prints the total average
#print(f"Average for a week: {average_segment(rainfall,s,e)}")#prints the average of a segment of a week 
#print(f"Average for a month: {average_segment(rainfall,0,29)}")