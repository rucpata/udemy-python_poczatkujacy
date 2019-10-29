f_smaller=3.141592653589793
f_bigger=3.87756392764

import math

#math.ceil() zwraca dla wskazanaego argumentu najmniejszą liczbę całkowitą
#która jest większa od wskazanego argumentu

print(math.ceil(f_smaller),math.ceil(f_bigger))
print('\n')

#math.floor() zwraca najwięszką liczbę która jest mniejsza od podanego arkumentu
print(math.floor(f_smaller),math.floor(f_bigger))
print('\n')


print(math.ceil(-f_smaller),math.ceil(-f_bigger))
print('\n')

print(math.floor(-f_smaller),math.floor(-f_bigger))
print('\n')

#math.pow( , ) liczba którą chcemy podnieść do potęgi, do jakiej potęgi
print(pow(2,8),pow(9,0.5))
print('\n')

# math.sqrt() do pierwiastka kwadratowego
print(math.sqrt(16))
print('\n')

#math.pi math.e
print(math.pi, math.e)
print('\n')

#
print(math.sin(math.pi/2),math.cos(math.pi/4))
print('\n')

