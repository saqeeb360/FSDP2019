# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:11:23 2019

@author: Windows
"""

import numpy as np 
import pandas as pd

df = pd.read_csv("PastHires.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
features[:,1] = le1.fit_transform(features[:, 1])
le2 = LabelEncoder()
features[:,3] = le2.fit_transform(features[:, 3])
le3 = LabelEncoder()
features[:,4] = le3.fit_transform(features[:, 4])
le4 = LabelEncoder()
features[:,5] = le4.fit_transform(features[:, 5])

features = features.astype(int)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
#currently employed 10-year veteran, previous employers 4,
# went to top-tire school, having Bachelor's Degree without Internship.
x = np.array([10,'Y',4,'BS','Y','N']).reshape(1,-1)
x[:,1] = le1.transform(x[:, 1])
x[:,3] = le2.transform(x[:, 3])
x[:,4] = le3.transform(x[:, 4])
x[:,5] = le4.transform(x[:, 5])

classifier.predict(x)

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix , accuracy_score
print(confusion_matrix(labels_test, labels_pred))  
print(accuracy_score(labels_test, labels_pred))


from sklearn.ensemble import RandomForestClassifier
classifier1 = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier1.fit(features_train, labels_train)  
labels_pred1 = classifier1.predict(features_test)

#employment of an unemployed 10-year veteran, ,previous employers 4,
# didn't went to any top-tire school, having Master's Degree with Internship.

y = np.array([10,'N',4,'MS','N','Y']).reshape(1,-1)
y[:,1] = le1.transform(y[:, 1])
y[:,3] = le2.transform(y[:, 3])
y[:,4] = le3.transform(y[:, 4])
y[:,5] = le4.transform(y[:, 5])


classifier1.predict(y)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred1))  
print(classification_report(labels_test,labels_pred1))  
print(accuracy_score(labels_test, labels_pred1))







