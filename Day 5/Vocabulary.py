# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:21:02 2019

@author: Windows
"""
from collections import Counter
import re

j=0
list1 = []
file1 = open("james_joyce_ulysses.txt",encoding="utf-8")
for line in file1:
    print(j)
    j=j+1
    if line:
        str1 = line.lower().strip()
        str1 = re.sub(r'[~!@#"$%-/’—‘.,;\'“”:?\[\]&*()\d_+]', "",str1)   
        str1 = str1.split()
        n = len(str1)
        for i in range(0,n):
            list1.append(str1[i])

dict1 = Counter(list1)
print("No of words : ",len(list1))
print("No of unique words : ",len(dict1))

j=0
list2=[]
file2 = open("metamorphosis_kafka.txt",encoding="utf-8")
for line in file2:
    print(j)
    j=j+1
    if line:
        str1 = line.lower().strip()
        str1 = re.sub(r'[~!@#"$%-/’—‘.,;\'“”:?\[\]&*()\d_+]', "",str1)   
        str1 = str1.split()
        n = len(str1)
        for i in range(0,n):
            list2.append(str1[i])
dict2 = Counter(list2)

j=0
list3=[]
file3 = open("sons_and_lovers_lawrence.txt",encoding="utf-8")
for line in file3:
    print(j)
    j=j+1
    if line:
        str1 = line.lower().strip()
        str1 = re.sub(r'[~!@#"$%-/’—‘.,;\'“”:?\[\]&*()\d_+]', "",str1)   
        str1 = str1.split()
        n = len(str1)
        for i in range(0,n):
            list3.append(str1[i])
dict3 = Counter(list3)



j=0
list4=[]
file4 = open("the_way_of_all_flash_butler.txt",encoding="utf-8")
for line in file4:
    print(j)
    j=j+1
    if line:
        str1 = line.lower().strip()
        str1 = re.sub(r'[~!@#"$%-/’—‘.,;\'“”:?\[\]&*()\d_+]', "",str1)   
        str1 = str1.split()
        n = len(str1)
        for i in range(0,n):
            list4.append(str1[i])
dict4 = Counter(list4)




j=0
list5=[]
file5 = open("robinson_crusoe_defoe.txt",encoding="utf-8")
for line in file5:
    print(j)
    j=j+1
    if line:
        str1 = line.lower().strip()
        str1 = re.sub(r'[~!@#"$%-/’—‘.,;\'“”:?\[\]&*()\d_+]', "",str1)                 
        str1 = str1.split()
        n = len(str1)
        for i in range(0,n):
            list5.append(str1[i])
dict5 = Counter(list5)

