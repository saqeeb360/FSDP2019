# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:52:58 2019

@author: Windows
"""

import numpy as np

num="6 9 2 3 5 8 1 5"
list1=num.split()
list1=list(map(lambda x:int(x),list1))
list2=np.array(list1)
list3=list2.reshape(4,2)
