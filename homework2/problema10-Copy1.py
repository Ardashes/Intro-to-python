import datetime
import calendar
import time
l = time.asctime()
y = datetime.date.today().year
m = datetime.date.today().month
t = datetime.date.today().day
print ("Local time ", l)
print ("current year ", y )
print ("current month " , m )
print ("today is " , t )
tday = datetime.datetime.today()
tdelta = datetime.timedelta(days=5)
print (tday - tdelta)
print (tday + tdelta)