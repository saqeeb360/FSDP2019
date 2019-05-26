# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:12:59 2019

@author: Windows
"""
from collections import OrderedDict
dict1=OrderedDict()

while True:                     #for
    user_input=input(">")       #multiple 
    if not user_input:        #inputs
        break                  #of str

    list1=user_input.split()  #converting str in list
    
    item=" ".join(list1[:-1])   #converting user_input name into string
    price=int(list1[-1])   #taking price

#    if item in dict1:
#        x=dict1.get(item)
#        price=x+price
      
    dict1[item]=dict1.get(item,0)+ price
    
for k in dict1:
    print(k,dict1[k])
    
    
