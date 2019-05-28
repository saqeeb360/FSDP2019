# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:35:39 2019

@author: Windows
"""
# Ques
# why do we remove one column from features ?
# why is it giving value thruohg prediction greater than one?-execute last line
# What is score?

import pandas as pd  
import numpy as np  

dataset = pd.read_csv('University_data.csv')  

features=dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

print(dataset.isnull().any(axis=0))

# Converting categorical data through label encoder and one hot encoder
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Removing dummy varible trap
features = features[:, 1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Training your model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting for a new value
#x=[0,0,0,1,330,4.5,4.5,10,5]
#x=np.array(x)
#x=x.reshape(1,9)
#print(regressor.predict(x))


le = labelencoder.transform(['Cabrini'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],330,4,4,7.7,1]
x = np.array(x)
regressor.predict(x.reshape(1, -1))


# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)






















