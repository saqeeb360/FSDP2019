# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:09:26 2019

@author: Windows
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,20,10000)


plt.hist(incomes, bins=50)
print("mean of income is "+str(np.mean(incomes)))

print("median of income is "+str(np.median(incomes)))

