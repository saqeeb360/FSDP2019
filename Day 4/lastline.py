# -*- coding: utf-8 -*-
"""
Created on Sat May 11 02:35:27 2019

@author: Windows
"""

n=input("Enter a name ")
name=n+".txt"
with open(name, "wt") as file1:
    print("Name changed")
with open(name, "rt") as file1:
    print(file1.read())