import os
import time

#os.getcwd() - zwraca informacje o bieżącym katalogu
print('Current directory is: ' + os.getcwd())


currentDir = os.getcwd()
filename = 'results.txt'
#os.path.join(..., ...) połączy ze sobą dwie ścieżki
fullpath = os.path.join(currentDir, filename)
print('\nThe constructed file path is: ' + fullpath)

#os.path.abspath(...) - określa położenie pliku (gdzie powstanie plik)
relativePath = 'output.txt'
print('\nThe absolute path is: ' + os.path.abspath(relativePath))

#os.path.basename(...) - zwróci samą nazwę pliku
#os.path.dirname(...) - zwróci ścieżkę dostępu do katalogu w którym znajduje sie dany plik
filepath = r'/Users/wlasciciel/Desktop/python/udemy/10_Operacje wejścia i wyjścia/results.txt'
print('\nThe file name part is: ' + os.path.basename(filepath))
print('\nThe directory part is: ' + os.path.dirname(filepath))

#os.path.exists(...) - sprawdza czy plik lub folder istnieją
print('\nIs file existing? ', os.path.exists(filepath))




if os.path.exists(filepath):
#os.path.getmtime(...) - kiedy została utworzona 
    print('\nLast modify date is: ', os.path.getmtime(filepath))
#time.localtime(os.path.getmtime(...) - data ostatniej modyfiakcji
    print( 'Last modify date is: ', time.localtime(os.path.getmtime(filepath)))
#os.path.getsize(...) - rozmiar pliku
    print('\nFile size is: ', os.path.getsize(filepath))
#os.path.isfile(...) - czy okreslona ścieżka identyfikuje plik czy katalog
    print('\nIs it a file?', os.path.isfile(filepath))
#os.path.isdir(...) - czy okreslona ścieżka identyfikuje plik czy katalog
    print('\Is it a dir? ', os.path.isdir(filepath))
#os.path.split(...) - oderwac ostatni fragment nazwy z sciezki dostepu pliku lub katalogi
    print('\nPath splitted:', os.path.split(filepath))
#os.path.split(...)
    print('\nOnly file name part:', os.path.split(filepath)[1])
#os.path.splitdrive(...) - oderwanie samej nazwy dysku oraz ścieżka dostępu do pliku
    print('\nPath splitted into drive:', os.path.splitdrive(filepath))
#os.path.splitdrive(...) - jesli chcesz samą nazwę dysku to pobierz element [0]
    print('Only drive:', os.path.splitdrive(filepath)[0])
