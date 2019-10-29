#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:26:04 2019

@author: wlasciciel
"""

s="A Python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message='Document "cv.doc" was printed on printed: XEROX'
print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])

tmp = message[message.find('"')+1:]

print(tmp[:tmp.find('"')])

