Schedule={
    "Computing":401,
    "Biology":211,
    "Electronics":75
}
name=input("Enter your name here: ")
subject=input("Enter your subject here: ")

if(subject in Schedule):
    print(f"Hi {name}, go to {Schedule.get(subject)} room  for {subject}.")
else: 
    print("I don't which room that class is in.")
        