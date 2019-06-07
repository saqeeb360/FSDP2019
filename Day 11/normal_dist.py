# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:38:41 2019

@author: Windows
"""

import matplotlib.pyplot as plt
import numpy 
x=numpy.random.normal(150,20,1000)
plt.hist(x,bins=100)

print("The standard deviation is : "+str(numpy.std(x)))
print("The variance is : "+str(numpy.var(x)))


