#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:39:57 2019

@author: wlasciciel
"""

age=89
isDrunk=True
isRestictedArea=False

if age <18:
    print('You are too young to buy alcohol')
else:
    if isDrunk:
        print('Are you drunk? We can not sell you alcohol')
    else:
        if isRestictedArea:
            print('Restricted area. Alcohol is forbidden')
        else:
            print('Ok, you can buy alcohol')
        
print('---')

if age <18:
    print('You are too young to buy alcohol')
elif isDrunk:
    print('Are you drunk? We cannot sell you alcohol')
elif isRestictedArea:
    print("Resticted area. Alcohol is forbidden")
else:
    print('Ok, you can buy alcohol')