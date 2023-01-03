import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('C:\data.csv')
x=dataset.iloc[:,[1,2]].values
print(x)

from sklearn.cluster import KMeans
wcss_list=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)
plt.plot(range(1,11),wcss_list)
plt.title("An elbow method graph")
plt.xlabel("no of clusters")
plt.ylabel("wcss_list")
plt.show()

kmeans=KMeans(n_clusters=3,init="k-means++",random_state=42)
y_predict=kmeans.fit_predict(x)
print(y_predict)

plt.scatter(x[y_predict==0,0],x[y_predict==0,1],s=100,c="blue",label="clus1")
plt.scatter(x[y_predict==1,0],x[y_predict==1,1],s=100,c="red",label="clus2")
plt.scatter(x[y_predict==2,0],x[y_predict==2,1],s=100,c="green",label="clus3")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c="black",label="cluster")
plt.legend()
plt.show()



