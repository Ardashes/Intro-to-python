list1 = ['Anna','Edgar']

def decorator_custom(func):
    def wrapper(*args, **kwargs):
        print(list1)
        func(*args, **kwargs)
        print(list1)
    return wrapper
    

@decorator_custom
def add_values(list2):
    for i in list2:
        if i not in list1:
            list1.append(i)
    return list1
    
add_values([1,2,3, 'Anna', 'ardo'])