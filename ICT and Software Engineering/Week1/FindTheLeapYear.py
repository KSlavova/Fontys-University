answer="yes"
while answer!="no":
      Y=int(input("Enter the year you want to check here: "))
      if(Y%4==0 and Y%100!=0 or Y%400==0):
            print("Leap year!")
      else: 
            print("Not a leap year.")
      print("Do you want to check another year?")
      answer=input("Answer: ")
      if(answer=="no"):
            print("End of program.")
