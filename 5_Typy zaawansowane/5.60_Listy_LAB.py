#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:15:43 2019

@author: wlasciciel
"""
#1
hitsTitles=['BROTHERS IN ARMS','BOHEMIANRHAPSODY','STAIRWAY TO HEAVEN',
            'RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hitsTitles)

#2
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)

#3
hitsTitles.insert(1,'HOTEL CALIFORNIA')
print(hitsTitles)

#4
hitsTitles.insert(0,'THE SOUND OF SILENCE')

#5
print(hitsTitles.index('HOTEL CALIFORNIA'))

#6
hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)

#7
hitsTitles[0]='ENJOY THE SILECE'
print(hitsTitles)

#8
hitsToRead=hitsTitles.copy()
print(hitsToRead)
#9
hitsToRead.reverse()
print(hitsToRead)

#10
hitsToRead.sort()
print(hitsToRead)

#11
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)

#12
additionalSongs=['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
print(additionalSongs)

#13
hitsToRead.extend(additionalSongs)
print(hitsToRead)

#14
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

#15
hitsToRead.clear()
print(hitsToRead)