correct_num=5

a=0
while a<10:
 guess=int(input("What is number?"))
 print (guess)
 a=a+1
 if guess==correct_num:
     print ("That was a good guess!")
     break