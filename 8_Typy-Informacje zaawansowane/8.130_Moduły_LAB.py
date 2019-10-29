inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

print('input data has', len(inputdata),'elements')
print('factor table has', len(factortable),'elements')

if len(inputdata)==len(factortable):
    i=0

    while i<len(inputdata):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)

        mininteger=math.floor(minvalue) #największa liczba całkowita mniejsza od minivalue
        maxinteger=math.ceil(maxvalue) #najmniejsza liczba całkowita większa od maxVALUE
        
        print(mininteger,'\t',inputdata[i],'\t',maxinteger)
        i+=1
else:
    print('inputdate and factortable need to have equal numner of elements')
    

print('---------------------------------')

import random
i=0
while i<len(inputdata):
    minivalue=inputdata[i]-random.random()*inputdata[i]
    maxvalue=inputdata[i]+random.random()*inputdata[i]
    print('minvalue',minivalue,'maxvalue',maxvalue)
    i+=1


print('-----------------------------------')

import datetime
print(datetime.date.today())
print(datetime.date.today().strftime('%Y-%m-%d'))
