# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:49:38 2019

@author: Windows
"""
with open("absent.txt","wt") as file1:
    while(True):
        name=input(">")
        if not name:
            break
        file1.write(name+"\n")

with open("absent.txt","r") as file1:
    msg=file1.read()
    print(msg)

    