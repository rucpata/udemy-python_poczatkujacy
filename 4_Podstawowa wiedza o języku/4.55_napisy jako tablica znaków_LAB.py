#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:44:32 2019

@author: wlasciciel
"""

q="THE EYES"
print(q)
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

q="a gentleman"
print(q)
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])

q="THE MORSE CODE"
print(q)
print(q[1:3]+q[6]+q[2]+q[3]+q[10:12]+q[4]+q[2]+q[3]+q[12]+q[11]+q[0]+q[7])

line='Program "Kropka nad i" nadamy o: 22:00'
time=line[line.find(':')+2:]

print(time)

tmp=line[line.find("")+1:]
title=tmp[:tmp.find("")]
print(title,time)
