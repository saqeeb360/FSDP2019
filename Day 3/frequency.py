# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:27:42 2019

@author: Windows
"""
from collections import OrderedDict
dict1=OrderedDict()
str1="Www.goo gle .com"
str1=str1.lower()
#str1="$".join(str1)
#list1=str1.split("$")

# METHOD 1
#for k in str1:
#    if k not in dict1:
#        dict1[k]=1
#    else:
#        x=dict1.get(k)
#        dict1[k]=x+1

# METHOD 2
#for k in str1:
#    dict1[k]=dict1.get(k,0)+1
#
#for k in dict1:
#    print(k,dict1[k])

# Method 3
from collections import Counter
print(dict(Counter(str1)))


        