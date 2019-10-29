''' 98-Instrukcja break'''

for candidate in range(2,31):


    for divider in range(2,candidate):


        if candidate %divider ==0:

            
            print('%2d is not a prime number=divider is%2d' % (candidate, divider))
            break
        
    else:
        print('%2d is prime!' %(candidate))

print('-----------------------------------')
''' 101 - Instrukcja continue'''

persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@company.eu','Rephael']

domain='mycompany.com'

emails=[]

for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email=person+'@'+domain
        emails.append(email)
for email in emails:
    print(email)

print('***********************************')

persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@company.eu','Rephael']

domain='mycompany.com'

emails=[]

for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email=person+'@'+domain
    emails.append(email)

for email in emails:
    print(email)
