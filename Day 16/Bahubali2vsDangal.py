# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:01:41 2019

@author: Windows
"""



import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

features1 = dataset.iloc[:, :-2].values  
labels1 = dataset.iloc[:,1].values 

from sklearn.linear_model import LinearRegression  
regressor1 = LinearRegression()  
regressor1.fit(features1, labels1) 

x=[10]
x=np.array(x)
x=x.reshape(1,1)

bahu=regressor1.predict(x)

features2 = dataset.iloc[:, :1].values  
labels2 = dataset.iloc[:,2].values 

from sklearn.linear_model import LinearRegression  
regressor2 = LinearRegression()  
regressor2.fit(features2, labels2) 

dan = regressor2.predict(x)
if bahu > dan:
    print("Bahu wins")
else:
    print("Dangle wins with ",dan,"crore")







