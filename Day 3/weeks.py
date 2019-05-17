# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:46:48 2019

@author: Windows
"""
tuple1=('Monday', 'Wednesday', 'Thursday')
list1=list(tuple1)
total=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list2=[]
for item in total:
    if item not in list1:
        list1.append(item)

tuple1=tuple(list1)
        