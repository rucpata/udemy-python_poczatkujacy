#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:39:36 2019

@author: wlasciciel
"""

numbers=[8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]

i=0
max=len(numbers)-1

while i<max:
    print(numbers[i],numbers[i+1])
    if numbers[i]**2==numbers[i+1]:
        print('\tFound!')
        
    i+=1
print('------------------------')
numbers=[8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]
i=0
max=len(numbers)-2

while i<max:
    print(numbers[i],numbers[i+1],numbers[i+2])
    if numbers[i]**2==numbers[i+1] and numbers[i+1]**2==numbers[i+2]:
        print('\tFound!')
        
    i+=1
    
print('-----------------')

texts=['zero','one','two','three','four','five','six','seven','eight','nine']

i=0
max=len(texts)-1

while i< max:
    print(i,texts[i],texts[i+1])
    if len(texts[i])==len(texts[i+1]):
        print('\tFound!')
    i+=1