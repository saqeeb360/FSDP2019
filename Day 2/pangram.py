# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:08:00 2019

@author: Saqeeb
Name:    Pangram

"""
str1="The quick brown fox jumps over the lazy dog."
str1=str1.lower()
str1=" ".join(str1)

list1=str1.split()

abc="abcdefghijklmnopqrstuvwxyz"
abc=" ".join(abc)
abc=abc.split()

temp_list=[]
for letter in list1:
    if letter in abc:          
        if letter not in temp_list:
            temp_list.append(letter) #temp_str=temp_str+letter
            temp_list.sort()
    
if (temp_list==abc):
    print("Pangram")
else:
    print("Not Pangram")       



