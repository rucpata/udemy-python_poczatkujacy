#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:43:37 2019

@author: wlasciciel
"""

number=1
previousNumber=0

while number<50:
    print(number+previousNumber)
    previousNumber=number
    number+=1
    
print('--------------------')

import random
my_number=random.randint(0,20)
trials=0

guess=-1
print('Guess my number!')

while guess != my_number:
    guess=int(input())
    
    if guess == my_number:
        print('You are right! It was:', my_number, 'You need',trials,'trials.')
    elif guess>my_number:
        print('Sorry - my number is smaller than',guess, 'Try again!')
    else:
        print('Sorry-my number is greater than', guess, 'Try again!')
    trials+=1 
print('--------------------')
