# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:10:25 2019

@author: Windows
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iq_size.csv")

features = df.iloc[:,1:4].values
labels = df.iloc[:,0].values

import statsmodels.api as sm

f_copy = features[:,[0,1,2]]
r_1 = sm.OLS(endog = labels, exog = f_copy).fit()
r_1.summary()

f_copy = features[:,[0,1]]
r_2 = sm.OLS(endog = labels, exog = f_copy).fit()

f_copy = features[:,0]
r_3 = sm.OLS(endog = labels, exog = f_copy).fit()
r_3.predict(np.array([90]).reshape(1,1))



plt.scatter(f_copy,labels)
plt.plot(f_copy, r_3.predict(f_copy))
plt.show


