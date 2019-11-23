import datetime
import time
import calendar
bday=datetime.date(1993,2,22)
print (bday)
print (bday.year)
print (bday.month)
print (bday.day)
print (bday.weekday())
tdelta=datetime.date.today()
print (tdelta - bday)
print (calendar.month(2017,5))
ydelta=datetime.timedelta(days = 1)
c=tdelta - ydelta
print ("yesterday:", c)
yydelta=datetime.timedelta(days=2)
print ( c + yydelta)
yyydelta=datetime.timedelta(days=3)
print ( c - yyydelta)