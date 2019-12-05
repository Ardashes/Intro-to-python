def dec1(func1):
    def wrapper():
        var1 = func1()
        return var1[0] + var1[1:].lower()
    return wrapper

def dec2(func2):
    def wrapper():
        var2 = func2()
        print(var2, '!!! Welcome to the Party.')
    return wrapper

@dec2
@dec1
def func():
    return 'HI EVERYONE'

func()