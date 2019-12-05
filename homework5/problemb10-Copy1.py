def list_func(list1=[]):
    for i in list1:
        yield (i+1)
        

my_list=list_func([1,2,3,4])