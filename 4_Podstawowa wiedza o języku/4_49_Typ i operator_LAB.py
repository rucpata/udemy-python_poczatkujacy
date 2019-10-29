#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:35:15 2019

@author: wlasciciel
"""

isAutomaticMode=True

is80PercentLight=True

isDirectLight=True

isRainy=False

turnLightsOn=isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:",isDirectLight)
print("Is it rainy:",isRainy)
print("TURN LIGHT ON:",turnLightsOn)