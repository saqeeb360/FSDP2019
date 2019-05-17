# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:30:01 2019

@author: Windows
"""

[int(i) for i in list1]

list2=[]
for i in list1:
    if int(i)>0:
        list2.append(True)
    else:
        list2.append(False)
 
[int(i)>0 for i in list1]

all([int(i)>0 for i in list1])

all(list(map(lambda x: int(x)>0,list2)))

list(map(lambda x: int(x)>0,list1))