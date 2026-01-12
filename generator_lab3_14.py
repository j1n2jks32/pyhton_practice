#Write a generator that yields squares of numbers from 1 to N. (lab3-14)
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i
for sq in square_numbers(5):
    print(sq)
