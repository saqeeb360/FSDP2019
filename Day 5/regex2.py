# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:35:31 2019

@author: Windows
"""
list1 = []
import re
while True:
    email=input(">")
    if not email:
        print()
        break
    result=re.match(r'^[A-z\d_-]+\@[A-z\d]+\.[A-z\.]{2,4}$', email)
    
    if result:
        list1.append(email)
    else:
        print("Invalid email")
print(list1)