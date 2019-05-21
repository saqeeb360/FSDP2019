# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:44:02 2019

@author: Windows
"""

import pandas as pd

data_df =pd.read_csv("training_titanic.csv")
#
#surv = data_df[(data_df['Survived']==1)]
#data_df['Survived']
#surv['Survived'].value_counts()
#

print("No of people survived : "+str(data_df['Survived'].value_counts()[1]))
print("No of people died : "+str(data_df['Survived'].value_counts()[0]))
print("% of people survived : "+str(data_df['Survived'].value_counts(normalize=True)[1]))
print("% of people died : "+str(data_df['Survived'].value_counts(normalize=True)[0]))

print("Males that survived vs males that passed away : ",data_df['Survived'][data_df['Sex']=='male'].value_counts()[1]," vs",
      data_df['Survived'][data_df['Sex']=='male'].value_counts()[0])

data_df['Age'] = data_df['Age'].fillna(data_df['Age'].mean())

data_df["Children"] = data_df["Age"].map(lambda x: 0 if x >18 else 1 )

data_df['Children'][data_df['Survived']==1].value_counts()


#data_2=data_df[(data_df['Survived']==1) & \
#               (data_df['Sex']=='male')
#               ]
#
#type(data_df[data_df['Sex']=='male'])
















