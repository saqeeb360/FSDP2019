# -*- coding: utf-8 -*-
"""
Created on Sat May 11 00:04:29 2019

@author: Windows
"""

import csv
list1=[]
dict1={}
with open("romeo.txt", "rt") as file1:
    file2=csv.reader(file1, delimiter=" ")
    for row in file2:
        print (row)
        list1=list1+row
    for word in list1:
        if word not in dict1:
            dict1[word]=1
        else:
            dict1[word]=dict1[word]+1
        
