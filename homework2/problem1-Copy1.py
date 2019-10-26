## problem1
project='cake'
difficulty=5
ingredients=['flour','butter','sugar','eggs', 'cocoa powder','baking powder']
x='apples'
b='butter'
m='margarinate'
e='eggs'
if x in ingredients:
    print ('apple is an ingredient') 
else: print('apple is not an ingredient')  
if b in ingredients:
    print ('butter is an ingredient')
else: print ('butter is not an igredient')  
if  m or e in ingredients:
    print ('there is egg and/or margarinate in the ingredients')
else: print ('''there isn't egg and/or margarinate''' ) 
if m and e in ingredients:
    print ('there is egg and margarinate')
else: print ('''there isn't egg and margarinate''')   
    
flour='175g'
butter='175g'
sugar='100g'
eggs=2
cocoa_powder= '1ts'
baking_powder=0.5


print ('flour -', flour)
print ('butter-',butter) 
print ('sugar -', sugar)
print ('eggs -', eggs)
print ('cocoa powder -', cocoa_powder)
print ('baking powder -', baking_powder)