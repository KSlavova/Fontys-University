secretPassword="gehein"
userpassword=input("Enter your password:")
while secretPassword!=userpassword:
    print("You entered the wrong password!")
    userpassword=input("Enter your password:")
print ("Thank you, you have access to the system!")