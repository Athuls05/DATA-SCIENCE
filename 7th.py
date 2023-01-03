import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

data=load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['target']=data.target

x_train,x_test,y_train,y_test=train_test_split(df[data.feature_names],df['target'],test_size=0.1,random_state=42)

clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
a=clf.predict(x_test)
print("The accuracy of Decison Tree in % is : ",accuracy_score(y_test,a)*100)