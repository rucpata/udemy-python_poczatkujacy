#1
import random
print('\n')
#2
for i in range(10):
    print(random.randint(1,100))
print('\n')
#3
number1=random.randint(1,100)
print('This first generated number is %d' %(number1))

counter=1
number2=random.randint(1,100)

while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)

print('I need %d attempts to generate %d again' %(counter, number1))
print('\n')
#4
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)

groupNumber=0

for i in range(len(countries)):
    if i % 4 ==0:
        groupNumber +=1
        print(' Gruop %d'%(groupNumber))
    print(countries[i])

