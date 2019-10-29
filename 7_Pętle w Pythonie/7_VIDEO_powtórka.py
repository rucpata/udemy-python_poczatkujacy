'''
i=10
imax=0

while i >= imax:
    print(i, "I like Python")
    i-=2
else:
    print('Now i=',i)
'''
'''
firstRow=1
lastRow=31
currentRow=firstRow
while currentRow <= lastRow:
    print('Row number', currentRow)

    currentRow+=1
'''
'''
n=1
nMax=13

z=n

while z <= nMax:
    print('Kwadrat z cyfry',z,'=',z*z,'Sześcian z cyfry',z,'=',z*z*z)
    z+=1
'''
'''
start=0
end=16
x=start

while x<=end:
    print(x,2**x)
    x+=1
'''
'''
start = 1
end = 10

i=start
while i <=10:
    print('x'*i)
    i+=1
'''
#2
'''
values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0
max = len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])

    if(values[i]<values[i+1] and values[i+1]<values[i+2]):
       print('\tFound:',values[i],values[i+1],values[i+2])
    i+=1
'''
'''

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
max=len(numbers)-1

while i<max:
    print(i,numbers[i],numbers[i+1])

    if numbers[i]**2==numbers[i+1]:
        print('\tFonud')
        
    i+=1
'''
'''
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
max=len(texts)-1

while i<max:
    print(i,texts[i],texts[i+1])

    if len(texts[i])==len(texts[i+1]):
           print('\tFound')
    i+=1
'''
'''
cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]

boxCapacity=90
box=[]
i=0

cargo.sort()
cargo.reverse()

print('The cargo list is:', cargo)
#while sum(box) + cargo[i] <boxCapacity and i<len(cargo):

while i<len(cargo) and (boxCapacity - sum(box) >= min(cargo)) :
    if(boxCapacity-sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print('This collected items sum is:',sum(box))
print('The elements are:',box)
'''

'''
number=1
previousNumber=0

while number <50:
    print(number+previousNumber)
    previousNumber=number
    number+=1

print('###########################')

import random
my_number=random.randint(0,20)
guess=-1
trials=0

print('Guess my number!')
while guess != my_number:  
    guess=int(input())
    trials+=1  
    if guess == my_number:
        print('Bingo!',my_number, 'Udao Ci się po', trials,'próbach')
    elif guess>my_number:
        print('Sorry-my number is smaller than your guess',guess, 'Try again!')
    else: 
        print('Sorry-my number is greater then your guess, Try again!')
'''

'''
persons=['Elizabeth','Srevan','Sebastian','Margaret','Svetlana','Raphel']

domain = 'mycompany.com'

for person in persons:
    email=person +'@' + domain

    print('Email for \t', person, '\tis\t', email)

else:
    print('-- end of the list --')
    
print('---------------------')

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dat in data:
    print(dat.upper())

for dat in data:
    element=dat.split(':')
    if element [0] == 'Error':
        print(element[1].upper())

    else:
        print(element[1])
'''

'''
for number in range(1,21):
    if number %2==0:
        print('Number%2d is %s' %(number,'even'))
    else:
        print('Number %2d is %s' %(number,'odd'))
    #print(number)
'''

'''
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

print('         ')

for i in range(1,10):
    if i %2 == 0:
        print(string_B)
    else:
       print(string_A)

print('         ')

for i in range (10):
    print('x'*i)

print('          ')

for i in range(10):
    if i %2==0:
        print('x'*i)
    else:
        print('o'*i)
'''

'''
for x in range(1,6):
    line=str(x)
    for y in range(1,6):
        line+=('\t%3d' %(x*y))
    print(line)
'''

#96
'''
i=10
result=1
for j in range(1,i+1):
    result*=j
print(i,result)


x=10

for i in range(1,x+1):
    result=1
    for j in range(1,i+1):
        result*=j
    print(i,result)


list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj,noun)
'''

#98
'''
for candidate in range(2,31):

    #isPrime=True

    for divider in range(2, candidate):

        if candidate % divider == 0:
            isPrime=False
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break
    else:
   # if isPrime:
        print('%2d is prime!' % (candidate))
'''

#99
'''t
ext = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'

words=text.split(' ')

short_text=' '
counter=0

for word in words:
    short_text += word+' '

    counter+=1

    if counter >= 20:
        print(short_text)
        break

print('------------')

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'  
    ]

for definition in definitions:
    words=definition.split(' ')
    short_text=''
    counter=0

    for word in words:

        short_text += word+' '
        counter+=1

        if counter>=20:
            print(short_text)
            break 
'''
#101
'''
persons=['Elizabeth','Srevan@sales.mycompany.com','Sebastian','Margaret','Svetlana@mycompany.eu','Raphel']
    
domain='mycompany.com'

emails=[]

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email=person+'@'+domain
    emails.append(email)

    for email in emails:
    print(email)
'''
'''
for person in persons:

    if '@' in person:
        emails.append(person)
    else:
        email=person+'@'+domain
        emails.append(email)
'''        

    
#102

menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""

'''

while True:

    print(menu)
    letter=input('Enter your choice')

    if letter == '1':
        print('Function COFFEE not implemented')
        input('Press enter')
        continue

    if letter =='2':
        print('Function TEA not implemented')
        input('Press enter')
        continue

    if letter=='3':
        print(smile)
        input('Press enter')
        continue

    if letter =='0':
        break

    input('You need to make a valid choice. Press ENTER and try again!')

