#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:23:20 2019

@author: wlasciciel
"""

values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0
max =len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])
    
    if values[i] < values[i+1] and values[i+1]< values[i+2]:
        print('\tFound:: ',values[i],values[i+1],values[i+2])
    
    i+=1