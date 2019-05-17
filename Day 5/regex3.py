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

number="4324-3546-5768-7981"

result=re.match(r'^[456]{1}[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}',number)
print(result)
    
if result:
    print(number)
else:
    print("Invalid")


