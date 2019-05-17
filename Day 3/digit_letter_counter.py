# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:42:36 2019

@author: Windows
"""

str1="Python 3.2"
str1=" ".join(str1)
str1=str1.lower()

list1=str1.split()

abc="asdfghjklqwertyuiopzxcvbnm"
dict1={}
i=0
j=0
for k in list1:     
    if k in "1234567890":
        j=j+1
        dict1["Digits"]=j
    elif k in abc:
        i=i+1
        dict1["Letters"]=i
for key in dict1:
    print(key,dict1[key])
    
    
        
        