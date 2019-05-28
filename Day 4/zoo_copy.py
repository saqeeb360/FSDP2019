# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:10:22 2019

@author: Windows
"""

import csv
animal_data = {}

#with open("zoo.csv","rt") as file1:
#    file2=csv.reader(file1)
#    next(file2)
#    for row in file2:
#        print (row)

with open("zoo.csv","rt") as file1:
    file2=csv.reader(file1)
    next(file2)
    for row in file2:
        if row[0] not in animal_data:
            animal_data[row[0]]=[[int(row[1])],[int(row[2])]]
        else:
            animal_data[row[0]][0].append(int(row[1]))
            animal_data[row[0]][1].append(int(row[2]))
print(animal_data)