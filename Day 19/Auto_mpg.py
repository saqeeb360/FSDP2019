# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:55:27 2019

@author: Windows
"""

import numpy as np
import pandas as pd

df = pd.read_csv("Auto_mpg.txt" , delimiter = "\s+" , header = None)

df.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
print("Car with max mpg :" ,df['car name'][df['mpg']==df['mpg'].max()])
df['horsepower'] = df['horsepower'].replace('?' , np.NAN)
df['horsepower'] = df['horsepower'].astype('float64')
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())

# df.isnull().any(axis=0)

features = df.iloc[:,1:-1]
labels = df.iloc[:,0].values


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25 , random_state = 0)  

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

from sklearn.tree import DecisionTreeRegressor  
regressor1 = DecisionTreeRegressor()  
regressor1.fit(features_train, labels_train)  

labels_pred1 = regressor1.predict(features_test)

score1 = regressor1.score(features_test,labels_test)

# Method Two

#train the model
from sklearn.ensemble import RandomForestRegressor
regressor2 = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor2.fit(features_train, labels_train)  
labels_pred2 = regressor2.predict(features_test)  
score2 = regressor2.score(features_test, labels_test)

#Find out the MPG value of a 80's model car of origin 3, 
# weighing 2630 kgs with 6 cylinders, 
#having acceleration around 22.2 m/s due to it's 100 horsepower engine giving 
#it a displacement of about 215. (Give the prediction from both the models)

x = [6,215,100,2630,22.2,80,3]
x = np.array(x)
x = x.reshape(1,-1)

regressor1.predict(x)
regressor2.predict(x)

