from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris_data=load_iris()
a=iris_data.data
b=iris_data.target

a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.3,random_state=42)

knn=KNeighborsClassifier(n_neighbors=9)
knn.fit(a_train,b_train)
c=knn.predict(a_test)
acc=accuracy_score(b_test,c)
print(c)
print(acc)