# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:27:29 2019

@author: Saqeeb
Name :  Pattern Builder

"""
x=input("Enter a number ")

j=0
str1="*"

while j < int(x):
    j=j+1
    print(str1*j)
while j > 0:
    j=j-1
    print(str1*j)
    
