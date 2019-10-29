#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:44:50 2019

@author: wlasciciel
"""
#1

musclePain=False
fever=True
weakness=True

#2

if musclePain and fever and weakness:
    print('suspiction of influenza')
else:
    print('The flu is unlikely')

 #3
   
if musclePain and fever and weakness:
    print('suspiction of influenza')   
elif not(musclePain or fever) and weakness:
    print('Just take a rest!')
else:
    print('You may be cold')
        
isMan=False 
if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('suspiction of influenza')
elif not(musclePain or fever) and weakness:
    print('Just take a rest')
else:
    print('You may be cold')
    
isCheckCompleted=False
print('CHECK IS COMPLETED'if isCheckCompleted else 'CHECK NOT DONE YET!') 
