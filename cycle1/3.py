import datetime
import calendar
noow=datetime.datetime.now()
date1= noow.strftime("%a %b %d %H:%M:%S IST %Y")
print("Date:",date1)
print(calendar.month(noow.year,noow.month))
