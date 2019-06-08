# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:14:53 2019

@author: Windows
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Train Dataset
df = pd.read_csv("train.csv")
# Test Dataset
df1 = pd.read_csv("test.csv")

# Checking the Data
df.iloc[:,-1].unique()
df.columns[-1]
df.isnull().any(axis = 0)[:100]
df['subject'].unique()

# Spliting the data into features and labels
features_train = df.iloc[:,:-2].values
labels_train = df.iloc[:,[-1]].values
features_test = df1.iloc[:,:-2].values
labels_test = df1.iloc[:,[-1]].values

"""
Implementing the Decision Tree Classifier 
"""
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(random_state=0)
dtc.fit(features_train,labels_train)
labels_pred_dct = dtc.predict(features_test)
score_dtc = dtc.score(features_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_dct))  

"""
Implementing the Random Forest Classifier
"""
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=20, random_state=0)
rfc.fit(features_train,labels_train)
labels_pred_rfc =  rfc.predict(features_test)
score_rfc = rfc.score(features_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_rfc)) 

"""
Implementing the Logistic Regression 
"""
from sklearn.linear_model import LogisticRegression
lrc = LogisticRegression()
lrc.fit(features_train,labels_train)
labels_pred_lrc =  lrc.predict(features_test)
score_lrc = lrc.score(features_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_lrc)) 

"""
Implementing the kNN
"""
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(features_train,labels_train)
labels_pred_knn =  knn.predict(features_test)
score_knn = knn.score(features_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_knn)) 

"""
Implementing the Labelencoder
"""
from sklearn.preprocessing import LabelEncoder
lbe = LabelEncoder()
labels_lbe_train = lbe.fit_transform(labels_train)
labels_lbe_test= lbe.transform(labels_test)

"""
Implementing Feature selections
"""
import statsmodels.api as sm
features_cons = features_train

i=0
while i < 100:
    features_cons = sm.add_constant(features_cons)
    regressor_OLS = sm.OLS(endog = labels_lbe_train, exog = features_cons).fit()
    list1 = regressor_OLS.pvalues
    max_percentage = list1.max()
    index = np.where(list1==max_percentage)[0][0]
    if max_percentage > 0.05:
        print("hello and drop",i)
        features_cons = np.delete(features_cons,(index),axis=1)
    else:
        break
    i = i + 1























