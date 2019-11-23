menu=["ice cream","chocolate","appple crisp","cookies"]
desert=input("What is desert?")
if desert in menu:
   print ("your desert will arrive in 10 minutes")
else:   
 while desert not in menu:
      desert1=input("What is the desert?")
      print ("please choose another desert")
      if desert1 in menu:
        print ("your desert wil arrive in 10 minutes")
        break
         
   


