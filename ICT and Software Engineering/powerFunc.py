def Power(numA,numB):
    p=1
    for i in range(0,numB,1):
        p*=numA
    return p

A=int(input("Enter number A: "))
B=int(input("Enter number B: "))
power=Power(A,B)
print(f"The result of the calculation is {power}.")