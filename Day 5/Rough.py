# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:34:14 2019

@author: Windows
"""

"""? = 0 or 1 occurance
   * = 0 or more occurance
   + = 1 or more occurance

"""


import re

str1= '1687abc.test@gmail.com, xyz@test.in, test.first@company.com nimish@gmail.co.in'
result = re.search(r'[0-9a-z_.-]+@[0-9a-z_.-]+\.+[0-9a-z_-]',str1)
print((result))

