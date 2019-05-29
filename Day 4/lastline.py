# -*- coding: utf-8 -*-
"""
Created on Sat May 11 02:35:27 2019

@author: Windows
"""
def lastline(filename):    
    with open(filename, "rb") as file1:
        print(file1.readlines()[-1])
lastline("romeo.txt")        
        
        
        