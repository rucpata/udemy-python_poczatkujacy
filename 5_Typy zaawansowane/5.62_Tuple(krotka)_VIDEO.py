#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:43:26 2019

@author: wlasciciel
"""
Tax=(4,7,8,23)

print(Tax[-1])
print(Tax.index(7)) #na której pozycji jest liczba 7
print(Tax.count(8)) #ile razy występuje liczba 8
print(max(Tax)) #maksymalna wartość

#tax.revert()  !nie można modyfikować tuple!

TaxList=list(Tax) #zmiana tuple na liste
TaxList.append(30)
NewTax=tuple(TaxList) #zmiana LISTY na TUPLE

print(Tax)
print(TaxList)
print(NewTax)

(tax1,tax2,tax3,tax4)=Tax
print(tax1,tax2,tax3,tax4)

a=1
b=10
print("a=", a, "\tb=",b)
#temp = a
#a=b
#b=temp

(a,b)=(b,a)
print("a =",a,"\tb=",b)