#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:32:16 2019

@author: wlasciciel
"""

countries=['FR','US','DE','RU'] #lista
countries[1]='GB' #zmiana wartości pozycji
print(countries[1]) #wyświetlenie jednej pozycji z listy

countries.append('PL') #dodanie na końcu listy
countries.insert(2,'ES') #dodanie na jedną konkretną pozycję
countries.remove('RU') #usunięcie z listy
countries.sort() #sortowanie listy
countries.reverse() #odwrócenie sortownia

print(countries.pop(2)) #pobiera i usuwa z listy
print(countries.index('PL')) #sprawdza czy jakiś element się znajduje na liście, jeśli tak to na której pozycji
print(countries.count('DE')) #sprawdza ile razy dany element występuje na liście

newList=['FI','SE']
countries.extend(newList) #dodanie nowej listy do starej 

countriesCopy = countries #zamienna nazwa do listy
countriesCopy = countries.copy() #skopiowanie listy 
countriesCopy.clear() #czyszczenie listy



print(countries)

