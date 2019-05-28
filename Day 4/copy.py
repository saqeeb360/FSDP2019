# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:59:41 2019

@author: Windows
"""
with open("words.txt", "rb") as file1:
    with open("new.txt", "wb") as file2:
        for line in file1:
            file2.write(line)

