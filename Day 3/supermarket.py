# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:12:59 2019

@author: Windows
"""
dict1={}

while True:             #for
    item=input(">")     #multiple 
    if not item:        #inputs
        break           #of str
    list1=item.split()
    keys1=list1[0:(len(list1)-1)]
    keys1=" ".join(keys1)
    value1=int(list1[-1])
    if keys1 in dict1:
        x=dict1.get(keys1)
        
        value1=x+value1
        
        
        
      
    dict1[keys1]=value1

for k in dict1:
    print(k,dict1[k])
    
    
