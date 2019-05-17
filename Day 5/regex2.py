# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:35:31 2019

@author: Windows
"""

import re
while True:
    email=input(">")
    if not email:
        break
    result=re.match(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}', email)
    print(result)
    
    if result:
        print(email)
    else:
        print("Invalid email")