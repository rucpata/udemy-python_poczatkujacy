#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:05:33 2019

@author: wlasciciel
"""
#1
MIN_LIKES=500
MIN_SHARES=100

num_likes=150
num_shares=900

if num_likes < MIN_LIKES:
    print('Jest za mało lików')
else:
    if num_shares < MIN_SHARES:
        print('Jest za mało udostępnień')
    else:
        print('Warunki promocji zostały spełnione')

print('-----------------')     

if num_likes<MIN_LIKES:
    print('Jest za mało lików')
elif num_shares<MIN_SHARES:
    print('Jest za mało udostępnień')
else:
    print('Warunki promocji zostały spełnione')

#2
print('-----------------') 

isPizzaOrder=True
isBigDrinkOrder=False
isWeekend=False   

if(isPizzaOrder or isBigDrinkOrder) and not isWeekend:
    print('Burger for FREE!!!')
else:
    if isWeekend:
        print('Come back on non-)