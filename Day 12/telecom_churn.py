# -*- coding: utf-8 -*-
"""
Created on Wed May 22 01:43:07 2019

@author: Windows
"""

import pandas as pd

df = pd.read_csv("Telecom_churn.csv")
df['churn'][(df['voice mail plan']=='yes') & (df['international plan']=='yes')].value_counts()[1]

