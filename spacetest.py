import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_absolute_error as mae

data=pd.read_csv("shuttle.trn",sep=" ",header=None)

print(data.shape)
# print(data.describe)
print(data.head(3))
X=data[data.columns[:9]]
y=data[data.columns[-1]]



# clf=DecisionTreeClassifier()
# clf.fit(X,y)
# y_pred=clf.predict(X)
# error=mae(y,y_pred)
# print(error)
#
# clf=SGDClassifier()
# clf.fit(X,y)
# y_pred=clf.predict(X)
# error=mae(y,y_pred)
# print(error)

clf=GaussianNB()
clf.fit(X,y)
y_pred=clf.predict(X)
error=mae(y,y_pred)
print(error)
