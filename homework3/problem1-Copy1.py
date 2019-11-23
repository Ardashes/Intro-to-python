import sys
list1=["Hello",1,True]
print (list1)
list2 = sys.argv[1:]

list1.extend(list2)


print (list1)