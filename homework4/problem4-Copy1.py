d={"name":"Armen","age":15,"grades":[10,8,8,4,6,7],"weight":8}
n= int(input("What is weight?"))
if "weight" in d.keys():
      d["weight"]=n
      print (d)
      
else: d["weight"]=n
print (d)