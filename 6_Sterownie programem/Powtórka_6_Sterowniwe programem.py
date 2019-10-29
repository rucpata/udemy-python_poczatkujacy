''' 68 - Instrukcja warunkowa IF'''

age= 27

if age>=18:
    print('You are adult and you can buy alcohol')

else:
    print('You are too young to buy alcohol')


isDrunk=False


if age>=18 and not isDrunk:
    print('You are adult and you can buy alcohol')

else:
    print('Sorry,we cannot sell tou alcohol')

isRestrictedArea=False

if age >=18 and not isDrunk and not isRestrictedArea:
    print('You are adult and you can buy alcohol')
else:
    ('Sorry, we cannot sell you alcohol')

print('------------------------')

'''71 - IF i ELSEIF'''


age = 27
isDrunk=True
isRestrictedArea=True

if age<18:
    print('You are too younf to buy alcohol')
else:
    if isDrunk:
        print('Are you drunk? We cannot sell you alcohol')
    else:
        if isRestrictedArea:
            print('Restricted area. Alcohol is forbidden')
        else:
            print('OK, you can buy alcohol')

print('------------------')

if age <18:
    print('You are too young to buy alcohol')
elif isDrunk:
    print('Are you drunk? We cannot sell you alcohol')
elif isRestrictedArea:
    print('Restricted area. Alcohol is forbidden')
else:
    print('Ok, you can buy alcohol')








        


