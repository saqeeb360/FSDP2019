# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:03:52 2019

@author: Windows
"""

dict1={"a" : 2, "b" : 15, "c" : 13}    
list1=[13,14,17,18,19]
i=0

for value in dict1.values():
    print ( value )
    if value not in list1:
        i=i+value
        
print(i)

   