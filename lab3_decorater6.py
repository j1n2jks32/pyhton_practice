#decorater lab3
def simple_decorater(fun):
    def  wrapper():
        print("before function runs")
        fun()
        print("after function runs")
    return wrapper
@simple_decorater
def say_hello():
    print("hello")
say_hello()
        
        
