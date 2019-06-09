# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:43:20 2019

@author: Windows
"""
"""? = 0 or 1 occurance
   * = 0 or more occurance
   + = 1 or more occurance

"""

import re

while True:    
    number= input(">").strip()
    if not number:
        print("Exiting...")
        break
    reg = r'^[456](\d{15}|\d{3}-\d{4}-\d{4}-\d{4}$)'
    
    result=re.match(reg,number)
    repeat = re.search(r'(\d)\1{3,}',number.replace("-",""))
    
        
    if not repeat and result:
        print("Valid")
    else:
        print("Invalid")


