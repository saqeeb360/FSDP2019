# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:24:39 2019

@author: Windows
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels="AEIOUaeiou"
list_final=[]

for state in state_name:
    temp_str=""
    for letter in state:
        if letter not in vowels:
            temp_str=temp_str+letter
    list_final.append(temp_str)

print(list_final)
