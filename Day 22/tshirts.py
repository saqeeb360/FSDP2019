# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:24:55 2019

@author: Windows
"""
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tshirts.csv")
features = df.iloc[:,[1,2]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3 , init = 'k-means++' , random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of tshirts')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()








