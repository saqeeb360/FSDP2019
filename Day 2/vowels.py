# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:59:12 2019

@author: Saqeeb
Name  : Vowels finder

"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels="AEIOUaeiou"
list_final=[]

for state in state_name:
    temp_str=[]
    for letter in state:
        if letter not in vowels:
            temp_str.append(letter)
    list_final.append("".join(temp_str))


