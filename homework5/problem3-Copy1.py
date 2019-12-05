def password(string):
    count=0
    
    for i in string:
        if i.isdigit():
            count+=1 
    if len(string) >= 10 and count >= 2:
        return True
    else:
        print('Invalid Password')