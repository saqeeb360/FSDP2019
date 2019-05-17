# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:15:36 2019

@author: Saqeeb
Name   :Translate

"""

str1="This is fun"
i=0
temp=""
while  i<len(str1):
    if str1[i] not in " AEIOUaeiou":
        temp=temp+str1[i]+"o"+str1[i]
    else:
        temp=temp+str1[i]
    i=i+1
print(temp)    