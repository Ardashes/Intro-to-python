def my_decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper
@my_decorator
def text():
    print("inside the function")
