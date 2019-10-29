#1
def PrintAnimal(*animals):
    # this function prints a cat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    for animal in animals:
        if animal=='cat':
            print(txt_cat)
        elif animal=='bear':
            print(txt_bear)
        elif animal=='bat':
            print(txt_bat)
        else:
            print("Connot print '%s'. Correct values for the parameter are: cat, bear, bat" %animal)
    return 

PrintAnimal('cat')
print('\n--------------------')
PrintAnimal('bear', 'cat')
print('\n--------------------')
PrintAnimal('bat', 'bear', 'cat')
PrintAnimal('unicorn')

print('---------------------------')

#2
from datetime import date

def DaysToEndOfYear(*dates):
    for date_today in dates:
        
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
        

DaysToEndOfYear(date(2020,12,20))
DaysToEndOfYear(date(1991,9,4),date(2009,1,15))
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date(2099,4,15))
