# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:49:27 2019

@author: Windows
"""

list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]

#for i in list1:
#    if i not in list2:
#        list2.append(i)
#    else:
#        print("hai",i)
#        list2.remove(i)
list1=list(set(list1))
list1.reverse()    
print(list1)
        
        