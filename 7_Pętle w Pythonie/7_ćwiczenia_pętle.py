'''78 - Pętla while'''
#1
firstRow=1
lastRow=31
currentRow=firstRow

while currentRow<=lastRow:
    print('Row number',currentRow)

    currentRow+=1
print('******************************')
#2
start=1
stop=13
number=start

while number<=stop:
    print(number,number**2,number**3)
    number+=1
print('******************************')
#3
start=0
stop=16
number=start

while number<=stop:
    print('2 do potęgi',number,'wynosi',2**number)
    number+=1
print('******************************')
#4

start=1
stop=10
num=start

while num<=stop:
    print('x'*num)
    num+=1

print('--------------------------------------------------')

'''81 - If w while - przykład wyszukiwania wzorca'''
#1
numbers=[8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i=0

max=len(numbers)-1

while i<max:
    print(i,numbers[i],numbers[i+1])

    if numbers[i]**2==numbers[i+1]:
        print('\tFOUND:',numbers[i],numbers[i+1])
    i+=1

print('******************************')
#2
numbers=[8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i=0

max=len(numbers)-2

while i<max:
    print(i,numbers[i],numbers[i+1],numbers[i+2])

    if numbers[i]**2==numbers[i+1] and numbers[i+1]**2==numbers[i+2]:
        print('\tFOUND:',numbers[i],numbers[i+1],numbers[i+2])
    i+=1

print('******************************')

#3
texts=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
max=len(texts)-1

while i<max:
    print(i,texts[i],texts[i+1])

    if len(texts[i])==len(texts[i+1]):
        print('\tFOUND!')

    i+=1

print('--------------------------------------------------')
'''84 - Pętła while - przykłady'''
#1

number=1
previousNumber=0

while number<50:
    print(number,'+',previousNumber,'=',number+previousNumber)
    previousNumber=number
    number+=1

print('******************************')

#2
import random
my_number = random.randint(0,20)
trials=0
guess=-1
print('Guess my number')

while guess!=my_number:
    guess=int(input())
    trials+=1
    if guess==my_number:
        print('You are right! It was:',my_number,'You needed',trials,'trials.')
    elif guess>my_number:
        print('Sorry-my number is smaller than your guess.',guess, 'Try again!')
    else:
        print('Sorry-my number is greater than your guess.',guess, 'Try again!') 
print('--------------------------------------------------')
'''90-FOR'''
#1
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dat in data:
    print(dat.upper())


print('******************************')
#2


for dat in data:
    elements=dat.split(':')
    print(elements[0].upper())
    print(elements[1])
    
print('******************************')
#3
for dat in data:
    elements=dat.split(':')
    if elements[0]=='Error':
        print(elements[1].upper())
    else:
        print(elements[1])
print('--------------------------------------------------')
''' 93 - Pętla wykonywana określoną ilość razy'''

#1
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for n in range(1,11):
    print(string_A)
print('******************************')
for n in range(1,10):
    if n %2!=0:
        print(string_A)
    else:
        print(string_B)
print('******************************')
for n in range(1,10):
    print('x'*n)
print('******************************')
for n in range(1,10):
    if n %2 !=0:
        print('o'*n)
    else:
        print('x'*n)
print('--------------------------------------------------')
'''96-Zagnieżdżona pętla for'''
#1
i=10
result=1

for j in range(1,i+1):
    result*=j
print(i,result)

print('******************************')
#2

x=10

for i in range(1,x+1):
    result=1
    for j in range(1,i+1):
        result*=j
    print(i,result)

print('******************************')

#3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for n in list_noun:
    for a in list_adj:
        print(a,n)
