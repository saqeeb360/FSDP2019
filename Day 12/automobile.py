# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:57:12 2019

@author: Windows
"""

import pandas as pd
import numpy as np

df=pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())


x = np.array( df['price'] ) 
print(np.min(x))
print(np.max(x))
print(np.std(x))
print(np.mean(x))
