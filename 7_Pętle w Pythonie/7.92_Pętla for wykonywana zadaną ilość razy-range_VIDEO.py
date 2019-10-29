for number in range(20): #wyświetla cyfry od 0 do 19
    print(number)

print('--------')

for number in range(1,21): #wyświetla od 1 do 20
    print(number)
 
print('--------')             

for number in range(1,21,2): #wyświetla co 2 cyfrę od 1
    print(number)

print('--------')             

for number in range(1,21): #sprawdzamy czy liczba jest parzysta czy nieparzysta
    if number %2 == 0: #cyfra dzielona przez dwa, reszta z dzielenia wynosi zero
        print('Number %2d is %s' % (number,'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))
