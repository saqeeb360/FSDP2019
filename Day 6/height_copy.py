# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:41:14 2019

@author: Windows
"""
from functools import reduce

people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},
          {'name': 'Sam'},{'name': 'Mary', 'height': 16},{'name': 'Isla', 'height': 90}]
#def xyz(x):
#    if 'height' in x:
#        return x['height']
#    else:
#        return (0)
list1=[]
def xyz(x):
    if 'height' in x:
        list1.append(x['height'])

list(map(xyz,people ))
print(list1)

def aver(list1):
    return reduce(lambda a,b:a+b,list1)/len(list1)

average=aver(list1)

