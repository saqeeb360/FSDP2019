# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:56:33 2019

@author: Windows
"""

import numpy as np
import pandas as pd

df = pd.read_csv("mushrooms.csv")

features = df.iloc[:,[5,-2,-1]].values
labels = df.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le0 = LabelEncoder()
features[:,0] = le0.fit_transform(features[:, 0])

le1 = LabelEncoder()
features[:,1] = le1.fit_transform(features[:, 1])

le2 = LabelEncoder()
features[:,2] = le2.fit_transform(features[:, 2])

ohe0 = OneHotEncoder(categorical_features = [-1])
features = ohe0.fit_transform(features).toarray()
features = features[:,1:]

ohe1 = OneHotEncoder(categorical_features = [-1])
features = ohe1.fit_transform(features).toarray()
features = features[:,1:]

ohe2 = OneHotEncoder(categorical_features = [-1])
features = ohe2.fit_transform(features).toarray()
features = features[:,1:]

labels = labels.reshape(8124,1)
le4 = LabelEncoder()
labels = le4.fit_transform(labels[:,0])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Applying Logistics Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(features_train,labels_train)

# Predicting the class label
labels_pred = lr.predict(features_test)

# Making a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# odor = a , population = s , habitat = g
x = ['a','s','g']
x = np.array(x)
x = x.reshape(1,-1)

x[:,0] = le0.transform(x[:,0])
x[:,1] = le1.transform(x[:,1])
x[:,2] = le2.transform(x[:,2])

x = ohe0.transform(x).toarray()
x = x[:,1:]
x = ohe1.transform(x).toarray()
x = x[:,1:]
x = ohe2.transform(x).toarray()
x = x[:,1:]

ans = lr.predict(x)



