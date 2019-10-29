''' 77 - Pętla while (while/else)'''

i=1
imax=10

while i<=imax:
    print('I like Python')
    i+=1 
else:
    print('Now i=',i)


i=10
imin=0

while i>=imin:
    print('I like Python')
    i-=1 
else:
    print('Now i=',i)

    
print('-----------------------------------------------------')


''' 80 - If w while - przykład: wyszukiwanie wzorca w ciągu liczb'''

values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i=0
max=len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])

    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print('\tFound:',values[i],values[i+1],values[i+2])
    i+=1



print('-----------------------------------------------------')

'''83 - While - przykład: pakowanie paczek do kontenera'''

cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print('This cargo list is:',cargo)
boxCapacity=90

box=[]

i=0
'''
while sum(box)+cargo[i]<boxCapacity and i<len(cargo):
    box.append(cargo[i])
    i+=1'''

while i<len(cargo) and (boxCapacity-sum(box)>=min(cargo)):
    if (boxCapacity-sum(box)>=cargo[i]):
        box.append(cargo[i])
    i+=1

print('The collected items sum is:',sum(box))
print('The elemnets are:',box)



print('-----------------------------------------------------')

'''89 - Pętla for'''

persons=['Elizabeth','Sreven','Sebastian','Margaret','Svetlana','Raphael']

domain='mycompany.com'

for person in persons:
    email=person+'@'+domain
    print('Email for \t', person,'\tis\t',email)
else:
    print('-- end of the list--')
    

print('-----------------------------------------------------')

''' 92 - Pętla for wykonywana określoną ilość razy - range '''

for number in range(1,21):
    if number %2==0:
        print('Number %2d is %s' % (number,'even'))
    else:
        print('Number %2d is %s' %(number,'odd'))
        
    #print(number)

print('-----------------------------------------------------')

''' 95- Zagnieżdżona pętla for'''

for x in range(1,6):
    line=str(x)
    for y in range(1,6):
        line+='\t%3d' %(x*y)
    print(line)
        
