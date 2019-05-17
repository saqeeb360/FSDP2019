# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:58:27 2019

@author: Windows
"""
"""? = 0 or 1 occurance
   * = 0 or more occurance
   + = 1 or more occurance

"""

import re
#3.3.3.3.3
#222.333
#+-2.33
#-.56
#+23.
#+53.335

number = "+-2.33-"

result=re.match(r'^[+-]?[0-9]*\.[0-9]+$', number)

print(result)
if result:
    print("True")
else:
    print("False")