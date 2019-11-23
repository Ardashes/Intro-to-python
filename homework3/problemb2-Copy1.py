a1=["cookies","chocolate",8,True,-3,-5,"chocolate",8,False,8]
b1=[8,True,10,14,"chocolate","milk","jelly",True,False,True]
set_a1=set(a1)
set_b1=set(b1)
union_ab=set_a1.union(set_b1)
intersection_ab=set_a1.intersection(set_b1)
union_ab.add("Kit-Kat")
union_ab.add("Oreo")
new_set= union_ab or intersection_ab
print(new_set)
print ("chocolate" in new_set)
new_set.remove("Oreo")
print(new_set)