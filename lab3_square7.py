def positive_numbers(fun):
    def wrapper(n):
        if n <= 0:
            print("Error: only positive numbers allowed")
        else:
            fun(n)  
    return wrapper

@positive_numbers
def sqr(num):
    print("square =", num * num)


sqr(5)  
sqr(-5) 
