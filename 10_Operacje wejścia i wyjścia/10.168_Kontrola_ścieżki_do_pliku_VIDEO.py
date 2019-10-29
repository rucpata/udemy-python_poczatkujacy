import os

while True:
    filename = input('Enter path to results filed')
    if os.path.isfile(filename):
        break
    else:
        print('File name is not correct, try again!')
                
print('The results file is %s' % (filename))
