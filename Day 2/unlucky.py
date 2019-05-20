# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:19:53 2019

@author: Windows
"""

str1=input("Enter number with comma seperated : ")
list1=str1.split(",")
list1=[int(i) for i in list1]
list2=[]
i=0
while i<len(list1):
    if (list1[i])==13:
        i=i+1
    else:
        list2.append(list1[i])
    i=i+1
print(sum(list2))