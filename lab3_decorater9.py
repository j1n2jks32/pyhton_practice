# Write a decorator that restrict number division by zero. (lab-9)
def prevent_zero_division(func):
    def wrapper(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed")
            return None
        return func(a, b)
    return wrapper

@prevent_zero_division
def divide(x, y):
    return x / y

print(divide(10, 2))
print(divide(10, 0))
