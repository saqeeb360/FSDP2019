# -*- coding: utf-8 -*-
"""
Created on Sat May 11 02:41:00 2019

@author: Windows
"""

import csv
dict1={}

with open("passwd.csv", "r") as file1:
    file2=csv.reader(file1,delimiter=":")
    for row in file2:
        if "#" not in row[0]:
            dict1[row[0]]=row[2]
            
    for item in dict1:
        print(item,dict1[item])

        