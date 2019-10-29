
line='This is a very STRANGE text'
line.capitalize() #tekst zostanie skonwertowany do zdania zaczynającego się dużą literą
print(line.capitalize())

line.title() #każde słowo zaczyna się wielką literą
print(line.title())

line.upper() #skonwertowanie tekstu do dużych liter
print(line.upper())

line.lower() #skonwertowanei tekstu do małych liter
print(line.lower())

line.swapcase() #każda duża na małą, a każda mała na dużą
print(line.swapcase())

line.casefold() #konwertuje znaki narodowe 
print(line.casefold())


print(line.count('e')) #liczy ile razy w tekście występuje lietera e


print(line.find('e')) #na której pozycji występuje ta litera, sprawdza od lewej

print(line.rfind('e')) #na której pozycji występuje litera e, sprawdza od prawej

print(line.index('e')) #występuje błąd jeśli szukamy znaku który nie występuje w tekście

print(line.rindex('e'))

print('e' in line)

print(line.startswith('THIS')) #czy dany tekst rozpoczya się danym ciągiem znaków

print(line.endswith('text')) #czy dany tekst kończy się danym ciągiem znaków

line="""gsgsdgsdgds
gsdgsdgheeeeeeee
5234iosos"""



import string
print(string.ascii_letters) #kod ASCII


print(string.digits) #losowanie z ASCII

print(line.split(' ')) #pozwoli rozbić napis na listę 

#odwrotność do split


gogo='This is a very STRANGE text'
print(gogo.split(' ')) #pozwoli rozbić napis na listę 
print(' '.join(gogo))#odwrotność do split



'''
line='ŻÓŁĆ'
print(line.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C').lower())
'''
