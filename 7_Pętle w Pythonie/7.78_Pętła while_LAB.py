#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:05:35 2019

@author: wlasciciel
"""
#1
firstRow=1
lastRow=31
currentRow=firstRow

while currentRow <= lastRow:
    print('Row number',currentRow)
    currentRow+=1
    
#2
print('######')

start=1
end=13
while start<= end:
    print(start**2,start**3)
    start+=1
    
print('######')

#3
start=0
end=16
x=start
while x <= end:
    print(x,2**x)
    x+=1
    
print('#####')

start=1
end=10
number=start
while number <= end:
    print(number *'x')
    number+=1