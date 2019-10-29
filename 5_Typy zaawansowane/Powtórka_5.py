'''59 - LISTA - zbiór elementów zapisany pod jedną nazwą zmiennej'''

countries=['FR','US','DE','RU']

countries[1]='GB' #zamiana elementu na 2 pozycji


print(countries[1])

countries.append('PL') #dodanie elementu na końcu listy
countries.insert(2,'ES') #dodaanie elementu na konkretną pozycję 
countries.remove('RU') #USUNIĘCIE z listy elementu
countries.sort() #sortowanie listy 
countries.reverse() #odwrócenie listy
print(countries.pop(2)) #wraca wartość znajdującą się na danej pozycji i usunie ją z listy
print(countries.index('PL')) #czy dany element występuje na liście i na jakiej pozycji
#jeśli chcę sprawdzić poołożenie elementu którego nie ma na liście pojawi się BŁĄD
print(countries.count('DE')) #ile razy pojawił się na liście ten element


newList=['FI','SE']
countries.extend(newList) #dodanie kraje z newList do aktualnej listy

countriesCopy=countries.copy() #skopiowanie listy
countriesCopy.clear() #czyści listę


print(countries)
print(countriesCopy)







print('-----------------------------')
'''62 - TUPLE(KROTKA) - listy statyczne'''

Tax=(4,7,8,23)
print(Tax[2]) #wyświetlenie pozycji 2
print(Tax[-1]) #odniesienie się do ostatniej pozycji
print(Tax.index(7)) #na której pozycji znajduje się WARTOŚĆ 7
print(Tax.count(8)) #ile razy wskazany argument występuje w tej statycznej liście
print(max(Tax)) #jaka jest maksymalna wartość występująca w Tax

# NIE MOŻNA modyfikować zawartości tuple !!!! WYSKAKUJE BŁĄD!!! Można ją jedynie odczytywać.

TaxList=list(Tax) #konwertacja taple na listę
TaxList.append(30) #dodanie wartości na końcu listy
NewTax=tuple(TaxList) #konwertacja listy na taple



print(Tax)
print(TaxList)
print(NewTax) 


(tax1,tax2,tax3,tax4)=Tax #zainiciowano 4 zmienne 
print(tax1,tax2,tax3,tax4) 


a=1
b=10
print('a=',a,'\tb=',b)

'''temp=a #tymczasowa zmienna

a=b
b=temp'''

(a,b)=(b,a) #zamiana wartości a na b, b na a
print('a=',a,'\tb=',b)

print('-----------------------------')

'''65 - DICTIONARY - słowniki'''

CountryLeaders={'PL':'Duda','US':'Trump'} #każdy z elementów składa się z 2 części KRAJ i AKTUALNY LIDER KRAJU

#print(CountryLeaders['US'])

CountryLeaders['DE']='Merkel' #dodawanie do listy kolejne pozycje

#print(CountryLeaders.keys())  #klucze PL US DE
#print(CountryLeaders.values()) #wartości Duda Trump Merkel
#print(CountryLeaders.items()) #kolekcja elementów związanych z kluczem jak i z elementami na daną chwilę

#print(CountryLeaders.popitem()) # DESTRUKTYWNA ITERACJA PO SŁOWNIKU jeśli trzeba przetworzyć wszystkie elementy ze słownika

#print(CountryLeaders.setdefault('FR','Marcon'))
'''chcemy wyświetlić informacje o liderze w FR,
zakładamy że ten loder nie jest zdefiniowany wiec od razu sami wpisujemy
TA WARTOŚĆ ZOSTANIE NA STAŁE DODANA DO LISTY'''

#print(CountryLeaders.get('RU'))
''' sprawdzamy kto jest liderem w RU, podanego klucza nie ma na liście'''

NewLeaders={'RU':'Putin','DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)
''' jeśli znajdzie taki sam klucz to go podmieni, jeśli nie znajdzie danego klucza
to doda ją do listy'''

print(CountryLeaders)




print(CountryLeaders)
