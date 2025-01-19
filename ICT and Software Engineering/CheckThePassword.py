password="Banana"
attempts=3
userPassword=input("Enter your password: ")

while password!=userPassword:
    print("Password incorrect!")
    attempts-=1
    userPassword=input("Enter your password: ")
    if(attempts==1):
        print("Your account has been blocked.") 
        break 
else:
    print("Password correct!")
