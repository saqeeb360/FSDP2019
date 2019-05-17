# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:11:26 2019

@author: Windows
"""

list1= ['abets', 'baaste']

x=list1[0]
y=list1[1]
x=" ".join(x)   
list1=x.split()
list1.sort()
x="".join(list1)

y=" ".join(y)   
list2=y.split()
list2.sort()
y="".join(list2)
if (x==y):
    print("Pangram")
else:
    print("Not Pangram")
    
i=i+1
    





    