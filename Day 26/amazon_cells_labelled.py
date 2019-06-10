# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:55:50 2019

@author: Windows
"""


import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

df = pd.read_csv("amazon_cells_labelled.txt" , delimiter = '\t',header = None)
df.columns = ["Review" , "Likes"]
corpus = []
ps = PorterStemmer()
for i in range(0,1000):
    review = re.sub(r'[^A-Za-z]'," ",df['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review
              if not word in set(stopwords.words('english'))]
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)
classifier.score(features_train,labels_train)


#applying knn on this text dataset
# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier()
classifier_knn.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier_knn.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
classifier_knn.score(features_train, labels_train)


"""
Predicting a review
"""
review = "Shamim said the order was very good bad and clean . beautiful , representation"
review = re.sub(r'[^A-Za-z]'," ",review)
review = review.lower()
review = review.split()
review = [word for word in review
          if not word in set(stopwords.words('english'))]
review = [ps.stem(word) for word in review]
review = ' '.join(review)

list1=[]
list1.append(review)
feature_ck = cv.transform(list1).toarray()
classifier_knn.predict(feature_ck)



