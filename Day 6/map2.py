# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:58:26 2019

@author: Windows
"""

names = ['Mary', 'Isla', 'Sam']

#for i in range(len(names)):
#    names[i] = hash(names[i])
#
#print (names)
def hash_int(x):
    return hash(x)
list1=list(map(hash_int,names))

list2=list(map(lambda x:hash(x),names))