# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:24:37 2019

@author: Windows
"""
list2=[]
while True:
    str1=input(" > ")
    if not str1:
        print(list2)
        break
    #take out name, age, and height in respective data types
    list1=str1.split(",")
    list1[1]=int(list1[1])
    list1[2]=int(list1[2])
    list1=tuple(list1)
    list2.append(list1)
    list2.sort()
    
    


 