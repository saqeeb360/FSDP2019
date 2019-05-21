# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:19:42 2019

@author: Windows
"""

import numpy as np
dict1={}

list1=np.random.randint(5,16,40)

#count=0
#for item in dict1:
#    x = dict1[item]
#    if x > count:
#        count=x

from collections import Counter
dict1=Counter(list1)

print("the most freq element is "+str(dict1.most_common()[0][0]))


#for k in dict1:
#    if dict1[k]==count:
#        print("the most freq element is "+str(k))
#        break
