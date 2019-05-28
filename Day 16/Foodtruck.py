# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:32:56 2019

@author: Windows
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv('Foodtruck.csv')  

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

x=[3.07]
x=np.array(x)
x=x.reshape(1,1)

print(regressor.predict(x))



