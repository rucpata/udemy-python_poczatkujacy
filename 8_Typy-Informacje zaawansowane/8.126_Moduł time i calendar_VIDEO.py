# playing with time

import time

print('Current time is... unix epoch', time.time()) #czas unixowy
print('\n') 

print('Current time is...tuple', time.localtime(time.time()))
print('\n')

print('Current time is... for human', time.asctime(time.localtime(time.time())))
print('\n') #najlepsze, nie mamy wpływu na sposób wyświetlania

print('Current time is...for human', time.localtime(time.clock()))
print('\n')

import calendar

print('---------------------------------------------')
print(calendar.month(2017,9,w=5,l=2)) #wrzesień 2017, w=na każdy dzień jest 5 znaków l=odstep miedzy liniami 2
print('---------------------------------------------')
print(calendar.month(2017,9))
print('---------------------------------------------')
print('week day is', calendar.weekday(2017,9,29))
print('---------------------------------------------')
calendar.setfirstweekday(6) #wpływa tylko na to jak kalendarz jest rysowany
print('---------------------------------------------')
print(calendar.month(2017,9))
print('---------------------------------------------')
print('week day is', calendar.weekday(2017,9,29))
print('---------------------------------------------')
print('is 2020 a leap years?', calendar.isleap(2020)) #czy rok 2020 jest przestępny
print('---------------------------------------------')
#ile było dni przestępnych w tych latach
print('Leap days 2000-2017',calendar.leapdays(2000,2017))
print('Leap days 2000-2020',calendar.leapdays(2000,2020))
print('Leap days 2000-2021',calendar.leapdays(2000,2021))

print(calendar.calendar(2018)) #rysuje kalendarz za cały rok
