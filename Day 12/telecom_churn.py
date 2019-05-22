# -*- coding: utf-8 -*-
"""
Created on Wed May 22 01:43:07 2019

@author: Windows
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Telecom_churn.csv")
#df['churn'][(df['voice mail plan']=='yes') & (df['international plan']=='yes')].value_counts()[1]

df['voice mail plan'][(df['churn']==pd.Series([True,False])[0]) & (df['international plan']=='yes')].value_counts()[1]
bol = pd.Series([True,False])

s=df['total intl charge'][(df['churn']==bol[0])]
pd.Series.sum(s)       

not_churn=df['total intl charge'][(df['churn']==bol[1])]    
pd.Series.sum(not_churn)       

plt.hist(s,bins=100) 
plt.hist(not_churn,bins=200)

#df['state'][(df['churn']==bol[0]) & (df[])]

#group data using rank followed  by discipline and sex
#df_rank=df.groupby(['rank', 'discipline','sex'])
#df_rank.groups
#df_rank.groups.keys()
#df_rank.count()


x=df.groupby('state')[['total night calls']].sum()

        
        























        