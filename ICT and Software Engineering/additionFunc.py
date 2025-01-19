A=int(input("Enter number A: "))
B=int(input("Enter number B: "))
sign=input("Enter the sign: ")

def calculation(numberA,numberB, calc):
    if calc=="+":
        add=numberA + numberB
    elif calc=="-":
        add=numberA - numberB
    elif calc=="*":
        add=numberA * numberB
    elif calc=="/":
        add=numberA / numberB
    #print(f"The sum of {numberA} and {numberB} equals {add}.")
    return add
plus=calculation(A,B,sign)
print(f"The result of the calculation is {plus}.")