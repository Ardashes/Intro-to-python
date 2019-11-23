list1=["a","abc","xyz","s","aba","1221","ab"]


count=0
for x in list1:
    if len(x)>=2:
       if x[0]==x[-1]:
         count+=1
         print (count)