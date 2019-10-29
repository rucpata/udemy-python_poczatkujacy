'''108-Trochę matematyki w Pythonie'''

f_smaller=3.141592653589793
f_bigger=3.8775639264

print(f_smaller,f_bigger)
print('\n')

#liczba całkowita
print(int(f_smaller),int(f_bigger))
print('\n')

#wartość bezwzględna
print(abs(f_smaller),abs(-f_smaller))
print('\n')

#zaokrąglenie wartości
print(round(f_smaller,2),round(f_bigger,2),round(f_bigger,3))
print('\n')

#wartość najmniejsza i wartość największa
print(min(f_smaller,f_bigger),max(f_smaller,f_bigger))
print('\n')



list=[1,2,3,4,5,4,4,5,4]

print(sum(list),len(list))
print('\n')

#obliczenie średniej
print(sum(list)/len(list))
print('\n')

#TYP FLOAT NIE JEST PRECYZYJNY
print(round(2.675,2))

print('-----------------------------------------')

'''111 - Korzystanie z modułów'''

import math #współgra z innymi funkcjami
print(math.pi)
print(math.floor(math.pi))

from math import* #można korzystać z jednej funkcji
print(pi)

print('-----------------------------------------')

'''114-moduł math'''

f_smaller=3.141592653589793
f_bigger=3.8775639264

import math

#math.ceil() - zwraca najmniejszą liczbę całkowitą, która jest większa od wskazanego argumentu
print(math.ceil(f_smaller),math.ceil(f_bigger))
print('\n')

#math.floor - zwraca największą liczbę całkowitąm, która jest mniejsza od wskazanego argumentu
print(math.floor(f_smaller),math.floor(f_bigger))
print('\n')

print(math.ceil(-f_smaller),math.ceil(-f_bigger))
print('\n')

print(math.floor(-f_smaller),math.floor(-f_bigger))
print('\n')

# math.pow(...,...) - (liczba którą chcemy podnieść do potęgi, do jakiej potęgi)
print(pow(2,8),pow(9,0.5))
print('\n')

#math.sqrt() - pierwiastek z ()
print(math.sqrt(16))
print('\n')

#stała PI & E 
print(math.pi,math.e)
print('\n')

#math.sin(...) math.cos(...)
print(math.sin(math.pi/2),math.cos(math.pi/4))
print('\n')
