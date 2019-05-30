# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:20:44 2019

@author: Windows
"""

import numpy as np
import pandas as pd

df = pd.read_csv("affairs.csv")

#check dataset is having a nan value or not
df.isnull().any(axis=0)

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

# Applying OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
ohe1 = OneHotEncoder(categorical_features=[6])
features = ohe1.fit_transform(features).toarray()
features = features[:,1:]
ohe2 = OneHotEncoder(categorical_features=[10])
features = ohe2.fit_transform(features).toarray()
features = features[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Applying Logistics Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(features_train,labels_train)

# Predicting the class label
labels_pred = lr.predict(features_test)

# Making a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Age = 25 , teacher = 4 , graduate = 17 , married = 3 , child = 1, religious = 4, marriage rate = 4 , 
# husband = farmer =2

x = [4,25,3,1,4,17,4,2]
x = np.array(x)
x = x.reshape(1,-1)
x = ohe1.transform(x).toarray()
x = x[:,1:]
x = ohe2.transform(x).toarray()
x = x[:,1:]
lr.predict(x)
