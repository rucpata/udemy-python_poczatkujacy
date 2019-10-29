#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:07:03 2019

@author: wlasciciel
"""

CountryLeaders={'PL':'Duda','US':'Trump'}

print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Merkel' #powiększenie słownika

'''
metody dostepnę dla DICTIONARY
dict.items()
dict.keys()
dict.values()
'''

# print(CountryLeaders.keys()) - wyświetla klucze
# print(CountryLeaders.values()) - wyświetla wartość przypisaną do klucza
# print(CountryLeaders.items()) - wyświetla kolekcja elementów kluczai wartości
#print(CountryLeaders.popitem()) #wyświetla ze słownika i automatycznie usuwa
#print(CountryLeaders.setdefault('FR','Macron')) dodanie nowego kraju 
#print(CountryLeaders.get('RU'))

NewLeaders={'RU':'Putin','DE':'Schulz'}
print(NewLeaders)  

CountryLeaders.update(NewLeaders) #aktualizacja starego dictionary

print(CountryLeaders)