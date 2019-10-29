#1
initilalCapital=2000
percent=0.03
maxTimeYears=10
year=0
capital=initilalCapital

while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year, 'you wille have:', capital)

else:
    print('the total revenue is', capital-initilalCapital)
    
print('-------------')
#2

number=20730906
cyfra=number

sumOfDigits=0

while cyfra>0:
    digit=cyfra % 10
    sumOfDigits += digit
    cyfra=cyfra//10
else:
    print('the sum of digits of', number, 'is', sumOfDigits)

#3
text='United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.'

wordLenght=6
listOfWords=text.replace('\n',' ').split(' ')
i=0
shortWords=0
longWords=0

while i<len(listOfWords):
    if len(listOfWords[i])>wordLenght:
           longWords+=1
    elif len(listOfWords[i])>0:
        shortWords+=1
    i+=1

print('Words shorter than', wordLenght, ':', shortWords)
print('Words longer than', wordLenght, ':', longWords)


