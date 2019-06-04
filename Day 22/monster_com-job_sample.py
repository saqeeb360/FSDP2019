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


def location_change(location_string):
    if re.findall(r'\, ?[A-Z]+ ?\d+',location_string):
        return location_string
    else:
        return np.nan

df["organization"] = df["organization"].fillna("Missing")
new_df = pd.DataFrame()
new_df["organization"] = df["organization"].apply(location_change)




