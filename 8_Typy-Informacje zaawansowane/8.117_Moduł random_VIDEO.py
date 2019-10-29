import random

# randim.randint(..) wylosuje liczbę całkowitą
print('One random number',random.randint(1,100)) #1<=N<=100
print('\n')

# od random.choice(...) 1 do 99 
print('Choosing rundom number from a range', random.choice(range(1,100)))
print('\n')

# random.randrange(..., ...) robi to samo co wyżej
print('Choosing rundom number from a range - easier', random.randrange(1,100))
print('\n')

# losowanie z pewnej listy. random.shuffle(...) powoduje to wymieszanie listy
list=['John','Ann','Peter','Susan','Emilu','Greg','Chris']
random.shuffle(list)
print('Reordered list:', list)
print('\n')

# random.random() poprostu rosuje float od 0 do 1
print('Just a random float', random.random())
print('\n')

