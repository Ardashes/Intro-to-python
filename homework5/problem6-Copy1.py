def name(user,*argv):
     
        if user=="admin":
           for arg in argv:
            print(arg,":",arg)
            
        else:
                
                
                print ("Access denied",user)