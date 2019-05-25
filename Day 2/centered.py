# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:11:07 2019

@author: Windows
"""

str1="1, 2,4,5 ,6,3,4,32,23,4,57,5,67,68, 3, 4, 100"

list1=str1.split(",")
list1=[int(i) for i in list1]
list1.sort()

print("Average is : ",int(sum(list1[1:-1])/(len(list1)-2)))
