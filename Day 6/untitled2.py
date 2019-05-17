# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:15:21 2019

@author: Windows
"""
#xyz=0
#list1=[]
#def checker(x):
#    if "bvale" in x.values():
#        xyz=True
#    else:
#        xyz=False
#    return xyz    
#
#list(map(checker,list1))

list1=[]
dict1={}
dict1["key"]=15
for i in range(0,9):
    dict1["key"]=i
    list1.append(dict1.copy())
    print(i)
    
for item in list1:
    item["key"]=4
    break






#
#str1="123,456,789"
#list1=str1.split(",")
#str2=""
#
#for item in list1:
#    str2=str2+item
#    
#print(str2)
#
#












