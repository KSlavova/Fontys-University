names=[]
heights=[]

for counter in range(1,4,1):
    n=input("Enter the players name: ")
    names.append(n)
    h=input("Enter the players height: ")
    heights.append(h)

tallest=max(heights)
i=heights.index(max(heights)) # i is the index of the biggest height
print(names[i] + " " + tallest)