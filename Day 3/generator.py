# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:46:48 2019

@author: Windows
"""
str1="1,2,3,4,5"
str1=str1.split(",")


list1=list(str1)
tuple1=tuple(str1)
print("List : ",list1)
print("Tuple : ",tuple1 )
"""while 0<len(str1):
    
    list1.append(int(str1[i]))
    tuple1.insert(int(str1[i]))
    i=i+1
    
print(list1)
print(list2)   


""" 