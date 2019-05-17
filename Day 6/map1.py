# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:41:14 2019

@author: Windows
"""
#list(map(lambda x: int(x)>0,list1)))
#list3=list(map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']),names))


import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

def nam_fun(x):
    return random.choice(code_names)
list3= list(map(nam_fun, names))
print(list3)


list4=list(map(lambda x:random.choice(code_names),names))
#for i in range(len(names)):
#    names[i] = random.choice(code_names)
#
#print (names)
#
