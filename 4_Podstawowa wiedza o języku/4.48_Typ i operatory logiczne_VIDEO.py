#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:50:38 2019

@author: wlasciciel
"""

IsWeekend=True
print("Is weekend =",IsWeekend)
Temperature =25
print("Temperature =",Temperature)

ToDoList=''
print("ToDoList=",ToDoList)

IsHappy=IsWeekend and Temperature >=20 and ToDoList ==''
print("IsHappy=",IsHappy)

IsHappy=not IsWeekend and Temperature < 20 and ToDoList !=''
print("IsHappy=",IsHappy)

IsHappy=IsWeekend and Temperature >=20 and ToDoList =='' \
or not IsWeekend and Temperature < 20 and ToDoList !=''
print("IsHappy=",IsHappy)