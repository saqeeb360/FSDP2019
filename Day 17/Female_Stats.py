# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:38:36 2019

@author: Windows
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Female_Stats.csv")

features = df.iloc[:,1:].values
labels = df.iloc[:,0]



import statsmodels.api as sm

f_copy = features[:, [0,1] ]
f_copy = sm.add_constant(f_copy)

regressor_OLS = sm.OLS(endog = labels , exog = f_copy).fit()
regressor_OLS.summary()

print("Both mother's height and father's are important")

f_1 = df.iloc[:,1:2]
f_2 = df.iloc[:,2:3]

from sklearn.linear_model import LinearRegression
lr_1 = LinearRegression()
lr_2 = LinearRegression()

lr_1.fit(f_1,labels)
lr_2.fit(f_2,labels)

print("Mom's Dependance",float(lr_1.coef_))
print("Dad's Dependance",float(lr_2.coef_))





