#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:46:32 2019

@author: wlasciciel
"""
#1
marketing=['loyality program','client promotion','market research']
print(marketing)

#2
marketing.append('public relations')
print(marketing)

#3
print(marketing[2])

#4
marketing.insert(1,'investor relations')
print(marketing)

#5
emailMarketing=marketing.copy()
print(emailMarketing)

#6
emailMarketing.sort()
print(emailMarketing)

#7
internalEmails=['internal communication']
print(internalEmails)

#8
emailMarketing.extend(internalEmails)
print(emailMarketing)

#9
eMarketing=tuple(emailMarketing)
print(eMarketing) 