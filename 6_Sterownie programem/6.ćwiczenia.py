'''70-Instrukcja warunkowa IF'''

#1
NUM_LIKES=501
NUM_SHARES=99

if NUM_LIKES>=500 and NUM_SHARES>=100:
    print('GREAT! Today our prizes drop 10%!!!')
else:
    print('We still need more likes and shares to start the promotion')


print('-------------------------')

#2
    
isPizzaOrder=True
isBigDrinkOrdered=True
isWeekend=False


if not isWeekend and (isPizzaOrder or isBigDrinkOrdered):
    print('Burger for FREE!!!')
else:
    print('Come to us on week day and consider buying Pizza or BigDrink to have Burger for free')
                      
print('-------------------------')

#3
diskSize=140
diskSizeUsed=133
fileSize=2

if diskSize-diskSizeUsed >= fileSize:
    print('File can be downloaded')
else:
    print('There isn\'t enough free disk space to download the file. Sorry:(')

print('-------------------------')

'''72 - Instrukcja if/elif'''
#1
num_likes=400
num_shares=140

if num_likes<500:
    print('We still need more likes to start the promotion')
elif num_shares<100:
    print('We still need more shares to start the promotion')
else:
    print('GREAT! Today our prizes drop 10%!!!')
print('-------------------------')
#2

isPizzaOrder=True
isBigDrinkOrdered=False
isWeekend=True

if not isWeekend and (isPizzaOrder or isBigDrinkOrder):
    print('Burger for FREE!!!')
elif isWeekend:
    print('Promocja obowiązuje jednie w dni poza weekendem')
else:
    print('Musisz zamówić pizzę lub duży napój')

print('-------------------------')
'''75 - IF'''
#1
musclePain=True
fever=True
weakness=False

if musclePain and fever and weakness:
    print('Suspicion of influenza')
else:
    print('The flu is unlikely')
    
print('-------------------------')
#3
if musclePain and fever and weakness:
    print('Suspicion of influenza')
elif weakness and not(fever or musclePain):
    print('Just take a rest!')
else:
    print('You may be cold')
    
print('-------------------------')  
#4
isMan=True

if (musclePain and fever and weakness) or isMan and (musclePain or fever or weakness):
    print('supicion of influenza')
elif not (muscelPain and fever) and weakness:
    print('Just take a rest!')
else:
    print('This only cold')

print('-------------------------')

isCheckCompleted=False

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET!')
    
    
