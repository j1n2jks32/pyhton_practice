#Write a decorator that ensures a function can only be called once. (lab3-10)
def call_once(func):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            print("Error: This function can only be called once")
            return None
        called = True
        return func(*args, **kwargs)

    return wrapper
@call_once
def greet():
    print("Hello!")

greet()
greet()   
