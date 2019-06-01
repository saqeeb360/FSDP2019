# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:10:24 2019

@author: Windows
"""

import numpy as np
import pandas as pd

df = pd.read_csv("breast_cancer.csv")

df.isnull().any(axis = 0)
df.info()

#removing null values, encoder = not req , standardisation = not req, 

list1 = df['G'].value_counts
df['G'] = df['G'].fillna(1.0)

features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values

#test_train_split

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

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

# predicting the tumor is cancerous or not
# if her Clump thickness is around 6, uniformity of cell size is 2,
# Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9,
# Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and
# Single Epithelial Cell Size is 2

x = np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)

print(classifier.predict(x))






















