import time

print(time.time())

print(time.localtime(time.time()))

import calendar

print(calendar.month(1991,9))
calendar.setfirstweekday(6)
print(calendar.month(1991,9))

print(calendar.isleap(2000))

print(calendar.calendar(2019))
