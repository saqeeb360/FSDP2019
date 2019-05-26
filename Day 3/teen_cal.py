# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:03:52 2019

@author: Windows
"""

str1 = input(" > ")
dict1={}
list1=str1.split(",")

list1[0]=list1[0][1:]
list1[-1]=list1[-1][0:-1]
for i in list1:
    list2=[]
    list2=i.split(":")
    list2[0]=list2[0].replace('"','')
    list2[0]=list2[0].replace(' ','')
    dict1[list2[0]]=int(list2[1])
    
    
    
#dict1={"a" : 2, "b" : 15, "c" : 13}    
list3=[13,14,17,18,19]
i=0

for value in dict1.values():
    if value not in list3:
        i=i+value
        
print("Sum = ",i)

   