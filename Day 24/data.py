# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:15:12 2019

@author: Windows
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.isnull().any(axis=0)
df.info()

country = df.iloc[:,31]

plt.pie()



