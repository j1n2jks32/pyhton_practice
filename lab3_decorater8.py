#Write a decorator that logs the arguments passed to a function.(lab3-8)
def log_args(func):
    def wrapper(a, b):
        print("Arguments passed:", a, b)
        return func(a, b)
    return wrapper
@log_args
def add(x, y):
    return x + y

result = add(5, 3)
print("Result:", result)
