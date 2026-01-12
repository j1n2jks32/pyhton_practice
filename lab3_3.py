#lab3 -3
def details(**kwargs):
    for  key,value in kwargs.items():
        print(f"{key}:{value}")
details(name="jnanesh",age=20,course="python")

