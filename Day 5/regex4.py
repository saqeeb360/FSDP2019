# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:54:17 2019

@author: Windows
"""

import re
list1 =[]
while True:
    email = input(">").strip()
    if not email :
        print("Exiting")
        break
    reg = r'^[A-Za-z\d_-]+@[A-Za-z\d]+\.[a-z]{2,4}$'
    result = re.match(reg , email)
    if result:
        list1.append(email)
        print("Valid")
    else:
        print("Invalid")
print(list1)
    
    
    
