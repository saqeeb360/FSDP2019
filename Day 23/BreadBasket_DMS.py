# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:05:12 2019

@author: Windows
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from apyori import apriori


df = pd.read_csv("BreadBasket_DMS.csv")

df['Item'] = df['Item'].replace('NONE', np.nan)
df = df.dropna(axis = 0)

max_count = df['Item'].value_counts()
plt.pie(max_count[0:15],labels=max_count.index[0:15] , explode = None )
plt.show()
trans = []

transaction = df.groupby(['Transaction'])['Item'].apply(lambda x : list(set(x)))

rules = apriori(transaction, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results = list(rules)
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")




