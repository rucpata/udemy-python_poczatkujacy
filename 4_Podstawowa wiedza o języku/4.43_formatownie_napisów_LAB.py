#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:37:43 2019

@author: wlasciciel
"""

helloMessage="Hello %s"
print(helloMessage %('Kate'))
print(helloMessage %('Chris'))

helloMessage="Hello {0:s}"
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

helloMessage="%s has %d %s"
print(helloMessage %('Kate', 1, 'animal'))
print(helloMessage %('Chris', 100000, '$')) 

helloMessage="{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format('Chris',1,'$'))

line="{0:20s} costs {1:6d} €"
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAI', 6))