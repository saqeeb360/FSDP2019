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
Implementing Feature selections using back elimination
"""
import statsmodels.api as sm
features_cons_train = features_train
features_cons_train = sm.add_constant(features_cons_train)
features_cons_test = features_test
features_cons_test = sm.add_constant(features_cons_test)
i=0
list1 = []
while True:
    regressor_OLS = sm.OLS(endog = labels_lbe_train, exog = features_cons_train).fit()
    array = regressor_OLS.pvalues
    max_percentage = array.max()
    index = np.where(array==max_percentage)[0][0]
    list1.append(list1)
    if max_percentage > 0.05:
        print("Executing..",i)
        features_cons_train = np.delete(features_cons_train,(index),axis=1)
        features_cons_test = np.delete(features_cons_test,(index),axis=1)
    else:
        break
    i=i+1

"""
New Features size and Labels size
"""
print(features_cons_train)
print(features_cons_test)


"""
Implementing the Decision Tree Classifier on revised dataset
"""
from sklearn.tree import DecisionTreeClassifier
dtc1 = DecisionTreeClassifier(random_state=0)
dtc1.fit(features_cons_train,labels_train)
labels_pred_dct1 = dtc1.predict(features_cons_test)
score_dtc1 = dtc1.score(features_cons_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_dct1))  

"""
Implementing the Random Forest Classifier
"""
from sklearn.ensemble import RandomForestClassifier
rfc1 = RandomForestClassifier(n_estimators=20, random_state=0)
rfc1.fit(features_cons_train,labels_train)
labels_pred_rfc1 =  rfc1.predict(features_cons_test)
score_rfc1 = rfc1.score(features_cons_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_rfc1)) 

"""
Implementing the Logistic Regression 
"""
from sklearn.linear_model import LogisticRegression
lrc1 = LogisticRegression()
lrc1.fit(features_cons_train,labels_train)
labels_pred_lrc1 =  lrc1.predict(features_cons_test)
score_lrc1 = lrc1.score(features_cons_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_lrc1)) 

"""
Implementing the kNN
"""
from sklearn.neighbors import KNeighborsClassifier
knn1 = KNeighborsClassifier(n_neighbors=5)
knn1.fit(features_cons_train,labels_train)
labels_pred_knn1 =  knn1.predict(features_cons_test)
score_knn1 = knn1.score(features_cons_test,labels_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_knn1)) 

"""
Visualising the score after feature selection through back elimination
"""

label = ['score_dtc', 'score_dtc1' ,'', 'score_knn' , 'score_knn1','',
          'score_lrc', 'score_lrc1','', 'score_rfc' , 'score_rfc1']

score = [score_dtc , score_dtc1 ,np.array(0), score_knn ,score_knn1,np.array(0),
         score_lrc,score_lrc1,np.array(0),score_rfc,score_rfc1]

x_axis = np.arange(len(label))
x=[1,1]
y=[-1,12]

plt.figure(figsize=[12,10])
plt.bar(x_axis,score)
plt.plot(y,x)
plt.grid(axis='both')
plt.xticks(x_axis,label , fontsize =14 , rotation = 90)
plt.title("Comparision of the score",fontsize=20)
plt.ylabel("Accuracy_Score",fontsize = 14)
plt.ylim(.5,1.1)
plt.savefig("Comparision_of_score.jpg")
plt.show()

"""
Conclusion :
   "The above accuracy score of the logistics regression is the 
    maximum without feature selection,
    and after feature selection the accuracy score decreases."    
"""
    
    
    
    
    
    























