# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:36:23 2019

@author: Windows
"""

import re
list1 = [] 

with open("simpsons_phone_book.txt","r") as file1:
    for i in file1:
        result = re.search(r'^J.*Neu',i)
        if result:
            list1.append(i.strip())

print(list1)
            








