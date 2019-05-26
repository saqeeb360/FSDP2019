# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:50:08 2019

@author: Windows
"""

list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)



