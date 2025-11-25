from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report

data=load_wine()
X=data.data
y=data.target
xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=42)
rf_classifier=RandomForestClassifier(n_estimators=100, random_state=42) 
rf_classifier.fit(xtrain,ytrain)

ypred=rf_classifier.predict(Xtest)
accuracy=accuracy_score(ytest,ypred)
print('accuracy:',accuracy)
print('Classification Report:\n', classification_report(ytest, ypred)) 
