#4 lab3
def is_prime(n):
    if n<=1:
        print(n,"is not prime")
        return
    for i in range(2,n):
        if n%i==0:
            print(n," is not a prime")
            return
    print(n,"is prime")
num=int(input("enter a number:"))
is_prime(num)
