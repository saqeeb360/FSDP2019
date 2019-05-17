# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:40:41 2019

@author: Windows
Name  :     Pallindromic Integer
"""
list1=[121,19,61,5, 14]

flag=True
for number in list1:
    if number < 0:
        print("False")
        flag=False
        break
if flag==True:
    for number in list1:
        y=str(number)
        z=y[::-1]
        if y==z:
            print("True")
            break



     
        