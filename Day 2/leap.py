# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:42:21 2019

@author: Windows
Name   :   Leap

"""

def leapyear(a):
    if (a%100==0):
        print("Not leap")
    elif(a%4==0):
        print("Leap")
    else:
        print("Not Leap")
a=input("Enter a year")
a=int(a)
leapyear(a)
    