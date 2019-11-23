a=[1,4,5,7,8,-2,0,-1]
print(a[3],a[5])
a_sorted=sorted(a,reverse=True)

print(a_sorted[1:4],a_sorted[2:7])
a_sorted.pop(2)
a_sorted.pop(3)
print (a_sorted)
b=["grapes","potatoes","tomatoes","orange","lemon","broccoli","carrot","sausages"]
b_sorted=sorted(b)
listc=[]
listc.append(a[1])
listc.append(a[2])
listc.append(a[3])
listc.append(b[4])
listc.append(b[5])
listc.append(b[6])
print(listc)