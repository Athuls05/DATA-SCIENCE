import matplotlib.pyplot as plt
a=[1,2,3]
b=[4,5,6]
plt.plot(a,b)
plt.title("My first graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

import plotly.express as px
fig=px.bar(x=["a","b","c"],y=[1,2,3])
fig.show()

from bokeh.plotting import figure,output_file,show
graph=figure(title="My Bokeh Graph")
u=[1,2,3]
v=[4,5,6]
graph.line(u,v)
show(graph)

import seaborn as sns
data=sns.load_dataset("iris")
sns.lineplot(x="sepal_length",y="sepal_width",data=data)
plt.show()