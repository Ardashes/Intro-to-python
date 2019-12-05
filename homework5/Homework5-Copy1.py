def my_range(n):
    c=0
    while c<=n:
        yield c
        c+=1
        if c>n:
            print("There are no values left")