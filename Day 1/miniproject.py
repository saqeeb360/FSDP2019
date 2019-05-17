# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:27:18 2019

@author: Saqeeb
"""

from random import randint
x=(randint(0,9))
y=input("Enter a number = ")
print("random number is " + str(x))
if (x==y):
    print("Winner")
else:
    print("Loser")
    