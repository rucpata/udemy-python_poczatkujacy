#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:24:32 2019

@author: wlasciciel
"""

#1
chanels={'Google':'1480','Email':'300','Natural Traffic':'440','TV Spot':'700'}
print(chanels)

#2
print(chanels['Email'])

#3
chanelsUpdate={'Natural Traffic':'520','News':'600'}
print(chanelsUpdate)

#4
chanels.update(chanelsUpdate)
print(chanels)

print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)
