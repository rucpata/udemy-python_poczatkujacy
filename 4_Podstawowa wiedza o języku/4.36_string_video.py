#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:46:14 2019

@author: wlasciciel
"""
#\n - new line
#\a  - beep(sound)
#|' - just apostrophe
#\\ - just backslash
#drive = 'c:\' #jest źle
drive = 'c\\'
folder = 'scripts\\python\\'
file ='myscript.py'
path = drive + folder + file
print(path)
path
justText = 'text with\nnewline'
print(justText)
justText = r"text with\nnwline" 
#r - surowy tekst, czyli znaki specjalne nie mają zastosowanie
print(justText)
justText="Mc Donald's"
print(justText)
justText='Mc Donald\'s'
print(justText)
line='He said "I like Python!"'
print(line)