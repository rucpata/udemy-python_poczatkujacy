from datetime import date
from datetime import timedelta
    
def GiveWorkingDay(year=date.today().year,\
                   month=date.today().month,\
                   day=date.today().day): #w nawiasie jest określone jakie parametry ma przekazać funkcja
#prints the nearest working day date
    
    

    #day=date.today()
    day=date(year,month,day)

    if day.weekday()==5:
        workingday=day+timedelta(days=2)
    elif day.weekday()==6:
        workingday=day+timedelta(days=1)
    else:
        workingday=day
    print('working day for',day,'is',workingday)

    return

GiveWorkingDay(2017,9)
GiveWorkingDay(2017,9,2)
GiveWorkingDay(2017,2)
