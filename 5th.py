from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

iris_data=datasets.load_iris()
a=iris_data.data
b=iris_data.target

x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=0.3,random_state=42)

model=GaussianNB()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(metrics.accuracy_score(y_test,y_pred))
