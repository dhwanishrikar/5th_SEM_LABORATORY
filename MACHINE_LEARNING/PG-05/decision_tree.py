import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

iris=load_iris()
X=iris.data
y=iris.target

xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=42)
clf=DecisionTreeClassifier(random_state=42)
clf.fit(xtrain,ytrain)

ypred=clf.predict(Xtest)
accuracy=accuracy_score(ytest,ypred)
print('accuracy:',accuracy)

plt.figure(figsize=(15,10))
tree.plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)

plt.show()