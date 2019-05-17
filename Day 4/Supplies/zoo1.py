# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:57:17 2019

@author: Windows
"""

import csv
dict1={}
old_l1=[]
old_l2=[]

with open("zoo.csv","r") as file1:
    file2=csv.reader(file1,delimiter=",")
    next(file2)
    for row in file2:
        if row[0] not in dict1:
            l1=[]
            l2=[]
            l1.append(int(row[1]))
            l2.append(int(row[2]))
            dict1[row[0]]=[l1,l2]
        else:
            old_l1=dict1[row[0]][0]
            old_l2=dict1[row[0]][1]
            old_l1.append(int(row[1]))
            old_l2.append(int(row[2]))
            dict1[row[0]]=[old_l1,old_l2]

           
        
        
        
        
        