def dec1(any_func):
    def wrapper():
        return any_func() + ", it's me!"
        
    return wrapper

def dec2(any_func):
    def wrapper():
        print("<u>", any_func(), "</u")
        
    return wrapper

@dec2
@dec1
def func():
    return 'Hi'