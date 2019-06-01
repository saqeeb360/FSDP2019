# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:00:23 2019

@author: Windows
"""

import numpy as np
import pandas as pd


from sklearn.datasets import load_iris
# df = datasets.load_iris().data
iris = load_iris()
# getting the data
df = pd.DataFrame(iris['data'] , columns = iris['feature_names'])
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df['species'] = df['species'].astype(str)
df.isnull().any(axis=0)
df.info()
# find missing data = not req,  standardize the data= req, encoder = not req 
features = df.iloc[:,:4].values
labels = df.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
features_train = ss.fit_transform(features_train)
features_test = ss.transform(features_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)
