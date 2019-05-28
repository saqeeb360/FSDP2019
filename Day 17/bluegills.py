# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:18:33 2019

@author: Windows
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bluegills.csv")

features = df.iloc[:,0:1].values
labels = df.iloc[:,1].values



from sklearn.linear_model import LinearRegression
r_1 = LinearRegression()
r_1.fit(features,labels)

plt.plot(features,r_1.predict(features))
plt.scatter(features,labels , color = "red")
plt.show()















from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
f_poly = poly_object.fit_transform(features)

r_2 = LinearRegression()
r_2.fit(f_poly,labels)

x = np.arange(min(features) , max(features) , 0.1 ).reshape(-1,1)

plt.plot(x, r_2.predict(poly_object.transform(x)))
plt.scatter(features,labels , color = "red")
plt.show()













