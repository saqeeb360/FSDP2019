# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:32:24 2019

@author: Windows
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

df = pd.read_csv("monster_com-job_sample.csv")
df1 = df.iloc[:,[-6,-5]]

def location_change(location_string):
    if re.findall(r'\, ?[A-Z]+ ?\d+',location_string):
        return "z2"+location_string
    elif re.findall(r'\, ?[A-Za-z]{2}',location_string):
        return "z1"+location_string
    else:
        return location_string

df1["organization"] = df1["organization"].fillna("Missing")
new_df = pd.DataFrame()
new_df["organization"] = df1["organization"].apply(location_change)
df1 = df1.apply(xyz)




list1 = []
df1["organization"] = df1["organization"].fillna("Missing")
def loc_chn(row):
    list1 = list(row)
    n = len(list1)
    for i in range(n):
        if 
    





df1_new = pd.DataFrame()
df1.apply(loc_chn , axis = 1)



