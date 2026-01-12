#19. Calculate the sum of numbers from 1 to N (user input).
n=int(input("entr a numbers"))
total=0
for i in range(1,n+1):
    total+=i
print("The sum of numbers from 1 to", n, "is:", total)
