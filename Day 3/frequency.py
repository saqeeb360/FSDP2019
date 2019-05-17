# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:27:42 2019

@author: Windows
"""

str1="Www.goo gle .com"
str1="$".join(str1)
str1=str1.lower()
list1=str1.split("$")

dict1={}
for k in list1:
    if k not in dict1:
        dict1[k]=1
    else:
        x=dict1.get(k)
        dict1[k]=x+1
for k in dict1:
    print(k,dict1[k])
        