#20. Print the multiplication table of a number (e.g., 5 × 1 = 5 ... 5 × 10 =50)
num=int(input("enter a namber to multiplication table"))
for i in range(1,11):
    print(f"{num} x {i}={num*i}")
