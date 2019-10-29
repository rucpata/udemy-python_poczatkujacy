data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dat in data:
    print(dat.upper())

print('-----------------')

for dat in data:
    elements = dat.split(':')
    print(elements[0].upper())
    print(elements[1].upper())

print('------------------')

for dat in data:
    elements=dat.split(':')
    if elements[0]=='Error':
        print(elements[1].upper())
    else:
        print(elements[1])    
    
