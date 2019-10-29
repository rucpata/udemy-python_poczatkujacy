#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:00:31 2019

@author: wlasciciel
"""

age = 27

if age >= 18: 
    print("You are adult and you can buy alcohol") 
else:
     print("You are too young to buy alcohol")   

isDrunk=False

if age >=18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")
    
isRestictedArea=False

if age >= 18 and not isDrunk and not isRestictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")