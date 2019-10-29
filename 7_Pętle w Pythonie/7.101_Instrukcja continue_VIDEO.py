persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@mycompany.eu','Repheal']

domain='mycompany.com'

emails=[]

for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email=person+'@'+domain
    emails.append(email)
    
'''
for person in persons:

    if '@' in person:
        emails.append(person)

    else:
        email = person+'@'+domain
        emails.append(email)
'''

for email in emails:
    print(email)
        
