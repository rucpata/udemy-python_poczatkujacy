#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:11:54 2019

@author: wlasciciel
"""
#1
MIN_LIKES=500
MIN_SHARES=100

num_likes=1300
num_shares=55

if num_likes >= MIN_LIKES and num_shares>= MIN_SHARES:
    print("Ceny produktów spadną o 10%")
else:
    print("Warunki promocji nie zostały spełnione")
    
#2
isPizzaOrder=True
isBigDrinkOrder=False
isWeekend=False

if(isPizzaOrder or isBigDrinkOrder) and not isWeekend:
    print("Gratulacje! Otrzymujesz kupon na darmowy burger")
else:
    print("Niestety warunki promocji nie zistały spełnione")
    
#3
diskSize=150
diskSizeUsed=133
fileSize=10

if diskSize - diskSizeUsed >= fileSize:
    print('The file can be dowloaded')
else:
    print('There isn\'t enough free disc space to download the file')