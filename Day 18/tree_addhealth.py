# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:58:13 2019

@author: Windows
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tree_addhealth.csv")
# df.isnull().any(axis=0)
df['age'] = df['age'].fillna(df['age'].mean())
df['ESTEEM1'] = df['ESTEEM1'].fillna(df['ESTEEM1'].mean())

# gender, age , Hispanic ,  White, Black, Native American and Asian, alcohol use,
# alcohol problems, marijuana use, cocaine use, inhalant use, availability of 
# cigarettes in the home, depression, and self-esteem 
features = df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels = df.iloc[:,7].values

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

# plotting the model graph
x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1
z_min, z_max = features_train[:, 2].min() - 1, features_train[:, 2].max() + 1
a_min, a_max = features_train[:, 3].min() - 1, features_train[:, 3].max() + 1
b_min, b_max = features_train[:, 4].min() - 1, features_train[:, 4].max() + 1
c_min, c_max = features_train[:, 5].min() - 1, features_train[:, 5].max() + 1
d_min, d_max = features_train[:, 6].min() - 1, features_train[:, 6].max() + 1
f_min, f_max = features_train[:, 8].min() - 1, features_train[:, 8].max() + 1
g_min, g_max = features_train[:, 9].min() - 1, features_train[:, 9].max() + 1
h_min, h_max = features_train[:, 10].min() - 1, features_train[:, 10].max() + 1
i_min, i_max = features_train[:, 11].min() - 1, features_train[:, 11].max() + 1
j_min, j_max = features_train[:, 12].min() - 1, features_train[:, 12].max() + 1
k_min, k_max = features_train[:, 13].min() - 1, features_train[:, 13].max() + 1
l_min, l_max = features_train[:, 14].min() - 1, features_train[:, 14].max() + 1


xx, yy, zz, aa, bb, cc, dd, ff, gg, hh, ii, jj, ll = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(z_min, z_max, 0.1),
                     np.arange(a_min, a_max, 0.1),
                     np.arange(b_min, b_max, 0.1),
                     np.arange(c_min, c_max, 0.1),
                     np.arange(d_min, d_max, 0.1),
                     np.arange(f_min, f_max, 0.1),
                     np.arange(g_min, g_max, 0.1),
                     np.arange(h_min, h_max, 0.1),
                     np.arange(i_min, i_max, 0.1),
                     np.arange(j_min, j_max, 0.1),
                     np.arange(k_min, k_max, 0.1),
                     np.arange(l_min, l_max, 0.1))
                     
# Obtain labels for each point in mesh using the model.
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the points
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')

plt.contourf(xx, yy, Z, alpha=0.3)
plt.show()




