#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:58:44 2019

@author: wlasciciel
"""

'''
Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50. 
Całość pomnóż przez 20, a następnie dodaj 1017. 
Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba. 
Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.
'''

shoesize=40
number=(shoesize*5+50)*20+1019-1991
print(number)

'''
Pomyśl liczbę nieujemną całkowitą. 
Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę. 
Powinno wyjść 5 - zawsze.
'''

x=99
number=(x*2+10)/2-x
print(number)
print(2+2*2)
print(7+7/7+7*7-7)

'''
Wykładowca mówi studentom. Zaliczysz semestr jeżeli 
masz obecność co najmniej 80% i średnią >= 3.0 
lub zaliczyłeś pracę semestralną. Zbuduj wyrażenie w 
Python które stwierdzi czy student, 
który ma obecność 0.85, średnią 3.5 
i nie zaliczył pracy semestralnej zda czy nie.
'''
presence=0.4
note=2.5
finalWorkOk=True
print('You need to be present and have good notes or do the final woek', presence >=0.8 and note >=3 or finalWorkOk)
'''
Wykładowca zmienił zdanie. Aby zaliczyć semest trzeba: 
mieć obecność co najmniej 80%, średnią >=3.0 i zaliczoną pracę. 
Czy teraz student zda?
'''
print(presence >=0.8 and note >=3 and finalWorkOk)