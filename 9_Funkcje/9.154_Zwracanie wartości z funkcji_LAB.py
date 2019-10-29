#1
def PrintAnimal(animal=''):
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

    if animal=='cat':
        print(txt_cat)
    elif animal=='bear':
        print(txt_bear)
    elif animal=='bat':
        print(txt_bat)
    else:
        print("Connot print '%s'. Correct values for the parameter are: cat, bear, bat" %animal)
        return False
    return True

PrintAnimal('cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal('unicorn')

print('---------------------------')

#2
from datetime import date

def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
    from datetime import date
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    return delta.days

print('Date: 2020-12-20 days to end of year: %d' %(DaysToEndOfYear(2020,12,20)))
print('*******')
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(1991,9,4)
DaysToEndOfYear()
