import datetime
import calendar
noow=datetime.datetime.now()
date1= noow.strftime("%a %b %d %H:%M:%S IST %Y")
print("Date:",date1)
date1= noow.strftime("%H:%M:%S")
print("Date:",date1)
date1= noow.strftime("%b %d %Y")
print("Date:",date1) 
