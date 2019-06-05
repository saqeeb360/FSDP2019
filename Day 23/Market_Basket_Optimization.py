# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:57:38 2019

@author: Windows
"""


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from apyori import apriori

df = pd.read_csv("Market_Basket_Optimisation.csv",header = None)

#transcation = list(df.apply(lambda x: list(set(x)) , axis=1))

def nan_remove(row):
    tmp = list(set(row))
    if np.nan in tmp:
        tmp.remove(np.nan)
    return tmp


transaction = list(df.apply(nan_remove , axis = 1))

#transaction = df.applymap(lambda x:[x] if pd.notnull(x) else []).sum(1).tolist()


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


