# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:29:02 2019

@author: Windows
"""

import csv
dict1={}

with open("zoo.csv","rt") as file1:
    file2=csv.reader(file1)
    next(file2)
    for row in file2:
        print (row)

with open("zoo.csv","rt") as file1:
    file2=csv.reader(file1)
    next(file2)
    for row in file2: 
        if row[0] not in dict1:
            code=[]
            water=[]
            code.append(int(row[1]))
            water.append(int(row[2]))
            dict1[row[0]]=[code,water]
        else:
            old_code=dict1[row[0]][0]
            old_water=dict1[row[0]][1]
            old_code.append(int(row[1]))
            old_water.append(int(row[2]))
            dict1[row[0]]=[old_code,old_water]
    print("\nWater req by each animal\n")
    for item in dict1:
        x=sum(dict1[item][1])  
        print(item +"  "+str(x))
    
    x=0
    for item in dict1 :
        x=x+sum(dict1[item][1]) 
    print("\nTotal req of water  " +str(x))
            
            
        